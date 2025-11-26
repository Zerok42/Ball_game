import pymunk
from pymunk import Vec2d
from pymunk.pygame_util import *

import pygame
from time import time

from random import randint
from math import degrees

pymunk.pygame_util.positive_y_is_up = False
class App():
    def __init__(self):
        #параметры PyGame
        self.RES = self.WIDTH, self.HEIGHT = 900, 720
        self.FPS = 60
        pygame.init()
        self.surface = pygame.display.set_mode(self.RES)
        self.surface.set_alpha(128)
        self.clock = pygame.time.Clock()
        self.draw_options = pymunk.pygame_util.DrawOptions(self.surface)


        with open('Max_score.txt', 'r') as f:
            self.max_score = float(f.read())



        #настройки Pymunk
        self.space = pymunk.Space()
        self.space.gravity = 0, 2500
        self.circles_list = []
        self.list_size = [15]
        self.offset_circle = 0
        self.win = False
        self.removed = False
        self.close_question = False
        self.font = pygame.font.Font(None, 36)
        self.all_sizes = [15, 17.5, 20, 22, 25, 28, 31, 34, 36, 38, 40, 42, 45, 48, 50, 54, 57, 60, 65, 70, 75, 80, 85,
                          120]
        self.dict_images = {}
        self.score = 0

        # Загрузка изображений
        self.exit = pygame.image.load('./images/exit.png').convert()
        self.bg = pygame.image.load('./images/background.png').convert()
        self.win_bg = pygame.image.load('./images/win_background.png').convert()
        self.win_bg = pygame.transform.scale(self.win_bg, (898 * (720/600), 720))
        self.big_x = pygame.image.load('./images/big_x.png').convert()
        self.text_ball = pygame.image.load('./images/text_ball.png').convert()
        self.text_ball = pygame.transform.scale(self.text_ball, (173, 20))
        self.text_exit = pygame.image.load('./images/text_exit.png').convert()
        self.image1 = pygame.image.load('./images/image1_big.png').convert_alpha()
        self.image2 = pygame.image.load('./images/image2_big.png').convert_alpha()
        self.image3 = pygame.image.load('./images/image3_big.png').convert_alpha()
        self.image4 = pygame.image.load('./images/image4_big.png').convert_alpha()
        self.image5 = pygame.image.load('./images/image5_big.png').convert_alpha()
        self.image6 = pygame.image.load('./images/image6_big.png').convert_alpha()
        self.image7 = pygame.image.load('./images/image7_big.png').convert_alpha()
        self.image8 = pygame.image.load('./images/image8_big.png').convert_alpha()
        self.image9 = pygame.image.load('./images/image9_big.png').convert_alpha()
        self.image10 = pygame.image.load('./images/image10_big.png').convert_alpha()
        self.image11 = pygame.image.load('./images/image11_big.png').convert_alpha()
        self.image12 = pygame.image.load('./images/image12_big.png').convert_alpha()
        self.image13 = pygame.image.load('./images/image13_big.png').convert_alpha()
        self.image14 = pygame.image.load('./images/image14_big.png').convert_alpha()
        self.image15 = pygame.image.load('./images/image15_big.png').convert_alpha()
        self.image16 = pygame.image.load('./images/image16_big.png').convert_alpha()
        self.image17 = pygame.image.load('./images/image17_big.png').convert_alpha()
        self.image18 = pygame.image.load('./images/image18_big.png').convert_alpha()
        self.image19 = pygame.image.load('./images/image19_big.png').convert_alpha()
        self.image20 = pygame.image.load('./images/image20_big.png').convert_alpha()
        self.image21 = pygame.image.load('./images/image21_big.png').convert_alpha()
        self.image22 = pygame.image.load('./images/image22_big.png').convert_alpha()
        self.image23 = pygame.image.load('./images/image23_big.png').convert_alpha()
        self.image24 = pygame.image.load('./images/image24_big.png').convert_alpha()
        for i in self.all_sizes:
            if i == 15:
                image = self.image1
            elif i == 17.5:
                image = self.image2
            elif i == 20:
                image = self.image3
            elif i == 22:
                image = self.image4
            elif i == 25:
                image = self.image5
            elif i == 28:
                image = self.image6
            elif i == 31:
                image = self.image7
            elif i == 34:
                image = self.image8
            elif i == 36:
                image = self.image9
            elif i == 38:
                image = self.image10
            elif i == 40:
                image = self.image11
            elif i == 42:
                image = self.image12
            elif i == 45:
                image = self.image13
            elif i == 48:
                image = self.image14
            elif i == 50:
                image = self.image15
            elif i == 54:
                image = self.image16
            elif i == 57:
                image = self.image17
            elif i == 60:
                image = self.image18
            elif i == 65:
                image = self.image19
            elif i == 70:
                image = self.image20
            elif i == 75:
                image = self.image21
            elif i == 80:
                image = self.image22
            elif i == 85:
                image = self.image23
            elif i == 120:
                image = self.image24
            self.dict_images[i] = image







    def slab(self):
        #платформа
        self.segment_shape = pymunk.Segment(self.space.static_body, (2, self.HEIGHT), (self.WIDTH, self.HEIGHT), 26)
        self.space.add(self.segment_shape)
        self.segment_shape.elasticity = 0
        self.segment_shape.friction = 1

        self.ne_bebra_shape = pymunk.Segment(self.space.static_body, (2, 1), (2, 900), 26)
        self.space.add(self.ne_bebra_shape)
        self.ne_bebra_shape.elasticity = 0
        self.ne_bebra_shape.friction = 1

        self.be_shape = pymunk.Segment(self.space.static_body, (625, 1), (625, 900), 26)
        self.space.add(self.be_shape)
        self.be_shape.elasticity = 0
        self.be_shape.friction = 1

        self.b_shape = pymunk.Segment(self.space.static_body, (900, 1), (900, 900), 26)
        self.space.add(self.b_shape)
        self.b_shape.elasticity = 0
        self.b_shape.friction = 1

    def draw_interface(self):
        # Отрисовываем весь интерфейс кроме штуки над мышкой
        if self.win == True:
            self.surface.blit(self.win_bg, (-75, 0))
            if self.removed == False:
                self.space.remove(self.ne_bebra_shape)
                self.space.remove(self.be_shape)
                self.space.remove(self.b_shape)
                self.removed = True
        else:
            self.surface.blit(self.bg, (0, 0))
            self.surface.blit(self.big_x, (688, 530))
            self.surface.blit(self.text_exit, (670, 490))
            self.surface.blit(self.text_ball, (670, 20))
            image = self.dict_images.get(self.size)

            text1 =self.font.render(f'Твой счет: {self.score}', 1, (0, 0, 0))
            self.surface.blit(text1, (652, 240))
            text2 = self.font.render(f'Макс счет: {self.max_score}', 1, (0, 0, 0))
            self.surface.blit(text2, (652, 280))
            image = pygame.transform.scale(image, (150, 150))
            self.surface.blit(image, (688,40))
            if self.close_question == True:
                self.surface.blit(self.exit, (120,200))


        return True

    def create_circle(self,pos, size):

        if self.offset_circle == 0:
            pos_list = [pos[0]-0.1, pos[1]-0.1]
            self.offset_circle = 1
        elif self.offset_circle == 1:
            pos_list = [pos[0] + 0.1, pos[1] + 0.1]
            self.offset_circle = 0
        self.circle_mass = 1
        self.circle_moment = pymunk.moment_for_circle(self.circle_mass,30,30)
        self.circle_body = pymunk.Body(self.circle_mass, self.circle_moment)
        self.circle_body.position = pos_list
        self.circle_shape = pymunk.Circle(self.circle_body, size)
        self.circle_shape.elasticity = 0.4
        self.circle_shape.friction = 1
        self.circle_shape.color = [255,255,255,0]
        self.circles_list.append((self.circle_shape))
        self.space.add(self.circle_body,self.circle_shape)


    def collision_handler(self, arbiter, data, fgf):
        # Получение форм, участвующих в столкновении
        shape1 = arbiter.shapes[0]
        shape2 = arbiter.shapes[1]
        radius1 = shape1.radius
        radius2 = shape2.radius
        # Проверка, являются ли формы кругами
        if isinstance(shape1, pymunk.Circle) and isinstance(shape2, pymunk.Circle):
            # Получение радиусов и координат центров кругов
            center1 = shape1.body.position
            center2 = shape2.body.position
            if radius2 == radius1:
                if shape1.body in self.space.bodies and shape1 in self.circles_list:
                    self.space.remove(shape1.body, shape1)
                    self.circles_list.remove(shape1)
                if shape2.body in self.space.bodies and shape2 in self.circles_list:
                    self.space.remove(shape2.body, shape2)
                    self.circles_list.remove(shape2)
                position = (center1.x + center2.x) / 2, (center1.y + center2.y) / 2
                self.create_circle(position, self.all_sizes[self.all_sizes.index(shape2.radius)+1])
                self.score += radius1
        return True






