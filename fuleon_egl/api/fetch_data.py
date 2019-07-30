from django.conf import settings
import yaml
import requests
from requests.exceptions import HTTPError


def fetch(url):


        response = requests.get(url)
        return response.text



def save(filename, data):
    with open("data/{filename}.json".format(filename=filename), 'w') as file:
        file.write(data)


def fetch_data():
    egl_server = settings.EGL_SERVER
    print(egl_server)
    with open('endpoint_to_file_map.yaml', 'r') as file:
        map = yaml.safe_load(file)
        for filename, query_string in map.items():
            url = "http://{egl_server}:8000/rest/data_links?{query_string}".format(egl_server=egl_server, query_string=query_string)
            data = fetch(url)
            save(filename, data)
