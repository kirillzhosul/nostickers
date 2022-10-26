from vkbottle.bot import Blueprint, Message


public_bp = Blueprint("For public handlers")


@public_bp.on.chat_message(sticker=[])
async def delete_sticker(message: Message, *args, **kwargs):
    await public_bp.api.messages.delete(
        peer_id=message.peer_id,
        cmids=message.conversation_message_id,
        delete_for_all=True,
    )
