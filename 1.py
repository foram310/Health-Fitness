from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
from BMI import open_dashboard

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="user_database"
)
cursor = db.cursor()

window = Tk()
window.state('zoomed') 
window.title('Health & Fitness')

# Window Icon
icon = PhotoImage(file='images/pic-icon.png')
window.iconphoto(True, icon)

# ======= Background Image Handling ======== 
canvas = Canvas(window, highlightthickness=0)
canvas.grid(row=0, column=0, sticky='nsew')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

bg_image = Image.open('images/bg.jpg')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, anchor='nw', image=bg_photo)

# ======= Content Container with Dynamic Resizing ======== 
content_frame = Frame(canvas, bg='#ffffff', relief='groove', bd=2)
content_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.7, relheight=0.7)

content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)  

def update_frame_size(event):
    """Ensure content stays centered and responsive.""" 
    if canvas.winfo_exists():  
        content_frame.update_idletasks()
        canvas.config(width=event.width, height=event.height)
        canvas.place(relwidth=1, relheight=1) 

window.bind('<Configure>', update_frame_size)

def show_frame(is_login=False):
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    if is_login:
        display_login()
    else:
        display_registration()
    
    load_vector_image() 

def load_vector_image():
    global label_vector_image 
    vector_image_path = 'images/vector.png' 
    try:
        vector_image = Image.open(vector_image_path)
        vector_image = vector_image.resize((550, 500), Image.Resampling.LANCZOS)
        vector_image = ImageTk.PhotoImage(vector_image)

        if 'label_vector_image' in globals():
            label_vector_image.destroy()

        label_vector_image = Label(content_frame, image=vector_image, bg='#ffffff') 
        label_vector_image.image = vector_image
        label_vector_image.place(relx=0.73, rely=0.5, anchor='center')
    except Exception as e:
        print(f"Error loading image: {e}")

load_vector_image()

