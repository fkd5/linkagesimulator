# linkagesimulator

## Our goal: 

Our goal is to simulate the movement of linkages (no more than 10) of a fixed length, connected by either fixed or free joints, that can or cannot rotate, respectively. 

This simulator can be used by students or engineers to demonstrate the possible paths obtained from a series of very simple connections. Fixed joints are used when a rigid connection is needed, such as a buildling structure connection, while free joints allow for rotational degrees of freedom, such as a human elbow. 

## Our submission: 

We are submitting two different coding methods. 

SimulatorDraft(PIL).py was our first attempt for displaying our simulator. However, we soon realized the low potential of PIL in terms of being able to constantly update a picture. Therefore, we switched to Tkinter, demonstrated by the Simulator(tkinter).py file. 

### To see the difference between two different graphics tools: 

Since this code was used purely as a demonstrator and as an intermediary step in this final project, it does not take in user input. Instead, we have selected the number, position, and movement of the joints automatically in the code. This code is used purely as a demonstration. 

1. Requires Python 2. However, to operate using Python 3, only a slight edit is necessary: change line (3) from Tkinter to tkinter. 
2. Ensure you have downloaded the files: application.py, joint.py, run.py.  
3. Run "simulator(PIL).py". Open the "View_Simulator.png" file that is created. Note how slow the code runs. We were unable to run the code any faster without the print statements not being able to catch up to our short time delays. 
4. Run "simulator(Tkinter).py". Note how much faster the code runs. Also note that the printing does slow down with higher numbers of links, as well as the code runs for a longer period of time. 

### To see the final simulator: 

The simulator takes in user input from the display window: desired number of joints. If the user would like to display a fixed joint, they will input the desired fixed angle of the joint. This fixed angle is relative to the horizontal, counterclockwise of the starting position of the joint. To simulate the potential degrees of motion, the code will rotate the free joints (in the counterclockwise direction) to a random angle. The resulting, final display will be a random orientation of the linkages, limited by certain fixed joints. Previous joint positions remain outlined on the screen to show simulator history. 

Instructions to run code: 
1. Requires Python 2. However, to operate using Python 3, only a slight edit is necessary: change line (3) from Tkinter to tkinter. 
2. Ensure you have downloaded the files: application.py, joint.py. 
3. Run the code "application.py"

## Other notes

The branche called "Fiona" has additional code that is not related to our final project, but will be kept for future work. 

