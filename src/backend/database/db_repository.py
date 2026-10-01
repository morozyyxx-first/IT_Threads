import asyncio
from sqlalchemy import select

from posts_service.models import PostSchema, NewPostSchema
from ORMS.posts_orm import PostsORM
from db_cfg import session_maker

class DatabaseRepository:
    def __init__(self):
        # Creating a local session for this clas
        self.session = asyncio.run(session_maker())


        # self.db = db_name
        # self.cursor = self.db.cursor()

        # Creating table when DatabaseRepository initialize
        # self.cursor.execute(
        #     """CREATE TABLE IF NOT EXISTS posts
        #     (post_id INT PRIMARY KEY,
        #     post_owner VARCHAR(20) NOT NULL,
        #     description TEXT NOT NULL,
        #     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
        # )

    # Method to fetch all posts from database,
    # and also we need to order the result by DESC
    async def get_posts(self) -> list[PostSchema]:
        query = select(PostsORM).order_by(PostsORM.created_at.desc())
        res = await self.session.execute(query)
        posts_list = res.scalars().all()
        await self.session.close()

        return posts_list

        # self.cursor.execute(
        #     """SELECT post_owner, description, created_at FROM posts ORDER BY created_at DESC"""
        # )
        # list_of_post_objects = self.cursor.fetchall()
        # return list_of_post_objects if list_of_post_objects else []

    # Method to create a new post
    async def add_new_post(
            self,
            data: NewPostSchema
    ) -> None:
        post_to_add = PostsORM(
            post_owner = data.post_owner,
            description = data.description,
        )
        self.session.add(post_to_add)
        await self.session.commit()
        await self.session.close()

        # obj_to_add = """INSERT INTO posts (post_owner, description, created_at) VALUES (?, ?, ?)"""
        # self.cursor.execute(obj_to_add, (data.post_owner, data.description, datetime.now()))
        # self.db.commit()

db_repo = DatabaseRepository()