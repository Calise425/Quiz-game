from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 16, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}",
                                 bg=THEME_COLOR,
                                 fg="white",
                                 font=("Helvetica", 12, "bold"))

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=FONT,
            fill=THEME_COLOR)
        self.canvas.config(bg="white")

        check_img = PhotoImage(file="images/true.png")
        x_img = PhotoImage(file="images/false.png")

        self.check_button = Button(image=check_img,
                                   cursor="hand2",
                                   border=0,
                                   highlightthickness=0,
                                   command=self.true_pressed)
        self.x_button = Button(image=x_img,
                               cursor="hand2",
                               border=0,
                               highlightthickness=0,
                               command=self.false_pressed)

        self.score_label.grid(column=1, row=0, sticky="E")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.check_button.grid(column=0, row=2)
        self.x_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.x_button.config(state="disabled")
            self.check_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
