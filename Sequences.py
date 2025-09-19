def simple_seq(n: int):
    seq = []
    i = 1
    while i != n+1:
        seq.append(i)
        i += 1
    
    print(*seq)
        
def woodall(n):
    wAll = []
    i = 1
    while i != n+1:
        num = i*2**i-1
        wAll.append(num)
        i += 1
    
    print(*wAll)


def odd_even(n):
    odEv = []
    i = 1
    while i != n+1:
        if i == 1:
            odEv.append(1)
        elif i % 2 != 0:
            num = i**2 -i
            odEv.append(num)
        elif i % 2 == 0:
            num = i**2
            odEv.append(num)

        i += 1
    print(*odEv)

if __name__ == '__main__':
    while True:
        n = int(input("INPUT HERE!: "))

        action = input("CHOOSE: \n[A] - Simple Sequence\n[B] - Woodall Number\n[C] - Even Odd\n").lower()
        if action == 'a':
            simple_seq(n)
        elif action == 'b':
            woodall(n)
        elif action == 'c':
            odd_even(n)
        else:
            print("BOBO ABC nga lang")

