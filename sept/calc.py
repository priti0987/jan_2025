# import tkinter as tk
# from tkinter import messagebox
#  # function for maximum number
# def find_biggest():
# # Try and except statement is used
#  # for handling the errors like zero
#  # division error etc.
#  # Put that code inside the try block
#  # which may generate the error
#  # if error occurs during code execution
#  # then it will be caught
#  # and handle by the except block
#  # if the user try to enter invalid number
#  # error message will show
# try:
#     num1 = float(entry1.get()) # Get first number
#     num2 = float(entry2.get()) # Get second number
# biggest = max(num1, num2) # find maximum number between
#  2 numbers
#  messagebox.showinfo("Result", f"The biggest number
#  between {num1} and {num2} is: {biggest}")
#  except ValueError:
# messagebox.showerror("Error", "Please enter valid numbers.")
#  # function for minimum number
#  def find_smallest():
#  try:
#  num1 = float(entry1.get())
#  num2 = float(entry2.get())
# smallest = min(num1, num2)
#  messagebox.showinfo("Result", f"The smallest number
#  between {num1} and {num2} is: {smallest}")
#  except ValueError:
#  messagebox.showerror("Error", "Please enter valid numbers.")
#  # function for addition
#  def calculate_sum():
#  try:
#  num1 = float(entry1.get())
#  num2 = float(entry2.get())
# sum_nums = num1 + num2
#  messagebox.showinfo("Result", f"The sum of {num1} and
#  {num2} is: {sum_nums}")
#  except ValueError:
#  messagebox.showerror("Error", "Please enter valid numbers.")
#  # function for subtraction
# def calculate_diff():
#  try:
#  num1 = float(entry1.get())
#  num2 = float(entry2.get())
# diff_nums = num1 - num2
#  messagebox.showinfo("Result", f"The difference   between
#  {num1} and {num2} is: {diff_nums}")
#  except ValueError:
#  messagebox.showerror("Error", "Please enter valid numbers.")
#  # function for multiplication
#  def calculate_product():
#  try:
# num1 = float(entry1.get())
#  num2 = float(entry2.get())
# product = num1 * num2
#  messagebox.showinfo("Result", f"The product of {num1} and
#  {num2} is: {product}")
#  except ValueError:
#  messagebox.showerror("Error", "Please enter valid numbers.")
#  # function for division
#  def calculate_div():
#  try:
#  num1 = float(entry1.get())
#  num2 = float(entry2.get())
#  # Check second number is equal to zero
#  # if it is, then value error raised
#  # it it is not, then calculate the quotient
#  if num2 == 0:
#  raise ValueError("Division by zero is not allowed.")
# div_nums = num1 / num2
#  messagebox.showinfo("Result", f"The division of {num1} and
#  {num2} is: {div_nums}")
#  except ValueError as e:
#  messagebox.showerror("Error", str(e))
#  # function for modulo operation
#  def calculate_modulo():
#  try:
#  num1 = float(entry1.get())
#  num2 = float(entry2.get())
# mod_nums = num1 % num2
#  messagebox.showinfo("Result", f"The remainder of {num1}
#  and {num2} is: {mod_nums}")
#  except ValueError:
#  messagebox.showerror("Error", "Please enter valid numbers.")
#  # Create the main window
#  root = tk.Tk()
# root.title("Number Operations")
#  # Create Label for Project title
#  # Apply font style to title label
#  font_bold = ("Helvetica",18,"bold")
#  label_title = tk.Label(root, text="Simple Math Operations Calculator")
#  label_title.config(fg="white",bg="Dark Green",font=font_bold)
#  label_title.grid(row=0, columnspan=3, padx=5, pady=5)
#  # Create and place widgets
#  label1 = tk.Label(root, text="Enter first number:")
#  label1.config(font=("Arial",10,"bold"))
#  label1.grid(row=1, column=1, padx=5, pady=5)
#  entry1 = tk.Entry(root)
#  entry1.grid(row=1, column=2, padx=5, pady=5)
#  label2 = tk.Label(root, text="Enter second number:")
#  label2.config(font=("Arial",10,"bold"))
#  label2.grid(row=2, column=1, padx=5, pady=5)
#  entry2 = tk.Entry(root)
#  entry2.grid(row=2, column=2, padx=5, pady=5)
#  biggest_button = tk.Button(root, text="Find Biggest",
#  command=find_biggest)
#  biggest_button.config(font=("Helvetica",10,"bold"))
#  biggest_button.grid(row=3, column=1, padx=5, pady=5)
#  smallest_button = tk.Button(root, text="Find smallest",
#  command=find_smallest)
#  smallest_button.config(font=("Helvetica",10,"bold"))
#  smallest_button.grid(row=3, column=2, padx=5, pady=5)
#  # Create button frame
#  button_frame = tk.Frame(root)
#  button_frame.grid(row=4, column=1, columnspan=2, padx=5,
#  pady=5)
#  # Create buttons inside the button frame
#  # Create sum button to find addition of two numbers
#  sum_button = tk.Button(button_frame, text="Sum",
#  command=calculate_sum)
# sum_button.grid(row=0, column=0, padx=5, pady=5)
#  sum_button.config(font=("Helvetica", 10, "bold"))
#  # Create diff button to find difference between  two numbers
#  diff_button = tk.Button(button_frame, text="Difference",
#  command=calculate_diff)
#  diff_button.grid(row=0, column=1, padx=5, pady=5)
#  diff_button.config(font=("Helvetica", 10, "bold"))
#  # Create product button to find product of two numbers
#  product_button = tk.Button(button_frame, text="Product",
#  command=calculate_product)
#  product_button.grid(row=0, column=2, padx=5, pady=5)
#  # the button's text will be displayed in a bold Helvetica font with
#  a size of 10
#  product_button.config(font=("Helvetica", 10, "bold"))
#  # Create div button to find quotient
#  div_button = tk.Button(button_frame, text="Division",
#  command=calculate_div)
#  div_button.grid(row=0, column=3, padx=5, pady=5)
#  div_button.config(font=("Helvetica", 10, "bold"))
#  # Create mod button to find remainder
#  mod_button = tk.Button(button_frame, text="Modulo",
#  command=calculate_modulo)
#  mod_button.grid(row=0, column=4, padx=5, pady=5)
#  mod_button.config(font=("Helvetica", 10, "bold"))
#  # Start the Tkinter event loop
#  root.mainloop()