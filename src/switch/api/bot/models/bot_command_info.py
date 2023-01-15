from typing import Optional
from switch.base import SwitchObject
from switch.utils.types import JSONDict


class BotCommandInfo(SwitchObject):
    def __init__(
        self,
        command: Optional[str] = None,
        description: Optional[str] = None,
        channel: Optional[bool] = False,
    ):
        self.bot_id = None
        self.command = command
        self.description = description
        self.channel = channel

    def from_json(self, data: JSONDict) -> "BotCommandInfo":
        if data is not None:
            self.bot_id = data.get("botId")
            self.command = data.get("command")
            self.description = data.get("description")
            self.channel = data.get("channel")
        return self

    def to_json(self) -> JSONDict:
        return {
            "botId": self.bot_id,
            "command": self.command,
            "description": self.description,
            "channel": self.channel,
        }
