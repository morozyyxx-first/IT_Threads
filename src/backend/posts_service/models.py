from typing import Union
from pydantic import BaseModel, Field
from datetime import datetime

class PostSchema(BaseModel):
    post_owner: str = Field(..., description = "Post owner username")
    description: str = Field(..., description = "Description of the post")
    created_at: Union[datetime, str] = Field(..., description = "Post creation date")

class NewPostSchema(BaseModel):
    post_owner: str = Field(..., description="Post owner username")
    description: str = Field(..., description="Description of the post")
    created_at: Union[datetime, str] = Field(..., description = "Post creation date")