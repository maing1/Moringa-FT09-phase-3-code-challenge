from __init__ import CURSOR, CONN

class Author:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.id}: {self.name}>'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        if not hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed after instantiation.")
        self._name = name

    @classmethod
    def save(self):
        """ Insert a new row with the name value of the current Author instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO departments (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM authors
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def articles(self):
        """Return list of employees associated with current department"""
        from article import Article
        sql = """
            SELECT * FROM articles
            WHERE author_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Article.instance_from_db(row) for row in rows
        ]

    def magazines(self):
        sql = """
            SELECT DISTINCT magazines.id, magazines.name, magazines.category 
            FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [
            type("Magazine", (), {"id": row[0], "name": row[1], "category": row[2]})
            for row in rows
        ]
