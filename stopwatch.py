
import tkinter as tk
from datetime import*

counter = 66600
running = False

def counter_label(label):
	def count():
		if running:
			global counter
			if counter==66600:
				display="Starting..."
			else:
				tt = datetime.fromtimestamp(counter)
				string = tt.strftime("%H:%M:%S")
				display=string

			label['text']=display
			label.after(1000, count)
			counter += 1
	count()

def Start(label):
	global running
	running=True
	counter_label(label)
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

def Stop():
	global running
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'	
	running = False

def Reset(label):
	global counter
	counter=66600
	if running==False:
		reset['state']='disabled'
		label['text']='Welcome!'
	else:
		label['text']='Starting...'

r = tk.Tk()
r.title("Stopwatch")
r.minsize(width=250, height=70)
label = tk.Label(r, text="Welcome!", fg="black", font="Roman 75 bold")
label.pack()
f = tk.Frame(r)
start = tk.Button(f, text='Start', width=6, command=lambda:Start(label),font='bold',fg='green')
stop = tk.Button(f, text='Stop',width=6,state='disabled', command=Stop,font='bold',fg='blue')
reset = tk.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label),font='bold',fg='red')
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")
r.mainloop()
