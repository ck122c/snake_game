import pygame          # pygame library import kiya – game banane ke liye
import sys             # sys exit ke liye use hota hai
import random          # random food position generate karne ke liye

CELL_SIZE = 30       # grid ka ek cell (block) 30 px ka hoga
CELL_NUMBER = 25       # total grid 25x25 = window size 500x500 ban jayega
FPS = 7              # game ki initial speed

# --- Colors ---
WHITE = (255,255,255)  # white color RGB
BLACK = (0,0,0)        # black color
RED = (200,30,30)      # red color for food
GREEN = (30,180,30)    # snake body color
DARK_GREEN = (0,120,0) # dark green
BLUE = (30,144,255)    # blue (game over text)
GRAY = (60,60,60)      # light grid lines
YELLOW = (255,215,0)   # yellow color for snake head

# ========================================================
# SNAKE CLASS – 
# ========================================================
class Snake:
    def __init__(self):
        self.body = [(7, 12), (6, 12), (5, 12)]   # snake start position (3 blocks)
        self.direction = (1, 0)                   # start me right direction me move karega
        self.grow_flag = False                    # food khane par True hoga

    def move(self):
        head_x, head_y = self.body[0]             # current head coordinate
        dx, dy = self.direction                   # movement direction (dx, dy)
        new_head = ((head_x + dx) % CELL_NUMBER,
                    (head_y + dy) % CELL_NUMBER)  # wrap-around logic (wall cross kar sakta hai)

        self.body.insert(0, new_head)             # new head ko list ke starting me insert kiya

        if self.grow_flag:                        # agar grow flag True hai
            self.grow_flag = False                # ek step grow karke flag reset
        else:
            self.body.pop()                       # otherwise tail remove (normal movement)

    def grow(self):
        self.grow_flag = True                     # food khane par grow flag set

    def set_direction(self, new_dir):
        opposite = (-self.direction[0], -self.direction[1])  # opposite direction check
        if new_dir != opposite:                   # snake ko ulta nahi mudne dena
            self.direction = new_dir              # direction update

    def collides_with_self(self):
        return self.body[0] in self.body[1:]      # agar head body se takraye → True

# ========================================================
# FOOD CLASS – Food ka random position 
# ========================================================
class Food:
    def __init__(self, snake_body):
        self.position = self.random_pos(snake_body) # food ko snake ke upar nahi rakhna

    def random_pos(self, snake_body):
        while True:                                 # random position search
            pos = (random.randint(0, CELL_NUMBER-1),
                   random.randint(0, CELL_NUMBER-1))
            if pos not in snake_body:               # agar pos snake ke upar nahi hai
                return pos                           # to valid position return karo

# ========================================================
# DRAWING FUNCTIONS – Screen par cheezein 
# ========================================================
def draw_grid(surface):
    for x in range(CELL_NUMBER):                             # vertical lines
        pygame.draw.line(surface, GRAY,
                         (x * CELL_SIZE, 0),
                         (x * CELL_SIZE, CELL_NUMBER * CELL_SIZE))

    for y in range(CELL_NUMBER):                             # horizontal lines
        pygame.draw.line(surface, GRAY,
                         (0, y * CELL_SIZE),
                         (CELL_NUMBER * CELL_SIZE, y * CELL_SIZE))

def draw_snake(surface, snake):
    for i, block in enumerate(snake.body):          # snake ke har block ko draw karo
        x, y = block
        rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE,
                           CELL_SIZE, CELL_SIZE)

        if i == 0:                                  # snake head
            pygame.draw.rect(surface, YELLOW, rect, border_radius=6)
        else:                                       # snake body me gradient color
            color = (0, 180 - i % 50, 0)
            pygame.draw.rect(surface, color, rect, border_radius=4)

        pygame.draw.rect(surface, BLACK, rect, 1)  # border line

def draw_food(surface, food):
    x, y = food.position
    rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE,
                       CELL_SIZE, CELL_SIZE)
    pygame.draw.ellipse(surface, RED, rect)        # food ko circle draw kiya
    pygame.draw.rect(surface, BLACK, rect, 1)      # border

def show_text(surface, text, size, pos, color=WHITE):
    font = pygame.font.SysFont("Arial", size, bold=True)  # font choose kiya
    surf = font.render(text, True, color)                 # text ko render kiya
    surface.blit(surf, pos)                               # screen par text draw

# ========================================================
# GAME LOOP – pura game yahan chal raha hai
# ========================================================
def game_loop():
    pygame.init()                                               # pygame start

    screen = pygame.display.set_mode((
        CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))      # main window

    pygame.display.set_caption("🐍 Snake Game - Press Esc to Quit") # window title
    clock = pygame.time.Clock()                                 # FPS control

    snake = Snake()                                             # snake object create
    food = Food(snake.body)                                     # food object create
    score = 0                                                   # starting score
    running = True                                              # game running flag
    game_over = False                                           # game over flag

    global FPS                                                  # FPS ko modify karne ke liye

    while running:                                              # main loop
        clock.tick(FPS)                                         # frame rate control

        # ----------------------- EVENTS -----------------------
        for event in pygame.event.get():                        # events check
            if event.type == pygame.QUIT:
                running = False                                 # window close

            if event.type == pygame.KEYDOWN:                    # key press
                if event.key == pygame.K_ESCAPE:
                    running = False                             # Escape = exit

                if not game_over:                               # game chal raha ho
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        snake.set_direction((0, -1))            # upar
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        snake.set_direction((0, 1))             # niche
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        snake.set_direction((-1, 0))            # left
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        snake.set_direction((1, 0))             # right

                else:                                           # game over ho chuka
                    if event.key == pygame.K_r:                 # R = restart
                        snake = Snake()
                        food = Food(snake.body)
                        score = 0
                        game_over = False
                        FPS = 10                                # restart speed

        # ----------------------- GAME LOGIC -----------------------
        if not game_over:
            snake.move()                                        # snake move karega

            if snake.body[0] == food.position:                  # food eat logic
                snake.grow()                                    # grow
                score += 1                                      # score increase
                food = Food(snake.body)                         # new food generate

                if score % 5 == 0 and FPS < 25:                 # speed increase logic
                    FPS += 1

            if snake.collides_with_self():                      # self collision
                game_over = True

        # ----------------------- DRAWING -----------------------
        screen.fill(BLACK)                                      # background
        draw_grid(screen)                                       # grid draw
        draw_snake(screen, snake)                               # snake draw
        draw_food(screen, food)                                 # food draw
        show_text(screen, f"Score: {score}", 24, (10, 10))      # score text

        if game_over:
            show_text(screen, "GAME OVER! Press R to Restart",
                      36, (50, CELL_SIZE * CELL_NUMBER // 2 - 20),
                      color=BLUE)                               # game over text

        pygame.display.flip()                                   # screen update

    pygame.quit()                                               # pygame quit
    sys.exit()                                                  # system exit

# ========================================================
# GAME START
# ========================================================
if __name__ == "__main__":
    game_loop()                                                 # loop start
