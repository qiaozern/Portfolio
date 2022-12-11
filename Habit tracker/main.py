# documentation: https://docs.pixe.la/

import requests
from datetime import datetime

USERNAME = "qiaozern"
TOKEN = "nuh12jbnggtkbh65op"
GRAPH = "pythonlearning"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# # Create user
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

#----------------------------------------------------------------#

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH,
    "name": "Python Learning Hours",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create graph
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

#----------------------------------------------------------------#

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()

# # Specific day
# today = datetime(year=2022, month=12, day=9)
# print(today.strftime("%Y%m%d"))


graph_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": str(input("How many hour you learn today? "))
}

# Post pixel
graph_response = requests.post(url=pixel_creation_endpoint, json=graph_body, headers=headers)
print(graph_response.text)

#----------------------------------------------------------------#

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "2.25"
}

# # Put pixel (Update)
# update_graph = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(update_graph.text)

#----------------------------------------------------------------#

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

# Delete pixel
# delete_graph = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_graph.text)

#----------------------------------------------------------------#
