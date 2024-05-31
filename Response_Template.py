RESPONSE_TEMPLATES = {
    'GREETING': [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Good day! How may I help you?",
        "Hey! How's it going? What do you need help with?",
        "Hi! How can I make your day better?",
        "Greetings! What can I do for you today?",
        "Hello! Hope you're having a great day. How can I help?",
        "Hi! What would you like to know today?"
    ],
    'FAREWELL': [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Farewell! If you need anything else, feel free to ask.",
        "Bye! Have a wonderful day!",
        "Goodbye! I'm here if you need any further assistance.",
        "Take care! Until next time.",
        "Goodbye! Stay safe and take care.",
        "Bye! Don't hesitate to reach out if you need more help."
    ],
    'TIME': [
        "The current time is {time}.",
        "It's {time} right now.",
        "The clock shows {time}.",
        "At this moment, it's {time}.",
        "Right now, it's {time}.",
        "The time now is {time}.",
        "Currently, it's {time}.",
        "It's exactly {time} at the moment."
    ],
    'DATE': [
        "Today is {date}.",
        "The date today is {date}.",
        "It's {date} today.",
        "The calendar shows {date} today.",
        "Today is {date}, mark your calendar!",
        "It's {date} on the calendar today.",
        "We're on {date} today.",
        "The date today is {date}, don't forget!"
    ],
    'WEATHER': [
        "The weather in {location} is currently {weather_condition} with a temperature of {temperature}°C.",
        "It's {weather_condition} and {temperature}°C in {location} right now.",
        "Currently, the weather in {location} is {weather_condition} with a temperature of {temperature}°C.",
        "In {location}, it's {weather_condition} and the temperature is {temperature}°C.",
        "Right now, the weather in {location} is {weather_condition} with a temperature of {temperature}°C.",
        "The current weather in {location} is {weather_condition} with a temperature of {temperature}°C.",
        "The weather today in {location} is {weather_condition} with a temperature of {temperature}°C.",
        "At this moment, the weather in {location} is {weather_condition} and {temperature}°C."
    ],
    'DAY_OF_WEEK': [
        "Today is {day_of_week}.",
        "It's {day_of_week} today.",
        "We're on {day_of_week}.",
        "The day today is {day_of_week}.",
        "It's {day_of_week} at the moment.",
        "Today happens to be {day_of_week}.",
        "On the calendar, it's {day_of_week}.",
        "We're currently on {day_of_week}."
    ],
    'REMINDER': [
        "I've set a reminder for {event} at {time}.",
        "Reminder added: {event} at {time}.",
        "Okay, I've scheduled a reminder for {event} at {time}.",
        "Your reminder for {event} at {time} has been set.",
        "Reminder for {event} at {time} is now scheduled.",
        "I've successfully set a reminder for {event} at {time}.",
        "You will be reminded about {event} at {time}.",
        "A reminder for {event} at {time} has been created."
    ],
    'NOTE_TAKING': [
        "Sure, I've noted that down: {note_content}.",
        "Your note has been saved: {note_content}.",
        "Got it! I've saved your note: {note_content}.",
        "Note saved: {note_content}.",
        "I've made a note of that: {note_content}.",
        "Your note: {note_content} has been recorded.",
        "I've taken a note of that: {note_content}.",
        "Noted: {note_content}. Anything else?"
    ],
    'JOKES': [
        "Why did the chatbot cross the road? To get to the other side!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't some couples go to the gym? Because some relationships don't work out.",
        "Why did the math book look sad? Because it had too many problems."
    ],
    'FACTS': [
        "Did you know? {interesting_fact}",
        "Here's a fun fact: {interesting_fact}",
        "Fact of the day: {interesting_fact}",
        "Interesting fact: {interesting_fact}",
        "Did you know this? {interesting_fact}",
        "Here's something interesting: {interesting_fact}",
        "You might find this interesting: {interesting_fact}",
        "Fun fact: {interesting_fact}"
    ],
    'MOTIVATION': [
        "Keep going! You're doing great.",
        "Success is on the way. Stay determined!",
        "Believe in yourself! You can achieve anything.",
        "Keep pushing forward, you're doing amazing!",
        "Stay positive and keep moving forward!",
        "Don't give up! Great things take time.",
        "Keep your head up and stay focused on your goals.",
        "You have the power to create change. Keep going!"
    ],
    'DIRECTIONS': [
        "To get to {place}, head {direction} and then turn {direction}.",
        "The quickest route to {place} is via {road/street}.",
        "Follow {direction} to reach {place}.",
        "To find {place}, go {direction} and then turn {direction}.",
        "Head {direction} to get to {place}.",
        "You can reach {place} by going {direction} and turning {direction}.",
        "The best way to get to {place} is by heading {direction} and then turning {direction}.",
        "Go {direction} and then {direction} to find {place}."
    ],
    'LOCAL_TIME': [
        "The current time in {location} is {local_time}.",
        "It's {local_time} in {location} right now.",
        "The time in {location} is {local_time}.",
        "Right now, it's {local_time} in {location}.",
        "The clock shows {local_time} in {location}.",
        "At this moment, it's {local_time} in {location}.",
        "Currently, it's {local_time} in {location}.",
        "The time now in {location} is {local_time}."
    ],
    'TECHNICAL_ISSUES': [
        "I'm sorry to hear you're having issues. Can you please provide more details?",
        "Let's try troubleshooting. Have you tried restarting the device?",
        "I understand your frustration. Let's see how we can resolve this.",
        "Can you describe the issue in more detail?",
        "Let's work on fixing this. Have you tried turning it off and on again?",
        "I'm here to help. Can you tell me more about the problem?",
        "Let's figure this out together. What's the issue you're experiencing?",
        "I'm sorry for the trouble. Let's see how we can fix this."
    ],
    'CONTACT_INFORMATION': [
        "You can reach us at {email_address} or call us at {phone_number}.",
        "For further assistance, contact us at {email_address}.",
        "Feel free to email us at {email_address} or call {phone_number}.",
        "You can get in touch with us via email: {email_address} or phone: {phone_number}.",
        "Our contact details are {email_address} and {phone_number}.",
        "For support, email us at {email_address} or call {phone_number}.",
        "Reach out to us at {email_address} or {phone_number}.",
        "Contact us at {email_address} or {phone_number} for more help."
    ],
    'COMPLIMENTS': [
        "Thank you! I appreciate your kind words.",
        "That's very kind of you to say!",
        "I appreciate the compliment!",
        "Thanks a lot! That means a lot to me.",
        "Thank you! I'm glad you think so.",
        "I appreciate your positive feedback!",
        "Thanks! Your words are encouraging.",
        "Thank you for the compliment!"
    ],
    'APOLOGIES': [
        "I'm sorry for any inconvenience caused.",
        "My apologies for the misunderstanding.",
        "I apologize for any trouble caused.",
        "I'm sorry if I've caused any inconvenience.",
        "Please accept my apologies.",
        "I regret any inconvenience caused.",
        "I'm sorry for any issues this may have caused.",
        "I apologize for any inconvenience."
    ],
    'USER_NAME': [
        "Hello {user_name}! How can I assist you today?",
        "Hi {user_name}! What can I do for you?"]
}
