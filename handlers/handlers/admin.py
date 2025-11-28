from aiogram import Router, types
from config import ADMIN_ID

router = Router()

@router.message(commands=["panel"])
async def panel(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        return
    
    text = """
🔧 پنل مدیریت:
/ban
/unban
/mute
/unmute
/info
"""
    await msg.answer(text)

@router.message(commands=["info"])
async def info(msg: types.Message):
    chat = msg.chat
    await msg.answer(f"""
📊 اطلاعات:
عنوان: {chat.title}
آیدی: {chat.id}
نوع: {chat.type}
""")
