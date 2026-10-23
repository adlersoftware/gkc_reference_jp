# Fixing Player Spine Rotation

If the player spine doesn’t rotate correctly when you move the mouse up and down in aim mode in third person, the cause is due to the spine orientation in the model.

For example, in this model, the local Y axis of this model spine, is the Y axis, which can be different in every model.

To fix this, go to the **Upper Body Rotation System** inspector in the gameObject **Player Controller** and configure the correct values in the field **Spine Up Vector**. It needs to be the same up transform orientation of the transform assigned in the field Spine Transform (mixamorig: Spine in this example). In this case, the value is (0,1,0) instead of (0,0,1) which is the default value.

In the default model of GKC, its spine orientation is Z for the local Y axis.

And the value used for this is (0,0,1).
