## Blinky

[work under process ... ]

### Description 

A full stack web development process tutorial using [Raspberry Pi](https://www.raspberrypi.org/) as a server and hardware controller.
Using [GPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) library, a led light is attached on Raspeberry Pi and controlled through an api,  `BlinkyApi`.

`BlinkyApi` is build with [Flask](http://flask.pocoo.org/) and has a [basic HTTP authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) process 
 and six endpoints:

    1. /api/root/ : List all availiable endpoints
    2. /api/led/<pin>/set/<state>/: Set led state on/off
    3. /api/led/status/: Led current status (ON or OFF)
    4. /api/login/: Authenticate and Login user 
    5. /api/logout/: Logout user 
    

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
  3. Other:  Stand alone `Python` Script to demonstrate `Rpi.GPIO` library
             && other support files
  
