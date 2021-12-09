# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def check_double_digit(_number: str) -> bool:
    for i in range(len(_number)-1):
        if _number[i] == _number[i+1]:
            return True
    return False


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def are_digits_greater_or_equal(_number: str) -> bool:
    for i in range(len(_number)-1):
        if int(_number[i+1]) < int(_number[i]):
            return False
    return True


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def check_double_digit_ex(_number: str) -> bool:
    doubles = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(_number)-1):
        if _number[i] == _number[i+1]:
            doubles[int(_number[i])] += 1;

    for d in doubles:
        if d == 1:
            return True;
    return False


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
start = 108457
end = 562041

count = 0
for number in range(start, end+1):
    number_string = str(number)
    if check_double_digit(number_string) and are_digits_greater_or_equal(number_string):
        count += 1
print(f'#1 passwords: {count}')

count = 0
for number in range(start, end+1):
    number_string = str(number)
    if check_double_digit_ex(number_string) and are_digits_greater_or_equal(number_string):
        count += 1
print(f'#2 passwords: {count}')