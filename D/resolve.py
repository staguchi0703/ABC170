def resolve():
    '''
    code here
    '''

    N = int(input())

    A_list = [int(item) for item in input().split()]    
    
    B_list = [0 for item in range(10**6+1)]

    for i in A_list:
        B_list[i] += 1
        
    cnt = 0

    while len(A_list) > 0:
        # print(A_list)
        cnt += 1
        temp = A_list[0]
        del A_list[0]

        is_same = False
        for item in A_list[:]:
            if item == temp:
                is_same = True
            if item % temp == 0:
                A_list.remove(item)
        
        if is_same:
            cnt -= 1

    print(cnt)

if __name__ == "__main__":
    resolve()



    # def is_prime(x):
    #     for i in range(2, int(math.sqrt(x))+1):
    #         if x % i == 0:
    #             return False
    #     else:
    #         return True

    # A_list_prime = [item for item in A_list if is_prime(item)]
    # A_list = [item for item in A_list if not is_prime(item)]
    # print(A_list_prime)
    # print(A_list)
    # cnt = len(A_list_prime)

    # print(cn