#include <memory>

class Node {
public:
    int expiration;
    int key;
    int value;
    std::shared_ptr<Node> prev;
    std::shared_ptr<Node> next;

    Node(int key, int value, int expiration, std::shared_ptr<Node> prev = nullptr, std::shared_ptr<Node> next = nullptr) 
        : key(key), value(value), expiration(expiration), prev(prev), next(next) {}
};
