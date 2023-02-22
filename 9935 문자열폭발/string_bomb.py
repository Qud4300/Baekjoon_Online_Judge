# BOJ 9935 문자열폭발

string = input().rstrip()
bomb = input().rstrip()
next_cursor = 0
stack = []
checkpoint = []

for c in string:
    stack.append(c)
    if c==bomb[next_cursor]:
        if c==bomb[-1]: # if given char finishes the bomb pattern, bomb explodes.
            while stack[-1] != bomb[0]:
                stack.pop()
            stack.pop() # Bomb pattern completely popped.
            if checkpoint: # if stack contains unfinished bomb pattern, load saved cursor position.
                next_cursor = checkpoint.pop()
            else: # no checkpoint to return?
                next_cursor = 0
        else: # given char is middle of bomb pattern, calm down and keep going.
            next_cursor += 1
    elif c==bomb[0]: # a new start of Bomb is given.
        checkpoint.append(next_cursor) # save current pattern progress.
        next_cursor = 1
    else: # if pattern brokes, reset the cursor
        next_cursor = 0
        checkpoint.clear()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
