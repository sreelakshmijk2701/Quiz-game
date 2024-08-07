class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_num):
        question = self.questions[question_num]['question']
        options = self.questions[question_num]['options']
        print(f"\n{question}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
    
    def get_user_input(self):
        while True:
            user_input = input("\nEnter your choice (1, 2, 3, or 4): ")
            if user_input.isdigit() and 1 <= int(user_input) <= 4:
                return int(user_input)
            else:
                print("Invalid input. Please enter a number between 1 and 4.")

    def check_answer(self, question_num, user_answer):
        correct_answer = self.questions[question_num]['answer']
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {correct_answer}")

    def conduct_quiz(self):
        for i in range(len(self.questions)):
            self.display_question(i)
            user_answer = self.get_user_input()
            self.check_answer(i, user_answer)
        print(f"\nYour final score is: {self.score}/{len(self.questions)}")


# Define quiz questions, options, and answers
questions = [
    {
        'question':"how many 'letters in alphebets'?",
        'options':["25","53","21","26"],
        'answer':4
    },
    {
        'question': "What is the capital of France?",
        'options': ["London", "Paris", "Berlin", "Rome"],
        'answer': 2
    },
    {
        'question': "What is the chemical symbol for water?",
        'options': ["H2O", "CO2", "O2", "H2SO4"],
        'answer': 1
    },
    {
        'question': "Who wrote 'To Kill a Mockingbird'?",
        'options': ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
        'answer': 1
    },
    {
        'question': "who is the aurthor of naruto?",
        'options': ["minato namikaze", "kishi moto", " orawa monkey d luffy", "obito uchiha"],
        'answer': 2
    }
    
]

# Create a Quiz object and conduct the quiz
quiz = Quiz(questions)
quiz.conduct_quiz()
