import json
import os

class UserManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences_file = f"user_{user_id}_preferences.json"
        self.history_file = f"user_{user_id}_history.json"
        self.preferences = self._load_preferences()
        self.history = self._load_history()

    def _load_preferences(self):
        if os.path.exists(self.preferences_file):
            with open(self.preferences_file, "r") as f:
                return json.load(f)
        return {"topics": []}

    def _load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as f:
                return json.load(f)
        return []

    def save_preferences(self):
        with open(self.preferences_file, "w") as f:
            json.dump(self.preferences, f)

    def save_history(self):
        with open(self.history_file, "w") as f:
            json.dump(self.history, f)

    def add_topic(self, topic):
        if topic not in self.preferences["topics"]:
            self.preferences["topics"].append(topic)
            self.save_preferences()

    def add_history(self, query):
        self.history.append(query)
        self.save_history()