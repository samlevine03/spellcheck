from dictionary import Dictionary

def main():
    dictionary = Dictionary()

    while True:
        word = input("Enter a word: ").lower()
        if word == "":
            break
        if dictionary.is_word(word):
            print(f"{word} is a word")
        else:
            suggestions = dictionary.suggest_words(word)
            print("That's not a word. Did you mean:")
            for suggestion in suggestions:
                print(suggestion[0])
            pass

if __name__ == "__main__":
    main()
