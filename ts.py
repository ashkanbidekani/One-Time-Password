import uuid
from datetime import datetime,timedelta
data = {
    "code": None,
    "created_at": None
}

def gen():
    data ["code"] = str(uuid.uuid4())
    data ["created_at"] = datetime.utcnow()
    lst = [data["code"], data["created_at"]]
    return lst
print(gen())