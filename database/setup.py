from connection import CURSOR, CONN

def create_tables():
    # Create authors table
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

    # Create magazines table
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """)

    # Create articles table
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY,
            author_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            FOREIGN KEY(author_id) REFERENCES authors(id),
            FOREIGN KEY(magazine_id) REFERENCES magazines(id)
        )
    """)

    CONN.commit()
