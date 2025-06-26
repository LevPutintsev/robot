import pygame
import csv
from ast import literal_eval

class Drower:
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

    # Инициализация Pygame
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        pygame.init()
    
    def __del__(self):
        pygame.quit()

    def parse_coord(self, coord_str):
        """Преобразует строку с координатами в кортеж чисел"""
        return literal_eval(coord_str.strip())

    def load_map(self, filename):
        """Загружает карту из CSV файла"""
        walls = []
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='|')
            next(reader)  # Пропускаем заголовок
            for row in reader:
                start = self.parse_coord(row[0])
                end = self.parse_coord(row[1])
                walls.append((start, end))
        return walls

    def draw_map(self, walls):
        self.screen.fill((255, 255, 255))
        """Отрисовывает карту на экране"""
        for start, end in walls:
            # Масштабируем координаты и смещаем для визуализации
            x1 = self.OFFSET_X + start[0] * self.SCALE
            y1 = self.OFFSET_Y + start[1] * self.SCALE
            x2 = self.OFFSET_X + end[0] * self.SCALE
            y2 = self.OFFSET_Y + end[1] * self.SCALE

            # Рисуем стену
            pygame.draw.line(self.screen, self.BLACK, (x1, y1), (x2, y2), 3)

    def flip(self):
        pygame.display.flip()