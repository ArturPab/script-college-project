# Generuje plik z rozszerzeniem .html
def createPage():
    allResultWords = []
    dictionaryWords = []
    resultWords = []
    refillArrays(dictionaryWords, allResultWords)
    matchingNumber = getMatchingNumber(dictionaryWords, allResultWords, resultWords)
    pageFile = open("index.html", "w", encoding='utf-8')

    # Tworzenie pliku html
    pageFile.write('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <title>Statystyka</title>
    </head>
    <body>
        <h1> Statystyka </h1>
        <h3>Na 100 słów znaleziono ''' + str(matchingNumber) + ''' co stanowi ''' + str((matchingNumber/100)*100) + '''%</h3>
        <table>
            <tr>
                <th>Wszystkie słowa</th>
                <th>Słowa znalezione według skryptu</th>
            </tr>
            '''
                   )
    for i in range(100):
        pageFile.write('''
            <tr>
                <td>''' + dictionaryWords[i] + '''</td>
                ''')
        if len(resultWords) > i:
            pageFile.write('''<td>''' + resultWords[i] + '''</td>''')
        pageFile.write("</tr>")

    pageFile.write('''
        </table>
    </body>
    ''')
    pageFile.close()


# Funkcja porownuje ze soba plik slownik.txt i result.txt i zwraca liczbe pasujacych do siebie slow
def getMatchingNumber(dictionaryWords, allResultWords, resultWords):
    matchingNumber = 0
    for dictionaryWord in dictionaryWords:
        for resultWord in allResultWords:
            if dictionaryWord == resultWord:
                resultWords.append(resultWord)
                matchingNumber += 1
    return matchingNumber


# Funkcja tworzy tablice z danych z plikow slownik.txt i result.txt
def refillArrays(dictionaryWords, allResultWords):
    dictionaryFile = open("slownik.txt", "r")
    resultFile = open("result.txt", "r")
    for i in range(100):
        allResultWords.append(resultFile.readline().strip())
        dictionaryWords.append(dictionaryFile.readline().strip())
    dictionaryFile.close()
    resultFile.close()
