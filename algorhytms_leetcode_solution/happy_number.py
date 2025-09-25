def is_happy(n):
    if len(str(n)) == 1:
        return n == 1
    else:
        lst = [int(i) ** 2 for i in str(n)]
        total = sum(lst)
        return is_happy(total)

