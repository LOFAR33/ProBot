from aiogram import Router, types
import openai
from config import OPENAI_KEY

router = Router()

openai.api_key = OPENAI_KEY

@router.message(commands=["ai"])
async def ai_chat(msg: types.Message):
    q = msg.text.replace("/ai ", "")
    r = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": q}]
    )
    await msg.answer(r.choices[0].message.content)
