from flask import Flask, request as r, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from openai import OpenAI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

class Interaction(db.Model):
    now = datetime.now()
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), index=True, unique=False)
    response = db.Column(db.String(500), index=True, unique=False)
    timestamp = db.Column(now.strftime("%d/%m/%Y %H:%M:%S"), index=True, unique=False)


@app.route('/process_text', methods=['POST'])
def process_text():
    user_text = r.json()
    client = OpenAI
    Response = client.chat.completions.create(model='gpt-4o',messages=user_text,max_tokens=150)

    Response_text = Response.choices[0].message.content

    interaction = Interaction(text = user_text, response=Response_text)
    db.session.add(interaction)
    try:
        db.session.commit()
    except:
        db.session.rollback()
    return jsonify({"response":Response_text})

