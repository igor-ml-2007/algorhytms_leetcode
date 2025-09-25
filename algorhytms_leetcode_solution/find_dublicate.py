def find_duplicate(array: list):
    for i in range(len(array)):
        if array[i] == array[i + 1]:
            return array[i]

