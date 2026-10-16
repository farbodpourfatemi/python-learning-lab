"""Count occurrences of the digit 5 in all integers from 1 through N."""

def count_fives(number: int) -> int:
    if number < 1:
        return 0
    return sum(str(value).count("5") for value in range(1, number + 1))


def main() -> None:
    try:
        number = int(input("Enter a positive integer: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    print(f"The digit 5 appears {count_fives(number)} times.")


if __name__ == "__main__":
    main()
