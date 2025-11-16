from tkinter import *
from tkinter import messagebox
import mysql.connector
from diet_plan import show_diet_plan 
from PIL import Image, ImageTk 

def open_dashboard(parent_frame, user_id, show_frame):
   
    for widget in parent_frame.winfo_children():
        widget.destroy()

    form_frame = Frame(parent_frame, bg="white")
    form_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    image_frame = Frame(parent_frame, bg="white")
    image_frame.grid(row=0, column=1, padx=5, pady=20, sticky="nsew")

    parent_frame.grid_columnconfigure(0, weight=0)
    parent_frame.grid_columnconfigure(1, weight=1)

    Label(form_frame, text="BMI CALCULATOR", font=("yu gothic ui", 30, "bold"), bg="white", fg="#1b87d2").grid(row=0, column=0, columnspan=2, pady=30, padx=90)

    current_height = DoubleVar()
    current_weight = DoubleVar()
    height = StringVar()
    weight = StringVar()
    age = StringVar(value="")

    def validate_age_input(new_value):
        return new_value == "" or new_value.isdigit()

    def update_height_scale(*args):
        try:
            h = float(height.get())
            current_height.set(h)
        except ValueError:
            pass

    def update_weight_scale(*args):
        try:
            w = float(weight.get())
            current_weight.set(w)
        except ValueError:
            pass

    def update_age_entry(*args):
        age_value = age.get()
        if age_value.startswith("0") and len(age_value) > 1:
            age.set(age_value[1:])

    height.trace_add("write", update_height_scale)
    weight.trace_add("write", update_weight_scale)
    age.trace_add("write", update_age_entry)

    validate_cmd = parent_frame.register(validate_age_input)

    Label(form_frame, text="Age (years)", bg="white", font=("yu gothic ui", 12, "bold")).grid(row=1, column=0, pady=10, padx=60)
    Entry(form_frame, textvariable=age, width=8, font=("yu gothic ui semibold", 20), bg="lightgrey", fg="black", bd=0, justify="center",
          validate="key", validatecommand=(validate_cmd, '%P')).grid(row=1, column=1, pady=10, padx=35, sticky='w')

    Label(form_frame, text="Height (cm)", bg="white", font=("yu gothic ui", 12, "bold")).grid(row=2, column=0, pady=10, padx=60)
    Entry(form_frame, textvariable=height, width=8, font=("yu gothic ui semibold", 20),
          bg="lightgrey", fg="black", bd=0, justify="center").grid(row=2, column=1, pady=10, padx=35, sticky='w')

    Scale(form_frame, from_=80, to=220, orient="horizontal", length=330, variable=current_height, bg="lightgrey",
          command=lambda value: height.set (f"{float(value):.2f}")).grid(row=3, column=0, columnspan=2, pady=10)

    Label(form_frame, text="Weight (kg)", bg="white", font=("yu gothic ui", 12, "bold")).grid(row=4, column=0, pady=10, padx=60)
    Entry(form_frame, textvariable=weight, width=8, font=("yu gothic ui semibold", 20),
          bg="lightgrey", fg="black", bd=0, justify="center").grid(row=4, column=1, pady=10, padx=35, sticky='w')

    Scale(form_frame, from_=10, to=200, orient="horizontal", length=330, variable=current_weight, bg="lightgrey",
          command=lambda value: weight.set(f"{float(value):.2f}")).grid(row=5, column=0, columnspan=2, pady=10)

    vector_image = Image.open('images/bmi.png') 
    vector_image = vector_image.resize((305, 305), Image.Resampling.LANCZOS)  # Adjust size as needed
    vector_photo = ImageTk.PhotoImage(vector_image)

    vector_label = Label(image_frame, image=vector_photo, bg="white")
    vector_label.image = vector_photo  
    vector_label.grid(row=3, column=0, columnspan=2, pady=10) 

    result_label = Label(image_frame, font=("yu gothic ui", 15, "bold"), bg="white", fg="#1b87d2")
    result_label.grid(row=4, column=0, columnspan=2, pady=5)

    health_label = Label(image_frame, font=("yu gothic ui", 12, "bold"), bg="white", fg="black", width=50, justify="center", anchor="center")
    health_label.grid(row=5, column=0, columnspan=2, pady=4)

    Button(form_frame, text="Calculate BMI", width=36, height=2, font=("yu gothic ui", 12, "bold"), bg="#1b87d2", fg="white",
       command=lambda: calculate_bmi(height, weight, age, result_label, health_label, user_id, form_frame, image_frame, show_frame)).grid(row=6, column=0, columnspan=2, pady=20)

