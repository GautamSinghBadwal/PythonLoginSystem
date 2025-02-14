import tkinter as tk
from tkinter import messagebox

# Function to save user data
def save_user_data(username, password):
    with open("user_data.txt", "a") as file:
        file.write(f"{username},{password}\n")

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password!")
        return

    save_user_data(username, password)
    messagebox.showinfo("Success", "Login Successful!")
    root.destroy()

# Create the GUI window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Add labels and entry fields
tk.Label(root, text="Login Page", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)
tk.Label(root, text="Username:", bg="#f0f0f0").pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:", bg="#f0f0f0").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Add login button
login_button = tk.Button(root, text="Login", command=login, bg="#007BFF", fg="white")
login_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
