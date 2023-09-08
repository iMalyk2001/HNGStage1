from fastapi import FastAPI
import datetime
from json import JSONEncoder
from http import HTTPStatus
app = FastAPI()


interns = {
        "slack_name" : "JealousAide",
        "track": "Backend",
        "utc_time" : datetime.datetime.now(),
        "github_file_url":"",
        "github_repo_url":"",
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