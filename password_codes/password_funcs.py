import pprint
import re
import math
import random
import sys

class Password():
    def __init__(self, password: str | None = None) -> None:
        self.password: str | None = password
        self.password_lower = None if self.password == None else self.password.lower()
        self.common_pswrds = []
        self.common_names = []
        self.is_common_name = False
        self.special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "~"]
        self.valid_chars_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.valid_chars_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        # self.passw_char_list = [c for c in self.password]
        self.passw_char_list: list | None = list(self.password) if self.password != None else None
        self.load_common_passwrds()
        self.load_common_names()
        self.is_common_name_true()


    def load_common_passwrds(self):
        self.common_pswrds.clear()

        try:
            with open("../100k-most-used-passwords-NCSC.txt", "r", newline="", encoding='utf-8') as file:
                self.common_pswrds = [item.strip() for item in file]

        except Exception as e:
            raise RuntimeError("Failed to load common names file") from e
    
    def load_common_names(self):
        self.common_names.clear()

        try:
            with open("../names.txt", "r", newline = "", encoding="utf-8") as file:
                self.common_names = [item.strip() for item in file]

        except Exception as e:
            raise RuntimeError("Failed to load common names file") from e

    
    def is_common_name_true(self):
        self.is_common_name = False
    
        if self.password != None:
            for name in self.common_names:
                # rf is needed because without f name is not a variable
                if re.search(rf"(?i){name}", self.password):
                    self.is_common_name = True
                    break
        
                
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value
    

    def password_correctness(self):
        invalid_char = []

        for c in self.passw_char_list:
            if (c not in self.valid_chars_lower 
                and c not in self.valid_chars_upper 
                and c  not in self.special_chars
                and c not in {str(i) for i in range(10)}):

                invalid_char.append(c)

        if invalid_char:
            raise Exception("There are invalid chars in your password! Note that space is also invalid!")            
        elif self.password in self.common_pswrds:
            raise Exception("Your password is considered a known/common password!")
        elif self.is_common_name:
            raise Exception("There is a common name in your password, pleas omit the name!")

        return "Correct"
    

    def password_hardness(self):
        passwrd_score = 0
        is_uppercase = False
        uppercase_counter = 0
        is_lowercase = False
        lowercase_counter = 0
        is_special_char = False
        special_char_counter = 0
        is_number = False
        number_counter = 0
        all_character_counter = len(self.passw_char_list)

        for char in self.passw_char_list:
            if char in self.special_chars:
                is_special_char = True
                special_char_counter += 1
            elif char.isdecimal():
                is_number = True
                number_counter += 1
            elif char.isalpha() and char.islower():
                is_lowercase = True
                lowercase_counter += 1
            elif char.isalpha() and char.isupper():
                is_uppercase = True
                uppercase_counter += 1


        passwrd_score += math.floor(all_character_counter / 3)
        passwrd_score += special_char_counter
        passwrd_score += math.floor(number_counter / 2)
        passwrd_score += math.floor(lowercase_counter / 2)
        passwrd_score += math.floor(uppercase_counter / 2)
        
        if is_number == True and is_lowercase == True and is_uppercase == True and is_special_char == True:
            passwrd_score += 4
        elif is_number == True and is_lowercase == True and is_uppercase == True and is_special_char == False:
            passwrd_score += 3
        elif is_number == False and is_lowercase == True and is_uppercase == True and is_special_char == True:
            passwrd_score += 3
        elif is_number == True and is_lowercase == False and is_uppercase == True and is_special_char == False:
            passwrd_score += 2
        elif is_number == True and is_lowercase == True and is_uppercase == False and is_special_char == False:
            passwrd_score += 2
        elif is_number == False and is_lowercase == False and is_uppercase == True and is_special_char == True:
            passwrd_score += 2
        elif is_number == False and is_lowercase == True and is_uppercase == False and is_special_char == True:
            passwrd_score += 2
        elif is_number == True and is_lowercase == False and is_uppercase == False and is_special_char == True:
            passwrd_score += 2
        elif is_number == False and is_lowercase == True and is_uppercase == True and is_special_char == False:
            passwrd_score += 0
            raise Exception("You can't use only letters!")
        elif is_number == True and is_lowercase == False and is_uppercase == False and is_special_char == False:
            passwrd_score = 0
            raise Exception("You can't use only numbers!")
        elif is_number == False and is_lowercase == False and is_uppercase == False and is_special_char == True:
            passwrd_score = 0
            raise Exception("You can't use only special characters!")

        if passwrd_score > 15:
            return "EXTRA HARD"
        elif passwrd_score > 10:
            return "Hard"
        elif passwrd_score > 5:
            return "Medium"
        else:
            return "Unexceptable"
    
    def create_password(self, char_quantity: int, passwrd_quantity: int | None = None, weight: list | None = None):
        
        weights: list = [1, 1, 1, 1] if weight == None else weight # there should be four integer here
        # passwrd_quantity: int = 1 if passwrd_quantity == None or 0 else passwrd_quantity
        passwrd_quantity: int = passwrd_quantity or 1
        choices = ["upper", "lower", "number", "special"]
        # choices_list = [random.choice(choices) for _ in range(char_quantity)]
        choices_list = random.choices(choices, weights=weights, k=char_quantity)
        passwrd_char_list = []
        for _ in range(passwrd_quantity):
                for choice in choices_list:
                    if choice == "upper":
                        passwrd_char_list.append(random.choice(self.valid_chars_upper))
                    elif choice == "lower":
                        passwrd_char_list.append(random.choice(self.valid_chars_lower))
                    elif choice == "number":
                        passwrd_char_list.append(str(random.choice([i for i in range(10)])))
                    elif choice == "special":
                        passwrd_char_list.append(random.choice(self.special_chars))
                
                passwrd_char_list.append(" ")
        
        if " " in passwrd_char_list:
            passwrd_list = "".join(passwrd_char_list).split(" ")
            passwrd_list.pop()
            return passwrd_list
        
        return "".join(passwrd_char_list).strip()
        




