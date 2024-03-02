import pygame
import math
import sys

class Object:
    def __init__(self, pos, vel, w, h, radius = 25, mass=10, gravity=pygame.math.Vector2(0,-1000), drag=0.1, color=(255,255,255)):
        self.color = color
        self.radius = radius
        self.mass = mass
        self.gravity = gravity
        self.drag = drag
        self.pos = pos
        self.vel = vel
        self.last_mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos()) 
        self.frames_since_collision = 500
        self.game_over = False
        self.score = 0
        self.font = pygame.font.SysFont("Times New Roman", 50)
        self.game_over_text = self.font.render("Game over", True, (255, 255, 255))
        self.restart_text = self.font.render("Restart", True, (0, 0, 0))
        self.exit_text = self.font.render("Exit", True, (0, 0, 0))
        self.mouse_hit_sound = pygame.mixer.Sound("mouse_hit.mp3")
        self.wall_hit_sound = pygame.mixer.Sound("wall_hit.mp3")

    def update(self, dt, w, h, difficulty):
        mouse_pos_pygame = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_pos = pygame.math.Vector2(mouse_pos_pygame.x,h-mouse_pos_pygame.y)
        if(self.game_over):
            if pygame.Rect(0.2*w, 0.6*h, 0.15*w, h*0.1).collidepoint(mouse_pos_pygame):
                self.game_over = False
                self.pos = pygame.math.Vector2(w*0.1,h*0.6)
                self.vel = pygame.math.Vector2(0.08789*w,0.732*h)
                self.score = 0
            elif pygame.Rect(0.2*w, 0.7*h, 0.15*w, h*0.1).collidepoint(mouse_pos_pygame) and pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()
            return

        self.pos += self.vel * dt
        self.vel += self.gravity * dt
        
        if (self.pos.y <= (self.radius*0.8)) and (self.pos.x >= 0.7*w):
            self.pos.y = (self.radius*0.8)
            self.vel.y *= -0.9
            pygame.mixer.Sound.play(self.wall_hit_sound)
        if (self.pos.y <= (self.radius)) and (self.pos.x <= 0.7*w):
            self.game_over = True
        if self.pos.y >= h-(self.radius*0.8):
            self.pos.y = h-(self.radius*0.8)
            self.vel.y *= -0.9
            pygame.mixer.Sound.play(self.wall_hit_sound)
        if self.pos.x >= w-(self.radius*0.8):
            self.pos.x = w-(self.radius*0.8)
            self.vel.x *= -0.9
            self.score+=1
            pygame.mixer.Sound.play(self.wall_hit_sound)
        elif self.pos.x <= (self.radius*0.8):
            self.pos.x = (self.radius*0.8)
            self.vel.x *= -0.9
            pygame.mixer.Sound.play(self.wall_hit_sound)
        
        distance_mouse_to_center = math.sqrt((self.pos.x-mouse_pos.x)**2+(self.pos.y-mouse_pos.y)**2)
        mouse_collided = distance_mouse_to_center <= self.radius

        if mouse_collided and (self.frames_since_collision>100):
            displacement_mouse = mouse_pos - self.last_mouse_pos
            mouse_vel = displacement_mouse / dt
            mouse_vel_magnitude = mouse_vel.length()
            desired_magnitude = 101.1*(mouse_vel_magnitude**0.3)*difficulty
            if(mouse_vel_magnitude != 0):
                self.vel = mouse_vel.normalize() * desired_magnitude
            else:
                self.vel *= -0.5
            self.frames_since_collision = 0
            pygame.mixer.Sound.play(self.mouse_hit_sound)
        else:
            self.frames_since_collision += 1
        self.last_mouse_pos = mouse_pos
        #exclusion zone
        if(mouse_pos.x >= 0.7*w):
            pygame.mouse.set_pos(0.7*w, h-mouse_pos.y)

    def draw(self, screen, w, h):
        pygame.draw.rect(screen, pygame.Color(100, 30, 30, 100), pygame.Rect(0.7*w, 0, 0.3*w, h))
        pygame.draw.line(screen,(255,255,255), (0.7*w,0), (0.7*w, h))
        pygame.draw.circle(screen, self.color, pygame.math.Vector2(self.pos.x, screen.get_size()[1] - self.pos.y), self.radius)
        if self.game_over:
            screen.blit(self.game_over_text, (w*0.2, 0.5*h))

            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), pygame.Rect(0.2*w, 0.6*h, 0.15*w, h*0.1))
            screen.blit(self.restart_text, (w*0.2, 0.6*h))

            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), pygame.Rect(0.2*w, 0.7*h, 0.15*w, h*0.1))
            screen.blit(self.exit_text, (w*0.2, 0.7*h))

        screen.blit(self.font.render("Score: " + str(self.score), True, (255, 255, 255)), (0.01*w, 0.01*h))



    