import os

if __name__ == '__main__':

    ### DAY 1 ###

    # read the input
    file_dir = os.path.dirname(__file__)
    input1 = open(os.path.join(file_dir, 'data/input1.txt'), 'r')
    input1_lines = input1.readlines()
    input1.close()

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    digits_text = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = []
    for line in input1_lines:
        big_number = [n for n in line if n in digits]
        small_number = big_number[0] + big_number[-1]
        numbers.append(int(small_number))
    print(sum(numbers))

    numbers = []
    for line in input1_lines:
        order_of_digits_text = []
        for digit in digits_text:
            if digit in line:
                first = line.index(digit)
                second = line.rindex(digit)
                if first != second:
                    order_of_digits_text.append((digits_text.index(digit), second))
                order_of_digits_text.append((digits_text.index(digit), first))

        for digit in digits:
            if digit in line:
                first = line.index(digit)
                second = line.rindex(digit)
                if first != second:
                    order_of_digits_text.append((int(digit), line.rindex(digit)))
                order_of_digits_text.append((int(digit), line.index(digit)))

        sorted_list = sorted(order_of_digits_text, key=lambda x: x[1])
        number = sorted_list[0][0] * 10 + sorted_list[-1][0]
        numbers.append(number)
    print(sum(numbers))
