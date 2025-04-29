#Message
print("This quiz will test how much you know about countries around the world and the United Nations Sustainable Development Goals (SDGs)")
print("There are 15 multiple-choice questions. For each question, choose the best answer: a, b, c, or d.")
print("Good luck and have fun!")

#score
count = 0
score = 0

#list for questions
questions = [
    "Which country is the largest producer of coffee?",
    "Which SDG focuses on 'Clean Water and Sanitation'?",
    "Which country has the most official languages?",
    "Which SDG focuses on 'Quality Education'?",
    "Which country was the first to grant women the right to vote?",
    "Which country is known for having no rivers?",
    "Which SDG aims to end poverty in all its forms?",
    "Which country has the world’s longest coastline?",
    "Which SDG focuses on Gender Equality?",
    "Which country consumes the most chocolate per capita?",
    "Which SDG is about Climate Action?",
    "Which country has the most pyramids?",
    "Which SDG promotes Affordable and Clean Energy?",
    "Which country is powered almost entirely by renewable energy?",
    "Which SDG focuses on Sustainable Cities and Communities?"
]

#Options for each question
options = [
    "a) Vietnam", "b) Colombia", "c) Ethiopia", "d) Brazil",
    "a) SDG 3", "b) SDG 6", "c) SDG 8", "d) SDG 10",
    "a) India", "b) Canada", "c) South Africa", "d) Switzerland",
    "a) SDG 2", "b) SDG 5", "c) SDG 4", "d) SDG 11",
    "a) Australia", "b) UK", "c) New Zealand", "d) Finland",
    "a) Vatican City", "b) Monaco", "c) San Marino", "d) Bahrain",
    "a) SDG 10", "b) SDG 1", "c) SDG 3", "d) SDG 6",
    "a) Russia", "b) Australia", "c) USA", "d) Canada",
    "a) SDG 2", "b) SDG 7", "c) SDG 5", "d) SDG 9",
    "a) Germany", "b) Belgium", "c) Switzerland", "d) France",
    "a) SDG 12", "b) SDG 13", "c) SDG 6", "d) SDG 3",
    "a) Egypt", "b) Mexico", "c) Sudan", "d) Peru",
    "a) SDG 7", "b) SDG 10", "c) SDG 3", "d) SDG 13",
    "a) Norway", "b) Iceland", "c) Costa Rica", "d) Bhutan",
    "a) SDG 11", "b) SDG 1", "c) SDG 16", "d) SDG 6"
]
#Correct answers
correct_answers = [
    "d", "b", "c", "c", "c", "a", "b", "d", "c", "c", "b", "c", "a", "c", "a"
]
#Explinations
explanations = [
    "Brazil has been the world’s largest coffee producer for over 150 years.",
    "SDG 6 is about ensuring clean water and sanitation for all.",
    "South Africa has 11 official languages, more than any other country.",
    "SDG 4 promotes inclusive and quality education.",
    "New Zealand gave women the right to vote in 1893.",
    "Vatican City has no rivers.",
    "SDG 1 is about ending poverty everywhere.",
    "Canada has the longest coastline in the world.",
    "SDG 5 is about gender equality.",
    "Switzerland eats the most chocolate per person.",
    "SDG 13 is about taking action for the climate.",
    "Sudan has more pyramids than Egypt.",
    "SDG 7 is about clean and affordable energy.",
    "Costa Rica uses mostly renewable energy.",
    "SDG 11 is about making cities safe and sustainable."
]

for i in range(15):
    print("Question " + str(i + 1) + ": " + questions[i])
    print("a) " + options[i][0])
    print("b) " + options[i][1])
    print("c) " + options[i][2])
    print("d) " + options[i][3])

    answer = input("Your answer (a/b/c/d): ")

    if answer == correct_answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect!")

    print("The correct answer was: " + correct_answers[i])
    print("Explanation: " + explanations[i])
    print()

print("Quiz finished!")
print("You scored " + str(score) + " out of 15.")

# Calculate rank
if score <= 5:
    print("Rank: Starter")
elif score <= 10:
    print("Rank: Learner")
else:
    print("Rank: Expert")

# Ask to play again
play_again = input("Would you like to play again? (yes or no): ")
if play_again == "yes":
    print("Restart the program to play again!")
else:
    print("Thank you for playing!")
