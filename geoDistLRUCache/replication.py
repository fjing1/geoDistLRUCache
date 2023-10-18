class Replication:
    def __init__(self, cache, network):
        self.cache = cache
        self.network = network

    def put(self, key, value, expiry_time):
        self.cache.put(key, value, expiry_time)
        self.network.send_data(key, value)

        # Replicate the data to all secondary nodes
        for node in self.network.nodes:
            if node != self.primary_node:
                # Here we assume that `send_data` sends a request to the node
                # to perform the write operation. You might need to modify this
                # based on your actual network communication code.
                self.network.send_data(node, key, value)