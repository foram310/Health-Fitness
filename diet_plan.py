from tkinter import *
from tkinter import ttk

login_frame = None 

def show_frame(frame):
    if frame:
        frame.tkraise()
        print(f"Showing frame: {frame}")
    else:
        print("Frame is not defined")

def go_back_to_login():
    print("Back button clicked") 
    show_frame(login_frame) 

def show_diet_plan(bmi_category, show_frame, go_back_function=None, show_both=False):
    parent = show_frame 

    for widget in parent.winfo_children():
        widget.destroy()

    header_frame = Frame(parent, bg="white")
    header_frame.pack(fill=X, pady=15, padx=10)

    back_button = Button(header_frame, text="Log Out", command=go_back_function, font=("yu gothic ui", 12), bg="#1b87d2", fg="white")
    back_button.grid(row=0, column=0, sticky='w')  

    heading_label = Label(header_frame, text=f"Diet Plan for {bmi_category} Category", font=("yu gothic ui", 20, "bold"), bg="white", fg="blue")
    heading_label.grid(row=0, column=1, padx=250)

    table_frame = Frame(parent, bg="white")
    table_frame.pack(fill=BOTH, expand=True)

    diet_plans = {
        "Underweight": {
            "Veg": {
                "Monday": [("Breakfast", "Oatmeal with Banana","8:00 AM"), ("Snack", "Almonds","10:00 AM"), ("Lunch", "Vegetable Stir-fry", "1:00 PM"), ("Snack", "Greek Yogurt", "4:00 PM"), ("Dinner", "Vegetable Curry", "7:00 PM")],
                "Tuesday": [("Breakfast", "Peanut Butter Toast","8:00 AM"), ("Snack", "Trail Mix","10:00 AM"), ("Lunch", "Vegetable Wrap", "1:00 PM"), ("Snack", "Fruit Smoothie", "4:00 PM"), ("Dinner", "Stir-fried Tofu with Rice", "7:00 PM")],
                "Wednesday": [("Breakfast", "Fruit Salad","8:00 AM"), ("Snack", "Cottage Cheese","10:00 AM"), ("Lunch", "Pasta with Veggies", "1:00 PM"), ("Snack", "Popcorn", "4:00 PM"), ("Dinner", "Vegetable Soup", "7:00 PM")],
                "Thursday": [("Breakfast", "Smoothie Bowl","8:00 AM"), ("Snack", "Peanut Butter Cookies","10:00 AM"), ("Lunch", "Rice with Beans", "1:00 PM"), ("Snack", "Cheese Sticks", "4:00 PM"), ("Dinner", "Vegetable Stir-fry", "7:00 PM")],
                "Friday": [("Breakfast", "Avocado Toast","8:00 AM"), ("Snack", "Hard-boiled Eggs","10:00 AM"), ("Lunch", "Quinoa Salad", "1:00 PM"), ("Snack", "Hummus with Veggies", "4:00 PM"), ("Dinner", "Vegetable Tacos", "7:00 PM")],
                "Saturday": [("Breakfast", "Breakfast Burrito","8:00 AM"), ("Snack", "Fruit Salad","10:00 AM"), ("Lunch", "Couscous with Veggies", "1:00 PM"), ("Snack", "Granola Bars", "4:00 PM"), ("Dinner", "Stuffed Peppers", "7:00 PM")],
                "Sunday": [("Breakfast", "Chia Pudding","8:00 AM"), ("Snack", "Nut Mix","10:00 AM"), ("Lunch", "Veggie Burger", "1:00 PM"), ("Snack", "Yogurt Parfait", "4:00 PM"), ("Dinner", "Vegetable Pasta", "7:00 PM")]
            },
            "Non-Veg": {
                "Monday": [("Breakfast", "Oatmeal with Banana","8:00 AM"), ("Snack", "Almonds","10:00 AM"), ("Lunch", "Chicken Breast with Quinoa", "1:00 PM"), ("Snack", "Greek Yogurt", "4: 00 PM"), ("Dinner", "Salmon with Veggies", "7:00 PM")],
                "Tuesday": [("Breakfast", "Peanut Butter Toast","8:00 AM"), ("Snack", "Trail Mix","10:00 AM"), ("Lunch", "Turkey Wrap", "1:00 PM"), ("Snack", "Fruit Smoothie", "4:00 PM"), ("Dinner", "Stir-fried Tofu with Rice", "7:00 PM")],
                "Wednesday": [("Breakfast", "Fruit Salad","8:00 AM"), ("Snack", "Cottage Cheese","10:00 AM"), ("Lunch", "Pasta with Chicken", "1:00 PM"), ("Snack", "Popcorn", "4:00 PM"), ("Dinner", "Grilled Shrimp", "7:00 PM")],
                "Thursday": [("Breakfast", "Smoothie Bowl","8:00 AM"), ("Snack", "Peanut Butter Cookies","10:00 AM"), ("Lunch", "Rice with Beans", "1:00 PM"), ("Snack", "Cheese Sticks", "4:00 PM"), ("Dinner", "Chicken Stir-fry", "7:00 PM")],
                "Friday": [("Breakfast", "Avocado Toast","8:00 AM"), ("Snack", "Hard-boiled Eggs","10:00 AM"), ("Lunch", "Quinoa Salad", "1:00 PM"), ("Snack", "Hummus with Veggies", "4:00 PM"), ("Dinner", "Pork Chops with Apples", "7:00 PM")],
                "Saturday": [("Breakfast", "Breakfast Burrito","8:00 AM"), ("Snack", "Fruit Salad","10:00 AM"), ("Lunch", "Couscous with Veggies", "1:00 PM"), ("Snack", "Granola Bars", "4:00 PM"), ("Dinner", "Fish Tacos", "7:00 PM")],
                "Sunday": [("Breakfast", "Chia Pudding","8:00 AM"), ("Snack", "Nut Mix","10:00 AM"), ("Lunch", "Veggie Burger", "1:00 PM"), ("Snack", "Yogurt Parfait", "4:00 PM"), ("Dinner", "Chicken Alfredo", "7:00 PM")]
            }
        },
        "Healthy Weight": {
            "Veg": {
                "Monday": [("Breakfast", "Smoothie with Spinach","8:00 AM"), ("Snack", "Carrot Sticks","10:00 AM"), ("Lunch", "Grilled Vegetable Salad", "1:00 PM"), ("Snack", "Apple Slices", "4:00 PM"), ("Dinner", "Vegetable Stir-fry", "7:00 PM")],
                "Tuesday": [("Breakfast", "Overnight Oats","8:00 AM"), ("Snack", "Edamame","10:00 AM"), ("Lunch", "Vegetable Sandwich", "1:00 PM"), ("Snack", "Cucumber Slices", "4:00 PM"), ("Dinner", "Baked Tofu with Quinoa", "7:00 PM")],
                "Wednesday": [("Breakfast", "Greek Yogurt with Berries","8:00 AM"), ("Snack", "Bell Pepper Strips","10:00 AM"), ("Lunch", "Pasta Primavera", "1:00 PM"), ("Snack", "Rice Cakes", "4:00 PM"), ("Dinner", "Stuffed Peppers", "7:00 PM")],
                "Thursday": [("Breakfast", "Whole Grain Toast","8:00 AM"), ("Snack", "Mixed Nuts","10:00 AM"), ("Lunch", "Caesar Salad", "1:00 PM"), ("Snack", "Dried Fruits", "4:00 PM"), ("Dinner", "Grilled Vegetable Skewers", "7:00 PM")],
                "Friday": [("Breakfast", "Fruit Smoothie","8:00 AM"), ("Snack", "Cheese Sticks","10:00 AM"), ("Lunch", "Mediterranean Bowl", "1:00 PM"), ("Snack", "Nut Butter on Crackers", "4:00 PM"), ("Dinner", "Vegetable Curry", "7:00 PM")],
                "Saturday": [("Breakfast", "Egg White Omelette","8:00 AM"), ("Snack", "Popcorn","10:00 AM"), ("Lunch", "Quinoa Salad", "1:00 PM"), ("Snack", "Celery with Peanut Butter", "4:00 PM"), ("Dinner", "Stuffed Zucchini", "7:00 PM")],
                "Sunday": [("Breakfast", "Pancakes with Maple Syrup","8:00 AM"), ("Snack", "Fruit Salad","10:00 AM"), ("Lunch", "Zucchini Noodles", "1:00 PM"), ("Snack", "Yogurt", "4:00 PM"), ("Dinner", "Vegetable Stir-fry", "7:00 PM")]
            },
            "Non-Veg": {
                "Monday": [("Breakfast", "Smoothie with Spinach","8:00 AM"), ("Snack", "Carrot Sticks","10:00 AM"), ("Lunch", "Grilled Chicken Salad", "1:00 PM"), ("Snack", "Apple Slices", "4:00 PM"), ("Dinner", "Steak with Asparagus", "7:00 PM")],
                "Tuesday": [("Breakfast", "Overnight Oats","8:00 AM"), ("Snack", "Edamame","10:00 AM"), ("Lunch", "Turkey Sandwich", "1:00 PM"), ("Snack", "Cucumber Slices", "4:00 PM"), ("Dinner", "Baked Salmon with Quinoa", "7:00 PM")],
                "Wednesday": [("Breakfast", "Greek Yogurt with Berries","8:00 AM"), ("Snack", "Bell Pepper Strips","10:00 AM"), ("Lunch", "Pasta Primavera", "1:00 PM"), ("Snack", "Rice Cakes", "4:00 PM"), ("Dinner", "Stuffed Peppers", "7:00 PM")],
                "Thursday": [("Breakfast", "Whole Grain Toast","8:00 AM"), ("Snack", "Mixed Nuts","10:00 AM"), ("Lunch", "Caesar Salad", "1:00 PM"), ("Snack", "Dried Fruits", "4:00 PM"), ("Dinner", "Grilled Shrimp with Veggies", "7:00 PM")],
                "Friday": [("Breakfast", "Fruit Smoothie","8:00 AM"), ("Snack", "Cheese Sticks","10:00 AM"), ("Lunch", "Mediterranean Bowl", "1:00 PM"), ("Snack", "Nut Butter on Crackers", "4:00 PM"), ("Dinner", "Grilled Chicken Thighs", "7:00 PM")],
                "Saturday": [("Breakfast", "Egg White Omelette","8:00 AM"), ("Snack", "Popcorn","10:00 AM"), ("Lunch", "Quinoa Salad", "1:00 PM"), ("Snack", "Celery with Peanut Butter", "4:00 PM"), ("Dinner", "Lamb Chops with Couscous", "7:00 PM")],
                "Sunday": [("Breakfast", "Pancakes with Maple Syrup","8:00 AM"), ("Snack", "Fruit Salad","10:00 AM"), ("Lunch", "Zucchini Noodles", "1:00 PM"), ("Snack", "Yogurt", "4:00 PM"), ("Dinner", "Vegetable Stir-fry", "7:00 PM")]
            }
        },
        "Overweight": {
            "Veg": {
                "Monday": [("Breakfast", "Greek Yogurt with Berries","8:00 AM"), ("Snack", "Sliced Cucumber","10:00 AM"), ("Lunch", "Vegetable Salad", "1:00 PM"), ("Snack", "Almonds", "4:00 PM"), ("Dinner", "Baked Tofu with Broccoli", "7:00 PM")],
                "Tuesday": [("Breakfast", "Oatmeal with Fruits","8:00 AM"), ("Snack", "Carrot Sticks","10:00 AM"), ("Lunch", "Quinoa with Roasted Vegetables", "1:00 PM"), ("Snack", "Popcorn", "4:00 PM"), ("Dinner", "Vegetable Stir-fry with Tofu", "7:00 PM")],
                "Wednesday": [("Breakfast", "Smoothie with Spinach","8:00 AM"), ("Snack", "Mixed Nuts","10:00 AM"), ("Lunch", "Whole Wheat Wrap with Hummus", "1:00 PM"), ("Snack", "Apple Slices", "4:00 PM"), ("Dinner", "Vegetable Stir-fry", "7:00 PM")],
                "Thursday": [("Breakfast", "Scrambled Eggs with Vegetables","8:00 AM"), ("Snack", "Celery with Peanut Butter","10:00 AM"), ("Lunch", "Lentil Soup with Salad", "1:00 PM"), ("Snack", "Rice Cakes", "4:00 PM"), ("Dinner", "Vegetable Curry", "7:00 PM")],
                "Friday": [("Breakfast", "Fruit Salad","8:00 AM"), ("Snack", "Yogurt","10:00 AM"), ("Lunch", "Vegetable Pasta", "1:00 PM"), ("Snack", "Dried Fruits", "4:00 PM"), ("Dinner", "Grilled Vegetable Skewers", "7:00 PM")],
                "Saturday": [("Breakfast", "Pancakes with Fruit","8:00 AM"), ("Snack", "Hard-boiled Eggs","10:00 AM"), ("Lunch", "Chickpea Salad", "1:00 PM"), ("Snack", "Dried Fruits", "4:00 PM"), ("Dinner", "Stuffed Peppers", "7:00 PM")],
                "Sunday": [("Breakfast", "Chia Pudding","8:00 AM"), ("Snack", "Smoothie","10:00 AM"), ("Lunch", "Stuffed Bell Peppers", "1:00 PM"), ("Snack", "Nut Mix", "4:00 PM"), ("Dinner", "Vegetable Stir-fry", "7:00 PM")]
            },
            "Non-Veg": {
                "Monday": [("Breakfast", "Greek Yogurt with Berries","8:00 AM"), ("Snack", "Sliced Cucumber","10:00 AM"), ("Lunch", "Grilled Chicken Salad", "1:00 PM"), ("Snack", "Almonds", "4:00 PM"), ("Dinner", "Baked Salmon with Broccoli", "7:00 PM")],
                "Tuesday": [("Breakfast", "Oatmeal with Fruits","8:00 AM"), ("Snack", "Carrot Sticks","10:00 AM"), ("Lunch", "Quinoa with Roasted Chicken", "1:00 PM"), ("Snack", "Popcorn", "4:00 PM"), ("Dinner", "Stir-fried Chicken with Veggies", "7:00 PM")],
                "Wednesday": [("Breakfast", "Smoothie with Spinach","8:00 AM"), ("Snack", "Mixed Nuts","10:00 AM"), ("Lunch", "Whole Wheat Wrap with Turkey", "1:00 PM"), ("Snack", "Apple Slices", "4:00 PM"), ("Dinner", "Grilled Shrimp with Vegetables", "7:00 PM")],
                "Thursday": [("Breakfast", "Scrambled Eggs with Vegetables","8:00 AM"), ("Snack", "Celery with Peanut Butter","10:00 AM"), ("Lunch", "Lentil Soup with Chicken", "1:00 PM"), ("Snack", "Rice Cakes", "4:00 PM"), ("Dinner", "Roasted Chicken with Quinoa", "7:00 PM")],
                "Friday": [("Breakfast", "Fruit Salad","8:00 AM"), ("Snack", "Yogurt","10:00 AM"), ("Lunch", "Vegetable Stir-fry with Chicken", "1:00 PM"), ("Snack", "Nuts", "4:00 PM"), ("Dinner", "Pork Chops with Apples", "7:00 PM")],
                "Saturday": [("Breakfast", "Pancakes with Fruit","8:00 AM"), ("Snack", "Hard-boiled Eggs","10:00 AM"), ("Lunch", "Chicken Pasta", "1:00 PM"), ("Snack", "Dried Fruits", "4:00 PM"), ("Dinner", "Stuffed Chicken Breasts", "7:00 PM")],
                "Sunday": [("Breakfast", "Chia Pudding","8:00 AM"), ("Snack", "Smoothie","10:00 AM"), ("Lunch", "Stuffed Bell Peppers", "1:00 PM"), ("Snack", "Nut Mix", "4:00 PM"), ("Dinner", "Beef Stir-fry", "7:00 PM")]
            }
        },
        "Obesity": {
            "Veg": {
                "Monday": [("Breakfast", "Vegetable Omelette","8:00 AM"), ("Snack", "Carrot Sticks","10:00 AM"), ("Lunch", "Lentil Salad", "1:00 PM"), ("Snack", "Apple Slices", "4:00 PM"), ("Dinner", "Vegetable Stir-fry with Tofu", "7:00 PM")],
                "Tuesday": [("Breakfast", "Quinoa Porridge","8:00 AM"), ("Snack", "Sliced Peppers","10:00 AM"), ("Lunch", "Chickpea Salad", "1:00 PM"), ("Snack", "Hummus with Cucumber", "4:00 PM"), ("Dinner", "Stuffed Zucchini", "7:00 PM")],
                "Wednesday": [("Breakfast", "Fruit Smoothie","8:00 AM"), ("Snack", "Mixed Nuts","10:00 AM"), ("Lunch", "Grilled Vegetable Salad", "1:00 PM"), ("Snack", "Yogurt", "4:00 PM"), ("Dinner", "Stir-fried Tofu with Veggies", "7:00 PM")],
                "Thursday": [("Breakfast", "Oatmeal with Nuts","8:00 AM"), ("Snack", "Rice Cakes","10:00 AM"), ("Lunch", "Lentil Soup with Salad", "1:00 PM"), ("Snack", "Fruit", "4:00 PM"), ("Dinner", "Stuffed Bell Peppers", "7:00 PM")],
                "Friday": [("Breakfast", "Avocado Toast","8:00 AM"), ("Snack", "Celery with Peanut Butter","10:00 AM"), ("Lunch", "Vegetable Bowl", "1:00 PM"), ("Snack", "Hard-boiled Eggs", "4:00 PM"), ("Dinner", "Grilled Tofu with Spinach", "7:00 PM")],
                "Saturday": [("Breakfast", "Smoothie Bowl","8:00 AM"), ("Snack", "Fruit Salad","10:00 AM"), ("Lunch", "Cauliflower Rice with Veggies", "1:00 PM"), ("Snack", "Nuts", "4:00 PM"), ("Dinner", "Vegetable Curry", "7:00 PM")],
                "Sunday": [("Breakfast", "Chia Seed Pudding","8:00 AM"), ("Snack", "Nut Mix","10:00 AM"), ("Lunch", "Vegetable Pasta", "1:00 PM"), ("Snack", "Yogurt", "4:00 PM"), ("Dinner", "Stuffed Peppers", "7:00 PM")]
            },
            "Non-Veg": {
                "Monday": [("Breakfast", "Egg White Omelette","8:00 AM"), ("Snack", "Sliced Cucumber","10:00 AM"), ("Lunch", "Grilled Chicken Salad", "1:00 PM"), ("Snack", "Almonds", "4:00 PM"), ("Dinner", "Baked Salmon with Broccoli", "7:00 PM")],
                "Tuesday": [("Breakfast", "Quinoa Porridge","8:00 AM"), ("Snack", "Carrot Sticks","10:00 AM"), ("Lunch", "Chicken Caesar Salad", "1:00 PM"), ("Snack", "Popcorn", "4:00 PM"), ("Dinner", "Stir-fried Chicken with Vegetables", "7:00 PM")],
                "Wednesday": [("Breakfast", "Fruit Smoothie","8:00 AM"), ("Snack", "Mixed Nuts","10:00 AM"), ("Lunch", "Turkey Wrap", "1:00 PM"), ("Snack", "Apple Slices", "4:00 PM"), ("Dinner", "Shrimp Stir-fry with Veggies", "7:00 PM")],
                "Thursday": [("Breakfast", "Oatmeal with Nuts","8:00 AM"), ("Snack", "Rice Cakes","10:00 AM"), ("Lunch", "Chicken Soup with Salad", "1:00 PM"), ("Snack", "Fruit", "4:00 PM"), ("Dinner", "Grilled Chicken with Asparagus", "7:00 PM")],
                "Friday": [("Breakfast", "Avocado Toast","8:00 AM"), ("Snack", "Celery with Peanut Butter","10:00 AM"), ("Lunch", "Grilled Fish Salad", "1:00 PM"), ("Snack", "Hard-boiled Eggs", "4:00 PM"), ("Dinner", "Turkey Meatballs with Zucchini", "7:00 PM")],
                "Saturday": [("Breakfast", "Smoothie Bowl","8:00 AM"), ("Snack", "Fruit Salad","10:00 AM"), ("Lunch", "Chicken Stir-fry", "1:00 PM"), ("Snack", "Nuts", "4:00 PM"), ("Dinner", "Stuffed Chicken Breast", "7:00 PM")],
                "Sunday": [("Breakfast", "Chia Seed Pudding","8:00 AM"), ("Snack", "Nut Mix","10:00 AM"), ("Lunch", "Taco Salad", "1:00 PM"), ("Snack", "Yogurt", "4:00 PM"), ("Dinner", "Baked Zucchini with Ground Turkey", "7:00 PM")]
            }
        }
    }
    style = ttk.Style()
    style.theme_use('clam') 
    style.configure("Treeview", background="white", foreground="black")
    style.configure("Treeview.Heading", background="#ADD8E6", foreground="black", font=("yu gothic ui", 10, "bold"))
    style.map("Treeview.Heading", background=[('active', '#ADD8E6')])

    # Vegetarian Diet Section
    veg_frame = Frame(table_frame, bg="white")
    veg_frame.pack(fill=BOTH, expand=True)

    veg_heading_frame = Frame(veg_frame, bg="white")
    veg_heading_frame.pack(pady=10)

    Label(veg_heading_frame, text="Vegetarian Diet Plan", font=("yu gothic ui", 16, "bold"), bg="white", fg="#1b87d2").pack(side=LEFT, padx=10)

    veg_tree = ttk.Treeview(veg_frame, columns=("Day", "Meal Type", "Food Item", "Time"), show="headings", height=7)
    veg_tree.heading("Day", text="Day")
    veg_tree.heading("Meal Type", text="Meal Type")
    veg_tree.heading("Food Item", text="Food Item")
    veg_tree.heading("Time", text="Time")
    veg_tree.column("Day", anchor=CENTER, width=100)
    veg_tree.column("Meal Type", anchor=CENTER)
    veg_tree.column("Food Item", anchor=CENTER)
    veg_tree.column("Time", anchor=CENTER)
    veg_tree.pack(side=LEFT, fill=BOTH, expand=True)

    veg_scroll = Scrollbar(veg_frame, orient="vertical", command=veg_tree.yview)
    veg_tree.configure(yscroll=veg_scroll.set)
    veg_scroll.pack(side=RIGHT, fill=Y)

    if bmi_category in diet_plans:
        for day, meals in diet_plans[bmi_category]["Veg"].items():
            for meal in meals:
                veg_tree.insert("", "end", values=(day if meal[0] == "Lunch" else "", meal[0], meal[1], meal[2]))

    non_veg_frame = Frame(table_frame, bg="white")
    non_veg_frame.pack(fill=BOTH, expand=True)

    non_veg_heading_frame = Frame(non_veg_frame, bg="white")
    non_veg_heading_frame.pack(pady=10)

    Label(non_veg_heading_frame, text="Non-Vegetarian Diet Plan", font=("yu gothic ui", 16, "bold"), bg="white", fg="#1b87d2").pack(side=LEFT, padx=10)

    non_veg_tree = ttk.Treeview(non_veg_frame, columns=("Day", "Meal Type", "Food Item", "Time"), show="headings", height=7)
    non_veg_tree.heading("Day", text="Day")
    non_veg_tree.heading("Meal Type", text="Meal Type")
    non_veg_tree.heading("Food Item", text="Food Item")
    non_veg_tree.heading("Time", text="Time")
    non_veg_tree.column("Day", anchor=CENTER, width=100)
    non_veg_tree.column("Meal Type", anchor=CENTER)
    non_veg_tree.column("Food Item", anchor=CENTER)
    non_veg_tree.column("Time", anchor=CENTER)
    non_veg_tree.pack(side=LEFT, fill=BOTH, expand=True)

    non_veg_scroll = Scrollbar(non_veg_frame, orient="vertical", command=non_veg_tree.yview)
    non_veg_tree.configure(yscroll=non_veg_scroll.set)
    non_veg_scroll.pack(side=RIGHT, fill=Y)

    if bmi_category in diet_plans:
        for day, meals in diet_plans[bmi_category]["Non-Veg"].items():
            for meal in meals:
                non_veg_tree.insert("", "end", values=(day if meal[0] == "Lunch" else "", meal[0], meal[1], meal[2]))

