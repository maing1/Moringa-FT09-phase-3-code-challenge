from __init__ import CURSOR, CONN
from author import Author
from article import Article

class Magazine:
    def __init__(self, id, name, category):
        """Initialize a Magazine instance with its attributes."""
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        """Save the Magazine instance to the database."""
        sql = "INSERT OR IGNORE INTO magazines (id, name, category) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.id, self.name, self.category))
        CONN.commit()

    def __repr__(self):
        return f"<Magazine {self.name}>"
    
    def articles(self):
        """Retrieve all articles associated with this magazine."""
        sql = """
            SELECT * FROM articles WHERE magazine_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        return CURSOR.fetchall()

    def contributors(self):
        """Retrieve all distinct authors who have written articles for this magazine."""
        sql = """
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        return CURSOR.fetchall()

    def article_titles(self):
        """Retrieve all article titles for this magazine."""
        articles = self.articles()
        return [article["title"] for article in articles] if articles else None

    def contributing_authors(self):
        """Retrieve all authors who have written more than 2 articles for this magazine."""
        sql = """
            SELECT a.*, COUNT(ar.id) AS article_count
            FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
            GROUP BY a.id
            HAVING article_count > 2
        """
        CURSOR.execute(sql, (self.id,))
        return CURSOR.fetchall()



