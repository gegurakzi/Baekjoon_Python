import sys

def next_state(state, char):
    if state == 'i':
        if char == '0':
            return 'a'
        elif char == '1':
            return 'b'
    elif state == 'a':
        if char == '0':
            return 'h'
        elif char == '1':
            return 'i'
    elif state == 'b':
        if char == '0':
            return 'c'
        elif char == '1':
            return 'h'
    elif state == 'c':
        if char == '0':
            return 'd'
        elif char == '1':
            return 'h'
    elif state == 'd':
        if char == '0':
            return 'd'
        elif char == '1':
            return 'e'
    elif state == 'e':
        if char == '0':
            return 'a'
        elif char == '1':
            return 'f'
    elif state == 'f':
        if char == '0':
            return 'g'
        elif char == '1':
            return 'f'
    elif state == 'g':
        if char == '0':
            return 'd'
        elif char == '1':
            return 'i'

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    out = []
    for i in range(T):
        input_arr = sys.stdin.readline()
        state = 'i'
        for char in input_arr:
            if char == '\n':
                break
            state = next_state(state, char)
            if state == 'h':
                break
        if state == 'f' or state == 'i' or state == 'e':
            res = 'YES'
        else:
            res = 'NO'
        out.append(res)
    for elem in out:
        sys.stdout.write(str(elem)+'\n')