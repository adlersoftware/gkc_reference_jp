# Configure Input on Vehicles

Configure the Input Manager for various Vehicles.

The customization of input on vehicles is almost exact to the process for the settings of input in the **Player Input Manager** component in the player.

First of all, you basically need to add or configure the input actions on the **Input Manager** component of GKC.

It is recommended to add a new input action category for each new vehicle if the new one that you want to add has a different input or special actions not present in the previous one. Of course, you can add the new actions in a previous category of vehicle input as well.

Once you have the new actions or the new category added to configure a new vehicle control, go to any of the GKC vehicles and in the main object itself, go to the component called **Input Action Manager**, more specifically, in the **Multi Axes List.**

If you added a new input category in Input Manager or just added or modified some input actions, press the button “Update Input List”:

Now, in the field “Axes” below that button, select the input category for this vehicle, in the case you added a new one. You will see a list with all the input categories configured in Input Manager, so select one of them. If you just added or modified input actions, no need to select a different input category in that field:

Now, inside Axes, press the button **Update Input List.**

And now, select each input that is on this list, and remove, edit or add new input actions based on what you need. On each input action, you only need to select the input action name on the field “Axes” according to the name of the input from Input Manager, and the type of press to use to activate this action (down, hold. or up).

Finally, configure or add a new event in the **Button Event**, drop the object with the component that has the function to activate, and configure the function itself on the event field. You can set as many events as you need on each input action:

Don’t forget to set a name for the action in the field “**Action Name**” as that name will be shown in the in-game control panel for that vehicle (it can be opened with N by default, and it can be disabled as well, to not be used).

And the same applies to each of the rest of the actions. Make sure to press the buttons to update the input action list if you add/remove/modify the input action on the Input Manager of GKC for the vehicle that you are going to use.
