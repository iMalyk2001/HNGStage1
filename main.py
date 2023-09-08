from fastapi import FastAPI
import calendar
from datetime import date,datetime
from json import JSONEncoder
from http import HTTPStatus
app = FastAPI()

dt = datetime.now()

interns = {
        "slack_name" : "JealousAide",
        "current_day" : dt.strftime('%A'),
        "utc_time" : dt,
        "track": "Backend",
        "github_file_url":"https://github.com/iMalyk2001/HNGStage1/blob/main/main.py",
        "github_repo_url":"https://github.com/iMalyk2001/HNGStage1",
        "status_code": HTTPStatus.OK.value
    }

class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()


@app.get("/api", status_code= 200)
def intern_ship(slack_name:str="JealousAide", track:str="Backend"):
    return interns