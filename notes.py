import json
import os

NOTES_FILE = os.path.expanduser("~/.notes.json")

class NoteManager:
    def __init__(self):
        self.notes = self._load()

    def _load(self):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE) as f:
                return json.load(f)
        return []

    def _save(self):
        with open(NOTES_FILE, "w") as f:
            json.dump(self.notes, f, indent=2)

    def add(self, text: str):
        self.notes.append({"text": text})
        self._save()

    def get_all(self):
        return self.notes

    def delete(self, index: int):
        if 0 <= index < len(self.notes):
            self.notes.pop(index)
            self._save()
