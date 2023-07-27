import enum


class EventType(enum.Enum):
    """Represents the type of a event."""

    # Chat
    MESSAGE = "MESSAGE"
    COMMAND = "COMMAND"
    CALLBACK_QUERY = "CALLBACK_QUERY"
    INLINE_QUERY = "INLINE_QUERY"

    # Community
    COMMUNITY_CHANNEL_CREATE = "COMMUNITY_CHANNEL_CREATE"
    COMMUNITY_CHANNEL_UPDATE = "COMMUNITY_CHANNEL_UPDATE"
    COMMUNITY_CHANNEL_DELETE = "COMMUNITY_CHANNEL_DELETE"
    COMMUNITY_GROUP_CREATE = "COMMUNITY_GROUP_CREATE"
    COMMUNITY_GROUP_UPDATE = "COMMUNITY_GROUP_UPDATE"
    COMMUNITY_GROUP_DELETE = "COMMUNITY_GROUP_DELETE"
    COMMUNITY_USER_BAN = "COMMUNITY_USER_BAN"
    COMMUNITY_USER_UNBAN = "COMMUNITY_USER_UNBAN"
    COMMUNITY_MEMBER_JOIN = "COMMUNITY_MEMBER_JOIN"
    COMMUNITY_MEMBER_LEAVE = "COMMUNITY_MEMBER_LEAVE"
    COMMUNITY_UPDATE = "COMMUNITY_UPDATE"
    COMMUNITY_DELETE = "COMMUNITY_DELETE"

    COMMUNITY_UNRESTRICT_USER = "COMMUNITY_UN_RESTRICT_USER"
    COMMUNITY_RESTRICT_USER = "COMMUNITY_RESTRICT_USER"