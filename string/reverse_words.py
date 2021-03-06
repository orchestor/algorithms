
def reverse(array, i, j):
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

def reverse_words(string):
    arr = list(string)
    n = len(arr)
    reverse(arr, 0, n-1)

    start = None
    for i in range(n):
        if arr[i] == " ":
           if start:
                reverse(arr, start, i-1)
                start = None
        elif i == n-1:
            if start:
                reverse(arr, start, i)
        else:
            if not start:
                start = i
    return "".join(arr)

test = "I am keon kim and I like pizza"
print(test)
print(reverse_words(test))




