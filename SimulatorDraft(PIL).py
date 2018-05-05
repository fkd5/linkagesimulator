from jointdraft import Jointdraft 
from PIL import Image, ImageDraw, ImageFont
import math
import random
import time


#constants on the .png size, as well as size of linkages and joints
IMAGE_SIZE = 400
LENGTH = 100
RADIUS = 15


def getjointfromuser():
	'''
	Gets list of joints by user input.

	INPUT: none

	RETURN:
		firstjoint: *joint*
			First joint on linked list of joints.
	'''

	#prevjoint = Null
	#FIRST one not part of while loop
	# get loc and weight
	# set to prevjoint
	#while loop for while user still wants to input joints (input isn't 'stop' or more than 10 joints)
		#get joint location by asking for angle and user some function somewhere
			#prevjoint.findlocfromangle()
		#get joint weight
		# attach to prevjoint
		# printjoints(firstjoint)
	#ask user if they want to attach the first and last joint to make a circle thing



	#make the first Joint only 
	ID=1

	#for taking in user input
	#loc = input("Location of first joint:")
	#weight = input("Type of joint 1 = fixed in position, not rotation; 0 = completely fixed)):")

	#properties of the first joint
	loc = (IMAGE_SIZE*.75, IMAGE_SIZE*.75)
	weight = 0
	startjoint=Jointdraft(ID, loc, weight=weight)

	#create a list of joints
	jnt_list=[]
	jnt_list.append(startjoint)

	end = 0 #calls end to the user input
	IDnum=2 #starting ID number

	#starting angle, reandom, for demonstration purpsoes
	angle = 45

	#to print 4 joints
	numberofjoints = 4
	while IDnum < numberofjoints+1 and end == 0:
		current_joint = jnt_list[-1]

		#taking in user input
		#angle = input("Angle (relative to last link) in CCW direction:")
		#local = tuple(int(a) for a in loc.split(","))

		if angle == "END":
			end = 1
			break

		#random weight, for demonstration purposes
		weight = 1

		#taking in user input
		#weight = input("Type of joint (1 = fixed in position, not rotation; 0 = completely fixed)):")

		#user can input END when they are done inputting information

		if weight == "END":
			end = 1
			break

		else: 
			#calculate the location of the next joint based on the angle and the length of the linkage
			a = LENGTH * math.cos(math.radians(angle)) + current_joint.location[0]
			b = LENGTH * -math.sin(math.radians(angle)) + current_joint.location[1]
			local = (a, b)

			#defin the next joint
			nextjoint = Jointdraft(IDnum, local , weight=weight, angle=angle)

			#create the link between the joints
			current_joint.suc = nextjoint
			nextjoint.pred = current_joint

			jnt_list.append(nextjoint)

			IDnum += 1 #go onto the next ID number

			printjoints(jnt_list)

		angle = random.randint(0, 360) #next random angle

	return jnt_list # list of joints


def printbackground():
	'''
	Print background. Have cool looking blue or red background with time counter in corner and maybe a
	frame thing or a pattern in the background.


	'''
	length = 1000

	img = Image.new('RGB', (length, length), color = 'pink')

	font = ImageFont.truetype("Verdana.ttf", 25)
	d = ImageDraw.Draw(img)
	d.text((length*.37,0), "LINKAGE SIMULATOR", font=font, fill=(255, 255, 255))
	img.save('View_Simulator.png')
	#img.close()

	pass

def printjoints(alljoints):

	'''

	Prints all the joints, by taking in the first joint and then referencing all the succeeding joints

	A single call to printjoint will print the current joint as well as the previous one. 

	'''

	for i in alljoints:
		printjoint(i)

def printjoint(joint):

	'''
	Print joints to file with links and ID numbers.  Joints in black to white depending on weight.
	Links in between joints.  ID numbers next to joints (or inside the joints in strong color).

	Prints a single joint, as well as the link connecting it to the previous joint. 
	'''

	#radius of circle
	radius = RADIUS

	img = Image.open('View_Simulator.png')
	d = ImageDraw.Draw(img)

	#draw current joing
	#calculate center of current joint
	cent_x = joint.location[0]
	cent_y = joint.location[1]

	#draw the current joint
	weight_curr = joint.weight

	newcolor=255*int(weight_curr)

	d.ellipse((cent_x - radius, cent_y - radius, cent_x + radius, cent_y + radius), fill = 0, outline = 'black')
	font = ImageFont.truetype("Verdana.ttf", 10)
	d.text((cent_x-3, cent_y), str(joint.ID), font=font, fill=(255, 255, 255))

	if joint.pred != None:

		#center of previous joint
		cent_x_p = joint.pred.location[0]
		cent_y_p = joint.pred.location[1]

	#draw the line from the previous joint. 
		d.line([(cent_x, cent_y), (cent_x_p, cent_y_p)], fill='grey', width = 3) 

	img.save('View_Simulator.png')

def applymomentum(joint, listofjoints):
	'''

	applies rotation to the joints that are fixed, based on a random angle

	'''
	rand_angle = random.randint(0, 360)

	original=joint.angle

	for i in range(0, rand_angle, 5):
		#moves joints by 5 degeres 
		joint.angle = original + i
		time.sleep(.25)
		counterjoint = joint

		while counterjoint.suc != None:
			counterjoint.findnextpos() #updates joint position based on moved angle
			counterjoint = counterjoint.suc

		#re-prints the background
		printbackground()
		#prints the joints, in the updated position
		printjoints(listofjoints)


if __name__ == "__main__":
	printbackground()
	joint = getjointfromuser() #obtains joint positions - from code, for demonstration purposes
	printjoints(joint)

	for j in joint: 
		applymomentum(j, joint) #apply angle change
		printbackground()
		printjoints(joint)
		time.sleep(.5) #time pause


