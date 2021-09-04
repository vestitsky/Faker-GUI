import faker
from tkinter import *

def tkFaker():
    def addToClip():
        root.clipboard_clear()
        root.clipboard_append(name)

    def update():
        root.destroy()
        tkFaker()

    root = Tk()
    root.geometry("350x150+220+80")
    fake = faker.Faker()
    name = fake.name()
    Label(root, text=name).grid(row=0,column=0)
    Button(root, text='Clip', command=addToClip).grid(row=0,column=1)
    Button(root, text='Reboot', command=update).grid(row=1)

    root.mainloop()

tkFaker()