from django.conf import settings
import yaml
import requests
from django.http import HttpResponse
from requests.exceptions import HTTPError


def fetch(url):

        response = requests.get(url)
        return response.text


def save(filename, data):
    with open("data/{filename}.json".format(filename=filename), 'w') as file:
        file.write(data)


def fetch_data(request=None):
    egl_server = settings.EGL_SERVER
    print(egl_server)
    with open('endpoint_to_file_map.yaml', 'r') as file:
        map = yaml.safe_load(file)
        for endpoint, data in map.items():
            for filename, query_string in data.items():
                if len(query_string)> 0:
                    url = "http://{egl_server}:8000/rest/{endpoint}?{query_string}".format(egl_server=egl_server,
                                                                                           endpoint=endpoint,
                                                                                           query_string=query_string)
                else:
                    url = "http://{egl_server}:8000/rest/{endpoint}".format(egl_server=egl_server,
                                                                            endpoint=endpoint)
                data = fetch(url)
                save(filename, data)
    if request is not None:
        return HttpResponse("ran cron")