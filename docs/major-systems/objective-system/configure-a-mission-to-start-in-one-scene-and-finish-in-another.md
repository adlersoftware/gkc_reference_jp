# Configure a Mission to Start in one Scene and Finish in Another

This is very simple, you only need to configure the same info on the Objective Event System component on the scene where it starts and where it ends (the scene where the mission is complete doesn’t require the trigger of the mission to be active, since the mission was already activated on another scene).

For this, make sure to configure the same scene ID and mission ID on the fields of the **Objective Event System** components on both scenes, so the system can link the info of one side in the other.

Here an example, where the build settings with the scene index are configured like this:

In the scene Level Manager Building Scene 1, this is the mission ID and scene ID values configured on the objective event system component:

The scene index is 5, since the scene uses that indes on the above build settings and the mission ID is 0 (it could be any other value, but in this case, this is the unique ID assigned to it on this scene).

On the second scene, where the mission is complete, which in this case is Level Manager Building Scene 2, the values on the objective event system are these:

Like previously, same values, being the mission ID a unique value on this new scene (make sure that for example in this case, no other objective event system has the mission ID field with 0, since each mission needs an unique value for this).

It is recommended to check the section CONFIGURE THE MAIN SCENE MANAGER to see more about how the different scenes are managed.