def open_diet_plan(bmi_category):
    global diet_window 
    diet_window = Toplevel()
    diet_window.title("Diet Plan")
    diet_window.geometry("800x600")

    frame = Frame(diet_window, bg="white")
    frame.pack(fill="both", expand=True)

    show_diet_plan(bmi_category, parent=frame, go_back_function=go_back_to_bmi, show_both=True)

if __name__ == "__main__":
    root = Tk()
    root.title("BMI Diet Plan")
    root.geometry("400x400")

    login_frame = Frame(root, bg="white")
    login_frame.pack(fill="both", expand=True)

    button_underweight = Button(root, text="View Diet Plan for Underweight", command=lambda: open_diet_plan("Underweight"))
    button_underweight.pack(pady=10)

    button_healthy_weight = Button(root, text="View Diet Plan for Healthy Weight", command=lambda: open_diet_plan("Healthy Weight"))
    button_healthy_weight.pack(pady=10)

    button_overweight = Button(root, text="View Diet Plan for Overweight", command=lambda: open_diet_plan("Overweight"))
    button_overweight.pack(pady=10)

    button_obesity = Button(root, text="View Diet Plan for Obesity", command=lambda: open_diet_plan("Obesity"))
    button_obesity.pack(pady=10)

    root.mainloop()
