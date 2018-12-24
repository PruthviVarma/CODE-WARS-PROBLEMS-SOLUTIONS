def two_sort(array):
    # your code here
    array.sort()
    result_string = ""
    a = array[0]
    for i in a:
        result_string = result_string + i + '***'
    return result_string.rstrip('*')
