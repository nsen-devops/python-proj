from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

my_app = Flask(__name__)

@my_app.route('/jira', methods = ["GET","POST"])
def createjiraticket():
    url = "https://domain.atlassian.net/rest/api/3/project"

    jira_user_name = ""
    API_TOKEN = ""
    auth = HTTPBasicAuth(jira_user_name, API_TOKEN)

    headers = {
    "Accept": "application/json"
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
    )

    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    output=json.loads(response.text)
    project_name=[]
    for i in range(len(output)):
        proj_name=output[i]["name"]
        project_name.append(proj_name)
    return project_name
if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)
