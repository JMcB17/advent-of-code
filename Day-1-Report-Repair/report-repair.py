with open('input.txt', 'r') as input_file:
    input_raw = input_file.read()

input_list = input_raw.split()

for i in range(len(input_list)):
    for j in range(len(input_list)):
        if i == j:
            continue
        else:
            if input_list[i]+input_list[j] == 2020:
                print(f'i: {i}, j: {j}')
                print(f'product: {i*j}')
