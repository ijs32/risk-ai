from classes.game import Game

def main():
    game = Game()

    status = game.status
    while status:
        game.take_turn()

        status = game.status

if __name__ == "__main__":
    main()