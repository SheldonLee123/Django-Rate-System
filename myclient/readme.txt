register
login http://sc16x2llxy.pythonanywhere.com/login/
logout
list
view

average professor_id module_code 
average JE1 CD1

rate professor_id module_code year semester rating(1-5)
rate JE1 CD1 2018 2 5

quit

admin site 
http://sc16x2llxy.pythonanywhere.com/admin/
username: ammar
passwoed: 1qa1qa1qa
``````````````````````````````````````````````````````````````````````````````````````````````````
register
This is used to allow a user to register to the service using a username, email and a password. When the command is invoked, the program prompts the user to enter the username, email, and password of the new user. The syntax for this command is:
register

login
This command is used to log in to the service. The syntax for this command is:
login http://sc16x2llxy.pythonanywhere.com/login/

logout
This causes the user to logout from the current session. The syntax for this command is:
logout

list
This is used to view a list of all module instances and the professor(s) teaching each of them (Option 1 above). The syntax for this command is:
list

view
This command is used to view the rating of all professors (Option 2 above). The syntax for this command is:
view

average
This command is used to view the average rating of a certain professor in a certain module (Option 3 above). The syntax of the command is: 
average professor_id module_code 
where:
professor_id is the unique id of a professor, and
module_code is the code of a module.

rate
This is used to rate the teaching of a certain professor in a certain module instance (Option 4 above).
It has the following syntax:
rate professor_id module_code year semester rating
where:
professor_id is the unique id of a professor, e.g. JE1,
module_code is the code of a module, e.g. CD1,
year is a teaching year, e.g. 2018,
semester is a semester number, e.g. 2, and
rating is a numerical value between 1-5.

quit 
type quit to exit the programme