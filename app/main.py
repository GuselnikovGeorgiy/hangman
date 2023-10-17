import os
import time
import words
import stages
import random
import subprocess


class Game:
    def clear_screen(self):
        print("\033[H\033[J")
        # subprocess.call('cls')
        # os.system('cls||clear')

    def run(self):
        self.start_game()
        self.loop()

    def start_game(self):
        self.clear_screen()  # os.system('cls||clear')
        print("\t\t--- Hangman ---\n")
        print("\t Ку Владу, Ку Марку ыыы")
        print("\tPress Enter to start a new game!")
        input()
        self.clear_screen()

    def choose_word(self):
        return random.choice(words.word_list).lower()

    def draw_hangman(self, tries):
        return stages.stages[tries]

    def draw_screen(self, word_list, tries):
        self.clear_screen()
        print(self.draw_hangman(tries))
        print()
        print("\t"+" ".join(word_list))
        print()
        print("\tattempts left: ", len(stages.stages)-1-tries)
        print()
        print("Your answer: ", end="")

    def endgame(self, win):
        time.sleep(1)
        self.clear_screen()
        print("\t\tGame is over!\n")
        if win:
            print("\tYou won! Congratulations!\n")
        else:
            print("\tYou lose! You were hanged :(\n")
        print("\tPress Enter to start a new game\n\tor Type 'q' to quit: ", end='')
        ans = input()
        if "q" not in ans.lower():
            self.loop()
        else:
            return

    def loop(self):
        word = self.choose_word()
        word_list = ['_']*len(word)
        selected_letters = []
        tries = 0
        while True:
            self.draw_screen(word_list, tries)
            if "".join(word_list) == word:
                time.sleep(1)
                self.endgame(True)
                return
            if tries == len(stages.stages)-1:
                time.sleep(1)
                break
            char = input().lower()
            if len(char) != 1:
                continue
            else:
                if not char.isalpha():
                    print('\tA quite strange letter.. lol')
                    time.sleep(1)
                elif char in word and char not in word_list:
                    indexes = [i for i, c in enumerate(word) if c == char]
                    for i in indexes:
                        word_list[i] = char
                elif char in word_list:
                    print("\tThis letter already guessed!")
                    time.sleep(1)
                elif char in selected_letters:
                    print("\tYou've already tried this letter!")
                    time.sleep(1)
                else:
                    tries += 1
                selected_letters.append(char)
        self.endgame(False)
        return


game = Game()
game.run()
