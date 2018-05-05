from tkinter import *
from joint import Joint
import math
import random
import time

class Application(Frame):
	# Window with simulation of joint movements.

	def createWidgets(self):
		# Set up screen with background and quit button.
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"]   = "red"
		self.QUIT["command"] =  self.quit

		self.QUIT.pack({"side": "left"})

		self.w = Canvas(root, width=IMAGE_SIZE,height=IMAGE_SIZE, bg='green')
		self.w.pack()


	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()


	def getjointfromfile(self, weights):
		'''
		Gets list of joints automatically.

		INPUT:
			weights: *float, list*
				List of fixed angles gathered from user input.  If angle is 'inf', the joint
				is not fixed.

		RETURN:
			jnt_list: *joint, list*
				List of joints which are also in a doubly linked list.
		'''

		ID=0
		jnt_list=[]

		# Initialize joints for each user input in weights
		while ID < len(weights):
			ID = ID + 1

			if weights[ID-1] == float('inf'):
				# Joint is not fixed.  Weight = 0 and angle is random.
				angle = random.randint(0, 360)
				w = 0 
			else:
				# Joint is fixed.  Weight = 1 and angle is given by user input in weights.
				angle = weights[ID-1]
				w = 1

			if ID == 1:
				# The first joint is located in the center of the screen.
				loc = (IMAGE_SIZE*.5, IMAGE_SIZE*.5)
				startjoint=Joint(ID, loc, weight=w)
				jnt_list.append(startjoint)
			else:
				# The location of the nextjoin depends on the location and angle of the last joint.
				current_joint = jnt_list[-1]
				a = LENGTH * math.cos(math.radians(angle)) + current_joint.location[0]
				b = LENGTH * -math.sin(math.radians(angle)) + current_joint.location[1]
				local = (a, b)
				nextjoint = Joint(ID, local , weight=w, angle=angle)
				# Add the nextjoint to a doubly linked list.
				current_joint.suc = nextjoint
				nextjoint.pred = current_joint
				# Add the nextjoin to the list of joints in jnt_list
				jnt_list.append(nextjoint)

		return jnt_list # list of joints

	def printjoints(self, alljoints, color):
		'''
		Prints a list of joints on the screen.

		INPUT:
			alljoints: *joint, list*
				List of joints which are also in a doubly linked list.
			color: *string*
				If 'green', colors will be set to erase joints by coloring them green.
				If 'default' or anything else, colors will be set to draw joints.
		'''

		# Changes default colors to green if color is 'green'.
		C1 = 'black'
		C3 = 'grey'
		if color == 'green':
			C1 = 'green'
			C3 = 'green'

		for joint in alljoints:

			# Print fixed joints in black and free joints in white.
			if joint.weight == 0 and color != 'green':
				C1 = 'white'
			elif joint.weight ==1 and color != 'green':
				C1 = 'black'

			# Radius and location of joint
			radius = RADIUS
			cent_x = joint.location[0]
			cent_y = joint.location[1]

			# Draw joint
			self.w.create_oval(cent_x-radius, cent_y-radius, cent_x+radius, cent_y+radius, fill=C1, tags=str(joint.ID))

			# Draw lines between joints.
			if joint.pred != None:

				# Center of previous joint
				cent_x_p = joint.pred.location[0]
				cent_y_p = joint.pred.location[1]

				# Draw the line from the previous joint. 
				self.w.create_line(cent_x, cent_y, cent_x_p, cent_y_p, fill=C3, width=5)


	def applymomentum(self, joint, listofjoints):
		'''
		Moves joint to new random location and prints movement in small intervals.

		INPUT:
			joint: *joint*
				Joint which will be moved to new random location.
			alljoints: *joint, list*
				List of joints which are also in a doubly linked list.
		'''

		# Move joint by a random angle.
		rand_angle = random.randint(0, 360)

		# Move joint by interval until we reach random angle.
		interval = 5
		original=joint.angle
		for i in range(0, rand_angle, interval):
			joint.angle = original + i
			counterjoint = joint
			# Erase old joints from screen.
			app.printjoints(listofjoints, 'green')
			# Move all successive joints to keep up with the joint we're moving.
			while counterjoint.suc != None:
				counterjoint.findnextpos(interval)
				counterjoint = counterjoint.suc
			# Print new joints to screen.
			app.printjoints(listofjoints, 'default')
			app.update_idletasks()
			app.update()
			# Pause program.
			time.sleep(.01)

