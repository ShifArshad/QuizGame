from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="shifana", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_check)
        self.right_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_check)
        self.false_button.grid(row=2, column=1)

        self.next_ques()

        self.window.mainloop()

    def next_ques(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, width=280)
        else:
            self.canvas.itemconfig(self.question_text, text="You have answered all questions")
            self.canvas.config(bg="white")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_check(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_check(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_ques)



