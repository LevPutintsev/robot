import csv
import time
from RobotGuide.RobotGuide import RobotGuide
from RobotGuide.RobotMap import RobotMap
from Visualizer.Drower import Drower
import pygame

def main():
    drower = Drower(900, 900)
    drower.load_map('res/map.csv')  # Убедитесь, что файл в той же директории

    robot = RobotGuide(64, [0.25, 0.25])
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_t:
                    drower.DEBUG = not drower.DEBUG
                elif event.key == pygame.K_q:
                    drower.SCALE += 10
                elif event.key == pygame.K_e:
                    drower.SCALE -= 10
                if event.key == pygame.K_w:
                    drower.map_position[1] += 10
                elif event.key == pygame.K_s:
                    drower.map_position[1] -= 10
                if event.key == pygame.K_a:
                    drower.map_position[0] += 10
                elif event.key == pygame.K_d:
                    drower.map_position[0] -= 10
                
                if event.key == pygame.K_i:
                    robot.position[1] -= 0.025
                elif event.key == pygame.K_k:
                    robot.position[1] += 0.025
                if event.key == pygame.K_j:
                    robot.position[0] -= 0.025
                elif event.key == pygame.K_l:
                    robot.position[0] += 0.025

        drower.draw_map()
        l = robot.tick()
        for d in l:
            if len(d) > 0:
                drower.draw_guide(robot.position, d)

        drower.drow_stat()
        drower.flip()

if __name__ == "__main__":
    main()