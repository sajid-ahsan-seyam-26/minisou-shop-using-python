sales = []


def update_sale():
    search_invoice_id = entery_search_invoice.get()

    if search_invoice_id == "":
        messagebox.showerror("Error", "Enter invoice ID")
        return

    found = False

    for sale in sales:

        if sale["invoice_id"] == search_invoice_id:

            product_code = entery_product_code.get()
            quantity_text = entery_quantity.get()
            discount_text = entery_discount.get()

            if quantity_text == "":
                messagebox.showerror("Error", "Enter quantity")
                return

            try:
                quantity = int(quantity_text)
            except:
                messagebox.showerror("Error", "Quantity must be number")
                return

            if discount_text == "":
                discount_percentage = 0
            else:
                try:
                    discount_percentage = float(discount_text)
                except:
                    messagebox.showerror("Error", "Discount must be number")
                    return

            if quantity > inventory[product_code]["stock"]:
                messagebox.showerror("Stock Error", "Not enough stock available")
                return

            unit_price = inventory[product_code]["price"]

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


def delete_sale():

    search_invoice_id = entery_search_invoice.get()

    if search_invoice_id == "":
        messagebox.showerror("Error", "Enter invoice ID")
        return

    found = False

    for sale in sales:

        if sale["invoice_id"] == search_invoice_id:

            sales.remove(sale)

            messagebox.showinfo("Success", "Sale deleted successfully")

            found = True
            break

    if found == False:
        messagebox.showerror("Error", "Invoice not found")


def clear_fields():

    enter_customer.delete(0, tk.END)
    entery_phone.delete(0, tk.END)
    entery_product_code.delete(0, tk.END)
    entery_quantity.delete(0, tk.END)
    entery_discount.delete(0, tk.END)




root = tk.Tk()
root.title("Mini Shop Management System")
root.geometry("900x700")


tk.Label(root, text="Customer Name").pack()
enter_customer = tk.Entry(root, width=40)
enter_customer.pack()


tk.Label(root, text="Phone Number").pack()
entery_phone = tk.Entry(root, width=40)
entery_phone.pack()


tk.Label(root, text="Product Code").pack()
entery_product_code = tk.Entry(root, width=40)
entery_product_code.pack()


tk.Label(root, text="Quantity").pack()
entery_quantity = tk.Entry(root, width=40)
entery_quantity.pack()


tk.Label(root, text="Discount %").pack()
entery_discount = tk.Entry(root, width=40)
entery_discount.pack()

tk.Label(root, text="Search Invoice ID").pack()
entery_search_invoice = tk.Entry(root, width=40)
entery_search_invoice.pack()

tk.Button(root, text="Add Sale", command=add_sale).pack(pady=5)

tk.Button(root, text="Show All Sales", command=show_all_sales).pack(pady=5)

tk.Button(root, text="Search Sale", command=search_sale).pack(pady=5)

tk.Button(root, text="Update Sale", command=update_sale).pack(pady=5)

tk.Button(root, text="Delete Sale", command=delete_sale).pack(pady=5)


output_text = tk.Text(root, width=100, height=20)
output_text.pack(pady=10)

root.mainloop()


        
