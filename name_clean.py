from auth import bullhorn_rest_token 
from datetime import datetime, timedelta
import requests

swimlane = ""
corp_id = ""
rest_url = f"https://rest{swimlane}.bullhornstaffing.com/rest-services/{corp_id}"
headers = {"BhRestToken":bullhorn_rest_token()}

now = datetime.now()
time_from = (now - timedelta(hours=100)).strftime("%Y%m%d%H%M%S")

def get_recently_commented_candidates():
    start = 200
    while start < 2000:
        print(start)
        url = f"{rest_url}/search/Candidate?fields=id,name,firstName,lastName,status&sort=-dateLastComment&query=isDeleted:0 AND dateLastComment:[{time_from} TO *]&count=200&start={str(start)}"
        response = requests.request("GET", url, headers=headers).json()

        def process_field(field):
            if field is not None and len(field) > 2:
                if field.islower() or field.isupper():
                    field = field.title()
                    field = field.strip()
                    return field, True
            return field, False
 
        for people in response['data']:
            first_name = people['firstName']
            last_name = people['lastName']
            id = people['id']
            payload = {}

            first_name, changed = process_field(first_name)
            if changed:
                payload["firstName"] = first_name

            last_name, changed = process_field(last_name)
            if changed:
                payload["lastName"] = last_name

            if payload:
                payload["name"] = first_name + " " + last_name
                url = f"{rest_url}/entity/Candidate/{id}"
                data = requests.request("POST", url, headers=headers, json=payload)
                print(data.json())


        start +=200

get_recently_commented_candidates()
