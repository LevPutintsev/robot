
import csv
import math
from ast import literal_eval
import time
from RobotGuide.RobotMap import RobotMap

class RobotGuide:
    r_map:RobotMap
    ray_count:int
    position:list
    way = []
    way_stop = ['маршрут i1', 'маршрут p1', 'маршрут t1', 'маршрут v2', 'маршрут a2', 'маршрут e2', 'маршрут f2']
    way_text = {
        'маршрут i1':'',
        'маршрут p1':''
    }
    # walk, goHome, waite, speach
    state = 'walk'

    def __init__(self, ray_count):
        self.r_map     = RobotMap()
        self.ray_count = ray_count
        self.load_map('res/Robot_Route.csv')
        self.position = self.way[0][0]
        self.state = 'waite'

    def SetStatus(self, stat):
        if stat == 'walk' and self.state != 'walk':
            self.load_map('res/Robot_Route.csv')
            print('data is loaded')
        elif stat == 'goHome' and self.state != 'goHome':
            self.load_map('res/To_start_route.csv')
        elif stat == 'speach':
            print(self.way_text[self.actualLoc])
            time.sleep(4)
            stat = 'walk'
        self.state = stat

    def load_map(self, filename):
        self.way= []
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='|')
            for i, row in enumerate(reader):
                start = self.parse_coord(row[0])
                end = self.parse_coord(row[1])
                name = row[2]
                self.way.append((start, end, name))

    def parse_coord(self, coord_str):
        """Преобразует строку с координатами в кортеж чисел"""
        return literal_eval(coord_str.strip())

    def MoveIter(start, end):
        i = 0.0
        flX = False if start[0] - end[0] <= 0 else True
        flY = False if start[1] - end[1] <= 0 else True
        while True:
            x = start[0] + i*(end[0] - start[0])
            y = start[1] + i*(end[1] - start[1])

            yield (x, y)

            if flX:
                if x < end[0]:
                    break
            else:
                if x > end[0]:
                    break
            if flY:
                if y < end[1]:
                    break
            else:
                if y > end[1]:
                    break
            i += 0.01

    def go(self):
        if self.state == 'waite':
            return
        if self.state == 'speach':
            return
        for point in self.way:
            for pos in RobotGuide.MoveIter(self.position, point[1]):
                self.position = pos
                yield 1
            if point[2] in self.way_stop:
                self.actualLoc = point[2]
                self.SetStatus('speach')

    def tick(self):
        mas = []
        for v in self.get_sensor_vectors():
            mas.append(self.r_map.RayCust([self.position, [self.position[0]+v[0],self.position[1]+v[1]]]))
        return mas
    
    def get_sensor_vectors(self):
        vectors = []
        for i in range(-100, 100, 100//(self.ray_count//2)):
            vectors.append([math.sin(math.pi*i/100), (math.cos(math.pi*i/100))])
            vectors.append([math.cos(math.pi*i/100), (math.sin(math.pi*i/100))])
        return vectors