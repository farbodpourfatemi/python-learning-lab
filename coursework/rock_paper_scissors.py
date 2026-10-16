"""A best-of-five Rock, Paper, Scissors terminal game."""
import random

CHOICES = ("rock", "paper", "scissors")
WINNING_PAIRS = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}


def winner(player: str, computer: str) -> int:
    """Return 1 for player win, -1 for computer win, 0 for a tie."""
    if player == computer:
        return 0
    return 1 if (player, computer) in WINNING_PAIRS else -1


def main() -> None:
    player_score = computer_score = 0
    while max(player_score, computer_score) < 3:
        player = input("Rock, paper, scissors, or quit: ").strip().lower()
        if player in {"quit", "exit"}:
            print("Game ended.")
            return
        if player not in CHOICES:
            print("Choose rock, paper, or scissors.")
            continue
        computer = random.choice(CHOICES)
        result = winner(player, computer)
        player_score += result == 1
        computer_score += result == -1
        print(f"You: {player} | Computer: {computer} | Score: {player_score}-{computer_score}")
    print("You win!" if player_score > computer_score else "Computer wins!")


if __name__ == "__main__":
    main()
