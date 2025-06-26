import csv
from ast import literal_eval

class RobotMap:
    walls = []
    def __init__(self):
        self.load_map('res/map.csv')

    def parse_coord(self, coord_str):
        """Преобразует строку с координатами в кортеж чисел"""
        return literal_eval(coord_str.strip())
    
    def load_map(self, filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='|')
            for i, row in enumerate(reader):
                start = self.parse_coord(row[0])
                end = self.parse_coord(row[1])
                name = str(i)
                self.walls.append((start, end, name))

    def segments_intersect(a1, a2, b1, b2):
        """
        Проверяет, пересекаются ли отрезки a1a2 и b1b2.

        Параметры:
            a1, a2 (tuple): Координаты (x, y) концов первого отрезка
            b1, b2 (tuple): Координаты (x, y) концов второго отрезка

        Возвращает:
            bool: True если отрезки пересекаются (включая совпадение концов)
            tuple: (x, y) координаты точки пересечения или None
        """
        # Преобразуем точки в удобные переменные
        x1, y1 = a1
        x2, y2 = a2
        x3, y3 = b1
        x4, y4 = b2

        # Вычисляем векторы
        dx12 = x2 - x1
        dy12 = y2 - y1
        dx34 = x4 - x3
        dy34 = y4 - y3

        # Вычисляем знаменатель
        denominator = dy34 * dx12 - dx34 * dy12

        # Проверка на параллельность (включая совпадение)
        if denominator == 0:
            # Отрезки параллельны или совпадают
            # Проверяем лежат ли концы одного отрезка на другом
            def on_segment(p, q, r):
                """Лежит ли точка q на отрезке pr?"""
                return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                        min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

            # Проверяем все 4 возможных случая
            if on_segment(a1, b1, a2):
                return True, b1
            if on_segment(a1, b2, a2):
                return True, b2
            if on_segment(b1, a1, b2):
                return True, a1
            if on_segment(b1, a2, b2):
                return True, a2
            return False, None

        # Вычисляем параметры t и u
        t = (dx34 * (y1 - y3) - dy34 * (x1 - x3)) / denominator
        u = (dx12 * (y1 - y3) - dy12 * (x1 - x3)) / denominator

        # Проверяем пересечение внутри отрезков
        if 0 <= t <= 1 and 0 <= u <= 1:
            # Находим точку пересечения
            x = x1 + t * dx12
            y = y1 + t * dy12
            return True, (x, y)

        return False, None
    
    def RayCust(self, l_vector:list):
        cross = []
        min = 4.0
        for wall in self.walls:
            dot = RobotMap.segments_intersect(wall[0], wall[1], l_vector[0], l_vector[1])
            if (dot[0]):
                dist = ((dot[1][0]-l_vector[0][0])**2 + (dot[1][1]-l_vector[0][1])**2)**0.5
                if dist < min:
                    cross = dot[1]
                    min = dist
        return cross