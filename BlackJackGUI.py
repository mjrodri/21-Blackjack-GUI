import tkinter as tk
import random

class BlackjackGUI:
    def __init__(self, master):
        self.master = master
        master.title("Blackjack")

        self.player_cards = []
        self.dealer_cards = []

        self.player_score = tk.StringVar()
        self.dealer_score = tk.StringVar()
        self.result_text = tk.StringVar()

        self.player_score.set("Player's Score: ")
        self.dealer_score.set("Dealer's Score: ")
        self.result_text.set("")

        self.player_score_label = tk.Label(master, textvariable=self.player_score)
        self.player_score_label.grid(row=0, column=0)

        self.dealer_score_label = tk.Label(master, textvariable=self.dealer_score)
        self.dealer_score_label.grid(row=0, column=1)

        self.result_label = tk.Label(master, textvariable=self.result_text)
        self.result_label.grid(row=1, columnspan=2)

        self.hit_button = tk.Button(master, text="Hit", command=self.hit)
        self.hit_button.grid(row=2, column=0)

        self.stand_button = tk.Button(master, text="Stand", command=self.stand)
        self.stand_button.grid(row=2, column=1)

        self.restart_button = tk.Button(master, text="Restart", command=self.restart)
        self.restart_button.grid(row=3, columnspan=2)

    def draw_card(self):
        """Return a random card from 1 to 11."""
        return random.randint(1, 11)

    def calculate_score(self, cards):
        """Calculate the score of a list of cards."""
        score = sum(cards)
        if score == 21 and len(cards) == 2:
            return 0  # Blackjack
        if 11 in cards and score > 21:
            cards.remove(11)
            cards.append(1)  # Convert an Ace from 11 to 1
        return score

    def hit(self):
        self.player_cards.append(self.draw_card())
        player_score = self.calculate_score(self.player_cards)
        self.player_score.set(f"Player's Score: {player_score}")
        if player_score > 21:
            self.result_text.set("Busted! You lose!")

    def stand(self):
        while self.calculate_score(self.dealer_cards) < 17:
            self.dealer_cards.append(self.draw_card())
        dealer_score = self.calculate_score(self.dealer_cards)
        self.dealer_score.set(f"Dealer's Score: {dealer_score}")
        if dealer_score > 21:
            self.result_text.set("Dealer busts! You win!")
        elif dealer_score > self.calculate_score(self.player_cards):
            self.result_text.set("You lose!")
        elif dealer_score < self.calculate_score(self.player_cards):
            self.result_text.set("You win!")
        else:
            self.result_text.set("It's a draw!")

    def restart(self):
        self.player_cards = []
        self.dealer_cards = []
        self.player_score.set("Player's Score: ")
        self.dealer_score.set("Dealer's Score: ")
        self.result_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()