import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.images = [pygame.image.load(f'img/sprites/turtles/leo/leo_stay_{i}.png') for i in range(1, 4)]
        self.images_wright = [pygame.image.load(f'img/sprites/turtles/leo/leo_wright_{i}.png') for i in range(1, 4)]
        self.images_wleft = [pygame.image.load(f'img/sprites/turtles/leo/leo_wleft_{i}.png') for i in range(1, 4)]
        self.image_sit = pygame.image.load(f'img/sprites/turtles/leo/leo_sit.png')
        self.image_jump = pygame.image.load(f'img/sprites/turtles/leo/leo_jump.png')
        self.image_arm = pygame.image.load(f'img/sprites/turtles/leo/leo_arm.png')
        self.image_arm_down = pygame.image.load(f'img/sprites/turtles/leo/leo_arm_down.png')
        self.image_foot = pygame.image.load(f'img/sprites/turtles/leo/leo_foot.png')
        self.image_foot_down = pygame.image.load(f'img/sprites/turtles/leo/leo_foot_down.png')
        self.image_block = pygame.image.load(f'img/sprites/turtles/leo/leo_block.png')
        self.index = 0
        self.image = self.images[self.index]
        self.x, self.y = 150, 260
        self.rect = self.image.get_rect()
        self.speed, self.m = 15, 1
        self.wright, self.wleft = False, False
        self.down, self.isjump = False, False
        self.fight_arm, self.fight_foot = False, False
        self.fight_arm_down, self.fight_foot_down = False, False
        self.block = False

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.rect.center = self.x, self.y
        if self.wright:
            self.x += self.speed
            self.image = self.images_wright[self.index]
            if self.x >= 730:
                self.x -= self.speed
        elif self.wleft:
            self.x -= self.speed
            self.image = self.images_wleft[self.index]
            if self.x <= 70:
                self.x += self.speed
        elif self.down and self.fight_arm:
            self.image = self.image_arm_down
            self.fight_arm = False
        elif self.down and self.fight_foot:
            self.image = self.image_foot_down
            self.fight_foot = False
        elif self.down:
            self.image = self.image_sit
        elif self.isjump:
            self.image = self.image_jump
            self.y -= (1 / 2) * self.m * (self.speed ** 2)
            self.speed -= 5
            if self.speed < 0:
                self.m = -1

            if self.speed == -20:
                self.isjump = False
                self.speed = 15
                self.m = 1

        elif self.fight_arm:
            self.image = self.image_arm
            self.fight_arm = False
        elif self.fight_foot:
            self.image = self.image_foot
            self.fight_foot = False
        elif self.block:
            self.image = self.image_block