#Отрисовка
    def main(self):

        handler = self.space.add_collision_handler(0, 0)
        handler.begin = self.collision_handler

        last_rotation_angles = {}
        self.size = 17.5
        start = time()
        amount_placed = 0

        self.slab()
        while True:

            self.draw_interface()

            if self.max_score <= float(self.score):
                self.max_score = float(self.score)

            self.space.step(1 / self.FPS)
            self.space.debug_draw(self.draw_options)

            for circle_shape in self.circles_list:
                ### КОРОЧЕ ТУТ ОТРИСОВЫВАЕТСЯ ИЗОБРАЖЕНИЯ МЯЧИКОВ
                # Calculate the position for the image
                p = Vec2d(circle_shape.body.position.x, circle_shape.body.position.y)

                # Calculate the current rotation angle
                angle_degrees = degrees(circle_shape.body.angle) + 180

                # Invert the rotation direction
                angle_degrees *= -1

                # Load the image based on the size of the ball
                image = self.dict_images.get(circle_shape.radius)
                if circle_shape.radius == 120:
                    self.win = True



                scaled_image = pygame.transform.scale(image, (circle_shape.radius * 2.2, circle_shape.radius * 2.2))

                # Rotate the image to match the circle's orientation
                rotated_image = pygame.transform.rotate(scaled_image, angle_degrees)

                # Calculate the offset to center the image on the circle
                offset = Vec2d(*rotated_image.get_size()) / 2
                p = p - offset

                # Draw the image on the surface
                self.surface.blit(rotated_image, (round(p.x), round(p.y)))

                # Update the last rotation angle
                last_rotation_angles[circle_shape] = angle_degrees

            # Отрисовываем полупрозрачный мяч над мышкой (задержка есть немного но пофиг)
            if (pygame.mouse.get_pos()[0])+self.size <= 600 and (pygame.mouse.get_pos()[0])-self.size >= 30 and pygame.mouse.get_pos()[1] <= 330 and self.close_question == False or self.removed == True:
                image = self.dict_images.get(self.size)
                image = pygame.transform.scale(image, (self.size*2.2, self.size*2.2))
                image.set_alpha(128)
                pos = [pygame.mouse.get_pos()[0]-self.size, pygame.mouse.get_pos()[1]-self.size]
                self.surface.blit(image, pos)

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    with open('Max_score.txt', 'w') as f:
                        f.write(str(self.max_score))
                    exit()


                if i.type == pygame.MOUSEBUTTONDOWN:
                    end = time()
                    if i.button == 1 and (i.pos[0])+self.size <= 600 and (i.pos[0])-self.size >= 30 and i.pos[1] <= 330 and self.close_question == False or self.removed == True:

                        if end - start >= 0.7:
                            amount_placed += 1

                            self.create_circle(i.pos, self.size)

                            self.size = self.list_size[randint(0, len(self.list_size)-1)]

                            # Добавляем в список новые мячи чтобы они могли спавниться
                            if amount_placed == 20:
                                self.list_size.append(self.all_sizes[1])
                            elif amount_placed == 30:
                                self.list_size.append(self.all_sizes[2])
                            elif amount_placed == 60:
                                self.list_size.append(self.all_sizes[3])
                            elif amount_placed == 80:
                                self.list_size.append(self.all_sizes[4])
                                self.list_size.remove(self.all_sizes[0])
                            elif amount_placed == 100:
                                self.list_size.append(self.all_sizes[5])
                                self.list_size.remove(self.all_sizes[1])
                            elif amount_placed == 120:
                                self.list_size.append(self.all_sizes[6])
                                self.list_size.remove(self.all_sizes[2])
                            elif amount_placed == 140:
                                self.list_size.append(self.all_sizes[7])
                                self.list_size.remove(self.all_sizes[3])
                            elif amount_placed == 160:
                                self.list_size.append(self.all_sizes[8])
                                self.list_size.remove(self.all_sizes[4])
                            elif amount_placed == 180:
                                self.list_size.append(self.all_sizes[9])
                                self.list_size.remove(self.all_sizes[5])
                            elif amount_placed == 200:
                                self.list_size.append(self.all_sizes[10])
                                self.list_size.remove(self.all_sizes[6])
                            elif amount_placed == 220:
                                self.list_size.append(self.all_sizes[11])
                                self.list_size.remove(self.all_sizes[7])
                            elif amount_placed == 240:
                                self.list_size.append(self.all_sizes[12])
                                self.list_size.remove(self.all_sizes[8])
                            elif amount_placed == 260:
                                self.list_size.append(self.all_sizes[13])
                                self.list_size.remove(self.all_sizes[9])
                            elif amount_placed == 280:
                                self.list_size.append(self.all_sizes[14])
                                self.list_size.remove(self.all_sizes[10])

                            start = time()
                    elif i.button == 1 and i.pos[0]>=133 and i.pos[0]<=287 and i.pos[1]>=343 and i.pos[1]<=427 and self.close_question == True:
                        with open('Max_score.txt', 'w') as f:
                            f.write(str(self.max_score))
                        exit()
                    elif i.button == 1 and i.pos[0]>=351 and i.pos[0]<=508 and i.pos[1]>=342 and i.pos[1]<=428 and self.close_question == True:
                        self.close_question = False


                    if i.button == 1 and i.pos[0]>=690 and i.pos[0]<=840 and i.pos[1]>=530 and i.pos[1]<=680:
                        if self.close_question == False:
                            self.close_question = True



            pygame.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = App()
    app.main()