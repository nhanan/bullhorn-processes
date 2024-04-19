from auth import bullhorn_rest_token 
from datetime import datetime, timedelta
import requests

swimlane = "X"
corp_id = "X"
rest_url = f"https://rest{swimlane}.bullhornstaffing.com/rest-services/{corp_id}"
headers = {"BhRestToken":bullhorn_rest_token()}

now = datetime.now()
time_from = (now - timedelta(hours=24)).strftime("%Y%m%d%H%M%S")

def get_recently_modified_candidates():
    start = 0
    while start < 2000:
        url = f"{rest_url}/search/Candidate?fields=id,name,firstName,lastName,status&sort=-dateLastmodified&query=isDeleted:0 AND dateLastModified:[{time_from} TO *]&count=200&start={str(start)}"
        response = requests.request("GET", url, headers=headers).json()

        def process_field(field):
            if len(field) > 1:
                if field.islower() or field.isupper():
                    field = field.title()
                    return field, True
            return field, False
 
        for people in response['data']:
            first_name = people['firstName'].strip()
            last_name = people['lastName'].strip()
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

get_recently_modified_candidates()
