# All rights reserved.
#
from typing import Union
from pyrogram.types import InlineKeyboardButton
from config import SUPPORT_CHANNEL, SUPPORT_GROUP
from VenomX import app

def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]

    # Support channel/group düymələrini əlavə etmək
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=SUPPORT_CHANNEL),
                InlineKeyboardButton(text=_["S_B_3"], url=SUPPORT_GROUP),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append([InlineKeyboardButton(text=_["S_B_4"], url=SUPPORT_CHANNEL)])
        if SUPPORT_GROUP:
            buttons.append([InlineKeyboardButton(text=_["S_B_3"], url=SUPPORT_GROUP)])

    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None, OWNER_NAME: str = None):
    """
    OWNER_NAME dəyişəni burada parametr kimi əlavə edildi.
    Dil düyməsi həmişə görünəcək.
    """
    buttons = [
        [InlineKeyboardButton(text=_["S_B_8"], callback_data="settings_back_helper")]
    ]

    # Support channel/group düymələri
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=SUPPORT_CHANNEL),
                InlineKeyboardButton(text=_["S_B_3"], url=SUPPORT_GROUP),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append([InlineKeyboardButton(text=_["S_B_4"], url=SUPPORT_CHANNEL)])
        if SUPPORT_GROUP:
            buttons.append([InlineKeyboardButton(text=_["S_B_3"], url=SUPPORT_GROUP)])

    # Bot qrup əlavə düyməsi
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )

    # Owner və Dil düymələri eyni sətirdə
    owner_row = []
    if OWNER and OWNER_NAME:
        # URL tam formatda olmalıdır
        owner_row.append(
            InlineKeyboardButton(
                text=_["S_B_7"], url=f"https://t.me/RespublicOwner"
            )
        )

    # Dil düyməsi həmişə əlavə edilir
    if _["ST_B_6"]:
        owner_row.append(
            InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")
        )

    if owner_row:
        buttons.append(owner_row)

    return buttons
