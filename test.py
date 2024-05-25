def g(path):
    with open(path,"r") as f:
        max1 = int(f.readline())
        max2 = int(f.readline())
        max3 = int(f.readline())
        while not max1>max2>max3:
            if max1<max2:
                max1,max2 = max2, max1
            if max1<max3:
                max1,max3 = max3, max1
            if max2<max3:
                max2,max3 = max3, max2
        print(max1,max2,max3)
        while (s := f.readline()):
            if s:
                current = int(s)
            print(current)
            if current >= max1:
                max1,max2,max3 = current,max1,max2
            elif current >= max2:
                max2,max3 = current,max2
            elif current >= max3:
                max3 = current
    return max1, max2, max3


print(g('numbers.txt'))