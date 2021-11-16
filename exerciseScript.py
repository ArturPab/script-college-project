# Funkcja sprawdzajaca czy liczba liter slowa word jest rowna liczbie dlugosci zadanej przez skrypt
def wordHaveCharsEnough(word, length):
    if len(word) == length:
        return True
    return False


# Funkcja sprawdza, czy istnieje podslowo z ostanich liter slowa czytane od tylu.
# Jezeli tak, to sprawdza czy istnieje takie podslowo czytane od przodu - jezeli nie, to zwraca wartosc True
def isSubstringCheckedProperly(substring, words):
    if words.get(substring[::-1]):
        if words.get(substring):
            return False
        return True
    return False


# Wlacza sie skrypt, gdzie pierwsza zminna to liczba liter słów, ktore skrypt ma wyszukac, druga zmienna to liczba ostatnich liter tych slow
def runScript(wordLength, substringLength):
    # Sprawdza poprawnosc danych
    if isDataCorrect(substringLength, wordLength):
        try:
            dictionaryFile = open("slownik.txt", "r")
            resultFile = open("result.txt", "w", encoding='utf-8')
        except FileExistsError:
            print("Oops!  That was no valid number.  Try again...")
        else:
            wordsWithWordLength = []
            wordsWithSubstringLength = {}
            saveResult(dictionaryFile, resultFile, substringLength, wordLength, wordsWithSubstringLength,
                       wordsWithWordLength)
            closeFiles(dictionaryFile, resultFile)


def isDataCorrect(substringLength, wordLength):
    return wordLength > substringLength


# Funkcja zamyka pliki
def closeFiles(dictionaryFile, resultFile):
    resultFile.close()
    dictionaryFile.close()


# Funkcja zapisuje wyniki do pliku
def saveResult(dictionaryFile, resultFile, substringLength, wordLength, wordsWithSubstringLength, wordsWithWordLength):
    findWords(dictionaryFile, substringLength, wordLength, wordsWithSubstringLength, wordsWithWordLength)
    # Petla wykonuje sie dopoki istnieje linia w pliku
    for word in wordsWithWordLength:
        if isSubstringCheckedProperly(word[len(word) - substringLength:], wordsWithSubstringLength):
            # Zapisuje slowo do pliku
            resultFile.write(word + '\n')


def findWords(dictionaryFile, substringLength, wordLength, wordsWithSubstringLength, wordsWithWordLength):
    for word in dictionaryFile:
        # Ucina biale znaki
        word = word.strip()
        # Znajduje slowa z dlugoscia zadana przez druga zmienna wejsciowa
        if wordHaveCharsEnough(word, substringLength):
            wordsWithSubstringLength[word] = word
        # znajduje slowa z dlugoscia zadana przez pierwsza zmienna wejsciowa
        elif wordHaveCharsEnough(word, wordLength):
            wordsWithWordLength.append(word)
