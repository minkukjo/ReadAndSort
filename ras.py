import sys


if len(sys.argv) > 3:
    filename = sys.argv[1]
    first = int(sys.argv[2])
    second = int(sys.argv[3])
    file = open(filename,'r',encoding="utf-8")
    text_str = file.readlines()
    arr = []
    for line in text_str:
        arr.append(line[first:second])
    
    arr.sort()

    for i in arr:
        print(i)
    
    

    file.close()
