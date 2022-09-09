import re

def differences(file1, file2):
    sec_lines = set(file1).symmetric_difference(file2)
    if sec_lines == set():
        return 'все одинаково\n'
    else:
        return f'{" ".join(sec_lines)} - не совпадение со вторым текстом\n'


def data_array(file):

    return f'Количество символов {len(file)}\nКоличество строк {len(file.split(" "))}\n' \
           f'Количество гласных букв {len(re.findall("([ауоыиэяюе])", file))}\n' \
           f'Количество согласных букв {len(re.findall("([бвгджзйклмнпрстфхцчшщ])", file))}\n' \
           f'Количество цифр {len(re.findall("([1234567890])", file))}\n'


def data_del(file):
    file = file.split(' ')
    item = file.pop(-1)
    return f"удаление последнего слова:\n{' '.join(file)}\n"


def get_max_str(line):
    return f"самая длинная строка: {max(line.split(' '), key=len)}\n"


def get_count(line):
    inp_user = input(f'{line}\nкакое слово:')
    return f'слово "{inp_user}" найдено {line.count(inp_user)} совпадения в тексте'


def compose_a_string(first, second):
    sp = []
    f_line = ''
    s_line = ''

    with open(first, 'r', encoding='utf-8') as file1:
        with open(second, 'r', encoding='utf-8') as file2:
            f_line = file1.read()
            s_line = file2.read()

    sp.append(differences(f_line, s_line))
    sp.append(data_array(f_line))
    sp.append(data_del(f_line))
    sp.append(get_max_str(f_line))
    sp.append(get_count(f_line))

    write_file(sp)


def write_file(sp):
    with open('write_text.txt', 'w', encoding='utf-8') as file:
        for line in sp:
            file.write(line)


compose_a_string('first_text.txt', 'second_text.txt')