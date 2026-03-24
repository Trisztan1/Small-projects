def main():
    texts = []
    ciphered_text = "FVZCYR PNRFNE PVCURE"

    for i in range(26):
        texts.append(breaking_tool(ciphered_text, i))

    for i, text in enumerate(texts):
        print(f"{i}. {text}")


def breaking_tool(text, key):
    chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    text = text.upper().strip()

    text_list = []
    new_text_list = []
    new_text = ""

    for i in text:
        text_list.append(i)

    for i, value in enumerate(text_list):
        if value == " ":
            new_text_list.append(value)
            continue

        position = chars.index(value)
        f_value = (position - key) % 26
        char = chars[f_value]
        new_text_list.append(char)
    
    for i in new_text_list:
        new_text += i


    return new_text


if __name__ == "__main__":
    main()