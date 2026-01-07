from fastapi import FastAPI, Request, HTTPException
import httpx
import os
from dotenv import load_dotenv
from fastapi import FastAPI
load_dotenv()  # ✅ FIRST LINE
from model import mnemoniser
api = FastAPI()


BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

api = FastAPI()

@api.get("/")
async def root():
    return {"status": "running"}

@api.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()

    # Extract message safely
    if "message" not in data:
        return {"ok": True}

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text == "/start":
        reply = "Bot is live. Send any message."
    else:
        reply =  mnemoniser(text)

    # Send reply back to Telegram
    async with httpx.AsyncClient() as client:
        await client.post(
            f"{TELEGRAM_API}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": reply
            }
        )

    return {"ok": True}
