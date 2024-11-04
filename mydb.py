import json
import os


class Database:

    def __init__(self, db_file='db.json'):
        self.db_file = db_file
        self._initialize_db()

    def _initialize_db(self):
        """Create an empty db.json file if it doesn't exist."""
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as db:
                json.dump({}, db)

    def _load_data(self):
        """Load the JSON data from db.json."""
        try:
            with open(self.db_file, 'r') as rf:
                return json.load(rf)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def _save_data(self, data):
        """Save data to db.json."""
        with open(self.db_file, 'w') as wf:
            json.dump(data, wf, indent=4)

    def add_data(self, name, email, password):
        """Add new user data to the database if the email does not already exist."""
        database = self._load_data()

        if email in database:
            return 0  # Email already exists
        else:
            database[email] = [name, password]
            self._save_data(database)
            return 1  # Registration successful

    def search(self, email, password):
        """Search for a user with the given email and password."""
        database = self._load_data()

        if email in database and database[email][1] == password:
            return 1  # Login successful
        else:
            return 0  # Incorrect email or password
