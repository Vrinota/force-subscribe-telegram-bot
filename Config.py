import os

class Config():
    ENV = bool(os.environ.get('ENV', True))  # Default to True if not explicitly set

    if ENV:
        BOT_TOKEN = os.environ.get("BOT_TOKEN")
        DATABASE_URL = os.environ.get("DATABASE_URL")
        APP_ID = int(os.environ.get("API_ID", 6))
        API_HASH = os.environ.get("API_HASH")
        
        # Handle missing or empty SUDO_USERS
        SUDO_USERS = []
        sudo_users_env = os.environ.get("SUDO_USERS", "")
        if sudo_users_env:
            SUDO_USERS = list(set(int(x) for x in sudo_users_env.split()))
        
        SUDO_USERS.append(939425014)  # Your default sudo user
        SUDO_USERS = list(set(SUDO_USERS))

    else:
        BOT_TOKEN = "8179949752:AAHsd3LUfOhz1RwJy1dcZX6BI6ABQqdAXag"
        DATABASE_URL = "sqlite:///force.db"
        APP_ID = 29675937 # Replace with your API ID
        API_HASH = "82e916576259746b890f9164acb1bf52"
        SUDO_USERS = [7199203071]  # Add more if needed


class Messages():
    HELP_MSG = [
        ".",
        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn off ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @viperadnan**"
    ]

    START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
