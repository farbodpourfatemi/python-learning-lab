"""Calculate an exact calendar age from a date of birth (Gregorian calendar)."""
from datetime import date


def calculate_age(birth: date, today: date) -> tuple[int, int]:
    if birth > today:
        raise ValueError("The date of birth cannot be in the future.")
    years = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    days = (today - birth).days
    return years, days


def main() -> None:
    try:
        birth = date.fromisoformat(input("Date of birth (YYYY-MM-DD): ").strip())
        years, days = calculate_age(birth, date.today())
    except ValueError as exc:
        print(f"Invalid date: {exc}")
        return
    print(f"Age: {years} completed years ({days:,} days / {days * 24:,} hours).")


if __name__ == "__main__":
    main()
