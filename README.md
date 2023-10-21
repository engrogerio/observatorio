flask-video-streaming
=====================

Supporting code for my article [video streaming with Flask](http://blog.miguelgrinberg.com/post/video-streaming-with-flask) and its follow-up [Flask Video Streaming Revisited](http://blog.miguelgrinberg.com/post/flask-video-streaming-revisited).
 
 
Configuring the actions panel on actions.json file:
=============================
 
## Actions can be:
* press - Normal press button:
    Can be set to a specific color or description depending on the status of a specific port.

* toggle - On / Off button.
    Can have a color configured for each of the states.
    The port has to be connected to a relay to turn electric equipments on / off.
    
* indicator - Acts like a light showing the status of an specifig output port.
    The port has to be connected to a sensor suplying either 0V or 3.3V

