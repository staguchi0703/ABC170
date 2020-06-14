def resolve():
    '''
    code here
    '''
    X, N = [int(item) for item in input().split()]
    if N > 0:
        a_list = [int(item) for item in input().split()]
        

        a = X
        b = X
        is_not_fond = True
        res = X
        while is_not_fond:
            if a in a_list:
                a += 1
            else:
                res = a
                is_not_fond = False
            if b in a_list:
                b -= 1
            else:
                res = b
                is_not_fond = False

        print(res)
    else:
        print(X)

if __name__ == "__main__":
    resolve()
