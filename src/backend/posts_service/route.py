from fastapi import APIRouter, HTTPException

from database.db_repository import db_repo
from .models import PostSchema, NewPostSchema

router = APIRouter(
    prefix = "/posts",
)

# Endpoint to get all posts from database and return the list of them
@router.get("/get_posts", response_model = list[PostSchema])
def fetch_posts() -> list[PostSchema]:
    try:
        if  len(db_repo.get_posts()) == 0:
            raise HTTPException(status_code=404, detail="Posts not found")

        posts = []

        # Then refactoring objects
        for post in db_repo.get_posts():
            post_obj = PostSchema(
                post_owner = post[0],
                description = post[1],
                created_at = post[2]
            )
            validated_post = PostSchema.model_validate(post_obj)
            # And adding them do list that will return by endpoint
            posts.append(validated_post)
        return posts
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))


# Endpoint to add new post into a database
@router.post("/add_new_post", response_model = NewPostSchema)
def add_new_post(
    payload: NewPostSchema
) -> NewPostSchema:
    try:
        db_repo.add_new_post(payload)
        return payload.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))