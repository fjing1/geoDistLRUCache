class Replication:
    def __init__(self, cache, network):
        self.cache = cache
        self.network = network

    def put(self, key, value, expiry_time):
        self.cache.put(key, value, expiry_time)

        # Replicate the data to all secondary nodes
        for node in self.network.nodes:
            # Iterate all the nodes
            self.network.send_data(key, value)
            if node != self.primary_node:
                # Here we assume that `send_data` sends a request to the node
                # to perform the write operation.
                self.network.send_data(node, key, value)
        # As consistency is very important for distributed cacheing or database system
        # here I conceptually implemented it, for future expansion
        def check_consistency(self, key):
            primary_value = self.cache.get(key)
            for node in self.network.nodes:
                if node != self.primary_node:
                    node_value = self.network.get_data(node, key)
                    if node_value != primary_value:
                        return False
            return True