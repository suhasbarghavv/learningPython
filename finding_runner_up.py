if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    max = 0
    second_max = min(arr)

    for m in arr:
        for n in arr:
            if (n >= m):
                max = n
            else:
                if ((n > second_max) & (n < max)):
                    second_max = n
    
    print second_max
