from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from datetime import datetime

from db_cfg import Base

class PostsORM(Base):
    __tablename__ = "posts"
    post_id = Column(Integer, primary_key = True, autoincrement = True)
    post_owner = Column(String(20), nullable = False)
    description = Column(Text, nullable = False)
    created_at = Column(TIMESTAMP, default = datetime.now())