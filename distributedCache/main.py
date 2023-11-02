import time

from LRUCache import LRUCache
from Node import Node
from network import Network
from replication import Replication
import threading


def rm_expired_items_periodically(cache, rmCycle):
    while True:
        time.sleep(rmCycle)
        cache.remove_expired_items()
def start_periodic_consistency_check(self, interval):
    def check_all_keys():
        while True:
            for key in self.cache.keys():
                if not self.check_consistency(key):
                    print(f"Data inconsistency detected for key {key}")
            time.sleep(interval)
    # Start the background task
    threading.Thread(target=check_all_keys).start()

def main():
    # Initialize the cache
    cache = LRUCache(capacity=2)

    # Initialize the network
    nodes = ["http://localhost:5000", "http://localhost:5001", "http://localhost:5002"]
    network = Network(nodes)

    # Initialize the replication
    replication = Replication(cache, network)
    # Start the periodic consistency check with an interval of 60 seconds
    replication.start_periodic_consistency_check(60)
    # Use the replication to put data into the cache and replicate it across nodes
    replication.put("key1", "value1", 60)
    replication.put("key2", "value2", 60)
    replication.put("key3", "value3", 60)

    # Start a separate thread that removes expired items every 60 seconds
    thread = threading.Thread(target=rm_expired_items_periodically, args=(cache, 60))
    thread.start()


if __name__ == "__main__":
    main()
