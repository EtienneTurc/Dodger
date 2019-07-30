import csv


def readCsv():
    with open('Leaderboard.csv', 'r') as readFile:
        spamreader = csv.reader(readFile, delimiter=',')
        data = []
        for row in spamreader:
            data.append(row)
    readFile.close()
    return(data)

def writeInCsv(score):
    with open('Leaderboard.csv', 'a', newline = '') as writeFile:
        writer = csv.writer(writeFile)
        row = ['Simon',str(score)]
        writer.writerow(row)
    writeFile.close()
