text = input("Введите строку: ")
newText = text.replace('а', 'о')
countReplacements = text.count('а')
totalCharacters = len(text)

print("Изменённая строка:", newText)
print("Количество замен:", countReplacements)
print("Количество символов в строке:", totalCharacters)