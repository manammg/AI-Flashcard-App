import sqlite3

def init_db():
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            tag TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def add_card(question, answer, tag="General"):
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cards (question, answer, tag) VALUES (?, ?, ?)",
                   (question, answer, tag))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()