from tkinter import *


def get_next_bill_number():
    try:
        with open('last_bill_number.txt', 'r') as f:
            last_number = int(f.read().strip())
    except FileNotFoundError:
        last_number = 0
    
    new_number = last_number + 1
    
    with open('last_bill_number.txt', 'w') as f:
        f.write(str(new_number))
    
    return new_number

# Product prices constants
PRICES = {
    # Cosmetics prices
    'bath_soap': 40,
    'face_cream': 140,
    'face_wash': 240,
    'hair_spray': 340,
    'hair_gel': 140,
    'body_lotion': 260,
    
    # Grocery prices
    'rice': 80,
    'food_oil': 180,
    'wheat': 60,
    'sugar': 45,
    'salt': 20,
    'daal': 160,
    
    # Cold Drinks prices
    'coca_cola': 60,
    'pepsi': 60,
    'fanta': 60,
    'sprite': 60,
    'limca': 60,
    'mountain_dew': 60
}

def calculate_total():
    try:
        # Cosmetics total
        total_cosmetics = (
            float(bath_soap_entry.get() or 0) * PRICES['bath_soap'] +
            float(face_cream_entry.get() or 0) * PRICES['face_cream'] +
            float(face_wash_entry.get() or 0) * PRICES['face_wash'] +
            float(hair_spray_entry.get() or 0) * PRICES['hair_spray'] +
            float(hair_gel_entry.get() or 0) * PRICES['hair_gel'] +
            float(body_lotion_entry.get() or 0) * PRICES['body_lotion']
        )
        
        # Grocery total
        total_grocery = (
            float(rice_entry.get() or 0) * PRICES['rice'] +
            float(food_oil_entry.get() or 0) * PRICES['food_oil'] +
            float(wheat_entry.get() or 0) * PRICES['wheat'] +
            float(sugar_entry.get() or 0) * PRICES['sugar'] +
            float(salt_entry.get() or 0) * PRICES['salt'] +
            float(daal_entry.get() or 0) * PRICES['daal']
        )
        
        # Cold Drinks total
        total_drinks = (
            float(coca_cola_entry.get() or 0) * PRICES['coca_cola'] +
            float(pepsi_entry.get() or 0) * PRICES['pepsi'] +
            float(fanta_entry.get() or 0) * PRICES['fanta'] +
            float(sprite_entry.get() or 0) * PRICES['sprite'] +
            float(limca_entry.get() or 0) * PRICES['limca'] +
            float(mountain_dew_entry.get() or 0) * PRICES['mountain_dew']
        )
        
        # Calculate subtotals and tax
        subtotal = total_cosmetics + total_grocery + total_drinks
        Discount = subtotal * 0.18  # 18% GST
        total = subtotal  - Discount
        
        # Generate bill
        bill_no = str(get_next_bill_number()).zfill(4)  # Pad with zeros to 4 digits
        bill_details = f'''
=============== RETAIL INVOICE ===============
Bill Number: {bill_no}
Customer Name: {name_entry.get()}
Phone Number: {phone_entry.get()}
============================================
Products                   Qty                             Price
============================================
'''
        
        # Add to bill area
        bill_area.delete(1.0, END)
        bill_area.insert(END, bill_details)
        
        # Add items with quantities > 0 to bill
        def add_to_bill(name, entry):
            qty = entry.get().strip()
            if qty and float(qty) > 0:
                price = float(qty) * PRICES[name]
                bill_area.insert(END,f"{name:<10}\t\t{qty:>3}\t\t{ price:>5.2f}\n")
        
        # Add cosmetics items
        for name, entry in [
            ('bath_soap', bath_soap_entry),
            ('face_cream', face_cream_entry),
            ('face_wash', face_wash_entry),
            ('hair_spray', hair_spray_entry),
            ('hair_gel', hair_gel_entry),
            ('body_lotion', body_lotion_entry)
        ]:
            add_to_bill(name, entry)
            
        # Add grocery items
        for name, entry in [
            ('rice', rice_entry),
            ('food_oil', food_oil_entry),
            ('wheat', wheat_entry),
            ('sugar', sugar_entry),
            ('salt', salt_entry),
            ('daal', daal_entry)
        ]:
            add_to_bill(name, entry)
            
        # Add cold drinks items
        for name, entry in [
            ('coca_cola', coca_cola_entry),
            ('pepsi', pepsi_entry),
            ('fanta', fanta_entry),
            ('sprite', sprite_entry),
            ('limca', limca_entry),
            ('mountain_dew', mountain_dew_entry)
        ]:
            add_to_bill(name, entry)
        
        # Add totals to bill
        bill_area.insert(END, f'''
============================================
Subtotal: {subtotal:>32.2f}
Discount (18%): {Discount:>31.2f}
Total: {total:>34.2f}
============================================
''')
    except ValueError:
        bill_area.delete(1.0, END)
        bill_area.insert(END, "Error: Please enter valid numbers")

# Initialize main window
root = Tk()
root.title("Retail Billing System")
root.geometry("1270x685+0+0")

# Make the root window responsive
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Main container frame
main_container = Frame(root)
main_container.grid(sticky="nsew")
main_container.grid_columnconfigure(0, weight=1)

# Header
header = Label(main_container, text="Retail Billing System", 
              font=("times new roman", 30, "bold"),
              bg="gray20", fg="gold", bd=12, relief=GROOVE)
header.grid(row=0, column=0, sticky="ew", pady=5)

# Customer details frame
frame1 = LabelFrame(main_container, text="Customer Details",
                  font=("times new roman", 15, "bold"),
                  bg="gray20", fg="gold", bd=12, relief=SUNKEN)