def calculate_bmi(height_var, weight_var, age, result_label, health_label, user_id, form_frame, image_frame, show_frame):
   
    veg_selected = BooleanVar(value=True) 
    non_veg_selected = BooleanVar(value=True)  
    
    try:
        height = float(height_var.get()) / 100 
        weight = float(weight_var.get())
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")
        health_label.config(text="")
        return  

    if height <= 0:
        result_label.config(text="Height must be greater than zero.")
        health_label.config(text="")
        return

    bmi = weight / (height ** 2)
    result_label.config(text=f"Your BMI: {bmi:.2f}")

    try:
        age_value = int(age.get())
    except ValueError:
        result_label.config(text="Please enter a valid age.")
        health_label.config(text="")
        return

    if age_value < 18:
        if bmi < 14.5:
            health_status = "Underweight"
        elif 14.5 <= bmi < 22.9:
            health_status = "Healthy Weight"
        elif 23 <= bmi < 25:
            health_status = "Overweight"
        else:
            health_status = "Obesity"
    elif 18 <= age_value < 65:
        if bmi < 18.5:
            health_status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            health_status = "Healthy weight"
        elif 25 <= bmi < 29.9:
            health_status = "Overweight"
        else:
            health_status = "Obesity"
    else:
        if bmi < 22:
            health_status = "Underweight"
        elif  22 <= bmi < 27:
            health_status = "Healthy Weight"
        else:
            health_status = "Overweight/Obesity"
    
    health_label.config(text=f"Health Status: {health_status}")

    diet_plan_button = Button(image_frame, text="View Diet Plan", width=22, height=2, font=("yu gothic ui", 11, "bold"),
        command=lambda: show_diet_plan(health_status, form_frame.master, show_frame), bg="#1b87d2", fg="white")
    diet_plan_button.grid(row=6, column=0, pady=20)

    back_button = Button(image_frame, text="Go back", width=22, height=2, font=("yu gothic ui", 11, "bold"), bg="#1b87d2", fg="white", command=lambda: show_frame(is_login=True))
    back_button.grid(row=6, column=1, pady=20)

    # Insert or update the results in the database
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='', 
            database='user_database'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM bmi_results WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            cursor.execute("UPDATE bmi_results SET height = %s, weight = %s, bmi = %s, health_status = %s WHERE user_id = %s",
                           (height_var.get(), weight_var.get(), bmi, health_status, user_id))
        else:
            cursor.execute("INSERT INTO bmi_results (user_id, height, weight, bmi, health_status) VALUES (%s, %s, %s, %s, %s)",
                           (user_id, height_var.get(), weight_var.get(), bmi, health_status))
        connection.commit()
        connection.close()
    except mysql.connector.Error as err:
        print("Error:", err)

def launch_bmi_page(parent, user_id, show_frame):
    parent.pack_propagate(False)
    parent.grid_propagate(False)

    background_label = Label(parent)
    background_label.pack(fill="both", expand=True)

    bg_image = Image.open('images/bg.jpg')
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    background_label.config(image=bg_photo)
    background_label.image = bg_photo 

    # Pass show_frame to open_dashboard
    open_dashboard(parent, user_id, show_frame)

if __name__ == "__main__":
    root = Tk()
    root.title("Login/Register -> BMI Calculator")

    def show_frame(is_login=False):
        print(f"Navigating to {'login' if is_login else 'other'} frame")

    launch_bmi_page(root, user_id, show_frame)
    root.mainloop()
