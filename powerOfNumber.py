def power(n, p) -> int :
    if p==0 :
        return 1

    return (n*power(n, p-1))


if __name__ == '__main__':
    n=input()
    p=input()
    print(power(int(n), int(p)))
