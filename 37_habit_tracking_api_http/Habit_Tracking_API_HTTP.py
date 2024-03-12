import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "yakov256"
TOKEN = "vrbwv4breec5gv21vse"

user_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response_create_user = requests.post(url=pixela_endpoint, json=user_parameters)
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_configure = {
    "id": "graph1",
    "name": "coding",
    "unit": "Km",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

response_create_graph = requests.post(url=graph_endpoint, json=graph_configure, headers=headers)
time_now = datetime.now()
# time_list = time_now.split("-")
# day = time_list[2].split(" ")

graph_post_config = {
    # "date": time_list[0] + time_list[1] + day[0],
    "date": time_now.strftime("%Y%m%d"),
    "quantity": "5",
    "optionalData": ""
}

pixel_post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_configure["id"]}"
response_create_pixel = requests.post(url=pixel_post_endpoint, json=graph_post_config, headers=headers)

yesterday = datetime(year=2024, month=3, day=11).strftime("%Y%m%d")
update_pixel_config = {
    "quantity": "2",
}

update_pixel_endpoint = f"{pixel_post_endpoint}/{yesterday}"
response_update_pixel = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)

delete_pixel_endpoint = update_pixel_endpoint
response_delete_pixel = requests.delete(url=delete_pixel_endpoint, headers=headers)
