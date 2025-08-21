from pyrogram.types import InlineKeyboardButton

import config
from VenomX import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_, bot_username, owner_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{bot_username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_1"], callback_data="settings_back_helper")
        ],
        [
            InlineKeyboardButton(text=_["S_B_7"], url=config.OWNER_NAME),
            InlineKeyboardButton(text=_["S_B_4"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons
