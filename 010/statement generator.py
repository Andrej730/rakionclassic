words  = ["Eagle Ring", "Illusion", "Sweety(9+)", "Skull Ring(10)", "Wizard Special(5+)", "Promise Ring(6+)", "Cas Ring(5)", "Protection(3+)", "Celline Green(6+)", "Celline Blue(6+)", "Celline Red(6+)", "Pain of Cell(4)"]
process = lambda word: '(m_item[i].name == "{}")'.format(word);
operationBetween = " ||\n"

processedWords = [process(word) for word in words]
print(len(words))
print(operationBetween.join(processedWords))
