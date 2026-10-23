# AI Patrol State

Any AI can use a patrol waypoint system to move around a path while searching for possible targets. For this, go to the main AI prefab parent and in the component “Add Patrol System To AI”, press the button “Add Patrol System To AI”.

A new object will be added to the scene, called “AI Waypoint Patrol”:

By default, it has a few waypoints configured and you can see that transform gizmo are shown in each waypoint, which is made to allow to move each waypoint separately without the need to select one by one and move them.

You can disable this gizmo on the option “Use Free Handle” in the component “AI Waypoint

Patrol”:

So the waypoint in the scene will only show the path itself and its direction.

Also, it is recommended that each time that waypoints are added or placed in a new position, press the button “Adjust To Surface”:

So all the waypoints are adjusted to the ground where they are located, in order to manage the navigation values properly, looking like this after pressing the button, in this lateral view of the scene:

You can edit the waypoint system, to add or remove more points or new zones to walk, so the AI can have more than one zone were to move around. Of course, you can just use a single patrol and set as many points as you need.

Once the waypoints are configured, go to the “AI Patrol System” component, and apply the settings that you prefer, like the speed of the AI while moving on the waypoints, the lower the value, the slower the character will move, changing from run by default to walk instead through them.

Also, you can also configure that the AI changes randomly to another waypoint, instead of moving through them in order, which is what they do by default.
