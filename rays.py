import math
import random

from PIL import Image, ImageDraw

from palettes import PALETTES

size = (8000, 6400)
palette = PALETTES[1]
n_particles = 20
random_range = 1.5
depth = 7
initial_length = 150
length_reduction = 0.95
line_width = 5
width_reduction = 0.8
branching_factor = 2


def draw_rays(output_file='rays.png'):
    image = Image.new('RGB', size, color='black')
    draw = ImageDraw.Draw(image)

    particles = [
        (random.random() * math.pi * 2, (image.width / 2, image.height / 2))
        for i in range(n_particles)
    ]

    def move_particle(pos, angle, length):
        return pos[0] + math.sin(angle) * length, pos[1] + math.cos(angle) * length

    def process_particle(p):
        last_pos = p[1]
        new_pos = move_particle(p[1], p[0], initial_length * (length_reduction ** d))
        color = random.choice(palette)
        draw.line(last_pos + new_pos, color, width=int(line_width * (width_reduction ** d)))

        return [(p[0] + random.random() * random_range - random_range / 2, new_pos)
                for i in range(branching_factor)]

    for d in range(depth):
        particles = [p
                     for particles in map(process_particle, particles)
                     for p in particles]

    image.save(output_file)


if __name__ == '__main__':
    for i in range(10):
        draw_rays(f'output/rays_{i + 1}.png')
