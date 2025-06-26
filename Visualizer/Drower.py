import pygame
import csv
from ast import literal_eval

class Drower:
    DEBUG = False
    # Цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    map_position = [0.0, 0.0]

    # Масштабирование координат (так как исходные координаты в диапазоне 0..1)
    SCALE = 500
    OFFSET_X, OFFSET_Y = 50, 50

    # Инициализация Pygame
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        pygame.init()
        self.font = pygame.font.Font(None, 36)
        self.font1 = pygame.font.Font(None, 25)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Визуализация карты помещения")
        self.getMillisecundCount = 0
    
    def __del__(self):
        pygame.quit()
        del self.font, self.font1, self.walls, self.screen

    def parse_coord(self, coord_str):
        """Преобразует строку с координатами в кортеж чисел"""
        return literal_eval(coord_str.strip())

    def load_map(self, filename):
        """Загружает карту из CSV файла"""
        walls = []
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='|')
            for i, row in enumerate(reader):
                start = self.parse_coord(row[0])
                end = self.parse_coord(row[1])
                print(f'{i}:\t{row[2]}')
                name = str(i)
                walls.append((start, end, name))
        self.walls = walls

    def drow_stat(self):
        # Создаем объект Surface для текста
        try:
            t = pygame.time.get_ticks()
            self.getTicksLastFrame   = (t-self.getMillisecundCount) / 1000.0
            self.getMillisecundCount = t
            text_surface = self.font.render(str(1//self.getTicksLastFrame), True, self.WHITE, self.BLACK) #text, антиальясинг, цвет текста, цвет фона

            # Получаем прямоугольник для текста
            text_rect = text_surface.get_rect()
            text_rect.center = (self.WIDTH-50, 15)
            self.screen.blit(text_surface, text_rect)
        except:
            print('g')

    def draw_map(self):
        self.screen.fill((200, 200, 200))
        """Отрисовывает карту на экране"""
        for start, end, name in self.walls:
            # Масштабируем координаты и смещаем для визуализации
            x1 = self.OFFSET_X + start[0] * self.SCALE
            y1 = self.OFFSET_Y + start[1] * self.SCALE
            x2 = self.OFFSET_X + end[0] * self.SCALE
            y2 = self.OFFSET_Y + end[1] * self.SCALE

            # Рисуем стену
            pygame.draw.line(self.screen, self.BLACK, (x1+self.map_position[0], y1+self.map_position[1]), 
                             (x2+self.map_position[0], y2+self.map_position[1])
                             , 3)
            if self.DEBUG:
                text_surface = self.font1.render(name, True, self.BLUE) #text, антиальясинг, цвет текста, цвет фона
                # Получаем прямоугольник для текста
                text_rect = text_surface.get_rect()
                text_rect.center = (x1+self.map_position[0], y1+self.map_position[1])
                self.screen.blit(text_surface, text_rect)

    def draw_guide(self, r, ar):
        x = self.OFFSET_X + ar[0] * self.SCALE
        y = self.OFFSET_Y + ar[1] * self.SCALE
        pygame.draw.circle(self.screen, self.RED, (x+self.map_position[0], y+self.map_position[1]), 2, 2)

        x = self.OFFSET_X + r[0] * self.SCALE
        y = self.OFFSET_Y + r[1] * self.SCALE
        pygame.draw.circle(self.screen, self.BLUE, (x+self.map_position[0], y+self.map_position[1]), 5, 5)

    def flip(self):
        pygame.display.flip()