import pygame
import environment
import object
import sys

env = environment.Environment()
ball = object.Object(
    pos = pygame.math.Vector2(env.w*0.1,env.h*0.6),
    vel = pygame.math.Vector2(0.08789*env.w,0.732*env.h),
    w = env.w,
    h = env.h
)

def game_screen(difficulty):
    env.objects.append(ball)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False   
        env.update(difficulty)
        env.clock_tick()
        env.draw()
    env.quit()

def credits_screen():
    font = pygame.font.SysFont("segoeuiemoji", 100)
    button_font = pygame.font.SysFont("segoeuiemoji", 40)
    text_surface = font.render("Nirman Dhandhania", True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.center = (env.w*0.5,env.h*0.5)

    back_text_surface = button_font.render("Back", True, (0, 0, 0))
    back_text_rect = back_text_surface.get_rect()
    back_button_rect = pygame.Rect(0, 0, back_text_rect.width + 20, back_text_rect.height + 20)
    back_button_rect.center = (env.w * 0.5, env.h*0.7)
    back_text_rect.center = back_button_rect.center

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False      
        env.screen.fill((0,0,0))
        env.screen.blit(text_surface,text_rect)

        pygame.draw.rect(env.screen, pygame.Color('white'), back_button_rect)
        env.screen.blit(back_text_surface, back_text_rect)

        mouse_pos = pygame.mouse.get_pos()
        if(back_button_rect.collidepoint(mouse_pos)) and pygame.mouse.get_pressed()[0]:
            menu_screen()

        pygame.display.flip()
        env.clock_tick()     
    env.quit()

def difficulty_screen():
    title_font = pygame.font.SysFont("segoeuiemoji", 70)
    button_font = pygame.font.SysFont("segoeuiemoji", 40)
    
    title_surface = title_font.render("Difficulty selection", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(env.w * 0.5, env.h * 0.15))

    easy_text_surface = button_font.render("Easy", True, (0, 0, 0))
    easy_text_rect = easy_text_surface.get_rect()
    easy_button_rect = pygame.Rect(0, 0, easy_text_rect.width + 20, easy_text_rect.height + 20)
    easy_button_rect.center = (env.w * 0.3, env.h*0.5)
    easy_text_rect.center = easy_button_rect.center

    medium_text_surface = button_font.render("Medium", True, (0, 0, 0))
    medium_text_rect = medium_text_surface.get_rect()
    medium_button_rect = pygame.Rect(0, 0, medium_text_rect.width + 20, medium_text_rect.height + 20)
    medium_button_rect.center = (env.w * 0.5, env.h*0.5)
    medium_text_rect.center = medium_button_rect.center

    hard_text_surface = button_font.render("Hard", True, (0, 0, 0))
    hard_text_rect = hard_text_surface.get_rect()
    hard_button_rect = pygame.Rect(0, 0, hard_text_rect.width + 20, hard_text_rect.height + 20)
    hard_button_rect.center = (env.w * 0.7, env.h*0.5)
    hard_text_rect.center = hard_button_rect.center

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False   
        
        env.screen.fill((0,0,0))
        
        env.screen.blit(title_surface, title_rect)

        pygame.draw.rect(env.screen, pygame.Color('green'), easy_button_rect)
        env.screen.blit(easy_text_surface, easy_text_rect)

        pygame.draw.rect(env.screen, pygame.Color('yellow'), medium_button_rect)
        env.screen.blit(medium_text_surface, medium_text_rect)

        pygame.draw.rect(env.screen, pygame.Color('red'), hard_button_rect)
        env.screen.blit(hard_text_surface, hard_text_rect)

        mouse_pos = pygame.mouse.get_pos()
        if easy_button_rect.collidepoint(mouse_pos):
            game_screen(0.8)
            sys.exit()
        elif medium_button_rect.collidepoint(mouse_pos):
            game_screen(1)
            sys.exit()
        elif hard_button_rect.collidepoint(mouse_pos):
            game_screen(1.5)
            sys.exit()
        
        pygame.display.flip()
        env.clock_tick()
        
    env.quit()

def menu_screen():
    title_font = pygame.font.SysFont("segoeuiemoji", 70)
    button_font = pygame.font.SysFont("segoeuiemoji", 40)

    title_surface = title_font.render("🎾Squash", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(env.w * 0.5, env.h * 0.15))

    play_text_surface = button_font.render("Play", True, (0, 0, 0))
    play_text_rect = play_text_surface.get_rect()
    play_button_rect = pygame.Rect(0, 0, play_text_rect.width + 20, play_text_rect.height + 20)
    play_button_rect.center = (env.w * 0.5, env.h*0.4)
    play_text_rect.center = play_button_rect.center

    credits_text_surface = button_font.render("Credits", True, (0, 0, 0))
    credits_text_rect = credits_text_surface.get_rect()
    credits_button_rect = pygame.Rect(0, 0, credits_text_rect.width + 20, credits_text_rect.height + 20)
    credits_button_rect.center = (env.w * 0.5, env.h*0.5)
    credits_text_rect.center = credits_button_rect.center

    exit_text_surface = button_font.render("Exit", True, (0, 0, 0))
    exit_text_rect = exit_text_surface.get_rect()
    exit_button_rect = pygame.Rect(0, 0, exit_text_rect.width + 20, exit_text_rect.height + 20)
    exit_button_rect.center = (env.w * 0.5, env.h*0.6)
    exit_text_rect.center = exit_button_rect.center

    rotation_angle = 0
    rotation_speed = 2
    pause_duration = 200
    pause_counter = 0 
    pause = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        env.screen.fill((0, 0, 0))

        rotated_title = pygame.transform.rotate(title_surface, rotation_angle)
        rotated_title_rect = rotated_title.get_rect(center=title_rect.center)
        env.screen.blit(rotated_title, rotated_title_rect)
        if not pause:
            rotation_angle += rotation_speed * env.dt
            if (rotation_angle >= 10) or (rotation_angle <= -10):
                pause = True
                rotation_speed *= -1
        else:
            rotation_angle += rotation_speed * env.dt * 0.1
            pause_counter += 1
            if pause_counter >= pause_duration:
                pause = False
                pause_counter = 0

        pygame.draw.rect(env.screen, pygame.Color('white'), play_button_rect)
        env.screen.blit(play_text_surface, play_text_rect)
        
        pygame.draw.rect(env.screen, pygame.Color('white'), credits_button_rect)
        env.screen.blit(credits_text_surface, credits_text_rect)

        pygame.draw.rect(env.screen, pygame.Color('white'), exit_button_rect)
        env.screen.blit(exit_text_surface, exit_text_rect)

        mouse_pos = pygame.mouse.get_pos()
        if(play_button_rect.collidepoint(mouse_pos)) and pygame.mouse.get_pressed()[0]:
            difficulty_screen()
            sys.exit()
        elif(credits_button_rect.collidepoint(mouse_pos)) and pygame.mouse.get_pressed()[0]:
            credits_screen()
            sys.exit()
        elif(exit_button_rect.collidepoint(mouse_pos)) and pygame.mouse.get_pressed()[0]:
            env.quit()
            sys.exit()


        pygame.display.flip()
        env.clock_tick()

menu_screen()