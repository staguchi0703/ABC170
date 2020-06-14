def resolve():
    '''
    code here
    '''

    in_list = [int(item) for item in input().split()]

    for i, item in enumerate(in_list):
        if item == 0:
            print(i+1)


if __name__ == "__main__":
    resolve()
