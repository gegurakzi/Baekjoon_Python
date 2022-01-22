import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    out = []
    for i in range(T):
        input_arr = list(map(int, sys.stdin.readline().split(' ')))
        if (input_arr[0] == input_arr[3]) and (input_arr[1] == input_arr[4]):
            if input_arr[2] == input_arr[5]: res = -1
            else: res = 0
        else:
            dist = (input_arr[0] - input_arr[3])**2 + (input_arr[1] - input_arr[4])**2
            rad_outer = (input_arr[2] + input_arr[5])**2
            rad_inner = (input_arr[2] - input_arr[5]) ** 2
            if dist == rad_outer or dist == rad_inner:
                res = 1
            elif dist > rad_outer or dist < rad_inner:
                res = 0
            elif rad_inner < dist and dist < rad_outer:
                res = 2
        out.append(res)
    for elem in out:
        sys.stdout.write(str(elem)+'\n')