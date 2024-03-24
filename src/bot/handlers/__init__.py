from .commands import command_router
from .messages import message_router

routers = (command_router, message_router)
