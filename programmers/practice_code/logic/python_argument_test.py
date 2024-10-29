#!/usr/bin/python3

from queue import PriorityQueue


def set_queue_recursive(queue, data: int):
    queue.put(data * -1)

def get_queue_recursive(queue) -> any:
    if queue.empty():
        return None
    return (queue.get() * -1)




que = PriorityQueue()

set_queue_recursive(que, 100)
print(que.qsize())

print(get_queue_recursive(que))

print(que.qsize())

# print(que.get())

