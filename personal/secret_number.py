"""Guess-the-number game with input validation and attempt count."""
import random


def play_game(secret: int) -> int:
    attempts = 0
    while True:
        answer = input("Guess an integer from 1 to 20 (or 'quit'): ").strip().lower()
        if answer in ("quit", "exit"):
            print("Game cancelled.")
            return attempts
        try:
            guess = int(answer)
        except ValueError:
            print("Please enter an integer.")
            continue
        if guess not in range(1, 21):
            print("Enter a number between 1 and 20.")
            continue
        attempts += 1
        if guess == secret:
            print(f"Correct in {attempts} attempt(s)!")
            return attempts
        print("Try higher." if guess < secret else "Try lower.")


if __name__ == "__main__":
    play_game(random.randint(1, 20))
