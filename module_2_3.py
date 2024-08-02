my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
while number < len(my_list):
    digit = number
    number = number + 1
    if my_list[digit] == 0:
        continue
    elif my_list[digit] < 0:
       break
    else:
        print(my_list[digit])