# Configure Input Rebind Menu Panel and Actions

The input can be edited in-game at any moment, allowing to change for example the key used for jump.

For this, a menu is configured for this system, and inside this menu, multiple panels for each group of actions and different actions buttons are created for each action in those groups.

This by default is made at the start, instantiating these elements in that moment, but these elements can be configured and instantiated in the editor, before starting the game, to avoid those instantiations at the start.

To configure this, follow these steps:

* Go to Input Manager inspector:
* Go to the section Rebing Input Menu Options:
* And set the number of panels and actions buttons inside each panel, to use it as a pooling list of elements to be used for the rebind menu, and press the button **Instantiate Rebind Menus And Actions Panels**:

You can see how these panels and elements are created inside the Edit Input Controls menu.

You can also, destroy these panels to create other amounts or instantiate them at the start with the button **Destroy Rebind Menus and Actions Panels**.

The options **Create Rebind Input Menu With Current Axes** will use the current amount of input categories and actions in each category to create the exact amount of panels for the rebind menu, instead of having a pooling list with panels and buttons that maybe will be left as not used due to the actions amount are lower that the amount of these panels.
