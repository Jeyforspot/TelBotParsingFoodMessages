import json

arr = []

with open(r"C:\Users\KL!ZMa\Desktop\projects\TelBotParsingFoodMessages\food_words.txt", encoding="utf-8") as list_of_words:
    for row in list_of_words:
        word = row.lower().split("\n")[0]
        if word != "":
            arr.append(word)


with open(r"C:\Users\KL!ZMa\Desktop\projects\TelBotParsingFoodMessages\food_words.json", "w", encoding="utf-8") as ready_made_words:
    json.dump(arr, ready_made_words)  # don't forget to set True!
