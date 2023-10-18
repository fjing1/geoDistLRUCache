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


def main():
    # Initialize the cache
    cache = LRUCache(capacity=2, expiration=60)

    # Initialize the network
    nodes = ["http://localhost:5000", "http://localhost:5001", "http://localhost:5002"]
    network = Network(nodes)

    # Initialize the replication
    replication = Replication(cache, network)

    # Use the replication to put data into the cache and replicate it across nodes
    replication.put("key1", "value1")
    replication.put("key2", "value2")
    replication.put("key3", "value3")

    # Start a separate thread that removes expired items every 60 seconds
    thread = threading.Thread(target=rm_expired_items_periodically, args=(cache, 60))
    thread.start()


if __name__ == "__main__":
    main()
