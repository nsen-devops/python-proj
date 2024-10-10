import requests
from requests.auth import HTTPBasicAuth
import json
from getpass import getpass

url = "https://nsen.atlassian.net/rest/api/3/project"

jira_user_name = input("Please enter your useremail for jira portal: ")
API_TOKEN = getpass(prompt=f"Please enter your API_TOKEN for user {jira_user_name} to authenticate with jira portal: ")

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

project_name=output[0]["name"]
print(project_name)

