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
    print(f"Day 01, Part 1: {sum(numbers)}")

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
    print(f"Day 01, Part 2: {sum(numbers)}")

    ### Day 2 ###

    # read the input
    input2 = open(os.path.join(file_dir, 'data/input2.txt'), 'r')
    input2_lines = input2.readlines()
    input2_lines = [line.split('\n')[0] for line in input2_lines]
    input2.close()

    # order: RED, GREEN, BLUE
    cubes_prompt = [12, 13, 14]

    game_ids = []
    total_power = []
    for line in input2_lines:
        game_id, sets = line.split(':')
        subsets = sets.split(';')
        valid_subset = True
        max_red, max_green, max_blue = 0, 0, 0
        for subset in subsets:
            reached_cubes = subset.split(',')
            cubes_sum = [0, 0, 0]
            for reached_cube in reached_cubes:
                split_list = reached_cube.split(' ')
                split_list = [x for x in split_list if x != '']
                if 'red' in split_list:
                    cubes_sum[0] += int(split_list[0])
                if 'green' in split_list:
                    cubes_sum[1] += int(split_list[0])
                if 'blue' in split_list:
                    cubes_sum[2] += int(split_list[0])

                # for Part 2
                if max_red < cubes_sum[0]:
                    max_red = cubes_sum[0]
                if max_green < cubes_sum[1]:
                    max_green = cubes_sum[1]
                if max_blue < cubes_sum[2]:
                    max_blue = cubes_sum[2]
                power_game = max_red * max_green * max_blue

            for i in [0, 1, 2]:
                if cubes_prompt[i] < cubes_sum[i]:
                    valid_subset = False
        if valid_subset:
            # add the gameID as a number to a list of IDs
            game_ids.append(int(game_id.split(' ')[1]))

        total_power.append(power_game)
    print(f"Day 02, Part 1: {sum(game_ids)}")
    print(f"Day 02, Part 2: {sum(total_power)}")
