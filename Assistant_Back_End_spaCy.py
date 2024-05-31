import csv

from flask import Flask, request, jsonify, send_file, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import spacy
from textblob import TextBlob
from Response_Template import RESPONSE_TEMPLATES
import random



print("Initializing Flask application...")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #To supress warnings
db = SQLAlchemy(app)

class Interaction(db.Model):
    now = datetime.now()
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), index=True, unique=False)
    response = db.Column(db.String(500), index=True, unique=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), index=True, unique=False)


# Could Have
# class Interaction(db.Model):
#     now = datetime.now()
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(500), index=True, unique=False)
#     response = db.Column(db.String(500), index=True, unique=False)
#     entities = db.Column(db.String(500), index=True, unique=False)
#     noun_chunks = db.Column(db.String(500), index=True, unique=False)
#     pos_tags = db.Column(db.String(500), index=True, unique=False)
#     sentiment = db.Column(db.String(500), index=True, unique=False)
#     topic_understood = db.Column(db.String(500), index=True, unique=False)
#     timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), index=True, unique=False)

nlp = spacy.load('en_core_web_sm')


def extract_entities(text):
    # Load the spaCy model
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    phrase_to_entity = {
        'time': 'TIME',
        'date': 'DATE',
        'today': 'DAY_OF_WEEK',
        'day': 'DAY_OF_WEEK',
        'joke': 'JOKES',
        'motivation': 'MOTIVATION',
        'weather': 'WEATHER',
        'hello': 'GREETING',
        'hi': 'GREETING',
        'hey': 'GREETING',
        'goodbye': 'FAREWELL',
        'bye': 'FAREWELL',
        'farewell': 'FAREWELL',
        'what is the time': 'TIME',
        'what is the date today': 'DATE',
        'what is the day today': 'DAY_OF_WEEK',
        'what day is it': 'DAY_OF_WEEK',
        'tell me a joke': 'JOKES',
        'give me some motivation': 'MOTIVATION',
        'what is the weather': 'WEATHER',
        'how are you': 'GREETING',
        'what is your name': 'GREETING',
        'see you later': 'FAREWELL',
        'take care': 'FAREWELL',
        'reminder': 'REMINDER',
        'note': 'NOTE_TAKING',
        'fact': 'FACTS',
        'directions': 'DIRECTIONS',
        'local time': 'LOCAL_TIME',
        'technical issue': 'TECHNICAL_ISSUES',
        'contact information': 'CONTACT_INFORMATION',
        'compliment': 'COMPLIMENTS',
        'apology': 'APOLOGIES',
        'user name': 'USER_NAME',
        'event information': 'EVENT_INFORMATION',
        'task status': 'TASK_STATUS'
    }

    # Check if the text contains any of the common phrases
    text_lower = text.lower()
    for phrase, entity_type in phrase_to_entity.items():
        if phrase in text_lower:
            entities.append((phrase, entity_type))

    print(f"Entities extracted: {entities}")  # Debug print
    return entities, doc


def generate_response(entities):
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%B %d, %Y")
    day_of_week = now.strftime("%A")

    for entity, label in entities:
        if label in RESPONSE_TEMPLATES:
            response_template = random.choice(RESPONSE_TEMPLATES[label])
            response = response_template.format(
                location=entity,
                name=entity,
                time=current_time,
                date=current_date,
                day_of_week=day_of_week
            )
            return response

    return "I'm not sure how to respond to that."


@app.route('/process_text', methods=['POST'])
def process_text():
    user_text = request.json.get("command")
    entities,doc = extract_entities(user_text)

    # Extract noun chunks
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]

    # Extract parts of speech
    pos_tags = [(token.text, token.pos_) for token in doc]

    # Sentiment analysis
    sentiment = TextBlob(user_text).sentiment

    # Generate a response
    what_was_understood = (f"I understood the following entities: {entities}. "
                           f"Noun chunks: {noun_chunks}. "
                           f"Parts of speech: {pos_tags}. "
                           f"Sentiment: {sentiment}.")

    Response_text = generate_response(entities)

    interaction = Interaction(
        text=user_text,
        response=Response_text,
    )
    db.session.add(interaction)

    try:
        db.session.commit()
    except:
        db.session.rollback()

    return jsonify({"response":Response_text})


@app.route('/download_csv')
def download_csv():
    interactions = Interaction.query.all()

    with open('interactions.csv', 'w') as csvfile:
        fieldnames = ['text', 'response', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for interaction in interactions:
            writer.writerow({
                'text': interaction.text,
                'response': interaction.response,
                'timestamp': interaction.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            })

    return send_file('interactions.csv', as_attachment=True)

if __name__ == '__main__':
    app.run()