# Password tool (`password_funcs.py`)

Small Python project for practice: check passwords and generate random ones in the terminal.

## About

The main part is a class called `Password`. It can:

- check if a password uses only allowed characters and is not a known weak password
- give a rough strength label (like Medium, Hard, etc.)
- create random passwords with weights for uppercase, lowercase, numbers, and special chars

There is also a `main()` loop so you can use it interactively.

## What you need

- Python **3.10 or newer** (the code uses `str | None` in type hints)
- Two text files, **one line per entry**, in the **parent folder** of where you run the script:
  - `../100k-most-used-passwords-NCSC.txt` — common passwords list
  - `../names.txt` — names (if your password matches a name in the list it fails the check)

The program opens those paths when you create a `Password` object. If a file is missing you get an error.

**Note:** It is easiest if you `cd` into the `password_codes` folder and run the script from there, so `../` points at the folder that actually has the `.txt` files.

## How to run

```
python password_funcs.py
```

Then type commands when it asks. Examples:

- `help` or `-h` — prints help text
- `check` — enter a password; it validates and shows strength
- `correct` — only checks if the password is "correct" (allowed chars, not common, no name)
- `create` — builds random password(s); you choose length, how many, and weights
- `commands` — lists commands
- `clear` — prints empty lines to clear the screen a bit
- `exit` — quit

## Files in this folder

| File | What it is |
|------|------------|
| `password_funcs.py` | password program |
| `breaking_ceaser_cipher.py` | different exercise, not part of the password menu |

## Author note

Made while learning Python. Uses only the standard library.
