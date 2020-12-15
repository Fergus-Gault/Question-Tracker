from random import randint
import os


class Main:
    def __init__(self, minrange=1, maxrange=50, thresh=5):
        self.minrange = minrange
        self.maxrange = maxrange
        self.score = 0
        self.thresh = thresh
        self.ans = ""
        self.question = ""
        self.valid = True
        self.correct = False
        self.dir = os.path.dirname(os.path.realpath(__file__)) # Gets python file directory
    
    def getScore(self): #Gets score from text file and assigns it to score attribute
        try:
            with open(f"{self.dir}/progress.txt","r") as progress:
                self.score = int(progress.readline(-1))
        except:
            with open(f"{self.dir}/progress.txt","w") as progress:
                progress.write(str(self.score))
            self.getScore()

    def genQuestions(self): #Generates questions based on score
        with open(f"{self.dir}/questions.txt","w") as self.question:
            if self.score < self.thresh: #If score less than thresh then questions are addition
                num1 = randint(self.minrange, self.maxrange)
                num2 = randint(self.minrange, self.maxrange)
                ans = num1 + num2
                self.question.write(f"{num1} + {num2} = {ans}\n")

            elif self.score >= self.thresh: #If score above thresh then questions are harder
                num1 = randint(self.minrange, self.maxrange)
                num2 = randint(self.minrange, self.maxrange)
                ans = num1 * num2
                self.question.write(f"{num1} x {num2} = {ans}\n")
    


    def checkAns(self):
        if self.ans.isdigit() == False: #If ans is a whole number it continues
            self.valid = False
        else: #Otherwise it will ask the user again
            self.valid = True

    def correctAns(self):
        if str(self.ans) == self.question[1].strip():
            self.correct = True
            self.score += 1 #If answer is correct then add one to score
        else: #If incorrect, tells user the answer
            self.correct = False

    def resetScore(self):
        with open(f"{self.dir}/progress.txt","w") as progress:
            progress.write(str(0))
        self.getScore()

    def playAgain(self):
        again = input("Do you want to get another questions? (y/n): ")
        if "n" in again:
            self.saveScore()
        else:
            self.genQuestions()

    def saveScore(self): #Saves score to file and exits program
        with open(f"{self.dir}/progress.txt","w") as progress:
            progress.write(str(self.score))

