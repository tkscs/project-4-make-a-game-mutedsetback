import pygame

pygame.init()

width = 1200
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 64)
black = (0, 0, 0)
blue = (80, 150, 255)
green = (60, 220, 90)
x = 80 #This is the distance setting for the walls. (Might use this for the flashlight effect later as it getting the flashlight could just expand your vision, instead of being directional)
size = 30
playersize = 20
player_speed = 4
maze = [
    "#.#####################################",
    "#.#...#...#...........#.........#.....#",
    "#.#.#.#.#.#.#########.#.#######.#.###.#",
    "#.#.#.#.#.#...#.....#.#.#...#...#.#...#",
    "#.#.#.#.#.###.#.###.#.#.#.#.#####.#.#.#",
    "#...#...#.#...#...#...#.#.#.......#.#.#",
    "#########.#.#####.#####.#.#####.###.#.#",
    "#...#...#...#...#.....#...#...#.#...#.#",
    "#.###.#.#######.#####.#####.#.###.###.#",
    "#...#.#.#...........#...#...#.....#...#",
    "#.#.#.#.#.###.#########.#.#########.###",
    "#.#.#.#.#.#.#.....#...#...#.....#...#.#",
    "#.#.#.#.#.#.#####.#.#.#######.#.#.###.#",
    "#.#...#.#.#...#...#.#.........#.#.#...#",
    "#.#####.#.#.#.#.#.#.#####.#######.###.#",
    "#...#.#.#.#.#.#.#.#.#.....#.....#.....#",
    "###.#.#.#.#.#.#.###.#.#####.###.#####.#",
    "#...#.#...#.#.#.#...#...#.....#.....#.#",
    "#.###.#######.#.#.#####.#.#####.#####.#",
    "#.#...........#.#.#...#...#...#...#...#",
    "#.#.###########.#.#.#######.#.###.#.###",
    "#.#...#.....#...#.#.....#...#.....#...#",
    "#.#.#.#.###.#.###.#.#.#.#.###########.#",
    "#.#.#.#...#.#.#...#.#.#.#.#.........#.#",
    "#.###.#.###.#.#.#####.###.#.#######.#.#",
    "#...#...#...#.#.#...#...#.#.......#...#",
    "###.#####.#.#.#.#.#.###.#.#######.#####",
    "#.........#.#.....#.....#.............#",
    "#####################################.#",
]

mazerows = len(maze)
mazecolombs = len(maze[0])

def creatwalls():
    list = []
    for row in range(mazerows):
        for col in range(mazecolombs):
            if maze[row][col] == "#":
                list.append(pygame.Rect(col * size, row * size, size, size))
    return list

walls = creatwalls()
exit = pygame.Rect((mazecolombs - 2) * size, (mazerows - 2) * size, size, size)
moveonX = size + size / 2
moveonY = size + size / 2
half = playersize / 2

def player():
    return pygame.Rect(moveonX - half, moveonY - half, playersize, playersize)

def distance(wall):
    closest_x = max(wall.left, min(moveonX, wall.right))
    closest_y = max(wall.top, min(moveonY, wall.bottom))
    diff_x = moveonX - closest_x
    diff_y = moveonY - closest_y
    return (diff_x * diff_x + diff_y * diff_y) ** 0.5

def controls(move_x, move_y):
    global moveonX, moveonY
    moveonX += move_x
    moveonY += move_y
    for wall in walls:
        if player().colliderect(wall):
            if move_x > 0:
                moveonX = wall.left - half
            elif move_x < 0:
                moveonX = wall.right + half
            if move_y > 0:
                moveonY = wall.top - half
            elif move_y < 0:
                moveonY = wall.bottom + half

haswon = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not haswon:
        keys = pygame.key.get_pressed()
        move_x = 0
        move_y = 0
        if keys[pygame.K_a]:
            move_x -= player_speed
        if keys[pygame.K_d]:
            move_x += player_speed
        if keys[pygame.K_w]:
            move_y -= player_speed
        if keys[pygame.K_s]:
            move_y += player_speed
        controls(move_x, 0)
        controls(0, move_y)
        if player().colliderect(exit):
            haswon = True
    screen.fill(black)
    pygame.draw.rect(screen, green, exit)
    for wall in walls:
        if distance(wall) < x:
            pygame.draw.rect(screen, (255, 255, 255), wall)
    pygame.draw.circle(screen, blue, (int(moveonX), int(moveonY)), playersize // 2)
    if haswon:
        text = font.render("You Won!", True, green)
        screen.blit(text, text.get_rect(center=(width // 2, height // 2)))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
