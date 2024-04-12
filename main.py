from tkinter import ttk

import tkinter as tk

import sqlite3

def refresh_window():
    for i in tree.get_children():
         tree.delete(i)
    root.update()
    #tree.delete()
    con1 = sqlite3.connect("\\\\srv\\NEW\\script\\baza.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM patients  ORDER BY time")
    rows = cur1.fetchall()    
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    con1.close()
    root.after(3000, refresh_window)


def View():
    con1 = sqlite3.connect("\\\\srv\\NEW\\script\\baza.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM patients ORDER BY time")
    rows = cur1.fetchall()    
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    con1.close()



# инициализация Tkinter


root = tk.Tk()
root.title("Электронная очередь ГБУЗ МО «НИКИ детства МЗ МО»")
root.geometry("700x700+200+200")
icon = tk.PhotoImage(file = "faviconV2.png")
root.iconphoto(False, icon)
root.configure(bg="white")
tree = ttk.Treeview(root, column=("Время", "ФИО"), show='headings')
tree.column("Время", anchor=tk.CENTER, minwidth=50, width=300, stretch="NO")
tree.heading("Время", text="Время")
tree.column("ФИО", anchor=tk.CENTER)
tree.heading("ФИО", text="Пациент")
style = ttk.Style()
style.configure("Treeview", font=(None, 30), rowheight=60)
style.configure("Treeview.Heading", font=('Helvetica', 30))
tree.pack(fill=tk.BOTH, expand=True)

View()
while True:
    root.after(3000, refresh_window)
    root.mainloop()

root.mainloop()
