import sys

queue = list()					# deque 안쓰고 list로만 품
n = int(sys.stdin.readline())			# 명령어 숫자 입력

for _ in range(n):
    cmd = sys.stdin.readline()			# 그냥 input()으로 받으면 시간초과
    if "push" in cmd:				# push
        queue.append(int(cmd.split(' ')[1]))
    elif "pop" in cmd:				# pop
        if not queue: print(-1)			# queue가 빈 경우
        else: print(queue.pop(0))
    elif "size" in cmd:				# size
        print(len(queue))
    elif "empty" in cmd:			# empty
        if not queue: print(1)			# queue가 빈 경우
        else: print(0)
    elif "front" in cmd:			# front
        if not queue: print(-1)			# queue가 빈 경우
        else: print(queue[0])
    elif "back" in cmd:				# back
        if not queue: print(-1)			# queue가 빈 경우
        else: print(queue[-1])