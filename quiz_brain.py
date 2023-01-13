class QuizBrain:
    def __init__(self, question_bank):
        self.question_no = 0
        self.question_list = question_bank

    def next_question(self):

        next_q = input(
            f'Q.{self.question_no}: {self.question_list[self.question_no].question} True/False ')
