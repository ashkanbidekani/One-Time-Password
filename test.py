from fastapi import FastAPI
import random
from datetime import datetime,timedelta

# from main import otp_data

# from main import otp_data

app = FastAPI()
@app.get("/")
#-----------------------------------------------------------------------------------------------------------------------
def home ():
    def gen():
# ----------------------------------------------------------------------------------------------------------------------
        otp_data = {
            "code": None,
            "created_at": None
        }

# ----------------------------------------------------------------------------------------------------------------------
        otp = random.randint(1000000, 100000000)
        otp_data["code"] = otp
        otp_data["created_at"] = datetime.now()

        return otp_data

    @app.get("/echo")
    def echo(number: int):
        if number == otp_data["code"]:
            return True
        else:
            return False
    return gen()