frame1.grid(row=1, column=0, sticky="ew", padx=5)
frame1.grid_columnconfigure(1, weight=1)
frame1.grid_columnconfigure(3, weight=1)
frame1.grid_columnconfigure(5, weight=1)

# Customer details entries
name_label = Label(frame1, text="Name", bg="gray20", 
                 fg="white", font=("times new roman", 15, "bold"))
name_label.grid(row=0, column=0, padx=20)
name_entry = Entry(frame1, font=("times new roman", 15, "bold"),
                 bd=5, relief=SUNKEN)
name_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

phone_label = Label(frame1, text="Phone", bg="gray20",
                  fg="white", font=("times new roman", 15, "bold"))
phone_label.grid(row=0, column=2, padx=20)
phone_entry = Entry(frame1, font=("times new roman", 15, "bold"),
                  bd=5, relief=SUNKEN)
phone_entry.grid(row=0, column=3, pady=10, padx=10, sticky="ew")

# Product details container
frame2 = Frame(main_container)
frame2.grid(row=2, column=0, sticky="nsew")
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=1)
frame2.grid_columnconfigure(2, weight=1)
frame2.grid_columnconfigure(3, weight=1)

# Cosmetics frame
frame3 = LabelFrame(frame2, text="Cosmetics",
                   font=("times new roman", 15, "bold"),
                   bg="gray20", fg="gold", bd=12, relief=SUNKEN)
frame3.grid(row=0, column=0, padx=8, pady=3, sticky="nsew")

# Create cosmetics entries
cosmetics_items = [
    ("Bath Soap", "bath_soap"),
    ("Face Cream", "face_cream"),
    ("Face Wash", "face_wash"),
    ("Hair Spray", "hair_spray"),
    ("Hair Gel", "hair_gel"),
    ("Body Lotion", "body_lotion")
]

for i, (label_text, var_name) in enumerate(cosmetics_items):
    Label(frame3, text=label_text, bg="gray20", fg="white",
          font=("times new roman", 15, "bold")).grid(row=i, column=0, pady=5, sticky="w")
    entry = Entry(frame3, font=("times new roman", 15, "bold"),
                 bd=5, relief=SUNKEN, width=10)
    entry.grid(row=i, column=1, pady=5, padx=10)
    globals()[f"{var_name}_entry"] = entry

# Grocery frame
frame4 = LabelFrame(frame2, text="Grocery",
                   font=("times new roman", 15, "bold"),
                   bg="gray20", fg="gold", bd=12, relief=SUNKEN)
frame4.grid(row=0, column=1, padx=8, pady=3, sticky="nsew")

# Create grocery entries
grocery_items = [
    ("Rice", "rice"),
    ("Food Oil", "food_oil"),
    ("Wheat", "wheat"),
    ("Sugar", "sugar"),
    ("Salt", "salt"),
    ("Daal", "daal")
]

for i, (label_text, var_name) in enumerate(grocery_items):
    Label(frame4, text=label_text, bg="gray20", fg="white",
          font=("times new roman", 15, "bold")).grid(row=i, column=0, pady=5, sticky="w")
    entry = Entry(frame4, font=("times new roman", 15, "bold"),
                 bd=5, relief=SUNKEN, width=10)
    entry.grid(row=i, column=1, pady=5, padx=10)
    globals()[f"{var_name}_entry"] = entry

# Cold Drinks frame
frame5 = LabelFrame(frame2, text="Cold Drinks",
                   font=("times new roman", 15, "bold"),
                   bg="gray20", fg="gold", bd=12, relief=SUNKEN)
frame5.grid(row=0, column=2, padx=8, pady=3, sticky="nsew")

# Create cold drinks entries
drinks_items = [
    ("Coca Cola", "coca_cola"),
    ("Pepsi", "pepsi"),
    ("Fanta", "fanta"),
    ("Sprite", "sprite"),
    ("Limca", "limca"),
    ("Mountain Dew", "mountain_dew")
]

for i, (label_text, var_name) in enumerate(drinks_items):
    Label(frame5, text=label_text, bg="gray20", fg="white",
          font=("times new roman", 15, "bold")).grid(row=i, column=0, pady=5, sticky="w")
    entry = Entry(frame5, font=("times new roman", 15, "bold"),
                 bd=5, relief=SUNKEN, width=10)
    entry.grid(row=i, column=1, pady=5, padx=10)
    globals()[f"{var_name}_entry"] = entry

# Bill area frame
frame6 = Frame(frame2, bd=10, relief=SUNKEN)
frame6.grid(row=0, column=3, padx=8, pady=5, sticky="nsew")

# Bill area widgets
bill_label = Label(frame6, text="Bill Area",
                 font=("times new roman", 15, "bold"),
                 bd=7, relief=SUNKEN)
bill_label.pack(fill=X)

scroll_bar = Scrollbar(frame6, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=Y)

bill_area = Text(frame6, width=40, height=20,
               font=("times new roman", 10, "bold"),
               bd=5, relief=SUNKEN,
               yscrollcommand=scroll_bar.set)
bill_area.pack(fill=BOTH, expand=True)
scroll_bar.config(command=bill_area.yview)

# Calculate button
calculate_btn = Button(frame2, text="Calculate Bill",
                      command=calculate_total,
                      font=("times new roman", 15, "bold"),
                      bg="gold", fg="black",
                      bd=7, relief=RAISED)
calculate_btn.grid(row=1, column=0, columnspan=4, pady=10)

root.mainloop()

