from aiogram import Router, types
import time

router = Router()

banned_words = ["porn","sex","xxx","کص","کس"]
banned_links = ["discord.gg","joinchat","porn","xnxx"]

user_flood = {}
user_warn = {}

MAX_MSG = 5
MAX_WARN = 3

@router.message()
async def anti_spam(msg: types.Message):
    uid = msg.from_user.id
    now = time.time()

    if uid not in user_flood:
        user_flood[uid] = []
    user_flood[uid] = [t for t in user_flood[uid] if now - t < 3]
    user_flood[uid].append(now)

    if len(user_flood[uid]) > MAX_MSG:
        await msg.chat.restrict(user_id=uid, permissions={"can_send_messages": False})
        await msg.answer("🚫 ارسال پیام زیاد — سکوت شدید!")
        return

    if msg.text:
        low = msg.text.lower()

        if any(w in low for w in banned_words):
            await msg.delete()
            user_warn[uid] = user_warn.get(uid, 0) + 1

            if user_warn[uid] >= MAX_WARN:
                await msg.chat.ban(uid)
                await msg.answer("⛔ کاربر ۳ اخطار گرفت و اخراج شد")
            else:
                await msg.answer(f"⚠️ اخطار {user_warn[uid]}/3")

            return

        if any(l in low for l in banned_links):
            await msg.delete()
            await msg.answer("⛔ ارسال لینک ممنوع است.")
            return

    if msg.new_chat_members:
        for u in msg.new_chat_members:
            if u.is_bot:
                await msg.chat.ban(u.id)
                await msg.answer("🤖 ربات ناشناس حذف شد.")
