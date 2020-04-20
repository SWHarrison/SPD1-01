def is_armstrong(num):

    if num // 10 == 0:
        return True

    all_0_or_1 = True
    for digit in str(num):

        if digit != "1" and digit != "0":
            all_0_or_1 = False

    if all_0_or_1:
        return False

    flag = True
    sum = 0
    i = 0

    while flag:

        counter = 0

        for digit in str(num):

            counter += int(digit) ** i

        i += 1

        if counter >= num:
            sum = counter
            flag = False

    if sum == num:
        return True

    else:
        return False

print(is_armstrong(9))
print(is_armstrong(10))
print(is_armstrong(153))
print(is_armstrong(154))
