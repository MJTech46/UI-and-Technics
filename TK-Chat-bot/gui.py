import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Chat Application")
root.geometry("400x500")

# Load user images
user1_img = Image.open("res/icon/user1.png")
user1_img = user1_img.resize((50, 50), Image.LANCZOS)
user1_photo = ImageTk.PhotoImage(user1_img)

user2_img = Image.open("res/icon/user2.png")
user2_img = user2_img.resize((50, 50), Image.LANCZOS)
user2_photo = ImageTk.PhotoImage(user2_img)

# Create a frame for the chat area
chat_frame = tk.Frame(root)
chat_frame.pack(pady=10)

# Create a scrolled text widget for the chat area
chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=50, height=20, state='disabled')
chat_area.pack()

# Create a frame for the input area
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Create an entry widget for typing messages
message_entry = tk.Entry(input_frame, width=40)
message_entry.pack(side=tk.LEFT, padx=10)

# Function to send a message
def send_message():
    message = message_entry.get()
    if message:
        chat_area.config(state='normal')
        chat_area.insert(tk.END, "You: " + message + "\n")
        chat_area.config(state='disabled')
        message_entry.delete(0, tk.END)

# Create a send button
send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

# Display user images
user1_label = tk.Label(root, image=user1_photo)
user1_label.pack(side=tk.LEFT, padx=10)

user2_label = tk.Label(root, image=user2_photo)
user2_label.pack(side=tk.RIGHT, padx=10)

# Run the application
root.mainloop()
