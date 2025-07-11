import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time)  # Call this function again after 1 second

# Create GUI window
root = tk.Tk()
root.title("🕒 Digital Clock")
root.geometry("300x100")
root.configure(bg="black")

# Create a label to show time
clock_label = tk.Label(root, font=('Helvetica', 40), fg='cyan', bg='black')
clock_label.pack(expand=True)

# Start the clock update loop
update_time()

# Keep the window running
root.mainloop()
