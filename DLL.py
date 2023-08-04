from collections import deque

list = deque()
n = int(input())

for loop in range(n):
  input_command = input()

  if input_command == "deleteFirst":
    list.popleft();
  elif input_command == "deleteLast":
    list.pop();
  else:
    com,num = input_command.split()
    if com == "insert":
      list.appendleft(num)
    elif com == "delete":
      if num in list:
        list.remove(num)
print(' '.join(list))