import tkinter as tk
import RPi.GPIO as GPIO

pin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

def turn_on():
    canvas.itemconfig(circle, fill="red")
    GPIO.output(pin, GPIO.HIGH)

def turn_off():
    canvas.itemconfig(circle, fill="gray")
    GPIO.output(pin, GPIO.LOW)

window = tk.Tk()
window.title("LED Control")
window.geometry("600x400")

# Label
label = tk.Label(window, text="LED", font=("Arial", 24))
label.pack(pady=20)

# Circle image
canvas = tk.Canvas(window, width=100, height=100, highlightthickness=0, bg=window.cget("bg"))
canvas.pack()
circle = canvas.create_oval(10, 10, 90, 90, fill="gray")

# Buttons
on_button = tk.Button(window, text="ON", command=turn_on, font=("Arial", 14))
on_button.pack(pady=10)
off_button = tk.Button(window, text="OFF", command=turn_off, font=("Arial", 14))
off_button.pack(pady=10)

window.mainloop()
