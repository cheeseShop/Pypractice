import random

def generator1(stringLength):
    alphabetString = "abcdefghijklmnopqrstuvwxyz "
    result = ""
    for i in range(stringLength):
        result = result + alphabetString[random.randrange(27)]
    return result

print (generator1(28))


def score(goal, testString):
    sameNumber = 0
    for i in range(len(goal)):
        if goal[i] == testString[i]:
            sameNumber = sameNumber + 1
    return sameNumber / len(goal)


def main():
    goalString = "methinks it is like a weasel"
    newString = generator1(28)
    bestScore = 0
    newScore = score(goalString,newString)
    while newScore < 1:
        if newScore > bestScore:
            print(newScore, newString)
            bestScore = newScore
        newString = generator1(28)
        newScore = score(goalString,newString)

main()



