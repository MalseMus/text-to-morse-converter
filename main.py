# The index of the letters and morse allign.
ALPHABET = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "0", " "
]

MORSE_LIST = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-..-", "--..", ".----", "..---", "...--", "....-", ".....",
    "-....", "--...", "---..", "----.", "-----", " "
]


# Converter:
def convert_string(string):
    morse_word = ""
    for letter in string.lower():
        position = ALPHABET.index(letter)
        morse_letter = MORSE_LIST[position]
        morse_word += f"{morse_letter} "
    return morse_word


# Actual Process
print("Welcome to the String-To-Morse Converter! \n"
      "Type any string, and We'll turn it to morse for you!")

chosen_string = input("Type string here: ")

final_morse = convert_string(chosen_string)
print(f"Your morse code is: {final_morse}")




