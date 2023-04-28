class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        answer = input(f'Q{self.question_number + 1}. {self.question_list[self.question_number].text}? (True/False): ')
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right")
            self.score += 1
        else:
            print("That was wrong")
        print(f"The answer was: {correct_answer}")
        print("\n")
