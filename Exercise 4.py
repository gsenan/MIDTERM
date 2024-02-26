def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

numbers = [6892149109325320763773670235239019412986, 6800923757255865070000705685527573290086, 1414884937242655719669145562427394884141, 9847255590886266818998186626880955527489]

for number in numbers:
    if palindrome(str(number)):
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")