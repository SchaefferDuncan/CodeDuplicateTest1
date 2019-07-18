def a_super_fast_sort(arr, low, high):
    if low < high:
        pi = break_up_the_band(arr, low, high)
        a_super_fast_sort(arr, low, pi - 1)
        a_super_fast_sort(arr, pi + 1, high)
