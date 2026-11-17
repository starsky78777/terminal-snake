import random
import curses

class SnakeGame:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        self.sh, self.sw = self.stdscr.getmaxyx()
        
        self.w = curses.newwin(self.sh, self.sw, 0, 0)
        self.w.keypad(1)
        self.w.timeout(100)
        self.reset_game()

    def reset_game(self):
        self.score = 0
        self.game_speed = 100
        self.w.timeout(self.game_speed)

        snk_x = int(self.sw / 4)
        snk_y = int(self.sh / 2)
        self.snake = [
            [snk_y, snk_x],
            [snk_y, snk_x - 1],
            [snk_y, snk_x - 2]
        ]

        self.key = curses.KEY_RIGHT
        self.spawn_food()

    def spawn_food(self):
        self.food = None
        while self.food is None:
            nf = [
                random.randint(2, self.sh - 2),
                random.randint(2, self.sw - 2)
            ]
            self.food = nf if nf not in self.snake else None
        
        try:
            self.w.addch(self.food[0], self.food[1], curses.ACS_PI)
        except curses.error:
            pass

    def run(self):
        while True:
            try:
                self.w.addstr(0, 2, f" Score: {self.score} | Press 'Q' to Quit ")
            except curses.error:
                pass

            next_key = self.w.getch()
            if next_key in [ord('q'), ord('Q')]:
                break

            self.key = self.key if next_key == -1 else next_key

            head = self.snake[0]
            if (head[0] in [0, self.sh - 1] or 
                head[1] in [0, self.sw - 1] or 
                head in self.snake[1:]):
                
                self.w.clear()
                msg = f" GAME OVER! Final Score: {self.score}. Press R to Restart or Q to Quit. "
                try:
                    self.w.addstr(int(self.sh/2), int((self.sw - len(msg))/2), msg)
                    self.w.refresh()
                except curses.error:
                    pass

                self.w.timeout(-1)
                while True:
                    k = self.w.getch()
                    if k in [ord('r'), ord('R')]:
                        self.w.clear()
                        self.reset_game()
                        break
                    elif k in [ord('q'), ord('Q')]:
                        return

            new_head = [head[0], head[1]]
            if self.key == curses.KEY_DOWN:
                new_head[0] += 1
            elif self.key == self.key == curses.KEY_UP: # Fixed syntax typo check
                new_head[0] -= 1
            # Standardizing directional checks cleanly:
            if self.key == curses.KEY_UP:
                new_head[0] -= 1
            elif self.key == curses.KEY_DOWN:
                new_head[0] += 1
            elif self.key == curses.KEY_LEFT:
                new_head[1] -= 1
            elif self.key == curses.KEY_RIGHT:
                new_head[1] += 1

            self.snake.insert(0, new_head)

            if self.snake[0] == self.food:
                self.score += 1
                if self.score % 5 == 0 and self.game_speed > 40:
                    self.game_speed -= 10
                    self.w.timeout(self.game_speed)
                self.spawn_food()
            else:
                tail = self.snake.pop()
                try:
                    self.w.addch(int(tail[0]), int(tail[1]), ' ')
                except curses.error:
                    pass

            try:
                self.w.addch(self.snake[0][0], self.snake[0][1], curses.ACS_CKBOARD)
            except curses.error:
                pass

def main(stdscr):
    game = SnakeGame(stdscr)
    game.run()

if __name__ == "__main__":
    curses.wrapper(main)
