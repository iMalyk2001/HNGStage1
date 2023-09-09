from fastapi import FastAPI
import pytz
from datetime import datetime
from http import HTTPStatus
app = FastAPI()


time_wat = datetime.utcnow()

interns = {
        "slack_name" : "JealousAide",
        "current_day" : time_wat.strftime('%A'),
        "utc_time" : datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": "backend",
        "github_file_url":"https://github.com/iMalyk2001/HNGStage1/blob/main/main.py",
        "github_repo_url":"https://github.com/iMalyk2001/HNGStage1",
        "status_code": HTTPStatus.OK.value
    }




@app.get("/api", status_code= 200)
async def intern_ship(slack_name:str="JealousAide", track:str="backend"):
    return interns