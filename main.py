from fastapi import FastAPI
from datetime import datetime, timezone
import datetime
from json import JSONEncoder
from http import HTTPStatus
app = FastAPI()

dt = datetime.datetime.now()
dt_str = dt.strftime('%Y-%m-%dT%H:%M:%SZ')

interns = {
        "slack_name" : "JealousAide",
        "current_day" : dt.strftime('%A'),
        "utc_time" : dt_str,
        "track": "backend",
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
def intern_ship(slack_name:str="JealousAide", track:str="backend"):
    return interns