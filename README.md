# Simple-Quiz-Application

📚 Quiz Application – Python Command-Line Application
This is a simple, interactive quiz application built using Python 3. It allows users to select from multiple topics and test their knowledge through multiple-choice questions loaded from a JSON file. The app runs entirely in the terminal/command-line and is ideal for beginner-level projects or personal learning.

✨ Features
✅ Multiple Topics: Choose from subjects like Math, Science, History, General Knowledge, and Computer.

📂 JSON-based Data: All questions and answers are stored externally in a question.json file.

📝 Multiple-Choice Format: Each question has 4 options (A-D), and the user selects the correct one.

🧠 Scoring System: Scores are calculated based on correct answers.

🔁 Navigation: Users can return to the main menu after each quiz to attempt other topics.

📊 Result Summary: After submitting the quiz, a total score and percentage are shown.

🚫 Input Validation: Handles invalid entries to avoid crashes.

📂 Project Structure
bash
quiz-app/
├── quiz_app.py          # Main Python script to run the application
├── question.json        # JSON file containing all quiz questions
├── README.md            # Project documentation
└── requirements.txt     # (Empty, since no external packages are used)
🧠 Topics Included
Each topic has 5 questions:

🧮 Math

🔬 Science

🏛️ History

🌍 General Knowledge

💻 Computer

You can easily expand the quiz by editing question.json.

📥 How to Run
Clone the repository:

bash
git clone https://github.com/your-username/quiz-app.git
cd quiz-app
Run the app (make sure Python 3 is installed):

bash
python quiz_app.py
🛠 Requirements
Python 3.x

No external libraries needed (uses json and sys from standard library)

