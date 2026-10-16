"""Demonstrate NumPy image slicing without hard-coded image dimensions."""
import argparse
from pathlib import Path
import numpy as np
from PIL import Image


def annotate_image(input_path: Path, output_path: Path) -> None:
    with Image.open(input_path) as image:
        pixels = np.asarray(image.convert("RGB"), dtype=np.uint8).copy()
    height, width = pixels.shape[:2]
    row, col = height // 2, width // 2
    pixels[row, :] = (0, 0, 0)
    pixels[:, col] = (0, 0, 0)
    offset = max(1, min(height, width) // 5)
    top, bottom = max(0, row - offset), min(height, row + offset)
    left, right = max(0, col - offset), min(width, col + offset)
    pixels[top:bottom, left] = (255, 0, 0)
    pixels[top:bottom, right - 1] = (255, 0, 0)
    pixels[top, left:right] = (255, 0, 0)
    pixels[bottom - 1, left:right] = (255, 0, 0)
    Image.fromarray(pixels).save(output_path)
    print(f"Saved {output_path} ({width}x{height})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Image you own or are allowed to use")
    parser.add_argument("--output", type=Path, default=Path("annotated.png"))
    args = parser.parse_args()
    annotate_image(args.image, args.output)


if __name__ == "__main__":
    main()
