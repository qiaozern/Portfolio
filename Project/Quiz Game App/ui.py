from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text=f"Question Text", 
            fill="black", 
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)
        
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        true_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.check_button.grid(column=0, row=2)
        
        false_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.cross_button.grid(column=1, row=2)

        self.get_next_question()
        
        self.window.mainloop()
        
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.canvas.config(bg="white")
            self.check_button.config(state=DISABLED)
            self.cross_button.config(state=DISABLED)

            
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)