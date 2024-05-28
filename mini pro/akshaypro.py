import json
import tkinter as tk

import importlib

# Load the JSON file
json = importlib.import_module('json')
with open('akki.json', 'r') as f:
    data = json.load(f)
    questions = data['questions']


# Define a function to find a question by ID
def find_question_by_id(q_id):
    for question in questions:
        if question['id'] == q_id:
            return question
    return None

# Define a function to find a question by text
def find_question_by_text(text):
    for question in questions:
        if question['text'] == text:
            return question
    return None

# Define a function to handle user input
def handle_input(user_input):
    # Check if the user wants to exit
    if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
        output.config(state=tk.NORMAL)
        output.insert(tk.END, "Goodbye!\n")
        output.config(state=tk.DISABLED)
        return True
    
    # Try to find a matching question
    question = find_question_by_text(user_input)
    if not question:
        output.config(state=tk.NORMAL)
        output.insert(tk.END, "Sorry, I don't know the answer to that question.\n")
        output.config(state=tk.DISABLED)
        return False
    
    # Print the answer
    output.config(state=tk.NORMAL)
    output.insert(tk.END, question['answer'] + "\n")
    output.config(state=tk.DISABLED)
    return False

# Define a function to handle button clicks
def on_click():
    user_input = input_field.get()
    input_field.delete(0, tk.END)
    if handle_input(user_input):
        window.destroy()

# Create the GUI
window = tk.Tk()
window.title("Python Chatbot")

input_frame = tk.Frame(window)
input_label = tk.Label(input_frame, text="Enter a question:")
input_label.pack(side=tk.LEFT)
input_field = tk.Entry(input_frame)
input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
input_field.focus_set()
input_button = tk.Button(input_frame, text="Ask", command=on_click)
input_button.pack(side=tk.LEFT)
input_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)

output_frame = tk.Frame(window)
output_label = tk.Label(output_frame, text="Answer:")
output_label.pack(side=tk.LEFT)
output = tk.Text(output_frame, state=tk.DISABLED, wrap=tk.WORD)
output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
output_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10, expand=True)

# Add buttons for each question
for question in questions:
    q_button = tk.Button(window, text=question['text'], command=lambda q=question: handle_input(q['text']))
    q_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

window.mainloop()
