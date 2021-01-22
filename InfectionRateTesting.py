##Introduction
name = input("Name :")
age = int(input("Age :"))
print(f'Welcome {name}({age})')
# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0


    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1


    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('InfectionRate: ', self.score,"/ 5" )
        if 3 > self.score >= 1:
            print("For your own health and that of other people, you should stay at home for 14 days.")
        elif self.score >= 3:
            print("You should go to the nearest health facility and be examined.")
        else:
            print("You are healthy, take care of social distancing and wear a mask..")
        print(f"Wish you healthy days {name}")
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1


        if questionNumber > totalQuestion:
            print('Quiz finished..')

        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100, '*'))




q1 = Question(f'Has {name}({age}) ever been abroad last 2 months?',["Y","N"],"Y")
q2 = Question(f"Does {name}({age}) cough complaint or throat ache?",["Y","N"],"Y")
q3 = Question("Is your body temperature above 38 degrees?",["Y","N"],"Y")
q4 = Question("Do you feel malaise?",["Y","N"],"Y")
q5 = Question("Do you have back pain?",["Y","N"],"Y")



questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)

quiz.loadQuestion()

