# python-blender-game-engine-scripting
###This repository contains some instructions to build a controller that allow users to control blender objects with Arduino

###To re-implement this system follow the next points:

#### ON BLENDER:

* Clone this repository with `git clone https://github.com/PeriniMatteo/python-blender-game-engine-scripting`

* Open Blender and be sure that there are a cube in the scene

* Set "Game Logic" environment as show in the screenshot

* Set "Blender Game" as rendering motor on the top right

* On the right you have to open the python file `pybge.py`

* Now on the bottom it is possible to create a new controller

* Set this to work with python script as ***module*** and write the name of the called method `pybge.readSer`

* Now it is important to add a sensor that will call the controller. To do that you can use an always True sensors as shown in the screenshot

* Finally You must connect the sensor to the controller with a line

#### ON ARDUINO (UNO)

* Simply upload the sketch on your arduino and connect it at your pc.

 ___It is possible that the serial port isn't the same as mine. You have to fix this in the python script___
 
 
### __HAVE FUN!__
