import tkinter as tk
from tkinter import messagebox

# ---------------- INVENTORY ----------------

inventory = {
    "P101": {"name": "Mini Perfume", "category": "Beauty", "price": 350, "stock": 20},
    "P102": {"name": "Plush Toy", "category": "Toy", "price": 650, "stock": 15},
    "P103": {"name": "Water Bottle", "category": "Lifestyle", "price": 450, "stock": 25},
    "P104": {"name": "Face Towel", "category": "Home", "price": 250, "stock": 30},
    "P105": {"name": "Makeup Mirror", "category": "Beauty", "price": 500, "stock": 18},
    "P106": {"name": "Travel Bag", "category": "Travel", "price": 1200, "stock": 10},
    "P107": {"name": "Headphone", "category": "Electronics", "price": 900, "stock": 12}
}

sales = []
invoice_counter = 1


# ---------------- ADD SALE ----------------

def add_sale():

    global invoice_counter

    customer_name = entry_customer.get()
    phone_number = entry_phone.get()
    product_code = entry_product_code.get()
    quantity_text = entry_quantity.get()
    discount_text = entry_discount.get()

    # Validation
    if customer_name == "" or product_code == "" or quantity_text == "":
        messagebox.showerror("Error", "Please fill all required fields")
        return

    if product_code not in inventory:
        messagebox.showerror("Error", "Product code not found")
        return

    try:
        quantity = int(quantity_text)
    except:
        messagebox.showerror("Error", "Quantity must be a number")
        return

    if quantity <= 0:
        messagebox.showerror("Error", "Quantity must be greater than 0")
        return

    # Discount
    if discount_text == "":
        discount_percentage = 0
    else:
        try:
            discount_percentage = float(discount_text)
        except:
            messagebox.showerror("Error", "Discount must be a number")
            return

    # Stock check
    if quantity > inventory[product_code]["stock"]:
        messagebox.showerror("Stock Error", "Not enough stock available")
        return

    # Product details
    product_name = inventory[product_code]["name"]
    category = inventory[product_code]["category"]
    unit_price = inventory[product_code]["price"]

    # Calculation
    subtotal = unit_price * quantity

    discount_amount = subtotal * discount_percentage / 100

    amount_after_discount = subtotal - discount_amount

    vat = amount_after_discount * 0.05

    total_amount = amount_after_discount + vat

    invoice_id = "M" + str(invoice_counter)

    # Store sale
    sale = {
        "invoice_id": invoice_id,
        "customer_name": customer_name,
        "phone_number": phone_number,
        "product_code": product_code,
        "product_name": product_name,
        "category": category,
        "quantity": quantity,
        "unit_price": unit_price,
        "subtotal": subtotal,
        "discount_percentage": discount_percentage,
        "discount_amount": discount_amount,
        "vat": vat,
        "total_amount": total_amount
    }

    sales.append(sale)

    # Reduce stock
    inventory[product_code]["stock"] -= quantity

    invoice_counter += 1

    messagebox.showinfo(
        "Success",
        "Sale added successfully\nInvoice ID: " + invoice_id
    )

    clear_fields()


# ---------------- SHOW SALES ----------------

def show_all_sales():

    output_text.delete(1.0, tk.END)

    if len(sales) == 0:
        output_text.insert(tk.END, "No sales data found")
        return

    count = 1

    for sale in sales:

        output_text.insert(tk.END, "------------- SALE " + str(count) + " -------------\n")

        output_text.insert(tk.END, "Invoice ID: " + sale["invoice_id"] + "\n")
        output_text.insert(tk.END, "Customer Name: " + sale["customer_name"] + "\n")
        output_text.insert(tk.END, "Phone Number: " + sale["phone_number"] + "\n")
        output_text.insert(tk.END, "Product Code: " + sale["product_code"] + "\n")
        output_text.insert(tk.END, "Product Name: " + sale["product_name"] + "\n")
        output_text.insert(tk.END, "Category: " + sale["category"] + "\n")
        output_text.insert(tk.END, "Quantity: " + str(sale["quantity"]) + "\n")
        output_text.insert(tk.END, "Unit Price: " + str(sale["unit_price"]) + "\n")
        output_text.insert(tk.END, "Subtotal: " + str(sale["subtotal"]) + "\n")
        output_text.insert(tk.END, "Discount: " + str(sale["discount_amount"]) + "\n")
        output_text.insert(tk.END, "VAT 5%: " + str(sale["vat"]) + "\n")
        output_text.insert(tk.END, "Total Amount: " + str(sale["total_amount"]) + "\n\n")

        count += 1


# ---------------- SEARCH SALE ----------------

