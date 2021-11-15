def wordHaveCharsEnough(word, length):
    if len(word) == length:
        return True
    return False


def isSubstringCheckedProperly(substring, words):
    if words.get(substring[::-1]):
        if words.get(substring):
            return False
        return True
    return False


def runScript(wordLength, substringLength):
    if wordLength > substringLength:
        dictionaryFile = open("slownik.txt",  "r")
        resultFile = open("result.txt", "w", encoding='utf-8')

        wordsWithWordLength = []
        wordsWithSubstringLength = {}

        for word in dictionaryFile:
            word = word.strip()
            if wordHaveCharsEnough(word, substringLength):
                wordsWithSubstringLength[word] = word
            elif wordHaveCharsEnough(word, wordLength):
                wordsWithWordLength.append(word)
        for word in wordsWithWordLength:
            if isSubstringCheckedProperly(word[len(word) - substringLength:], wordsWithSubstringLength):
                resultFile.write(word + '\n')
        resultFile.close()
        dictionaryFile.close()
