
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\jarri\OneDrive\Escritorio\Gestion de monitores\Informacion de monitorias\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1203x876")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 876,
    width = 1203,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    350.9999999999999,
    251.0,
    anchor="nw",
    text="Gestion de monitores ",
    fill="#000000",
    font=("Newsreader Regular", 48 * -1)
)

canvas.create_rectangle(
    155.9999999999999,
    307.0,
    965.9999999999999,
    309.00006103515625,
    fill="#E6E6E6",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    550.9999999999999,
    150.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=366.9999999999999,
    y=781.0,
    width=404.0,
    height=95.0
)

canvas.create_text(
    448.9999999999999,
    752.0,
    anchor="nw",
    text="PROMEDIO DE SEMESTRE",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    326.9999999999999,
    752.0,
    844.9999999999999,
    753.0,
    fill="#000000",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    597.4999999999999,
    732.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=381.9999999999999,
    y=718.0,
    width=431.0,
    height=27.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    346.9999999999999,
    732.0,
    image=image_image_2
)

canvas.create_text(
    458.9999999999999,
    667.0,
    anchor="nw",
    text="MATERIA DE MONITORIA",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    326.9999999999999,
    662.0,
    844.9999999999999,
    663.0,
    fill="#000000",
    outline="")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    597.4999999999999,
    641.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=381.9999999999999,
    y=627.0,
    width=431.0,
    height=27.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    343.9999999999999,
    643.0,
    image=image_image_3
)

canvas.create_text(
    528.9999999999999,
    580.0,
    anchor="nw",
    text="SEMESTRE",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    326.9999999999999,
    575.0,
    844.9999999999999,
    576.0,
    fill="#000000",
    outline="")

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    597.4999999999999,
    557.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=381.9999999999999,
    y=543.0,
    width=431.0,
    height=27.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    343.9999999999999,
    558.0,
    image=image_image_4
)

canvas.create_text(
    520.9999999999999,
    406.0,
    anchor="nw",
    text="FACULTAD",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    318.9999999999999,
    398.0,
    836.9999999999999,
    399.0,
    fill="#000000",
    outline="")

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    589.4999999999999,
    381.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=373.9999999999999,
    y=368.0,
    width=431.0,
    height=25.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    343.9999999999999,
    380.0,
    image=image_image_5
)

canvas.create_text(
    528.9999999999999,
    504.0,
    anchor="nw",
    text="PREGRADO",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    318.9999999999999,
    490.0,
    836.9999999999999,
    491.0,
    fill="#000000",
    outline="")

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    597.4999999999999,
    465.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=381.9999999999999,
    y=451.0,
    width=431.0,
    height=27.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    343.9999999999999,
    466.0,
    image=image_image_6
)

canvas.create_text(
    451.9999999999999,
    333.0,
    anchor="nw",
    text="Informacion para monitorias",
    fill="#000000",
    font=("NewsreaderRoman Regular", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
