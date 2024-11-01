import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk

# Initialize the main application window
root = tk.Tk()
root.title("Chat Bot")
root.geometry("450x400")

# User icons
user1_image_path = "res/icon/user1.png"  
user2_image_path = "res/icon/user2.png"
send_icon_path = "res/icon/send_icon.png"

# Load and resize user images
def load_image(image_path, size=(30, 30)):
    img = Image.open(image_path)
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

user1_image = load_image(user1_image_path)
user2_image = load_image(user2_image_path)
send_icon_image = load_image(send_icon_path, size=(25, 25))

# Frames for chat display and user input
chat_frame = tk.Frame(root)
chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Scrollable chat box
chat_box = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state='disabled', height=20)
chat_box.pack(fill=tk.BOTH, expand=True)

# Entry widget for typing messages
message_entry = tk.Entry(root, width=40, font=("Arial", 12))

# Button to send the message
def send_message(user, message, user_image):
    chat_box.config(state='normal')
    chat_box.image_create(tk.END, image=user_image)  # Display user's image
    chat_box.insert(tk.END, f" {user}: {message}\n", 'message')  # Insert message text
    chat_box.config(state='disabled')
    chat_box.see(tk.END)  # Scroll to the latest message
    message_entry.delete(0, tk.END)  # Clear input field

# Bind enter key to send message
def on_enter(event):
    user_message = message_entry.get()
    if user_message:
        send_message("User1", user_message, user1_image) 

# Set up the button for sending messages
send_button = tk.Button(
    root,
    image=send_icon_image ,
    text="Send", borderwidth=0 ,
    command=lambda: on_enter(None) ,
    cursor="hand2"
)


send_button2 = tk.Button(
    root,
    image=send_icon_image ,
    text="Send", borderwidth=0 ,
    command=lambda: on_enter(None) ,
    cursor="hand2"
)


# packing of widgets
send_button2.pack(side=tk.LEFT, padx=10, pady=10)
message_entry.pack(side=tk.LEFT, padx=10, pady=10)
send_button.pack(side=tk.LEFT, padx=10, pady=10)

# Bind Enter key to message entry
root.bind('<Return>', on_enter)

# Run the application
root.mainloop()
