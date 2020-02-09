from collections import deque


# Fifo


# Her bruger vi dequeue object
urlstack = deque([])

urlstack.append(1)
urlstack.append(2)
urlstack.append(3)
urlstack.append(4)
print(urlstack)
urlstack.popleft()
print(urlstack)
urlstack.popleft()
urlstack.popleft()
urlstack.popleft()

# Check for empty:
if not urlstack:
    print("empty queue")
