import sqlite3 as sql
from datetime import datetime

from posts_service.models import PostSchema, NewPostSchema
from .db_config import settings

db = sql.connect(settings.DB_URL, check_same_thread = False)

class DatabaseRepository:
    def __init__(self, db_name: sql.Connection):
        self.db = db_name
        self.cursor = self.db.cursor()

        # Creating table when DatabaseRepository initialize
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS posts 
            (post_id INT PRIMARY KEY, 
            post_owner VARCHAR(20) NOT NULL, 
            description TEXT NOT NULL, 
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
        )

    # Method to fetch all posts from database,
    # and also we need to order the result by DESC
    def get_posts(self) -> list[PostSchema]:
        self.cursor.execute(
            """SELECT post_owner, description, created_at FROM posts ORDER BY created_at DESC"""
        )
        list_of_post_objects = self.cursor.fetchall()
        return list_of_post_objects if list_of_post_objects else []

    # Method to create a new post
    def add_new_post(
            self,
            data: NewPostSchema
    ) -> None:
        obj_to_add = """INSERT INTO posts (post_owner, description, created_at) VALUES (?, ?, ?)"""
        self.cursor.execute(obj_to_add, (data.post_owner, data.description, datetime.now()))
        self.db.commit()

db_repo = DatabaseRepository(db)