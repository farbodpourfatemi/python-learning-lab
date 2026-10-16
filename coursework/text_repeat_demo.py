"""A safe version of an early repetition/automation exercise.

The original script automated sending repeated messages in another application.
This version demonstrates loops locally without sending messages to anyone.
"""

def repeat_text(text: str, count: int) -> list[str]:
    if not 0 <= count <= 100:
        raise ValueError("count must be between 0 and 100")
    return [text for _ in range(count)]


def main() -> None:
    text = input("Text to repeat locally: ")
    for line in repeat_text(text, 5):
        print(line)


if __name__ == "__main__":
    main()
