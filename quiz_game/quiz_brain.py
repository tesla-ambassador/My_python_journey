class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f'Q{self.question_number}. {current_question.text} (True/False): ').capitalize()
        self.check_answer(user_input, current_question.answer)
        
    def check_answer(self, user_answer, answer):
        if user_answer == answer:
            self.score += 1
        print(f'Your answer is: {user_answer}\nThe actual answer is: {answer}')