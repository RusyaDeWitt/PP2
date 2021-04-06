import pygame
import math

pygame.init()

W = 800
H = 600

screen = pygame.display.set_mode((W, H))


class Point:
    # constructed using a normal tupple
    def __init__(self, point_t=(0, 0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])

    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))

    def __mul__(self, scalar):
        return Point((self.x * scalar, self.y * scalar))

    def __div__(self, scalar):
        return Point((self.x / scalar, self.y / scalar))

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)


def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=4):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement.__div__(length)
    for index in range(0, int(length / dash_length), 2):
        start = origin + (slope * index * dash_length)
        end = origin + (slope * (index + 1) * dash_length)
        pygame.draw.line(surf, color, start.get(), end.get(), width)


def draw_dashed_lines(surf, color, points, width, dash_len):
    for i in range(len(points) - 1):
        draw_dashed_line(surf, color, points[i], points[i + 1], width, dash_len)


def get_points(f, xrange, step, kx, ky, center):
    num = math.ceil((xrange[1] - xrange[0]) / step)
    x_values = (x * step + xrange[0] for x in range(num + 1))
    func = ((kx * x, ky * f(x)) for x in x_values)
    points = tuple(map(lambda x: (x[0] + center[0], -x[1] + center[1]), func))
    return points


k = 2 / 3

xrange = (-3 * math.pi, 3 * math.pi)
step = 0.1
kx = (k * W) / (6 * math.pi)
ky = (k * H) / 2
center = (W // 2, H // 2)

sin_points = get_points(math.sin, xrange, step, kx, ky, center)
cos_points = get_points(math.cos, xrange, step, kx, ky, center)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))

    start = (1 - k) / 2
    end = (k + (1 - k) / 2)

    pygame.draw.aaline(screen, (0, 0, 0), (start * W, H // 2), (end * W, H // 2), 4)
    pygame.draw.aaline(screen, (0, 0, 0), (W // 2, start * H), (W // 2, end * H), 4)

    bounding_points = ((start * W, start * H),
                       (end * W, start * H),
                       (end * W, end * H),
                       (start * W, end * H))
    pygame.draw.aalines(screen, (0, 0, 0), True, bounding_points, 2)

    draw_dashed_lines(screen, (0, 0, 255), cos_points, 2, 3)
    pygame.draw.aalines(screen, (255, 0, 0), False, sin_points)

    pygame.display.flip()