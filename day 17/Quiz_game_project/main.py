from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

QuetionBank = []

qData = question_data
quetion = Question()


for item in qData:
    text = item["text"]
    ans = item["answer"]
    tempObj = Question(text , ans)
    QuetionBank.append(tempObj)



QuizBrainApp = QuizBrain(QuetionBank)

while(QuizBrainApp.still_have_questions()):
    QuizBrainApp.nextQuestion()


print("You have completed your test.")
print(f"Your final score is {QuizBrainApp.score}/{QuizBrainApp.quetionNumber}.")
