from deep_translator import GoogleTranslator

print("===== Language Translator =====")

text = input("Enter Text: ")

print("\nSelect Language")
print("1. Marathi")
print("2. Hindi")
print("3. French")

choice = input("Enter Choice: ")

languages = {
    "1": "mr",
    "2": "hi",
    "3": "fr"
}

if choice in languages:
    translated = GoogleTranslator(
        source='auto',
        target=languages[choice]
    ).translate(text)

    print("\nTranslated Text:")
    print(translated)

else:
    print("Invalid Choice")
