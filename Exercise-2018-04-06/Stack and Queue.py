# # Stack
# # Last-in-First-Out
# stack = ['book1', 'book2', 'book3']
# print(stack)
#
# stack.append('book4')
# print(stack)
# for i in range(4):
#     print(stack.pop())
# print(stack)
#


# Queue
# First-in-First-out
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append('Erica')
print(queue)
print(queue.popleft())
print(queue)
