---
sidebar_position: 1
---

# Bots
Every bot is an instance of the `BotApp` class. You can create a new bot by calling the `BotApp` constructor and passing it the bot token and the bot description.

```python
from swibots import BotApp

app = BotApp("token", "your bot description")

app.run()

```

## Register bot commands

**In order to be able to use the bot commands, you need to register them with the `set_bot_commands` method of the app.** This method accepts a list of `BotCommand` objects.

```python
from swibots import BotApp, BotCommand

app = BotApp("token", "your bot description")

app.set_bot_commands([
    BotCommand("hello", "Hello description", True),
    BotCommand("bye", "By description", False)
])

app.run()
```

The app will update your bot commands every time you run it, you can disable this behavior (for example, you just want to register your commands one time and you are not planning to update them) 
setting `auto_update_bot` param on the `BotApp` constructor to `False`.


:::note
The server will only send commands to the bot if those commands are registered commands database of the bot.
:::

### `BotCommand` class

The `BotCommand` class is a dataclass that contains the following fields:

- `command:str` - The command name.
- `description:str` - The command description.
- `channel:bool` - Whether the command is available for use in communities or not.