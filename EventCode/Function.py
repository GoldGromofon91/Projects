import re


# day 1
def gen_obj(input_data):
    """
    Генерирует список
    :param input_data: передаваемый файл
    :return: список данных
    """
    with open(input_data, 'r') as file:
        file_obj = [int(row.strip()) for row in file]
    return file_obj


def check_2020(data, part=1):
    """
    :param data: входные параметры
    :param part: часть задачи(default =1)
    :return: ответ в зависимости от части задачи
    """
    num_obj = gen_obj(data)
    if part == 1:
        result = [n1 * n2 for id, n1 in enumerate(num_obj) for n2 in num_obj[id:] if n1 + n2 == 2020]
        return print(result[0])
    elif part == 2:
        result = [n1 * n2 * n3 for n1 in num_obj for n2 in num_obj for n3 in num_obj if n1 + n2 + n3 == 2020]
        return print(result[0])


def gen_obj_task_2(input_data):
    """
    Генерирует список
    :param input_data: передаваемый файл
    :return: список данных
    """
    with open(input_data, 'r') as file:
        file_obj = [row.strip() for row in file]  # [:3]  #
    return file_obj


def generate_rules_words(data):
    """
    Generation splitting data
    :param data:
    :return:
    """
    lenght_rule = []
    word_rule = []
    string_check = []
    for unres_string in data:
        lenght_rule.append(unres_string.split(':')[0].split(' ')[0].split('-'))
        word_rule.append(unres_string.split(': ')[0].split(' ')[1])
        string_check.append(unres_string.split(': ')[1])
    return lenght_rule, word_rule, string_check


def check_password(data, part=1):
    """
    Start 2 day
    :param data:
    :param part:
    :return:
    """
    res_count = 0
    file_password = gen_obj_task_2(data)
    length_rule, word_rule, string_check = generate_rules_words(file_password)

    if part == 1:
        for index_word in range(len(string_check)):
            count_word = string_check[index_word].count(word_rule[index_word])
            if word_rule[index_word] in string_check[index_word] and (
                    int(length_rule[index_word][1]) >= count_word >= int(length_rule[index_word][0])):
                res_count += 1
            continue
        return print(res_count)
    elif part == 2:
        for idx_word in range(len(string_check)):
            if word_rule[idx_word] in string_check[idx_word] and (
                    string_check[idx_word][int(length_rule[idx_word][0]) - 1] == word_rule[idx_word] or
                    string_check[idx_word][int(length_rule[idx_word][1]) - 1] == word_rule[idx_word]) \
                    and not (string_check[idx_word][int(length_rule[idx_word][0]) - 1] == word_rule[idx_word] and
                             string_check[idx_word][int(length_rule[idx_word][1]) - 1] == word_rule[idx_word]):
                res_count += 1
        return print(res_count)


# day 3
def count_tree(road_map, stepX, stepY):
    x, y = 0, 0
    count_tree = 0
    while y < len(road_map):
        if road_map[y][x] == '#':
            count_tree += 1
        x = (x + stepX) % len(road_map[0])
        y += stepY
    return count_tree


def check_count_tree(road, part=1, stepX=None, stepY=None):
    """
    Start 3 day
    :param road: map from task
    :param part: part of task
    :param stepX: step to X
    :param stepY: step to Y
    :return: result count tree
    """
    road_obj = gen_obj_task_2(road)
    if part == 1:
        stepX, stepY = 3, 1
        return count_tree(road_obj, stepX, stepY)
    elif part == 2:
        diff_course = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        res = 1
        for idx in diff_course:
            stepX, stepY = idx[0], idx[1]
            res = res * count_tree(road_obj, stepX, stepY)
        return res


# day 4
def get_passport_object(input_data, part=None):
    with open(input_data, 'r') as file:
        obj = file.read().split('\n\n')
        alpha_objects = [elem.replace('\n', ' ') for elem in obj][:30]
        passport_data = []

        for elem in alpha_objects:
            passport_item = {}
            while True:
                match = re.match(r'^(\w\w\w):([^\s]+)\s', elem)
                if not match:break
                key, val = match.groups()
                passport_item[key] = val
                elem = elem[match.span()[1]:]
            passport_data.append(passport_item)
    return passport_data


def check_passport(passport_data, part=None):
    passport_objects = get_passport_object(passport_data)
    print(passport_objects)


if __name__ == '__main__':
    print('Loading from Function.py')
    check_passport('input_t4.txt')
