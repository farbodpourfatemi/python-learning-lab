# Python Learning Lab

A collection of **introductory Python coursework and personal practice**, organized by topic. Based on exercises completed while studying Python with Aiolearn; reviewed and refactored for readability, validation, safety, and reusability. This is coursework, not a collection of production systems.

## Exercises

| File | Topic |
| --- | --- |
| `coursework/count_fives.py` | Functions, loops, and string operations |
| `coursework/age_calculator.py` | Dates and input validation |
| `coursework/weather_cli.py` | HTTP requests and environment variables |
| `coursework/rock_paper_scissors.py` | Loops, conditionals, game rules |
| `coursework/numpy_image_practice.py` | NumPy arrays and image operations |
| `coursework/text_repeat_demo.py` | Safe demonstration of loops |
| `coursework/qr_code_generator.py` | QR code generation |
| `personal/random_mission.py` | Random sampling and user interaction |
| `personal/secret_number.py` | Input validation and guessing logic |

## Quick start

Python 3.10+ recommended.

```bash
python -m venv .venv
# Activate the virtual environment before installing packages.
python -m pip install -r requirements.txt
python coursework/count_fives.py
python coursework/qr_code_generator.py "https://example.com"
```

`weather_cli.py` requires an OpenWeather API key stored in the **`OPENWEATHER_API_KEY`** environment variable (never commit a real key). `numpy_image_practice.py` takes a path to your own image and writes `annotated.png`.

## Notes

- This repository is for educational demonstration and documents learning progress.
- Some lessons were adapted for safety and portability; notably, message automation now prints locally rather than sending repeated messages.
- Original class handouts, private data, passwords, and API keys have not been included.
- Before publishing any course-derived work, confirm your course allows public sharing of its materials.
