def number_pattern(n):
    nums = ''
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        for num in range(1, n+1):
            STR_num = str(num)
            nums += STR_num + ' '
    return nums.rstrip()

print(number_pattern(4))
print(number_pattern(12))