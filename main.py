from tkinter import *
import time

# -----------------------------------------------------------------------------------------
# LOGIC
# -----------------------------------------------------------------------------------------

starting_time = 0
user_text = ""

timer = None


def start_calculating(event):
    global starting_time, timer

    if starting_time == 0:
        starting_time = time.localtime().tm_sec

    if timer is not None:
        window.after_cancel(timer)

    if event.char:
        timer = window.after(3000, reset_app)

    starting_time = time.localtime().tm_sec
    return


def reset_app():
    global starting_time, timer
    starting_time = 0
    typing_area.delete('1.0', 'end')
    window.after_cancel(timer)


# -----------------------------------------------------------------------------------------
# UI SETUP
# -----------------------------------------------------------------------------------------

BORDER = "#3C2C3E"
FG = 'khaki'
BG = "#4B5D67"

FONT_FAMILY1 = 'Calibri'
FONT_FAMILY2 = 'Helvetica'

FONT_SIZE1 = 14
FONT_SIZE2 = 18
FONT_SIZE3 = 24

FONT_STYLE1 = 'normal'
FONT_STYLE2 = 'italic'
FONT_STYLE3 = 'bold'

PARA_FONT = (FONT_FAMILY1, FONT_SIZE1, FONT_STYLE3)
PARA_FONT2 = (FONT_FAMILY1, 12, FONT_STYLE2)
HEAD_FONT = (FONT_FAMILY2, FONT_SIZE3, FONT_STYLE1)

heading = "WRITE WITH MAGICAL INK"
instruction = "If you don't press any key for 3 seconds, the text you have written will disappear"

window = Tk()
window.minsize(width=1030, height=520)
window.title('Disappearing Text Desktop App')
window.config(bg=BG)

heading = Label(text=heading, font=HEAD_FONT, bg=BG, fg=FG, padx=10, pady=10)
instruction = Label(text=instruction, font=PARA_FONT2,
                    fg=FG, bg=BG, pady=10)
typing_area = Text(font=PARA_FONT, bg=BG, fg=FG, width=100, height=15, wrap='w',
                   highlightcolor=BORDER, highlightthickness=4, highlightbackground=BORDER,
                   padx=5, pady=5)
typing_area.bind('<KeyPress>', start_calculating)

heading.pack()
instruction.pack()
typing_area.pack()

window.mainloop()

