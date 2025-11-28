from aiogram import Router, types
import random

router = Router()

@router.message(commands=["games"])
async def game_list(msg: types.Message):
    await msg.answer("""
🎮 لیست بازی‌ها:
/dice — تاس  
/guess — حدس عدد  
/slot — شانس  
""")

@router.message(commands=["dice"])
async def dice(msg: types.Message):
    await msg.answer_dice()

@router.message(commands=["guess"])
async def guess(msg: types.Message):
    num = random.randint(1, 10)
    await msg.answer("یک عدد بین 1 تا 10 انتخاب کردم!")

@router.message(commands=["slot"])
async def slot(msg: types.Message):
    items = ["🍒","🍉","⭐","💎"]
    r = random.choice(items)
    await msg.answer(f"🎰 نتیجه: {r}")
