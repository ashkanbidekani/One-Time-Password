import random
from datetime import datetime,timedelta
#---------------------------------------------------------------------------------------------------------------------
otp_data = {
    "code": None,
    "created_at": None
}
#---------------------------------------------------------------------------------------------------------------------
def gen():
    otp = random.randint(1000000,100000000)
    otp_data ["code"] = otp
    otp_data ["created_at"] = datetime.now()
    return otp_data
#---------------------------------------------------------------------------------------------------------------------
def validation(input_code):
    if otp_data["code"] == None:
        return "There is no generated password "
    now = datetime.now()
    created = otp_data["created_at"]

    if now - created > timedelta(seconds=10):
        return "Your one-time password has expired. "

    if input_code == otp_data["code"] :
        return "The password is Correct"

    else:
        return "The passsword is not correct"
#---------------------------------------------------------------------------------------------------------------------
code = gen()
print("OTP:", code)
#---------------------------------------------------------------------------------------------------------------------
user_input = int(input("Enter OTP: "))
print(validation(user_input))