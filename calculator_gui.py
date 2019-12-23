from tkinter import *
from functools import partial

def create_ymxb_gui():
	ymxb_gui = Toplevel()
	ymxb_gui.title('y = mx + b')

	Label(ymxb_gui, text='m').grid(row=2,column=0)
	Label(ymxb_gui, text='x').grid(row=3,column=0)
	Label(ymxb_gui, text='b').grid(row=4,column=0)

	y = StringVar()
	m = StringVar()
	x = StringVar()
	b = StringVar()

	y.set("enter values for m, x, and b")

	Entry(ymxb_gui,textvariable=y).grid(row=1,column=1)
	Entry(ymxb_gui,textvariable=m).grid(row=2,column=1)
	Entry(ymxb_gui,textvariable=x).grid(row=3,column=1)
	Entry(ymxb_gui,textvariable=b).grid(row=4,column=1)

	Button(ymxb_gui, text='calculate', command = partial(calculate_ymxb, m, x, b)).grid(row=6,column=0)
	Button(ymxb_gui, text='return', command = ymxb_gui.destroy).grid(row=6,column=1)

def calculate_ymxb(m, x, b):
	answer = float(m.get()) * float(x.get()) + float(b.get())
	quote = "the y-value to your linear equation is %s" % answer
	answer_gui = Toplevel()
	answer_gui.title("ANSWER")
	t = Text(answer_gui)
	t.grid()
	t.insert(END, quote)
	Button(answer_gui, text='return', command = answer_gui.destroy).grid(row=10)

def main():
	calculator = Tk()
	calculator.title('Calculator')

	Button(calculator, text='y = mx + b', command = create_ymxb_gui).grid(row=0,column=0)

	Button(calculator, text='quit', command = calculator.destroy).grid(row=5,column=5)

	calculator.mainloop()

if __name__ == "__main__":
	main()