import math
from tkinter import *


from fpdf import FPDF

# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

pdf.set_font("Arial", size=12)
TYPING_TIME = 1
time_loop = None

window = Tk()
window.config(padx=20, pady=20, bg="#f7f5dd")
window.title("Don't stop writing")

a = []


def counter(writing_secs):
    count_min = math.floor(writing_secs / 60)
    count_sec = writing_secs % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    count_timer = f"{count_min}:{count_sec}"
    timer_text.config(text=count_timer)

    if writing_secs > 0:
        global time_loop
        time_loop = window.after(1000, counter, writing_secs - 1)

    if writing_secs % 5 == 0:
        b = typing_space.get(1.0, "end")
        a.append(b)
        if len(a) == 2:
            print(a)
            same = a[0] == a[1]
            if same:
                typing_space.delete(1.0, "end")
                stop_time()
            elif writing_secs == 0:
                stop_time()
            a.pop(0)


def start_time():
    typing_space.config(state="normal")
    writing_secs = TYPING_TIME * 60
    counter(writing_secs)


def stop_time():
    window.after_cancel(time_loop)
    print(a[1])
    pdf.cell(200, txt=a[1])
    pdf_file = pdf.output("result.pdf")




welcome_label = Label(text="Start typing.\n"
                           "You have 5 minutes to write down your thoughts.\n"
                           "Stop for 5 seconds and you lose everything you've written", bg="#f7f5dd",
                      font=("Courier", 20))
welcome_label.grid(row=0, column=0)

enter_button = Button(text="Start typing", bg="#9bdeac", font=("Courier", 20, "bold"), command=start_time)
enter_button.grid(row=1, column=0)

timer_text = Label(text="5:00", font=("Courier", 20, "bold"), foreground="red", background="white")
timer_text.grid(row=2, column=0, padx=10, pady=10)

typing_space = Text(window, font=("Calibri", "13"), height=10, state="disabled")
typing_space.grid(row=3, column=0, padx=10, pady=10)

window.mainloop()
