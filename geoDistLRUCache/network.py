import requests

class Network:
    def __init__(self, nodes):
        self.nodes = nodes  # A list of URLs for each node in the system

    def send_data(self, key, value):
        for node in self.nodes:
            requests.post(node, data={'key': key, 'value': value})
