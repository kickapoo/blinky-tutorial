## Blinky

[work under process ... ]

### Description 

A full stack web development process tutorial using [Raspberry Pi](https://www.raspberrypi.org/) as a server and hardware controller.
Using [GPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) library, a led light is attached on Raspeberry Pi and controlled through an api,  `BlinkyApi`.

`BlinkyApi` is build with [Flask](http://flask.pocoo.org/) and has a [basic HTTP authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) process 
 and six endpoints:

    1. /api/root/ : List all availiable endpoints
    2. /api/led/pin/on/: Set led attached on 'pin' number, ON
    3. /api/led/pin/off/: Set led attached on 'pin' number, OFF
    4. /api/led/status/: Led current status (ON or OFF)
    5. /api/login/: Authenticate and Login user 
    6. /api/logout/: Logout user 
    

On top of the `BlinkyApi`, [User Interface (UI)](https://en.wikipedia.org/wiki/User_interface) is handled 
by `BlinkyApp` build with [AngularJs](https://angularjs.org/) framework.
`BlinkyApp` features are:

    1. User Authentication, 
       User can login/logout (Not Register).
       
    2. User can set up his Raspberry Pi connection,
       A form with fields that saves user Raspberry Pi IP address, Led pin number.
       
    3. User can set on/off led,
       A button that displays the next action i.e. if led is "ON", display a button "OFF" and vise versa.


### Folder Structure 

Repo has the following structure:

  1. RaspServer: Configuration files for [Nginx](http://nginx.org/), [supervisor](http://supervisord.org/) and [Git](https://git-scm.com/) on Raspberry Pi.
  2. Blinky:  Files for `BlinkyApi` and 'BlinkyApp'.
  3. Others:  Stand alone `Python` Script to demonstrate `Rpi.GPIO` library.
  
