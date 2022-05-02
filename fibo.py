
def recursive_nth_fibo(idx_in_fibo):
    if idx_in_fibo == 0:
        return 0
    if idx_in_fibo == 1:
        return 1
    else:
        return recursive_nth_fibo(idx_in_fibo - 1) + recursive_nth_fibo(idx_in_fibo -2)




def main():
    idx_in_fibo = int(input("write num: "))
    print(recursive_nth_fibo(idx_in_fibo))

    fibo_list = []
    for num in range(0, idx_in_fibo+1):
        fibo_list.append(recursive_nth_fibo(num))
    print(fibo_list)



if __name__ == "__main__":
    main()
