# solution 1
def find_duplicate(array: list):
    for i in range(len(array)):
        if array[i] == array[i + 1]:
            return array[i]

# solution 2
def find_duplicate(array):
    fast, slow = 0, 0
    while True:
        slow = array[slow]
        fast = array[array[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = array[slow]
        slow2 = array[slow2]
        if (slow == slow2):
            return slow


