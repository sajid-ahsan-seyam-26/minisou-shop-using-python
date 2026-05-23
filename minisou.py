import tkinter as tk 
from tkinter import messagebox
inventory = {
    "P101": {"name": "Mini Perfume", "category": "Beauty", "price": 350, "stock": 20},
    "P102": {"name": "Plush Toy", "category": "Toy", "price": 650, "stock": 15},
    "P103": {"name": "Water Bottle", "category": "Lifestyle", "price": 450, "stock": 25},
    "P104": {"name": "Face Towel", "category": "Home", "price": 250, "stock": 30},
    "P105": {"name": "Makeup Mirror", "category": "Beauty", "price": 500, "stock": 18},
    "P106": {"name": "Travel Bag", "category": "Travel", "price": 1200, "stock": 10},
    "P107": {"name": "Headphone", "category": "Electronics", "price": 900, "stock": 12}
}
invoice_counter=1
def add_sale():
    global invoice_counter
    customer_name=enter_customer.get()
    phone_number=entery_phone.get()
    product_code=entery_product_code.get()
    quantity_text=entery_quantity.get()
    discount_text=entery_discount.get()


    if customer_name=="" or product_code=="" or quantity_text=="":
        messagebox.showerror("error","please fill in all required fields")
        return
    if product_code not in inventory:
        messagebox.showerror("error","product code is not found")
        return
    try:
        quantity=int(quantity_text)
    except:
        messagebox.showerror("error","quantity must be a number")
    if quantity<=0:
        messagebox.showerror("error","quantity must be greater than 0")
        return
    if discount_text=="":
        discount_percent=0
    else:
        try:
            discount_percent=float(discount_text)
        except:
            messagebox.showerror("error","discount must be a number")
            return
    if quantity>inventory[product_code]["stoke"]:
        messagebox.showoring("stock error","not enough stock availabe")
        return
        product_name=inventory[product_code]["name"]
        category=inventory[product_code]["category"]
        unit_price=inventory[product_code]["price"]
        subtotal=unit_price*quantity
        discount_amount=subtitle*discount_percentage/100
        amount_after_discount=subtotal-discount_amout
        vat=amount-after_discount*0.05
        total_amount=amount_after_discount+vat
        invoice_id="m"+str(invoice_counter)
        sales={
        "invoice_id":invoice_id,
        "customer name":phone_number,
        "product_code":product_code,

        "product_name":product_name,
        "category":category,
        "quantity":quantity,
        "unit_price":quantity,
        "subtotal":subtotal,
        "discount_percentage":discount_percentage,
        "discount_amount":discount_amount,
        "vat":vat,
        "total amount":total_amount
        }
        sales.append(sales)
        inventory[product_cosde]["stock"]=inventory[product_code]["stock"]-quantity
        invoice_counter=invoice_counter+1
        messageboc.showinfo(
            "success",
            "sales added successfully .\ninvoice Id:"+invoice_id)
        




