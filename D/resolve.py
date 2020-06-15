def resolve():
    '''
    code here
    '''

    N = int(input())
    A_list = [int(item) for item in input().split()]
    A_list.sort()


    dp = [0 for item in range(A_list[-1]+1)]
    for item in A_list:

        temp = item
        while temp <= A_list[-1]:
            dp[temp] += 1
            temp += item

    cnt = 0
    for item in A_list:
        if dp[item] == 1:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    resolve()
