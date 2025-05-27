import sqlite3

class Database:
    def __init__(self, path="db.sqlite3"):
        self.path = path
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.path)

    def create_table(self):
        with self.connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    note TEXT
                )
            """)

    def add_contact(self, name, phone, note):
        with self.connect() as conn:
            conn.execute("INSERT INTO contacts (name, phone, note) VALUES (?, ?, ?)", (name, phone, note))

    def delete_contact(self, contact_id):
        with self.connect() as conn:
            conn.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))

    def get_all_contacts(self):
        with self.connect() as conn:
            cursor = conn.execute("SELECT * FROM contacts")
            return cursor.fetchall()

    def clear_all_contacts(self):
        with self.connect() as conn:
            conn.execute("DELETE FROM contacts")
