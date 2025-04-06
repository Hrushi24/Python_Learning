from question_model import Question

class QuizBrain:

    def __init__(self , quetionListName):
        self.quetionNumber = 0
        self.QuetionList = quetionListName
        self.score = 0

    def still_have_questions(self):
        if(len(self.QuetionList) != self.quetionNumber):
            return True
        else:
            return False
        
    
    def nextQuestion(self):
        question = self.QuetionList[self.quetionNumber]
        choice = input(f"Q.{self.quetionNumber + 1 }. {question.text}. (True / False)? :").lower()
        self.check_correct_answer(choice , question.answer)
        self.quetionNumber += 1


    def check_correct_answer(self,userInput , correctAnswer):
        
        if(userInput.lower() == correctAnswer.lower()):
            print("Correct , You got this !!!")
            self.score += 1
        else:
            print("Oops!! That's wrong.")
        
        print(f"Correct answer is : {correctAnswer}")
        print(f"Your current score is : {self.score} / {self.quetionNumber + 1}.")
        print("\n")
