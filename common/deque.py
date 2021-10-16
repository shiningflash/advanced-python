from collections import deque

if __name__ == '__main__':
      # insert back (right)
      dq = deque()
      dq.append(1)
      dq.append(2)
      dq.append(3)
      dq.append(4)
      dq.append(5)
      print(dq) # deque([1, 2, 3, 4, 5])

      # insert front (left)
      dq.appendleft(0)
      print(dq) # deque([0, 1, 2, 3, 4, 5])

      # remove from back (right)
      dq.pop()
      dq.pop()
      print(dq) # deque([0, 1, 2, 3])

      # remove from front (left)
      dq.popleft()
      dq.popleft()
      print(dq) # deque([2, 3])

      # remove all 2
      dq.remove(2)
      print(dq) # deque([3])
