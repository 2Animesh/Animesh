from tools import Evaluate

random_questions = [
    "How many sides does a square have?\n(a)4 \n(b)5 \n(c)3\n ",
    "\n\nWhat is the colour of an orange? \n(a)red \n(b)pink \n(c)orange\n",
    "\n\nHow many hours in a day? \n(a)12 \n(b)24 \n(c)18\n"
]

random_answers = [
    Evaluate(questions[0], "a"),
    Evaluate(questions[1], "c"),
    Evaluate(questions[2], "b")
]

def Programme(stored_answer):
    score= 0
    for i in stored_answer:
        response = input(i.Q)
        if response == i.answer:
            score += 1

    return str(score)

print("Your score is " + Programme(random_answers))

