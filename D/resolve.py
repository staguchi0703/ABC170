def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    A_list = [int(item) for item in input().split()]

    A_list.sort()
    cnt = 0

    if A_list:
        dp = [True for item in range(A_list[-1]+1)]
        for item in A_list:
            if dp[item]: 
                temp = item
                while temp <= A_list[-1]:
                    temp += item
                    dp[temp] = False

    for item in A_list:
        if dp[item]:
            # dp[item]が複数か単数かの判断を入れたら行けるはず
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    resolve()
