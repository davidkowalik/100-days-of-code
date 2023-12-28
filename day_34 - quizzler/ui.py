import tkinter as ttk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        #window setup
        self.window = ttk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        #canvas setup
        self.canvas = ttk.Canvas()
        self.canvas.config(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.queston_text = self.canvas.create_text(150, 125, text="Question...", font=('Arial', '20', 'italic'), width=280)
        
        #buttons setup
        true_button_img = ttk.PhotoImage(file='images\\true.png')
        false_button_img = ttk.PhotoImage(file='images\\false.png')

        self.true_button = ttk.Button()
        self.true_button.config(background=THEME_COLOR, image=true_button_img, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=0, row=2)

        self.false_button = ttk.Button()
        self.false_button.config(background=THEME_COLOR, image=false_button_img, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(column=1, row=2)

        #label setup
        self.score = ttk.Label()
        self.score.config(text="Score: 0", font=('Arial', '12'), bg=THEME_COLOR, foreground="white")
        self.score.grid(column=1, row=0)

        self.get_next_question() 

        self.window.mainloop() 

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.queston_text, text= q_text)
        else:
            self.canvas.itemconfig(self.queston_text, text= "All 10 questions answered. You done!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer="true"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer="false"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)