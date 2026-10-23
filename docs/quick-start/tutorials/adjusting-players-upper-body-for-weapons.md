# Adjusting Player's Upper Body for Weapons

The player’s upper body rotation can be configured for aim mode in Third Person. This is made in the inspector **Upper Body Rotation System** in the **Player Controller** gameObject, allowing to configure how fast the rotations are done and the clamp values used for the spine rotation. The object to follow is the actual transform followed for the player’s torso, which is inside the main camera, so you can move it up or down to adjust the orientation when the player aims.

In this case, you configure a new model, and something like this happens:

The cause is that the spine bones are not correctly configured in the **Upper Body Rotation System**, in the gameObject **Player Controller**, due to the skeleton hierarchy is slightly different in this case. In the example above, the system has taken the hips as the first bone, this is incorrect.

But you only need to set the correct bones. To do this go to the inspector and make sure to place the bones which belong to the spine and the chest, like this:

But if this happens, you need to take another step, which is to move the **Player Elements** gameObject from its current hierarchy position to inside the Chest transform configured in the inspector, in this case, the Spine2.

Like this, the player's weapon should move correctly, rotating the player’s upper body and without any issue.
