import json
import time
from datetime import datetime

import requests

formatted_date = datetime.today().date()
days = formatted_date.weekday()
formatted_date = '2024-11-04'
days = datetime.strptime(formatted_date, '%Y-%m-%d').date().weekday()



url = "http://192.168.1.170:8080/Login/Login"
insert_url = 'http://192.168.1.170:8080/Admin/Timesheet/InsertMultipleTimesheets'
payload = json.dumps({
    "UserName": "ppatel",
    "Password": "pk7/DgeD8kjXZo9sLj4hnA=="
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
data = response.json()
tk = data.get('token')
token = f'Bearer {tk}'

print(token)

headers1 = {
    'Content-Type': 'application/json',
    'Authorization': token
}
# print(headers1)
ts1 = [{
    "projectId": 1,
    "projectTypeId": 5,
    "moduleId": 1063,
    "task": "EZ Energy tasks",
    "billableHours": "0.50",
    "nonBillableHours": "0",
    "startTime": f"{formatted_date}T04:30:00.000Z",
    "finishTime": f"{formatted_date}T05:00:00.000Z",
    "description": "Reviewed the EZ asana and read the definitions of the tasks and comments",
    "date": f"{formatted_date}",
    "employeeId": 7070,
    "createdBy": 7070
}]
ts1 = json.dumps(ts1)
ts2 = [{
    "projectId": 1,
    "projectTypeId": 6,
    "moduleId": 1063,
    "task": "Morning meeting",
    "billableHours": "0.5",
    "nonBillableHours": "0",
    "startTime": f"{formatted_date}T05:00:00.000Z",
    "finishTime": f"{formatted_date}T05:30:00.000Z",
    "description": "Scrum meeting with team for task planning",
    "date": f"{formatted_date}",
    "employeeId": 7070,
    "createdBy": 7070
}]
ts2 = json.dumps(ts2)
ts3 = [
    {
        "projectId": 1,
        "projectTypeId": 6,
        "moduleId": 1063,
        "task": "Daily BA team meeting",
        "billableHours": "0.5",
        "nonBillableHours": "0",
        "startTime": f"{formatted_date}T05:30:00.000Z",
        "finishTime": f"{formatted_date}T06:00:00.000Z",
        "description": "Define the accountability of the tasks for individuals and clarified the requirement related questions.",
        "date": f"{formatted_date}",
        "employeeId": 7070,
        "createdBy": 7070
    }
]
ts3 = json.dumps(ts3)
ts4 = [
    # {"projectId": 1, "projectTypeId": 5, "moduleId": 1063, "task": "Follow up with the DS team", "billableHours": "0.5",
    #  "nonBillableHours": "0", "startTime": f"{formatted_date}T12:00:00.000Z",
    #  "finishTime": f"{formatted_date}T12:30:00.000Z",
    #  "description": "Followed up with TLs on the completed tasks vs carried forward tasks. ",
    #  "date": f"{formatted_date}", "employeeId": 7070, "createdBy": 7070},
    {"projectId": 1, "projectTypeId": 5, "moduleId": 1063, "task": "Follow up and Asana comments", "billableHours": "0.5",
     "nonBillableHours": "0", "startTime": f"{formatted_date}T12:30:00.000Z",
     "finishTime": f"{formatted_date}T13:00:00.000Z",
     "description": "Took Follow up from BA, dev and QA team and added the tasks status in EZ asana along with the required clarifications from DL",
     "date": f"{formatted_date}", "employeeId": 7070, "createdBy": 7070}]
ts4 = json.dumps(ts4)
ts5 = [{
    "date": f"{formatted_date}",
    "projectId": 1,
    "moduleId": 1063,
    "createdBy": 7070,
    "employeeId": 7070,
    "task": "client meeting",
    "description": "Client meeting to discuss the issues and requirements. Summarize the work with BA team.",
    "billableHours": "1.25",
    "nonBillableHours": "0.00",
    "startTime": f"{formatted_date}T13:15:00.000Z",
    "finishTime": f"{formatted_date}T14:30:00.000Z",
    "projectTypeId": 6
}]
ts5 = json.dumps(ts5)

response1 = requests.request("POST", insert_url, headers=headers1, data=ts1)
print(response1)
print('request 1 is completed')
time.sleep(1)

response2 = requests.request("POST", insert_url, headers=headers1, data=ts2)
print(response2)
print('request 2 is completed')
time.sleep(1)

response3 = requests.request("POST", insert_url, headers=headers1, data=ts3)
print(response3)
print('request 3 is completed')
time.sleep(1)

response4 = requests.request("POST", insert_url, headers=headers1, data=ts4)
print(response4)
print('request 4 is completed')

# if days == 1 or days == 2:
#     response5 = requests.request("POST", insert_url, headers=headers1, data=ts5)
#     print(response5)
#     print('request 5 is completed')
