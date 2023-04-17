import pygame

screen_width = 1280
screen_height = 720
dark = (50, 50, 50)
light = (225, 225, 225)
slow = 12
fast = 15
fmq = 20
black = "#000000"
white = "#FFFFFF"

player = pygame.Rect(10, screen_height/2 - 70, 10, 140)
ai = pygame.Rect(screen_width - 20, screen_height/2 - 70 , 10 , 140)
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)

base_color = light
screen_theme = dark
player_speed = 0
ai_speed = 8
player_score = 0
opponent_score = 0
theme_text = "Thème: Sombre"
text_hovering_color = "#8b8b8b"
ball_speed_x = slow
ball_speed_y = slow
ball_text = "Balle: Lente"