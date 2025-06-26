import csv
from Visualizer.Drower import load_map, pygame, screen, draw_map, WHITE

def main():
    walls = load_map('res/map.csv')  # Убедитесь, что файл в той же директории
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        draw_map(walls)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()