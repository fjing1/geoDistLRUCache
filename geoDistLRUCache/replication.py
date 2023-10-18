class Replication:
    def __init__(self, cache, network):
        self.cache = cache
        self.network = network

    def put(self, key, value, expiry_time):
        self.cache.put(key, value, expiry_time)
        self.network.send_data(key, value)