def search_sale():

    search_invoice_id = entry_search_invoice.get()

    output_text.delete(1.0, tk.END)

    found = False

    for sale in sales:

        if sale["invoice_id"] == search_invoice_id:

            output_text.insert(tk.END, "Sale Found\n\n")

            output_text.insert(tk.END, "Invoice ID: " + sale["invoice_id"] + "\n")
            output_text.insert(tk.END, "Customer Name: " + sale["customer_name"] + "\n")
            output_text.insert(tk.END, "Phone Number: " + sale["phone_number"] + "\n")
            output_text.insert(tk.END, "Product Code: " + sale["product_code"] + "\n")
            output_text.insert(tk.END, "Product Name: " + sale["product_name"] + "\n")
            output_text.insert(tk.END, "Category: " + sale["category"] + "\n")
            output_text.insert(tk.END, "Quantity: " + str(sale["quantity"]) + "\n")
            output_text.insert(tk.END, "Unit Price: " + str(sale["unit_price"]) + "\n")
            output_text.insert(tk.END, "Subtotal: " + str(sale["subtotal"]) + "\n")
            output_text.insert(tk.END, "Discount: " + str(sale["discount_amount"]) + "\n")
            output_text.insert(tk.END, "VAT 5%: " + str(sale["vat"]) + "\n")
            output_text.insert(tk.END, "Total Amount: " + str(sale["total_amount"]) + "\n")

            found = True
            break

    if found == False:
        output_text.insert(tk.END, "Sale not found")


# ---------------- UPDATE SALE ----------------

def update_sale():

    search_invoice_id = entry_search_invoice.get()

    if search_invoice_id == "":
        messagebox.showerror("Error", "Enter invoice ID")
        return

    found = False

    for sale in sales:

        if sale["invoice_id"] == search_invoice_id:

            quantity_text = entry_quantity.get()
            discount_text = entry_discount.get()

            try:
                quantity = int(quantity_text)
            except:
                messagebox.showerror("Error", "Quantity must be number")
                return

            if discount_text == "":
                discount_percentage = 0
            else:
                discount_percentage = float(discount_text)

            unit_price = sale["unit_price"]

            subtotal = unit_price * quantity

            discount_amount = subtotal * discount_percentage / 100

            amount_after_discount = subtotal - discount_amount

            vat = amount_after_discount * 0.05

            total_amount = amount_after_discount + vat

            sale["quantity"] = quantity
            sale["subtotal"] = subtotal
            sale["discount_percentage"] = discount_percentage
            sale["discount_amount"] = discount_amount
            sale["vat"] = vat
            sale["total_amount"] = total_amount

            messagebox.showinfo("Success", "Sale updated successfully")

            found = True
            break

    if found == False:
        messagebox.showerror("Error", "Invoice not found")


# ---------------- DELETE SALE ----------------

def delete_sale():

    search_invoice_id = entry_search_invoice.get()

    found = False

    for sale in sales:

        if sale["invoice_id"] == search_invoice_id:

            sales.remove(sale)

            messagebox.showinfo("Success", "Sale deleted successfully")

            found = True
            break

    if found == False:
        messagebox.showerror("Error", "Invoice not found")


# ---------------- CLEAR FIELDS ----------------

def clear_fields():

    entry_customer.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_product_code.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_discount.delete(0, tk.END)


# ---------------- GUI ----------------

root = tk.Tk()

root.title("Mini Shop Management System")

root.geometry("900x700")


# Customer Name
tk.Label(root, text="Customer Name").pack()

entry_customer = tk.Entry(root, width=40)
entry_customer.pack()


# Phone Number
tk.Label(root, text="Phone Number").pack()

entry_phone = tk.Entry(root, width=40)
entry_phone.pack()


# Product Code
tk.Label(root, text="Product Code").pack()

entry_product_code = tk.Entry(root, width=40)
entry_product_code.pack()


# Quantity
tk.Label(root, text="Quantity").pack()

entry_quantity = tk.Entry(root, width=40)
entry_quantity.pack()


# Discount
tk.Label(root, text="Discount %").pack()

entry_discount = tk.Entry(root, width=40)
entry_discount.pack()


# Search Invoice
tk.Label(root, text="Search Invoice ID").pack()

entry_search_invoice = tk.Entry(root, width=40)
entry_search_invoice.pack()


# Buttons
tk.Button(root, text="Add Sale", width=20, command=add_sale).pack(pady=5)

tk.Button(root, text="Show All Sales", width=20, command=show_all_sales).pack(pady=5)

tk.Button(root, text="Search Sale", width=20, command=search_sale).pack(pady=5)

tk.Button(root, text="Update Sale", width=20, command=update_sale).pack(pady=5)

tk.Button(root, text="Delete Sale", width=20, command=delete_sale).pack(pady=5)


# Output Box
output_text = tk.Text(root, width=100, height=20)

output_text.pack(pady=10)


root.mainloop()
