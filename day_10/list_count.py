def frequency_counter(data_list):
    # Write code here
    new_dict = {}
    for i in range(len(data_list)):
        count_1 = data_list.count(data_list[i])
        new_dict[data_list[i]] = count_1

    return new_dict

data_list = [5, 5, 5, 5, 5, 5]


result = frequency_counter(data_list)
print(result)