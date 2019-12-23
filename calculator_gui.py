import tkinter as tk
from functools import partial

#y = mx + b GUI, input m,x,b values to show y
def create_ymxb_gui():
	ymxb_gui = tk.Tk()
	ymxb_gui.title('y = mx + b')

	tk.Label(ymxb_gui, text='m').grid(row=1)
	tk.Label(ymxb_gui, text='x').grid(row=2)
	tk.Label(ymxb_gui, text='b').grid(row=3)

	y = tk.StringVar()
	m = tk.StringVar()
	x = tk.StringVar()
	b = tk.StringVar()

	y_entry = tk.Entry(ymxb_gui,textvariable=y)
	y_entry.grid(row=0,column=1)
	m_entry = tk.Entry(ymxb_gui,textvariable=m)
	m_entry.grid(row=1,column=1)
	x_entry = tk.Entry(ymxb_gui,textvariable=x)
	x_entry.grid(row=2,column=1)
	b_entry = tk.Entry(ymxb_gui,textvariable=b)
	b_entry.grid(row=3,column=1)

	calculate_button = tk.Button(ymxb_gui, text='calculate', 
								 command = partial(calculate_ymxb, m_entry, x_entry, b_entry))
	calculate_button.grid(row=4,column=0)
	return_button = tk.Button(ymxb_gui, text='return',command = ymxb_gui.destroy)
	return_button.grid(row=4,column=1)

	ymxb_gui.mainloop()

#calculating y = mx + b
def calculate_ymxb(m, x, b):
	m = m.get()
	x = x.get()
	b = b.get()
	answer = float(m) * float(x) + float(b)

calculator = tk.Tk()
calculator.title('Calculator')

ymxb_button = tk.Button(calculator, text='y = mx + b', command = create_ymxb_gui)
ymxb_button.pack()

quit_button = tk.Button(calculator, text='QUIT', command = calculator.destroy)
quit_button.pack()

calculator.mainloop()

#TODO: redo app as a class