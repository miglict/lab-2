import math


def calculate_area():
    print("Вычисление площади заштрихованной фигуры")

    try:
        # запрос радиуса
        r = float(input("Введите радиус R: "))

        if r < 0:
            print("Ошибка: Радиус не может быть отрицательным.")
            return

        # Вычисляем площадь по частям
        # 1. Треугольник во II четверти: (1/2) * R * R
        s_triangle = 0.5 * r * r

        # 2. Сектор в I четверти (четверть круга): (pi * R^2) / 4
        s_sector_1 = (math.pi * r ** 2) / 4

        # 3. Полукруг внизу (III и IV четверти): (pi * R^2) / 2
        s_semicircle = (math.pi * r ** 2) / 2

        # Суммарная площадь
        total_area = s_triangle + s_sector_1 + s_semicircle

        # Вывод результата
        print("-" * 30)
        print(f"Площадь треугольника: {s_triangle:.4f}")
        print(f"Площадь верхнего сектора: {s_sector_1:.4f}")
        print(f"Площадь нижнего полукруга: {s_semicircle:.4f}")
        print("=" * 30)
        print(f"Итоговая площадь фигуры: {total_area:.4f}")

    except ValueError:
        print("Ошибка: Пожалуйста, введите числовое значение.")


if __name__ == "__main__":
    calculate_area()