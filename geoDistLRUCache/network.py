import requests
import pickle
import hashlib

class Network:
    def __init__(self, nodes):
        self.nodes = nodes  # A list of URLs for each node in the system

    def send_data(self, key, value):
        # Serialize the value with pickle
        serialized_value = pickle.dumps(value)

        # Determine which node to send the data to based on the key
        node = self._get_node(key)

        # Send the data to the appropriate node
        requests.post(node, data={'key': key, 'value': serialized_value})

    def _get_node(self, key):
        # Use a simple hash of the key to determine the node
        hash_value = hashlib.sha256(key.encode()).hexdigest()
        index = int(hash_value, 16) % len(self.nodes)
        return self.nodes[index]
