"""Import all routers and add them to routers_list."""
from .admin import admin_router
from .notification import notification_router
from .user import user_router

routers_list = [
    admin_router,
    user_router,
    notification_router,
]

__all__ = [
    "routers_list",
]
