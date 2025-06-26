
import math
from RobotGuide.RobotMap import RobotMap


class RobotGuide:
    r_map:RobotMap
    ray_count:int
    position:list

    def __init__(self, ray_count, position):
        self.r_map     = RobotMap()
        self.ray_count = ray_count
        self.position  = position
    
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