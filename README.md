# trackGenerator
Drone racing track generator based on python, math and telegram bot

Trying to implement automatic generation of a drone racing track using python.
The idea is that first of all we get number of gates and flags. Then we have a function 
of n variables which we need to optimize; 
F(x1, ... , xn) = hardness of track, where xi - element. We will need to optimize gates
and flag usage and hit the aimed harness of track, which will be defined by user.

The actual track generation algorithm will be discussed latter, after I finish the 
optimization of hardness and elements usage problem ...
