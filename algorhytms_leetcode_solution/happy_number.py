# solution 1
def is_happy(n):
    if len(str(n)) == 1:
        return n == 1
    else:
        lst = [int(i) ** 2 for i in str(n)]
        total = sum(lst)
        return is_happy(total)


#solution 2
def sq_numbers(n):
    return sum(int(i) ** 2 for i in str(n))


def is_happy(n):
    if len(str(n)) == 1 and n != 1:
        return False
    if n == 1:
        return True

    slow = sq_numbers(n)
    fast = sq_numbers(sq_numbers(n))
    while slow != fast:
        if slow == 1 or fast == 1:
            return True

        slow = sq_numbers(slow)
        fast = sq_numbers(fast)
    return slow == 1
