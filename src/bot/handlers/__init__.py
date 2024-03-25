# from .commands import command_router
# from .messages import message_router
from .handler_commands import command_router
from .handler_messages import message_router

routers = (command_router, message_router)
