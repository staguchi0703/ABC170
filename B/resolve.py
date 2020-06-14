def resolve():
    '''
    code here
    '''
    X, Y = [int(item) for item in input().split()]

    if 0 <= (Y - 2*X) <= 2*X:
        b = (Y - 2*X) % 2
        print('Yes') if b==0 else print('No')
    else:
        print('No')


if __name__ == "__main__":
    resolve()
