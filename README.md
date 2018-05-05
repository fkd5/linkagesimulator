# linkagesimulator

Simulates the movement of linkages (no more than 10) of a fixed length, connected by either fixed or free joints, that can or cannot rotate, respectively. 
This simulator can be used by students or engineers to demonstrate the possible paths obtained from a series of very simple connections. Fixed joints are used when a rigid connection is needed, such as a buildling structure connection, while free joints allow for rotational degrees of freedom, such as a human elbow. 

The simulator will take in user input from the window: desired number of joints. If the user would like to display a fixed joint, they will input the desired fixed angle of the joint. This fixed angle is relative to the horizontal, counterclockwise of the starting position of the joint. To simulate the potential degrees of motion, the code will rotate the free joints (in the counterclockwise direction) to a random angle. The resulting, final display will be a random orientation of the linkages, limited by certain fixed joints. Previous joint positions remain outlined on the screen to show simulator history. 

Instructions to run code: 
1. Requires Python 2. However, to operate using Python 3, only a slight edit is necessary: change line (3) from Tkinter to tkinter. 
2. Ensure you have downloaded the files: application.py, joint.py. 
3. Run the code "application.py"
