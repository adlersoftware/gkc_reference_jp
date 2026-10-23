# Tutorial - Create a New Character with the Manual Creator

## Written Tutorial

There is also a manual mode to create a new character. This mode is used when the automatic system hasn’t assigned the bones as the character needs (due to a special skeleton hierarchy). For this, follow these steps:

* Drag and drop a player’s prefab in the scene.
* Drag and drop the new model you want to assign to the player.
* Open **Build Player** inspector, set to true the field Assign Bones Manually, and assign the new model in the field New Character Model:
* Press the button **Search Bones On New Character** and the bones needed will be assigned in the inspector automatically:
* Then, assign the bones (in case that weren't assigned correctly with the automatic mode) and press the button **Build Character**, so the old player’s model is replaced by the new one, and all the fields needed are assigned.

The same can be done with the ragdoll (by default the ragdoll is created with the above process), so bones can be assigned manually to add the ragdoll parts on them properly in case the system didn’t create it correctly.&#x20;

### Manually Set Up Ragdoll

* Go to the **Ragdoll Builder** inspector and set to true Assign Bones Manually.&#x20;
* Make sure the animator of the player is assigned in the field Animator.
* Press the button Search Bones On New Character and the bones will be assigned automatically, like in the build player:
* Assign the bones that weren’t assigned properly and press the button **Build Ragdoll**. The ragdoll will be added like this:
