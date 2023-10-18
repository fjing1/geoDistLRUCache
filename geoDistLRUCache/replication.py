class Replication:
    def __init__(self, cache, network):
        self.cache = cache
        self.network = network

    def put(self, key, value):
        self.cache.put(key, value)
        self.network.send_data(key, value)
