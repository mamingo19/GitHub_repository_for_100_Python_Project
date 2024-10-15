import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "xryctfuvygibhuon786",
    "username": "darwind",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url = pixela_endpoint,json = user_params)
print(response.text)