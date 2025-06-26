import csv
from Visualizer.Drower import Drower
import pygame

def main():
    drower = Drower(800, 600)
    walls = drower.load_map('res/map.csv')  # Убедитесь, что файл в той же директории
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        drower.draw_map(walls)
        drower.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()