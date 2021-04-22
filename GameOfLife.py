import pygame
import numpy as np

#Initializing the background color.
dead_col = (0, 0, 0)
alive_col = (255, 255, 255)
background_col = (255, 0, 0)
grid_col = (30, 30, 60)

#Core of The Simulation.
#Calculates the status of the cells in the next time step,
#and applies the rules of the game of life to all cells
def update(surface, _curx, _ssx):
    #2D field and initialized with zero, without the dead cells
    next = np.zeros((_curx.shape[0], _curx.shape[1]))
    
    #Iterating all over the cells
    for r, c in np.ndindex(_curx.shape):
        number_alive = np.sum(_curx[r-1:r+2, c-1:c+2]) - _curx[r, c]

        if _curx[r, c] == 1 and number_alive < 2 or number_alive > 3:
            col = dead_col
        elif (_curx[r, c] == 1 and 2 <= number_alive <= 3) or (_curx[r, c] == 0 and number_alive == 3):
            next[r, c] = 1
            col = alive_col

        col = col if _curx[r, c] == 1 else background_col
        pygame.draw.rect(surface, col, (c*_ssx, r*_ssx, _ssx-1, _ssx-1))
    #Each cell is assigned a color that corresponds to its status.
    #the new state of the simulation is returned
    return next

#Initializing the variables, creating patterns called gliders.
def init(dimensionx, _dim):
    cells = np.zeros((_dim, dimensionx))
    #Pattern of the glider.
    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    pos = (3,3)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells

#initializes the program and contains an event loop 
#with which pygame checks whether the program has been ended by the user.
#As long as the program has not ended,
#the update function is called and the simulation continues
def main(dimensionx, _dim, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimensionx * cellsize, _dim * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    cells = init(dimensionx, _dim)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(grid_col)
        cells = update(surface, cells, cellsize)
        pygame.display.update()
        
#main(dimensionx, _dim_ cellsize)
if __name__ == "__main__":
    main(70, 50, 8)