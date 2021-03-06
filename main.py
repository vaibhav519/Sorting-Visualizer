import display
import pygame
from algs import algorithmsDict, runAlgorithm
from random import randint


# Global Variables: numBars, delay, toDraw, button
# They were declared in display.py


def main():
    numbers = []
    running = True
    display.algorithmBox.add_options(list(algorithmsDict.keys()))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            display.sizeBox.update(event)
            display.delayBox.update(event)
            display.algorithmBox.update()
            display.startButton.update()
            a_set = set(range(display.numBars))

            if display.startButton.isActive:
                # Set the values given by the user
                display.numBars = int(display.sizeBox.value)
                display.delay = display.delayBox.value - display.delayBox.rect.x - 6
                algorithm = display.algorithmBox.get_active_option()
                # Generates a random list
                numbers = [randint(10, 400) for _ in range(display.numBars)]
                # Executes the chosen algorithm
                runAlgorithm(algorithm.lower(), numbers)
                display.toDraw = True
            display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)


if __name__ == '__main__':
    main()
