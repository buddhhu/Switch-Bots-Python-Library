from typing import Callable, Optional
import switch
from switch.bots.filters.filter import Filter


class OnUserBan:
    def on_user_ban(self: "switch.BotApp" = None, filter: Optional[Filter] = None) -> Callable:
        """Decorator for handling user ban."""

        def decorator(func: Callable) -> Callable:
            if isinstance(self, switch.BotApp):
                self.add_handler(switch.bots.handlers.UserBannedHandler(func, filter))

            return func

        return decorator
