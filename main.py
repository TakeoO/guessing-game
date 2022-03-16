import json
import random

questions = json.load(open("questions.json"))

print("Dobrodošli v igri - UGANI GLAVNO MESTO :)")
username = input("Enter your username: ")
attempts = 0
for tries in range(3):
    randomDict = random.choice(questions)
    userAnswer = input("Kaj je glavno mesto %s: " % (randomDict['country']))
    rightAnswer = randomDict['city']

    if userAnswer == rightAnswer:
        print("Congratz! Your answer was correct!")
        attempts += 1
    else:
        print("Wrong answer, the right answer was %s" % rightAnswer)

resultFile = open("result.txt", "a")
resultFile.write("\n%s:%s" % (username, str(attempts)))
resultFile.close()

scoreList = []
with open("result.txt", "r") as file:
    scoreListLines = file.read().split("\n")
    for line in scoreListLines:
        if ":" in line:
            name, score = line.split(":")
            scoreList.append({
                "name": name,
                "score": int(score)
            })

sortedScores = sorted(scoreList, key=lambda item: (item['score']), reverse=True)[:3]
print(sortedScores)
