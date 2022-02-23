import json
import requests
from datetime import datetime


TOKEN = ""
URL_PIXE = "https://pixe.la/v1/users" 
USERNAME = ""
SERVER = "graph1"
TODAY = datetime.now()

document_pixe = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=URL_PIXE, json=document_pixe)
# print(response.text)


URL_PIXE_GRAPHS = f"{URL_PIXE}/{USERNAME}/graphs"
document_pixe_graphs = {
    "id": SERVER,
    "name": "Reading book",
    "unit": "page",
    "type": "int",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=URL_PIXE_GRAPHS, json=document_pixe_graphs, headers=header)
# print(response.text)


URL_PIXE_GRAPHS_ADD = f"{URL_PIXE}/{USERNAME}/graphs/{SERVER}"
document_pixe_graphs_add = {
    "date": TODAY.strftime("%Y%m%d"),
    "quantity": "47"
}

# response = requests.post(url=URL_PIXE_GRAPHS_ADD, json=document_pixe_graphs_add, headers=header)

# print(response.text)

URL_PIXE_GRAPHS_UPDATE = f"{URL_PIXE}/{USERNAME}/graphs/{SERVER}/{TODAY.strftime('%Y%m%d')}"
document_pixe_graphs_update = {
    "quantity": "14"
}

# response = requests.put(url=URL_PIXE_GRAPHS_UPDATE, json=document_pixe_graphs_update, headers=header)
# print(response.text)

URL_PIXE_GRAPHS_DELETE = f"{URL_PIXE}/{USERNAME}/graphs/{SERVER}/{TODAY.strftime('%Y%m%d')}"

# response = requests.delete(url=URL_PIXE_GRAPHS_DELETE, headers=header)
# print(response.text)
