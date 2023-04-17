#Importation des modules, fichiers et des valeurs nécéssaires
import pygame, sys, variables, random
from button import Button
from variables import *

#Initiation de PyGame, de la fenêtre et définition de la variable pour la résolution de l'écran
pygame.init()
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
pygame.display.set_caption("PYNG")
screen = pygame.display.set_mode((variables.screen_width, variables.screen_height))

#Fonction pour définir la police d'écriture
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

#Fonction pour la page du menu
def menu():
    while True:
        #Définition du fond d'écran et de la variable pour détecter la position de la souris
        screen.fill((variables.screen_theme))
        mouse = pygame.mouse.get_pos() 
        
        #Affichage du texte "PYNG" sur le haut de l'écran
        menu_text = get_font(115).render("PYNG", True, variables.base_color)
        menu_rect = menu_text.get_rect(center = (640,100))
        screen.blit(menu_text, menu_rect)
        
        #Affichage du crédit en bas à droite de l'écran
        cred_text = get_font(10).render("Fait par Lorenzo NOCCHI", True, variables.base_color)
        cred_rect = cred_text.get_rect(center = (1150,710))
        screen.blit(cred_text, cred_rect)
        
        #Affichage de la version en bas à gauche de l'écran
        ver_text = get_font(10).render("Version 1.0", True, variables.base_color)
        ver_rect = cred_text.get_rect(center = (125,710))
        screen.blit(ver_text, ver_rect)
        
        #Création des variables boutons
        play_button = Button(image=None, pos=(640, 300), text_input="JOUER", font=get_font(60), base_color=variables.base_color, hovering_color=variables.text_hovering_color)
        options_button = Button(image=None, pos=(640, 450), text_input="OPTIONS", font=get_font(60), base_color=variables.base_color, hovering_color=variables.text_hovering_color)
        quit_button = Button(image=None, pos=(640, 600), text_input="QUITTER", font=get_font(60), base_color=variables.base_color, hovering_color=variables.text_hovering_color)
        
        #Affichage des boutons et mise en place de l'interraction avec
        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse)
            button.update(screen)
        
        #Liste des évenements de la fonction "menu()"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.checkForInput(mouse):
                    play()
                elif options_button.checkForInput(mouse):
                    options()
                elif quit_button.checkForInput(mouse):
                    pygame.quit()
                    sys.exit()
        
        #Définition du rafraichissement de l'image
        pygame.time.Clock().tick(60)
        pygame.display.update()

#Fonction pour la page du jeu
def play():
    #Remise de la balle à la position x0 y0
    ball_reset()
    variables.player_score = 0
    variables.opponent_score = 0
    while True:
        #Définition du fond d'écran
        screen.fill((variables.screen_theme))
        
        #Définition des variables de texte pour le score
        player_score_text = pygame.font.Font("assets/font.ttf", 32).render(f"{variables.player_score}", False, variables.base_color)
        opponent_score_text = pygame.font.Font("assets/font.ttf", 32).render(f"{variables.opponent_score}", False, variables.base_color)
        
        #Affichage du score
        screen.blit(player_score_text, (variables.screen_width/2 + 20, variables.screen_height/2))
        screen.blit(opponent_score_text, (variables.screen_width/2 - 50, variables.screen_height/2))
        
        #Affichage des raquettes, de la balle et de la ligne séparatoire au milieu
        pygame.draw.rect(screen, variables.base_color, player)
        pygame.draw.rect(screen, variables.base_color, ai)
        pygame.draw.rect(screen, variables.base_color, ball)
        pygame.draw.aaline(screen, variables.base_color, (screen_width/2,0), (screen_width/2, screen_height))
        
        #Liste des évenements de la fonction "play()"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    variables.player_speed += 7
                elif event.key == pygame.K_UP:
                    variables.player_speed -= 7
                elif event.key == pygame.K_ESCAPE:
                    menu()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    variables.player_speed -= 7
                elif event.key == pygame.K_UP:
                    variables.player_speed += 7
        
        #Appel de fonctions pour les interactions avec la balle et les raquettes
        ball_movement()
        player_movement()
        ai_movement()
        
        #Définition du rafraichissement de l'image
        pygame.time.Clock().tick(60)
        pygame.display.update()

def options():
    while True:
        screen.fill((variables.screen_theme))
        mouse = pygame.mouse.get_pos()

        options_text = get_font(90).render("OPTIONS", True, variables.base_color)
        options_rect = options_text.get_rect(center = (640,100))
        screen.blit(options_text, options_rect)
        
        theme_button = Button(image=None, pos=(640, 300), text_input=variables.theme_text, font=get_font(55), base_color=variables.base_color, hovering_color=variables.text_hovering_color)
        ball_button = Button(image=None, pos=(640, 450), text_input=variables.ball_text, font=get_font(55), base_color=variables.base_color, hovering_color=variables.text_hovering_color)
        back_button = Button(image=None, pos=(640, 640), text_input="RETOUR", font=get_font(40), base_color=variables.base_color, hovering_color=variables.text_hovering_color)

        for button in [theme_button, ball_button, back_button]:
            button.changeColor(mouse)
            button.update(screen)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if theme_button.checkForInput(mouse):
                    if variables.screen_theme == dark:
                        variables.screen_theme = light
                        variables.base_color = black
                        variables.theme_text = "Thème: Clair"
                    else:
                        variables.screen_theme = dark
                        variables.base_color = white
                        variables.theme_text = "Thème: Sombre"
                elif ball_button.checkForInput(mouse):
                    if variables.ball_speed_x == slow:
                        variables.ball_speed_x = fast
                        variables.ball_speed_y = fast
                        variables.ball_text = "Balle: Rapide"
                    elif variables.ball_speed_x == fast:
                        variables.ball_speed_x = fmq
                        variables.ball_speed_y = fmq
                        variables.ball_text = "Balle: Flash McQueen"
                    else:
                        variables.ball_speed_x = slow
                        variables.ball_speed_y = slow
                        variables.ball_text = "Balle: Lente"
                elif back_button.checkForInput(mouse):
                    menu()
        
        pygame.time.Clock().tick(60)
        pygame.display.update()

def ball_movement():
    global ball_speed_x, ball_speed_y
    variables.ball.x += variables.ball_speed_x
    variables.ball.y += variables.ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        variables.ball_speed_y *= -1
    
    if ball.left <= 0:
        variables.player_score += 1
        ball_reset()
    
    elif ball.right >= screen_width:
        variables.opponent_score += 1
        ball_reset()
        
    if variables.ball.colliderect(player) or variables.ball.colliderect(ai):
        variables.ball_speed_x *= -1
        

def player_movement():
    player.y += variables.player_speed
    if player.top <= 0:
        player.top = 0
    elif player.bottom >= variables.screen_height:
        player.bottom = variables.screen_height

def ai_movement():
    if ai.top < ball.y:
        ai.top += variables.ai_speed
    elif ai.bottom > ball.y:
        ai.bottom -= variables.ai_speed
    if ai.top <= 0:
        ai.top = 0
    elif ai.bottom >= variables.screen_height:
        ai.bottom = variables.screen_height

def ball_reset():
    ball.center = (screen_width/2, screen_height/2)
    variables.ball_speed_y *= random.choice((1, -1))
    variables.ball_speed_x *= random.choice((1, -1))

menu()