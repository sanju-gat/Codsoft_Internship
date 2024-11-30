# Task 2
# Calculstor


import tkinter as tk

inval = ''
def click(item):
	global inval
	inval += item
	disp.set(inval)
def clear():
	global inval
	inval = ''
	disp.set(inval)

def equal():
	global inval
	try:
		disp.set(str(eval(inval)))
	except:
		disp.set('<error>')
	inval = ''

win = tk.Tk()
win.geometry("330x350")
win.title('Calculator')
win.resizable(0,0)

disp = tk.StringVar()

in_frame = tk.Frame(win,width=300,height=100)
in_frame.pack(side = tk.TOP,pady=15,padx=10)

in_field = tk.Entry(in_frame,width = 300,textvariable = disp,justify=tk.RIGHT,font = 'arial 18 bold')
in_field.pack(ipady=20)



B_frame = tk.Frame(win,height=400,width=350)
B_frame.pack()

btn_c = tk.Button(B_frame,text='C',width=30,command = lambda:clear()).grid(row=0,column=0,columnspan=3,ipady=10)
btn_d = tk.Button(B_frame,text=' / ',width=10,command = lambda:click('/')).grid(row=0,column=3,ipady=10)
btn_9 = tk.Button(B_frame,text=' 9 ',width=10,command = lambda:click('9')).grid(row=1,column=0,ipady=10)
btn_8 = tk.Button(B_frame,text=' 8 ',width=10,command = lambda:click('8')).grid(row=1,column=1,ipady=10)
btn_7 = tk.Button(B_frame,text=' 7 ',width=10,command = lambda:click('7')).grid(row=1,column=2,ipady=10)
btn_m = tk.Button(B_frame,text=' * ',width=10,command = lambda:click('*')).grid(row=1,column=3,ipady=10)
btn_6 = tk.Button(B_frame,text=' 6 ',width=10,command = lambda:click('6')).grid(row=2,column=0,ipady=10)
btn_5 = tk.Button(B_frame,text=' 5 ',width=10,command = lambda:click('5')).grid(row=2,column=1,ipady=10)
btn_4 = tk.Button(B_frame,text=' 4 ',width=10,command = lambda:click('4')).grid(row=2,column=2,ipady=10)
btn_a = tk.Button(B_frame,text=' + ',width=10,command = lambda:click('+')).grid(row=2,column=3,ipady=10)
btn_3 = tk.Button(B_frame,text=' 3 ',width=10,command = lambda:click('3')).grid(row=3,column=0,ipady=10)
btn_2 = tk.Button(B_frame,text=' 2 ',width=10,command = lambda:click('2')).grid(row=3,column=1,ipady=10)
btn_1 = tk.Button(B_frame,text=' 1 ',width=10,command = lambda:click('1')).grid(row=3,column=2,ipady=10)
btn_s = tk.Button(B_frame,text=' - ',width=10,command = lambda:click('-')).grid(row=3,column=3,ipady=10)
btn_t = tk.Button(B_frame,text=' x10 ',width=10,command = lambda:click('*10')).grid(row=4,column=0,ipady=10)
btn_0 = tk.Button(B_frame,text=' 0 ',width=10,command = lambda:click('0')).grid(row=4,column=1,ipady=10)
btn_dt = tk.Button(B_frame,text=' . ',width=10,command = lambda:click('.')).grid(row=4,column=2,ipady=10)
btn_e = tk.Button(B_frame,text=' = ',width=10,command = lambda:equal()).grid(row=4,column=3,ipady=10)


win.mainloop()
