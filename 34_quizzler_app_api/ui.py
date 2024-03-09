from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))

        self.label_score = Label(text="Score: 0", fg="White", bg=THEME_COLOR,
                                 highlightthickness=0,
                                 font=("Arial", 15, "bold"))
        self.label_score.grid(row=0, column=1)

        right = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right, highlightthickness=0, command=self.check_true)
        self.right_button.grid(row=2, column=0)

        wrong = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0, command=self.check_false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_it_right):
        if is_it_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
