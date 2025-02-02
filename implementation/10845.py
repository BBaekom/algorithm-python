import sys, queue

input = sys.stdin.readline

q = queue.Queue()

N = int(input().rstrip())

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        q.put(cmd[1])
    elif cmd[0] == 'pop':
        if q.empty():
            print(-1)
        else:
            print(q.get())
    elif cmd[0] == 'size':
        print(q.qsize())
    elif cmd[0] == 'empty':
        if q.empty():
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if q.empty():
            print(-1)
        else:
            print(q.queue[0])
    elif cmd[0] == 'back':
        if q.empty():
            print(-1)
        else:
            print(q.queue[-1])
        
        