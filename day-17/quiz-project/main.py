# Import the necessary classes and modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

# Create the question bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Shuffle the question bank to randomize the order of questions
random.shuffle(question_bank)

# Instantiate QuizBrain with the shuffled question bank
quiz = QuizBrain(question_bank)

# Game loop to ask questions
while quiz.still_has_questions() and quiz.question_number < 10:
    quiz.next_question()

# Print the user's final score
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
