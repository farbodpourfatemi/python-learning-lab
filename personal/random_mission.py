"""Random-mission generator: an interactive Python learning project."""
import random

MISSIONS = [
    "Explore an abandoned research station.",
    "Retrieve the lost map from ancient ruins.",
    "Escort a research team through a mountain pass.",
    "Investigate a mysterious signal from deep space.",
    "Deliver medical supplies to a remote settlement.",
    "Protect a convoy during a difficult expedition.",
]


def generate_mission() -> tuple[str, int, int]:
    return random.choice(MISSIONS), random.randint(1, 5), random.randrange(10, 101, 10)


def main() -> None:
    while True:
        name, level, xp = generate_mission()
        print(f"\nMission: {name}\nLevel: {level} | XP: {xp}")
        answer = input("Accept? [yes/no/exit]: ").strip().lower()
        if answer == "yes":
            print("Mission accepted!")
            break
        if answer == "exit":
            print("Goodbye!")
            break
        if answer != "no":
            print("Unknown response. Try again.")


if __name__ == "__main__":
    main()
