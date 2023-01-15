class QuizBrain:
    def __init__(self, question_ban):
        self.question_no = 0
        self.score = 0
        # self.anss
        self.question_list = question_ban

    def more_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        # self.question_no += 1
        ans = input(
            f'Q.{self.question_no + 1}: {self.question_list[self.question_no].question} True/False ')
        self.correct_ans(ans, self.question_list[self.question_no].ans)
        self.question_no += 1

    def correct_ans(self, user_ans, correct_ans):
        if user_ans == correct_ans:
            self.score += 1

    def final_score(self):
        print(
            f"You have completed the trivia and you got {self.score} questions correctly!")
