from Assistant_Back_End_Flask import app, db  # Make sure to import your Flask app and db

with app.app_context():
    db.create_all()
    print("Database tables created")
