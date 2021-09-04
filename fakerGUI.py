import faker
from tkinter import *

root = Tk()
fake = faker.Faker()
name = fake.name()


Label(root, text=name).pack()
Button(root, text='Clip', command=lambda:root.clipboard_append(name)).pack()
Button(root, text='New', command=lambda:name).pack()


root.mainloop()