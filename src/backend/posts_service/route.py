from fastapi import APIRouter, HTTPException

from database.db_repository import db_repo
from .models import PostSchema, NewPostSchema

router = APIRouter(
    prefix = "/posts",
)

# Endpoint to get all posts from database and return the list of them
@router.get("/get_posts", response_model = list[PostSchema])
async def fetch_posts() -> list[PostSchema]:
    try:

        got_posts = await db_repo.get_posts()

        posts = []

        # Then refactoring objects
        for post in got_posts:
            post_obj = PostSchema(
                post_owner = post.post_owner,
                description = post.description,
                created_at = post.created_at
            )
            validated_post = PostSchema.model_validate(post_obj)
            # And adding them do list that will return by endpoint
            posts.append(validated_post)
        return posts
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))


# Endpoint to add new post into a database
@router.post("/add_new_post", response_model = NewPostSchema)
async def add_new_post(
    payload: NewPostSchema
) -> NewPostSchema:
    try:
        await db_repo.add_new_post(payload)
        return payload.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))