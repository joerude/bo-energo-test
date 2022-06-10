def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def find_roots(a, b, c):
    import math

    for color in (a, b, c):
        if not isfloat(color):
            return "Введенные значения должны быть числами"

    a, b, c = float(a), float(b), float(c)

    discriminant = b ** 2 - 4 * a * c  # discriminant
    if discriminant < 0:
        result = 'Корней нет'
    elif discriminant == 0:
        x1 = -b / (2 * a)
        result = f'x = {x1}'
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        result = f'x₁ =  {str(x1)}, x₂ = {str(x2)}'
    return result


def guess_the_color_from_the_number(number):
    from random import randint, sample

    if number < 1 or number > 100:
        return "Ошибка, число должно быть от 1 до 100"

    color_subjects_dict = {}
    subjects = list(range(1, 101))

    red = randint(10, 20)
    green = red + randint(1, 10)
    blue = 100 - green - red

    blue_lst = sample(subjects, blue)
    subjects = [x for x in subjects if x not in blue_lst]
    green_lst = sample(subjects, green)
    subjects = [x for x in subjects if x not in green_lst]
    red_lst = subjects

    color_subjects_dict.setdefault(tuple(blue_lst), "blue")
    color_subjects_dict.setdefault(tuple(green_lst), "green")
    color_subjects_dict.setdefault(tuple(red_lst), "red")

    for subjects, color in color_subjects_dict.items():
        if number in subjects:
            return color
