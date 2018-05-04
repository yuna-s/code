import sys
#3:fizz 5:bizz 12
check_lst = []
length = len(sys.argv)
argv = sys.argv[1:length]
lest=0

for i, word in enumerate(argv):
    if i == length-2:
        N = word
        try:
            N=int(N)
        except ValueError:
            print("pls type int")
            break
    else:
        strlst = word.split(":")
        try:
            check_lst.append(strlst)
        except ValueError:
            print("pls type int")
            sys.exit()
        #check_strlst.append(strlst[1])

for check in check_lst:
    try:
        i = int(check[0])
    except ValueError:
        print("pls type int")
        sys.exit()

    if N % i == 0:
        print("{0}".format(check[1]), end="")
        lest = 1

if lest == 0:
    print("{0}".format(N), end="")

print()
