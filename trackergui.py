import tkinter
import os
from questiontracker3 import Main

'''
ADD ABILITY TO RESET SCORE x
IMPROVE VISUALS
REDO GEOMETRY
ADD PLAY AGAIN FEATURE?
ADD NEXT QUESION FEATURE?
TIDY UP CODE

'''
class guiMain:
    def __init__(this, height = 300, width = 300):
        this.height = height
        this.width = width
        this.question = ""
        this.gui = tkinter.Tk() # creates gui
        this.trackerMain = Main(vars[0], vars[1], vars[2])
        this.dir = os.path.dirname(os.path.realpath(__file__)) # Gets python file directory
        this.dispA = tkinter.Label(this.gui) # Creates Label that displays if user was correct or not
        this.dispQ = tkinter.Label(this.gui) # Creates Label that asks the question
        this.scoreL = tkinter.Label(this.gui)

    def runGui(this):
        this.gui # Runs gui
        this.gui.title("Question Tracker 3") # Gives gui title
        this.gui.geometry(f"{this.height}x{this.width}") # Gives dimensions
        this.trackerMain.getScore()
        this.displayScore() # Displays that score
        this.gui.mainloop()


    def displayScore(this):
        scoreTitle = tkinter.Label(this.gui, text="Score:") # Displays score title
        scoreTitle.place(x = 25, y = 20)
        this.scoreL.config(text=this.trackerMain.score)
        this.scoreL.place(x = 25, y = 40)
        this.trackerMain.genQuestions() # Generates Question
        this.displayQuestion() # After generation, displays the question

    def displayQuestion(this):
        with open(f"{this.dir}/questions.txt","r") as this.question:
            for line in this.question:
                this.trackerMain.question = line.split("=")
                this.dispQ.config(text= f"What is {this.trackerMain.question[0]}?")
                this.dispQ.place(x=50,y=50)
        this.getAns()
    
    def getAns(this):
        this.ansBox = tkinter.Entry(this.gui)
        this.ansBox.place(x=50,y=80)
        this.ansBox.config(state=tkinter.NORMAL)
        submit = tkinter.Button(this.gui, text="Submit", command=this.Return)
        submit.place(x=50, y=110)
        this.resetButton()

    def Return(this):
        this.trackerMain.ans = this.ansBox.get()
        this.trackerMain.checkAns()
        this.dispA.place(x=200,y=200)
        
        if this.trackerMain.valid == False:
            
            this.trackerMain.checkAns()
            this.dispA.config(text= "Please enter a valid number")
            this.ansBox.delete(0, "end")
            this.getAns()

        else:            
            this.ansBox.delete(0, "end")
            this.trackerMain.correctAns()

            if this.trackerMain.correct == True:
                this.dispA.config(text="That is correct!")
            else:
                this.dispA.config(text = f"That is incorrect! The answer was {this.trackerMain.question[1]}")

            this.end()

    def resetButton(this):
        reset = tkinter.Button(this.gui, text="Reset", command=this.reset)
        reset.place(x=100, y= 100)
    
    def reset(this):
        this.dispA.config(text="")
        this.trackerMain.resetScore()
        this.displayScore()
    
    
    def end(this):
        
        this.trackerMain.saveScore()
        this.runGui()

#Main Program
if __name__ == "__main__":
    vars = (1, 50, 5)
    main = guiMain(500, 500)
    main.runGui()


