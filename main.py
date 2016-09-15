from visualisation import Visualiser
import settings


if __name__ == '__main__':
    visual_chess = Visualiser()
    visual_chess.draw_chessboard("black")
    visual_chess.game.chess_start()
    visual_chess.redraw_situation()
    settings.canvas.bind("<Button-1>", visual_chess.move_clicked)
    settings.root.mainloop()
