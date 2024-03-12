from auth import start 
import requests

swimlane = SWIMLANE
corp_id = CORP_ID
rest_url = f"https://rest{swimlane}.bullhornstaffing.com/rest-services/{corp_id}"
BhRestToken = start()
headers = {"BhRestToken":BhRestToken}


# Find all client contacts with "Salesforce App Cloud" as a Skill
def get_client_contacts_with_field_value():
    start = 0
    url = f"{rest_url}/query/ClientContact?fields=id,clientCorporation,skills&sort=-id&where=skills.name='Salesforce App Cloud'&count=200&start={str(start)}"
    headers = {"BhRestToken":BhRestToken}
    response = requests.request("GET", url, headers=headers).json()
    num_of_results = len(response['data'])

    while num_of_results > 199:
        url = f"{rest_url}/query/ClientContact?fields=id,clientCorporation,skills&sort=-id&where=skills.name='Salesforce App Cloud'&count=200&start={str(start)}"
        response = requests.request("GET", url, headers=headers).json()
        start += 200
        num_of_results = len(response['data'])
        for dm in response['data']:
            print(dm['id'])
            bhid = str(dm['clientCorporation']['id'])
            add_org_cloud(bhid,"Salesforce App Cloud")
    else:
        url = f"{rest_url}/query/ClientContact?fields=id,clientCorporation,skills&sort=-id&where=skills.name='Salesforce App Cloud'&count=200&start={str(start)}"
        response = requests.request("GET", url, headers=headers).json()
        num_of_results = len(response['data'])
        for dm in response['data']:
            print(dm['id'])
            bhid = str(dm['clientCorporation']['id'])
            add_org_cloud(bhid,"Salesforce App Cloud")
        return
            
# Add new value ("Salesforce App Cloud") to "customTextBlock3" field on client contact's org
def add_org_cloud(bhid, new_cloud):
    url = f"{rest_url}/entity/ClientCorporation/{bhid}?fields=id,customTextBlock3" #customTextBlock3 is new field to write into
    data = requests.request("GET", url, headers=headers).json()
    # print(data)
    cloud_list = data['data']['customTextBlock3']
    if cloud_list is None:
        cloud_list = new_cloud
        payload = {"customTextBlock3" : cloud_list}
        data = requests.request("POST", url, headers=headers, json=payload)
        print(data.json())
    else:
        if new_cloud not in cloud_list:
            cloud_list.append(new_cloud)
            payload = {"customTextBlock3" : cloud_list}
            data = requests.request("POST", url, headers=headers, json=payload)
            print(data.json())

get_client_contacts_with_field_value()
