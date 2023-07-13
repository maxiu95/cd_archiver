I'm a big fan of collecting CDs and as my 
collection grows I find myself in the 
situation of forgetting what I have already 
bought and what I haven't. 

To solve this problem I have created an 
archiving program that allows me to update 
and keep in touch with my ever growing 
collection. 

I have made two iterations of the same 
program. One that runs completely from the 
command line utilising command line 
arguements for efficiency and speed, as 
well as a GUI version built using the 
Tkinter library for more ease of use.Both 
share the same functionality and can 
interact with each other, accessing the same 
data. 

The funtions included are as follows:

CREATE- while the command line app does this 
automatically (no need to call the function)  
when no CSV file is found, the 
GUI app has a button that will create one 
for you.
 
WRITE- this allows the user to update their 
archive as it writes directly to the archive 
CSV.

READ- this function will print your whole 
collection to the screen organised 
alphabetically by artist and album.

FIND- not sure if you've bought that one 
already? Find will search through the CSV 
file for the artist or album and grab all 
instances for you. If nothing comes up, 
you're free to buy!

SHUFFLE- ever been unsure what to listen to 
next? Shuffle will select an album at random 
from your archive for you.


The command line iteration utilises command 
line arguements to call each function. Just 
add the name of the function after the 
program name to call it. 
python cd_archiver.py <function name>


Not a CD collector yourself? The code can be 
easily modified to fit your collector needs 
be it books, games etc etc.
