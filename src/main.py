import pygame as pg


pg.init()
pg.display.init()
pg.display.set_caption("random window amongus")


screen = pg.display.set_mode([500, 800])

image = pg.image.load("src/unknown.png")

x = 0
y = 0
up = False
down = False
left = False
right = False
gravity = 0.001
friction = -0.1
x_speed = 0
y_speed = 0
x_acc = 0
y_acc = 0


while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:

            quit()

        if event.type == pg.KEYDOWN:

            # Up and down

            if event.key == pg.K_w:

                up = True
                down = False

            if event.key == pg.K_s:

                up = False
                down = True

            # Left and right

            if event.key == pg.K_a:

                left = True
                right = False

            if event.key == pg.K_d:

                left = False
                right = True

        if event.type == pg.KEYUP:

            # Up and down

            if event.key == pg.K_w:

                up = False

            if event.key == pg.K_s:

                down = False

            # Left and right

            if event.key == pg.K_a:

                left = False

            if event.key == pg.K_d:

                right = False


    # Apply physics

    x_acc += x_speed * friction
    x_speed += x_acc
    y_speed += y_acc

    x += x_speed + 0.5 * x_acc
    y += y_speed + 0.5 * y_acc


    # Move player

    x_acc = 0
    y_acc = gravity

    if up:

        y_acc = -20

    if down:

        y_acc = 0.002

    if left:

        x_acc = -0.002

    if right:

        x_acc = 0.002


    screen.fill((0, 0, 0))
    screen.blit(image, (x, y))
    pg.display.flip()