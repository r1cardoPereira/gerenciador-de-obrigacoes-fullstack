from fastapi import APIRouter

from app.api.routes import items, login, private, users, utils
from app.api.routes.document import router as document_router 
from app.api.routes.company import router as company_router
from app.api.routes.notification import router as notification_router
from app.api.routes.reminder import router as reminder_router

from app.core.config import settings

api_router = APIRouter()

api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(utils.router)
api_router.include_router(items.router)
api_router.include_router(document_router)
api_router.include_router(company_router)
api_router.include_router(notification_router)
api_router.include_router(reminder_router)


if settings.ENVIRONMENT == "local":
    api_router.include_router(private.router)
