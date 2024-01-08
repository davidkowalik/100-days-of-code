import requests
from datetime import datetime

# my graph url: https://pixe.la/v1/users/noobby/graphs/graph001.html

PIXELA_TOKEN = "d$3k*Ah&F2JTAjWM"
USER_NAME = "noobby"
GRAPH_ID = "graph001"

pixela_endpoint = "https://pixe.la/v1/users"
users_params = {
    "token":PIXELA_TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

pixela_headers = {
    "X-USER-TOKEN":PIXELA_TOKEN
}

# # create new user-----------------------------------------------
# r = requests.post(url=pixela_endpoint, json=users_params)
# print(r.text)

# # create new graph------------------------------------------

# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
# print(graph_endpoint)


# graph_params = {
#     "id":GRAPH_ID,
#     "name":"Programing study",
#     "unit":"Hour",
#     "type":"float",
#     "color":"ajisai",
# }
# r = requests.post(url=graph_endpoint, json=graph_params, headers=pixela_headers)
# print(r.text)

# add pixel to the graph------------------------------------------
today = datetime.now()

s=today.strftime("%Y%m%d")

add_pixel_body={
    "date":today.strftime("%Y%m%d"),
    "quantity":"2",
}

add_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
r = requests.post(url=add_pixel_endpoint, json=add_pixel_body, headers=pixela_headers)
print(r.text)
print(s)

# update pixel-------------------------------------------
# update_pixel_body={
#     "quantity":"1",
# }

# update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# r = requests.delete(url=update_pixel_endpoint, headers=pixela_headers)
# print(r.text)
