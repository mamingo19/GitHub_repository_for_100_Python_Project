import requests
import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1st"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url = pixela_endpoint,json = user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "times",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(response.text)

pixel_creation_endpoint = f" {pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50",
}

# requests.post(url=pixel_creation_endpoint, json = pixel_data, headers = headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "25",
}

# requests.put(url=update_endpoint, json=new_pixel_data, headers = headers)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response1 = requests.delete(url = delete_endpoint, headers = headers)
# print(response1.text)