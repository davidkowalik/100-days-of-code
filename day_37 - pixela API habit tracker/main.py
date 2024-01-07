import requests

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
# # create new user
# r = requests.post(url=pixela_endpoint, json=users_params)
# print(r.text)

# create new graph

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
print(graph_endpoint)

graph_params = {
    "id":GRAPH_ID,
    "name":"Programing study",
    "unit":"Hour",
    "type":"float",
    "color":"ajisai",
}
r = requests.post(url=graph_endpoint, json=graph_params)
prnit(r.text)