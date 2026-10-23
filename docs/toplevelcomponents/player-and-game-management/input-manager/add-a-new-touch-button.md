# Add a New Touch Button

For this process, you can either configure a new input action or assign a touch button to an input action already configured.

For this, go to the input manager component (from GKC) and press the button **Select Main Touch Button Panel On Editor**.

Then, select the panel where you want to add a new touch button, or create a new panel and add the new touch button there. You can enable the touch button panel (and disable the rest of the touch panels, so you can see better the main panel that you are configuring) and place the new button where you need it on the screen, along with customizing its size, texture, color, etc...

Now, press the button **Get Touch Button List**. You will see that the main touch panel has been disabled again to hide it on the screen until it is used in-game:

From there, in each input action, you can select the category of the touch button panel and the button name. Now that a new button has been added, this will also appear when selecting the category of the touch buttons where this new button has been added (the category is the main panel where the touch button has been added, in the above example, it would be the

**Main Controls** category, which is the name of the panel itself.

Each panel is like the category for regular controls, weapons, powers, examine devices, use photo mode, etc… so through event options, you can change the current touch control scheme (you have categories, and you can define control schemes, which are combinations of these touch panels) to combine for example regular controls with weapons and similar.

Back to configure the touch button in a specific action, open the **Multi Axes List** and select the category of input and the action input itself to set the new touch button:

For this example, let’s add a new action and set the new touch button there:

So in the **Touch Panel** field, you select the category of the touch controls where the new touch button was added and the new touch button itself:

And now, that touch button will activate that input on play mode and in build as well. If you assigned that touch button to a previous action, there are no more extra steps. If you added a new action, you only need to follow the steps in the previous part of this doc to set the action events which that button will trigger in the player input system component, in the player controller gameObject.

You can also check the tutorial video for this process, which you can see here:&#x20;

{% embed url="<https://www.youtube.com/watch?v=_7C7wYB0iIA>" %}
