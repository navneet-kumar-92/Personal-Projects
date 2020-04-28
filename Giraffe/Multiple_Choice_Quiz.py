from question import Question

question_prompts = [
    "What color are apples?\n (a) Red (b) Purple (c) Orange\n\n",
    "What color are Bananas?\n (a) Red (b) Yellow (c) Orange\n\n",
    "What color are Grapes?\n (a) Red (b) Green (c) Orange\n\n",
]

# print(question_prompts[2])


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for ques in questions:
        answer = input(ques.prompt)
        if answer == ques.answer :
            score += 1
    print("Hey! You got " + str(score) + " questions correct out of " + str(len(questions)) + " !")

run_test(questions)
