//
// Created by Fei Jing on 2023-12-14.
//

#ifndef GEODISTLRUCACHE_LINKEDLIST_H
#define GEODISTLRUCACHE_LINKEDLIST_H

#include <memory>

class Node {
public:
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;
};

class LinkedList {
public:
    LinkedList() : head(nullptr), tail(nullptr) {}

    void add_to_head(std::shared_ptr<Node> item) {
        if (head != nullptr) {
            item->next = head;
            head->prev = item;
        }

        if (tail == nullptr) {
            tail = item;
        }

        head = item;
    }

    void unlink(std::shared_ptr<Node> item) {
        if (item == nullptr) {
            return;
        }

        auto prev_item = item->prev.lock();
        auto next_item = item->next;

        if (prev_item != nullptr) {
            prev_item->next = next_item;
        }

        if (next_item != nullptr) {
            next_item->prev = prev_item;
        }

        if (head == item) {
            head = next_item;
        }

        if (tail == item) {
            tail = prev_item;
        }

        item->prev.reset();
        item->next.reset();
    }

private:
    std::shared_ptr<Node> head;
    std::shared_ptr<Node> tail;
};

#endif //GEODISTLRUCACHE_LINKEDLIST_H
