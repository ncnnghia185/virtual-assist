from tkinter import *
from PIL import Image, ImageTk
import action
import speech_to_text
# Ask function
def ask():
    user_value = speech_to_text.speech_to_text()
    bot_value = action.action(user_value)
    text.insert(END, 'User --->'+user_value+"\n")
    if bot_value != None:
        text.insert(END, 'Bot <---'+str(bot_value)+"\n")
    if bot_value =="Shut Down":
        main.destroy()

# Send function
def send():
    user_value = entry.get()  # Lấy nội dung nhập bởi người dùng từ entry
    bot_value = action.action(user_value)
    text.insert(END, 'User ---> ' + user_value + "\n")
    if bot_value is not None:
        text.insert(END, 'Bot <--- ' + str(bot_value) + "\n")
    if bot_value == "Shut Down":
        main.destroy()

# Delete function
def delete():
    text.delete('1.0', "end")

main = Tk()
main.title("Assistant")
main.geometry("500x675")
main.resizable(FALSE, FALSE)
main.config(bg="#FF9999")

# Frame
frame = LabelFrame(main, padx=100, pady=7, borderwidth=3, relief="raised", bg="#FF9999")
frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Text Label
text_label = Label(frame, text="Assistant", bg="#FF9969", fg="black", font=("Arial", 15, "bold"))
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
image = ImageTk.PhotoImage(Image.open("images/assistant.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# Text Widget
text = Text(main, font=("Arial", 15, "bold"), bg="#FFFFCC")
text.place(x=100, y=200, width=375, height=150)

# Entry Widget
entry = Entry(main, justify=CENTER)
entry.place(x=100, y=400, width=375, height=40)

# Button 1
btn1 = Button(main, text="ASK", bg="#FF9955", padx=40, pady=16, borderwidth=2, relief=SOLID, command=ask)
btn1.place(x=70, y=575)

# Button 2
btn2 = Button(main, text="SEND", bg="#FF9955", padx=40, pady=16, borderwidth=2, relief=SOLID, command=send)
btn2.place(x=225, y=575)

# Button 3
btn3 = Button(main, text="DELETE", bg="#FF9955", padx=40, pady=16, borderwidth=2, relief=SOLID, command=delete)
btn3.place(x=400, y=575)

main.mainloop()