# Get joints
def findinputs():
	'''
	Gets list of angles from user input.

	RETURN:
		weights: *float, list*
			List of fixed angles gathered from user input.  If angle is 'inf', the joint
			is not fixed.
		'''

	# Initialize variable names.
	global weights
	counting = Tk()
	label_names=['Joint1', 'Joint2', 'Joint3', 'Joint4', 'Joint5', 'Joint6', 'Joint7', 'Joint8', 'Joint9', 'Joint10']

	J1=Label()
	J2=Label()
	J3=Label()
	J4=Label()
	J5=Label()
	J6=Label()
	J7=Label()
	J8=Label()
	J9=Label()
	J10=Label()

	E1=Entry()
	E2=Entry()
	E3=Entry()
	E4=Entry()
	E5=Entry()
	E6=Entry()
	E7=Entry()
	E8=Entry()
	E9=Entry()
	E10=Entry()

	entry_variables=[E1, E2, E3, E4, E5, E6, E7, E8, E9, E10]
	label_variables=[J1, J2, J3, J4, J5, J6, J7, J8, J9, J10]

	# Instructions for user input on screen.
	firstlabel=Label(counting, text="Input number of joints (max 10). Then, hit CONTINUE.")
	firstlabel.grid(row=0, column=0)
	valueinput=Entry(counting, bd=2)
	valueinput.grid(row=1, column=0)

	weights=[]

	def sum_up():
		# Accepts input for number of joints and deletes lets_count button
		secondlabel=Label(counting, text="If any joints are to be fixed, input the angle for the specific joint. Then, hit GO.")
		secondlabel.grid(row=3, column=0)
		for i in range(0, int(valueinput.get())):
			label_variables[i]=Label(counting, text=label_names[i])
			label_variables[i].grid(row=4+i, column=0)
			entry_variables[i]=Entry(counting, bd=2)
			entry_variables[i].grid(row=4+i, column=1)
		deletebutton(lets_count)


	def checkjoints():
		# Accepts input fixed joint angles, deletes checkfixed button, and closed window.
		global weights
		for i in range(0, int(valueinput.get())):
			# Free joints are assigned weight of 'inf'.
			if str(entry_variables[i].get())=='':
				weights.append(float('inf'))
			# Fixed joints are assigned input value as a float
			else:
				assert str.isdigit(entry_variables[i].get()), "invalid input (number required)"
				weights.append(float(entry_variables[i].get()))
		deletebutton(checkfixed)
		delete()

	def delete():
		counting.destroy()

	def deletebutton(button):
		button.destroy()

# Initialize buttons.
	lets_count = Button(counting, text="CONTINUE", width=9, command=sum_up)
	checkfixed = Button(counting, text="GO", width=9, command=checkjoints)
	lets_count.grid(row=20, columnspan=2)
	checkfixed.grid(row=21, columnspan=2)
	counting.mainloop()
	return weights

# Constants
IMAGE_SIZE = 750
LENGTH = 100
RADIUS = 15

# Get list of weights from user.
weights = findinputs()

# Run simulation
root = Tk()
app = Application(master=root)
joint = app.getjointfromfile(weights)
app.printjoints(joint, 'default')

# Move each free joint to a position determined by a random angle.
for j in joint:
	if j.suc != None and j.weight == 0:
		app.applymomentum(j, joint)

app.mainloop()
root.destroy()