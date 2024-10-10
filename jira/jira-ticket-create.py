import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nsen.atlassian.net/rest/api/3/project"

jira_user_name = input("Please enter your useremail for jira portal: ")
API_TOKEN = input(f"Please enter your API_TOKEN for user {jira_user_name} to authenticate with jira portal: ")

auth = HTTPBasicAuth(jira_user_name, API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Order entry fails when selecting supplier.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10003"
    },
    "project": {
      "key": "AB"
    },
    "summary": "Main order flow broken"
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

