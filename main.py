from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()  # ✅ FIRST LINE
from .model import mnemoniser
api = FastAPI()

@api.get("/")
async def root():
    return {"message": "Hello World"}

payload = {
    "message": "What is cagr"
}
# a = payload.get("message")
# print(a)

# @api.post("/telegram/webhook")
def listener(payload: dict):
    message = payload.get("message")
    print("The User Prompt is ", message)
    print("The User Prompt  type is ", type(message))
    if not message:
        return {"satus": True}
    
    response = mnemoniser(message)
    print(response)

    return {"data": response}

    

listener(payload)

