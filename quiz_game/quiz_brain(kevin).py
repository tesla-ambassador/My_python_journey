class QuizBrain:
    def __init__(self):
        self.score = 0
    
    def ask(self, question):
        print(question)
        self.user_input = input('').capitalize()
    
    def check_answer(self, answer):
        if self.user_input == answer:
            self.score += 1
            return True
        else:
            print('Sorry that is a wrong answer')
            print(f'Your score is {self.score}')
            return False
    
    def check_end(self, no_of_questions):
        if self.score == no_of_questions:
            print('Congratulations, you have passed the entire quiz')
            print(f'Your score is {self.score}')
            return False