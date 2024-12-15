from __init__ import CURSOR, CONN
from author import Author

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return (f"<Article {self.id}: {self.title}, {self.content}, " +
               f"Author ID: {self.author_id}"
               f"Magazine ID: {self.magazine_id}")
    
    @classmethod
    def save(self):
        sql = """
                INSERT OR IGNORE INTO articles (id, title, content, author_id, magazine_id)
                VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.id, self.title, self.content, self.author_id, self.magazine_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    @classmethod
    def author(self):
        """Retrieve the author of the article using its author_id."""
        sql = """
        SELECT * FROM authors WHERE id = ?
        """
        CURSOR.execute(sql, (self.author_id,))
        return CURSOR.fetchone()

    @classmethod
    def magazine(self):
        """Retrieve the magazine of the article using its magazine_id."""
        sql = """
        SELECT * FROM magazines WHERE id = ?
        """
        CURSOR.execute(sql, (self.magazine_id,))
        return CURSOR.fetchone()

