def start_game():
    points = 0
    question = 1
    correctQuestions = []
    wrongQuestions = []

    for key in questions:
        print("")
        print(key)
        for i in options[question - 1]:
            print(i)
        points += check_ans(input("A,B or C?: ").upper(),questions[key])
        question += 1
    stats(points)
def check_ans(answear,correct_answear):
    if (answear == correct_answear):
        print("Correct")
        answeres.append(answear)
        return 1
    else:
        print("Wrong, the correct answear was "+ correct_answear)
        answeres.append(answear)
        return 0

def stats(end_points):
    print("\nYou got " + str(end_points) +" out of " + str(len(questions)) + " Points.")
    #print("Your answeres" + str(answeres))
    #print("\n Correct answeres" + str(correct_answear))

answeres = []
correct_answear = []

questions = {
    "What is 9+10?": "C",
    "Python is a...?": "A"
}

options = [
     ["A: 19", "B: 19", "C: 21"],
     ["A: Programming Language", "B: Snake", "C: Car"]
    ]


start_game()