def login_user():
    email = email_entry.get()
    password = password_entry.get()
    
    try:
        cursor.execute("SELECT id FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        
        if user:
            user_id = user[0]
            print("Login successful, preparing to display BMI dashboard...")
            label_vector_image.destroy()

            for widget in content_frame.winfo_children():
                widget.destroy()
                
            open_dashboard(content_frame, user_id, show_frame)
        else:
            messagebox.showerror("Error", "Invalid email or password.")
    except Exception as e:
        print(f"Login error: {e}")
        messagebox.showerror("Error", "An error occurred during login.")

# Registration functionality
def register_user():
    username = name_entry.get()
    email = email_reg_entry.get()
    password = password_reg_entry.get()
    confirm_password = confirm_password_entry.get()

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    try:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Email already registered!")
            return
        
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
        db.commit()
        messagebox.showinfo("Success", "Registration successful!")
        show_frame(is_login=True)
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        messagebox.showerror("Error", f"Database error: {err}")

# Password visibility toggle
def password_command(entry):
    if entry.cget('show') == '•':
        entry.config(show='')
    else:
        entry.config(show='•')

# Forgot Password functionality
def forgot_password():
    email = email_entry.get()
    if not email:
        messagebox.showinfo("Forgot Password", "Please enter your email to reset the password.")
        return
    try:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            messagebox.showinfo("Password Recovery", f"Instructions to reset your password have been sent to {email}.")
        else:
            messagebox.showerror("Error", "Email not registered.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        messagebox.showerror("Error", "An error occurred during password recovery.")

# Display login screen with "Forgot Password" option
def display_login():
    for widget in content_frame.winfo_children():
        widget.destroy()

    login_frame = Frame(content_frame, bg='#ffffff')
    login_frame.grid(row=0, column=0, padx=(100, 0), pady=75, sticky='nw')

    Label(login_frame, text='Login', font=("yu gothic ui", 30, 'bold'), fg="#1b87d2", bg='#ffffff').grid(row=0, column=0, padx=90, pady=(20, 10), sticky='w')
    Label(login_frame, text='Email', font=("yu gothic ui", 11, 'bold'), fg="#89898b", bg='#ffffff').grid(row=1, column=0, pady=(10, 5), sticky='w')

    global email_entry
    email_entry = Entry(login_frame, font=("yu gothic ui semibold", 12), highlightthickness=2)
    email_entry.grid(row=2, column=0, pady=5, sticky='ew')

    Label(login_frame, text='Password', font=("yu gothic ui", 11, 'bold'), fg="#89898b", bg='#ffffff').grid(
        row=3, column=0, pady=(10, 5), sticky='w')

    global password_entry
    password_entry = Entry(login_frame, show='•', font=("yu gothic ui bold", 12), highlightthickness=2)
    password_entry.grid(row=4, column=0, pady=5, sticky='ew')

    # Row for "Show Password" and "Forgot Password" buttons
    options_frame = Frame(login_frame, bg='#ffffff')
    options_frame.grid(row=5, column=0, sticky='w')

    Checkbutton(options_frame, text='Show Password', bg='#ffffff', 
                command=lambda: password_command(password_entry)).grid(row=0, column=0, pady=5, padx=(0, 70), sticky='w')

    Button(options_frame, text="Forgot Password", command=forgot_password, fg="#1b87d2", bg='#ffffff', font=("yu gothic ui", 10), borderwidth=0).grid(
        row=0, column=1, pady=5)

    Button(login_frame, text='Login', command=login_user, bg='#1b87d2', fg='#f8f8f8',
           font=("yu gothic ui bold", 15), width=25).grid(row=7, column=0, pady=(10, 5), sticky='ew')

    Button(login_frame, text='Sign Up', command=lambda: show_frame(is_login=False),
           font=("yu gothic ui bold", 12), fg="#89898b", bg='#ffffff', borderwidth=0).grid(row=8, column=0, pady=10, sticky='ew')

def display_registration():
    for widget in content_frame.winfo_children():
        widget.destroy()

    reg_frame = Frame(content_frame, bg='#ffffff')
    reg_frame.grid(row=0, column=0, padx=(100, 0), pady=10, sticky='nw')

    Label(reg_frame, text='Register', font=("yu gothic ui", 30, 'bold'), bg='#ffffff', fg="#1b87d2").grid(
        row=0, column=0, padx=90, pady=(20, 10), sticky='w')

    Label(reg_frame, text='Full Name', font=("yu gothic ui", 11, 'bold'), bg='#ffffff', fg="#89898b").grid(
        row=1, column=0, pady=(10, 5), sticky='w')

    global name_entry
    name_entry = Entry(reg_frame, font=("yu gothic ui semibold", 12), highlightthickness=2)
    name_entry.grid(row=2, column=0, pady=5, sticky='ew')

    Label(reg_frame, text='Email', font=("yu gothic ui", 11, 'bold'), bg='#ffffff', fg="#89898b").grid(
        row=3, column=0, pady=(10, 5), sticky='w')

    global email_reg_entry
    email_reg_entry = Entry(reg_frame, font=("yu gothic ui semibold", 12), highlightthickness=2)
    email_reg_entry.grid(row=4, column=0, pady=5, sticky='ew')

    Label(reg_frame, text='Password', font=("yu gothic ui", 11, 'bold'), bg='#ffffff', fg="#89898b").grid(
        row=5, column=0, pady=(10, 5), sticky='w')

    global password_reg_entry
    password_reg_entry = Entry(reg_frame, show='•', font=("yu gothic ui semibold", 12), highlightthickness=2)
    password_reg_entry.grid(row=6, column=0, pady=5, sticky='ew')

    Label(reg_frame, text='Confirm Password', font=("yu gothic ui", 11, 'bold'), bg='#ffffff', fg="#89898b").grid(
        row=7, column=0, pady=(10, 5), sticky='w')

    global confirm_password_entry
    confirm_password_entry = Entry(reg_frame, show='•', font=("yu gothic ui semibold", 12), highlightthickness=2)
    confirm_password_entry.grid(row=8, column=0, pady=5, sticky='ew', padx=0)  # Removed padding to the right

    Button(reg_frame, text='Register', command=register_user, bg='#1b87d2', fg='#f8f8f8',
           font=("yu gothic ui bold", 15), width=25).grid(row=9, column=0, pady=(20, 5), sticky='ew')

    Button(reg_frame, text='Sign in', command=lambda: show_frame(is_login=True),
           font=("yu gothic ui bold", 12), fg="#89898b", bg='#ffffff', borderwidth=0).grid(row=10, column=0, pady=10, sticky='ew')

# Initialize with Login View
show_frame(is_login=True)

# Run the main loop
window.mainloop()

# Close the database connection on exit
db.close() 