def main():
    try:
        greetings()
        command_list = ["help/-h", "exit", "check", "create", "correct", "commands", "clear"]

        while True:
            user_input = input("Give me a command: ").strip().lower()

            if user_input == "exit":
                print("Thank you for using the program.")
                break
            elif user_input == "commands":
                print(command_list)
                print()
            elif user_input in ["help", "-h"]:
                greetings()
            elif user_input == "check":
                while True:
                    passwrd = Password(input("Give me your password to check: "))
                    try:
                        passwrd.password_correctness()
                    except Exception as e:
                        print(e)
                        continue

                    print(passwrd.password_hardness())

                    if choice_question():
                        continue
                    else:
                        break

            elif user_input == "create":
                while True:
                    passwrd = Password()
                    try:
                        char_quantity = int(input("Tell me how much charater should your password be: "))
                        password_quantity = int(input("Tell me how much password do you want to be generated for you: "))
                        weights = get_weights()
                    except ValueError:
                        print("That is not a valid number/integer, try again!")
                        continue
                    
                    while True:
                        try:
                            password_container = passwrd.create_password(char_quantity, password_quantity, weights)
                            passwrds_with_values = {}

                            for item in password_container:
                                passwrd = Password(item)
                                passwrds_with_values.update({item: passwrd.password_hardness()})
                                
                            for i, item in enumerate(passwrds_with_values):
                                print(f"{i + 1}. {item}: {passwrds_with_values[item]}")
                        
                            break
                        except:
                            continue

                    if choice_question():
                        continue
                    else:
                        break
            elif user_input == "correct":
                passwrd = Password(input("Give me your password to check: "))
                try:
                    print(passwrd.password_correctness())
                except Exception as e:
                    print(e)
            elif user_input == "clear":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    except EOFError:
        sys.exit("Thank you for using the program.")





                
 ###### FUNTIONS ######               

def get_weights() -> list:
    print(
        """
        There are weights options when you create a password. 
        Weights looks like this [upper, lower, number, special] substitute these values with numbers
        based on which would you prefere more to be present in your password. If you want every value type
        to be represented equaly just give these values [1, 1, 1, 1].

        Please choose based on the followings:
        - should your password contain more letter (upper or lowercase)
        - should it contain more special characters (!, @, #, $, %, ^, &, *, _, ~)
        - should it contain more decimals/numbers 0-9
        """)
                
    upper_weight = int(input("Give me a weight number for uppercase letters: "))
    lower_weight = int(input("Give me a weight number for lowercase letters: "))
    number_weight = int(input("Give me a weight for numbers: "))
    special_weight = int(input("Give me a weight number for special characters: "))

    return [upper_weight, lower_weight, number_weight, special_weight] 

def choice_question():
    while True:
        print()
        u_input = input("Would you like do this again or get back to give another command [yes/-y | no/-n]: ").strip().lower()
        if u_input in ["yes", "-y"]:
            return True
        elif u_input in ["no", "-n"]:
            return False
        else:
            print("Don't understand try again.")

def greetings():
    return print(
        """
        This is a password checker and creator!

        You will be able to check whether your password is hard or difficult enough to be considered good.
        Or in case if you don't have any password but you would like to, you can create one for yourself
        using my built in password creator.
        - You will be able to choose in this case between many options. I suggest you to creat more passwords
            then just one and compare them which you like more or which is more hard/difficult/strong.

        To navigate in the program you can use different commands. Which are the followings:
        - help/-h - this will show all the commands in case you forget them
        - exit - this will exit the program
        - check - this will check your password how strong it is
        - create - this will create a or multiple password for you depending on your choices
        - correct - this will only check whether your password is correct. Note that this will be check anyway when using `check`.
        - commands - this will show you the usable commands
        - clear - to clear the terminal
        """
        )



    
     
if __name__ == "__main__":
    main()