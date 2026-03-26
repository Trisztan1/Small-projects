from numpy._core.defchararray import add
import pyperclip as pyp
import pandas as pn

def main():
    text = pyp.paste()

    pyp.copy(adding_bullet_stars(text))


def adding_bullet_stars(text):
    text = list(text)
    for index, char in enumerate(text):
        if char == "\n":
            text[index] = "\n* "
    text[0] = f"* {text[0]}"
    
    return "".join(text)

def adding_bullet_stars_2(text):
    split_text = text.split("\n")
    for i in range(len(split_text)):
        split_text[i] = f"* {split_text[i]}"
    
    return "\n".join(split_text)



if __name__ == "__main__":
    main()
