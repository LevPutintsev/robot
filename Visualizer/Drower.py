import pygame
import csv
from ast import literal_eval

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Визуализация карты помещения")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Масштабирование координат (так как исходные координаты в диапазоне 0..1)
SCALE = 500
OFFSET_X, OFFSET_Y = 100, 50

def parse_coord(coord_str):
    """Преобразует строку с координатами в кортеж чисел"""
    return literal_eval(coord_str.strip())

def load_map(filename):
    """Загружает карту из CSV файла"""
    walls = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|')
        next(reader)  # Пропускаем заголовок
        for row in reader:
            start = parse_coord(row[0])
            end = parse_coord(row[1])
            walls.append((start, end))
    return walls

def draw_map(walls):
    """Отрисовывает карту на экране"""
    for start, end in walls:
        # Масштабируем координаты и смещаем для визуализации
        x1 = OFFSET_X + start[0] * SCALE
        y1 = OFFSET_Y + start[1] * SCALE
        x2 = OFFSET_X + end[0] * SCALE
        y2 = OFFSET_Y + end[1] * SCALE
        
        # Рисуем стену
        pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 3)
        
        # Рисуем точки начала и конца (для наглядности)
        pygame.draw.circle(screen, RED, (int(x1), int(y1)), 5)
        pygame.draw.circle(screen, BLUE, (int(x2), int(y2)), 5)