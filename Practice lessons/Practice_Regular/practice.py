import re
"""Перевірити, що рядок складається виключно з літер, цифр, знаків підкреслення та пробілів.
    Попередня задача, але рядок додатково повинен мати від 10 до 20 символів включно"""
"""Попередня задача, але рядок не повинен починатись та закінчуватись проміжком"""

def check(string):
    # pattern = re.compile('^\w[\s\w]{8,18}\w$')
    if re.fullmatch('^\w[\s\w]{8,18}\w$', string):
        return True
    return False

mylist = ['1_2_3_4_5_6_7_8_', '111111111111111111111']

for el in mylist:
    print(el, check(el), len(el))


"""Написати функцію, що для об’єкта класу Point генерує рядок зі звичним для математики
зображенням точки площини (координати в круглих дужках через кому)"""

def point_generator(input_string):
    pattern = re.compile(r'\bPoint\(([0-9]+),([0-9]+)\)')
    res = re.sub(pattern, r'\g<1>, \g<2>', input_string)
    
    return res

print(point_generator('Point(1,2)'))