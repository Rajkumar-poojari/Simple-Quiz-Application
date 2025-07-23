import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("500x400")
        self.q_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.questions = []
        self.selected_option = tk.StringVar()

        self.load_questions()

    def load_questions(self):
        try:
            with open("question.json", "r") as file:  # Updated filename
                self.data = json.load(file)
                self.show_topic_selection()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load questions.\n{str(e)}")
            self.root.destroy()

    def show_topic_selection(self):
        self.clear_window()
        tk.Label(self.root, text="Select a Topic", font=("Arial", 16)).pack(pady=20)

        for topic in self.data.keys():
            tk.Button(self.root, text=topic, width=20, command=lambda t=topic: self.start_quiz(t)).pack(pady=5)

    def start_quiz(self, topic):
        self.topic = topic
        self.questions = self.data[topic]
        self.q_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.show_question()

    def show_question(self):
        self.clear_window()
        question_data = self.questions[self.q_index]

        tk.Label(self.root, text=f"Question {self.q_index + 1}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text=question_data["question"], wraplength=400, font=("Arial", 12)).pack(pady=10)

        self.selected_option.set(None)
        for opt in question_data["options"]:
            tk.Radiobutton(self.root, text=opt, variable=self.selected_option, value=opt[0], font=("Arial", 11)).pack(anchor='w')

        if self.q_index < len(self.questions) - 1:
            tk.Button(self.root, text="Next", command=self.next_question).pack(pady=20)
        else:
            tk.Button(self.root, text="Submit Quiz", command=self.submit_quiz).pack(pady=20)

    def next_question(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option before proceeding.")
            return

        correct = self.questions[self.q_index]["answer"]
        if selected == correct:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1

        self.q_index += 1
        self.show_question()

    def submit_quiz(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option before submitting.")
            return

        correct = self.questions[self.q_index]["answer"]
        if selected == correct:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1

        self.show_result()

    def show_result(self):
        self.clear_window()
        total_questions = len(self.questions)
        percentage = round((self.correct_answers / total_questions) * 100, 2)

        tk.Label(self.root, text="Quiz Completed!", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text=f"Correct Answers: {self.correct_answers}", font=("Arial", 12)).pack()
        tk.Label(self.root, text=f"Incorrect Answers: {self.incorrect_answers}", font=("Arial", 12)).pack()
        tk.Label(self.root, text=f"Score: {percentage}%", font=("Arial", 12)).pack(pady=5)

        if percentage == 100:
            message = "🎉 Perfect Score!"
        elif percentage >= 50:
            message = "👍 Good job!"
        else:
            message = "😟 Keep practicing!"

        tk.Label(self.root, text=message, font=("Arial", 12)).pack(pady=10)

        tk.Button(self.root, text="Take Another Quiz", command=self.show_topic_selection).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

        self.save_score_to_file()

    def save_score_to_file(self):
        try:
            with open("scores.txt", "a") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{timestamp} - Topic: {self.topic}, Correct: {self.correct_answers}, "
                        f"Incorrect: {self.incorrect_answers}, Score: {self.correct_answers}/{len(self.questions)}\n")
        except Exception as e:
            messagebox.showwarning("Warning", f"Could not save score.\n{str(e)}")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
