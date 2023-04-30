This is a tool I designed to take input from the PigmentSaveFile and turn 
all the codes in there into a class object

The object is then added into a dictionary to be called on wherever it is at
I used regular expressions to navigate and change the code, and also used
wxPython to create my own UI for the note system.

To use the program - You first select what tab you want to use

Find - find the code you type into the box

Create - creates a NEW code, must have a code typed into the code box
You only need to specifiy the code, everything else can be left blank
hit the save button when ready to save

Edit - Edits the code you have typed into the code box
if you just type the code and press enter, it will show the info on the side panel
when you have editted the value you want, you hit the edit button to save your changes

I did start to create a config file to change different attributes of the UI but
decided against it due to time restraints. Will most likely add when I get more time