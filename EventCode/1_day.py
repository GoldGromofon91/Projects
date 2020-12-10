from Function import check_2020, check_password,check_count_tree

print('*' * 100 + '\n' + '\t' * 11 + 'First_Day')
check_2020('input.txt', part=1)
check_2020('input.txt', part=2)

print('*' * 100 + '\n' + '\t' * 11 + 'Second_Day')
check_password('input_t2.txt', part=1)
check_password('input_t2.txt', part=2)

print('*' * 100 + '\n' + '\t' * 11 + 'Third_Day')
print(check_count_tree('input_t3.txt', part=1))
print(check_count_tree('input_t3.txt', part= 2))
