"""Generate a QR code from a user-provided URL or text. No embedded secrets."""
import argparse
from pathlib import Path
import qrcode


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", help="A URL or text to encode")
    parser.add_argument("--output", type=Path, default=Path("qrcode.png"))
    args = parser.parse_args()
    if not args.text.strip():
        parser.error("The text cannot be empty")
    qrcode.make(args.text).save(args.output)
    print(f"Saved QR image to {args.output}")


if __name__ == "__main__":
    main()
