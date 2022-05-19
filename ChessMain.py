import pygame as p

WIDTH = 720
HEIGHT = 800
DIMENSION_R = 10
DIMENSION_C = 9
SQ_SIZE_W = WIDTH // DIMENSION_C
SQ_SIZE_H = HEIGHT // DIMENSION_R
MAX_FPS = 15
IMAGES = {}

#ban co
board= [[1, 2, 3, 4, 5, 6, 7, 8, 9],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 10, 0, 0, 0, 0, 0, 11, 0],
         [12, 0, 13, 0, 14, 0, 15, 0, 16],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [-12, 0, -13, 0, -14, 0, -15, 0, -16],
         [0, -10, 0, 0, 0, 0, 0, -11, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [-1, -2, -3, -4, -5, -6, -7, -8, -9]

# danh sach cac nuoc di
moves = [[[0, 2, 3, 4, 5, 6, 7, 8, 9],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 10, 0, 0, 0, 0, 0, 11, 0],
         [12, 0, 13, 0, 14, 0, 15, 0, 16],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [-12, 0, -13, 0, -14, 0, -15, 0, -16],
         [0, -10, 0, 0, 0, 0, 0, -11, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [-1, -2, -3, -4, -5, -6, -7, -8, -9]],
        [[0, 2, 3, 4, 5, 6, 7, 8, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 10, 0, 0, 0, 0, 0, 11, 9],
         [12, 0, 13, 0, 14, 0, 15, 0, 16],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [-12, 0, -13, 0, -14, 0, -15, 0, -16],
         [0, -10, 0, 0, 0, 0, 0, -11, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [-1, -2, -3, -4, -5, -6, -7, -8, -9]]
        ]
#lay hinh may quan co
def loadImages():
    pieces = ["bC", "bE", "bK", "bKn", "bM", "bP", "bR", "rC", "rE", "rK", "rKn", "rM", "rP", "rR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Img/"+piece+".png"), (SQ_SIZE_W,SQ_SIZE_H))

#visualize
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    loadImages()
    running = True

    background_image = p.image.load("Img/boardchess.png").convert()
    screen.blit(background_image, [0, 0])
    drawGameState(screen, board)
    presses = -1

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        mouse_presses = p.mouse.get_pressed()
        num_states = len(moves)
        if mouse_presses[0]:
            presses += 1
            if presses < num_states:
                screen.blit(background_image, [0, 0])
                drawGameState(screen, moves[presses])
                p.display.flip()
        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen,board):
    get_piece = {1: "bR", 9: "bR", 2: "bKn", 8: "bKn", 3: "bE", 7: "bE",
                 4: "bM", 6: "bM", 5: "bK", 10: "bC", 11: "bC", 12 : "bP",
                 13: "bP" , 14: "bP", 15: "bP",16: "bP",
                 -1: "rR", -9: "rR", -2: "rKn", -8: "rKn", -3: "rE", -7: "rE",
                 -4: "rM", -6: "rM", -5: "rK", -10: "rC", -11: "rC", -12: "rP",
                 -13: "rP", -14: "rP", -15: "rP", -16: "rP"}
    for r in range(DIMENSION_R):
        for c in range(DIMENSION_C):
            if board[r][c] != 0:
                piece = get_piece[board[r][c]]
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE_W,r*SQ_SIZE_H,SQ_SIZE_W,SQ_SIZE_H))

main()