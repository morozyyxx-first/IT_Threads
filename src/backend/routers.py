from fastapi import APIRouter

from posts_service import route

router = APIRouter(prefix = "/api", tags = ["API"])
router.include_router(route.router)
