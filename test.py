from fastapi import FastAPI
import random
from datetime import datetime,timedelta
#-----------------------------------------------------------------------------------------------------------------------

app = FastAPI()
data = {
    "code": None,
    "created_at": None
}
#-----------------------------------------------------------------------------------------------------------------------

@app.get("/generation")
def gen():
    # password = random.randint(100000,999999)
    data ["code"] = random.randint(100000,999999)
    data ["created_at"] = datetime.utcnow()
    return data
#-----------------------------------------------------------------------------------------------------------------------

@app.get("/validate")
def validation(code: int):
    if data["code"] is None:
        return {"status":"No OTP generated yet"}
    # 1
    now = datetime.utcnow()
    created_at = data["created_at"]

    if now - created_at > timedelta(seconds= 10):
        return {"status": "Invalid (expired)"}
    # 2
    if code != data["code"]:
        return {"status": "Invalid (wrong code)"}
    # 3
    return {"status":"OK (valid)"}
    # 4

