import matplotlib.pyplot as plt
import numpy as np

def ndc_to_screen(ndc_x, ndc_y, screen_width, screen_height):
    screen_x = (ndc_x + 1) * (screen_width / 2)
    screen_y = (-ndc_y + 1) * (screen_height / 2)
    return screen_x, screen_y

def main():
    screen_width = 800
    screen_height = 600

    ndc_x = 0.3
    ndc_y = -0.6

    screen_x, screen_y = ndc_to_screen(ndc_x, ndc_y, screen_width, screen_height)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, screen_width)
    ax.set_ylim(0, screen_height)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle='--', linewidth=0.5)

    ax.plot(screen_x, screen_y, 'bo', markersize=5)
    ax.axhline(y=screen_y, color='r', linestyle='dotted')
    ax.axvline(x=screen_x, color='r', linestyle='dotted')

    plt.show()

if __name__ == "__main__":
    main()
