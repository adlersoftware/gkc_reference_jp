# Configure the Main Scene Manager

This system allows to connect different Scenes between each other ingame, so the player can change from one Scene to another using some element of the level, like a button to press, a

trigger to enter, an event, like pick an object, using a fast travel station, etc…

Think about this system like in borderlands games, where the player reaches the limit of the level, with some kind of gate where he press the interaction button, and he moves to another new level, being a different zone. And of course, the player can return to the previous one, using the gate where he appears in the zone.

To configure this Scene manager, go to the upper tool bar of unity, select **Game Kit**

**Controller->Main Managers->Add Main Level Manager Ingame**.

In this menu, you can place the different types of gates to change of Scene, according to what you need. The current types are **by Button**, so the player can use the interaction button when he is on the range of the gate to trigger the change of level.

**By event**, this can be triggered by any object with an event attached, for example, picking ammo from the ground or a weapon or an inventory object can activate the change of Scene.

**By trigger**, so basically, when the player enters inside a trigger, it will change of Scene automatically.

And also, **a travel station**, a physical trave station which can be placed anywhere on the level and will allow the player to select a Scene to travel (these scenes can be unlocked once the player reaches the travel station of each Scene or by default, have unlocked all the Scene available to travel, according to your type of game).

Once you place one of these **changes of Scene objects** (from now, we will call this object **CSO**) , you have to go to the component **Level Manager ingame**. This component is used to configure the current ID of this CSO (**Level Manager ID**) and the Scene number to travel (**Scene Number To Load**), and inside of that Scene, the ID of the CSO to use as a place to appear **(Level Manager ID to Load**).

It is like an address, and you can have one or many CSO in each Scene, so each one has its own direction.

You can see an example of this in the Scenes Level Manager Building Scene 1 and 2, where in the first door in the exterior of the building, there is one of these CSO, configured with its ID and the scene and ID to use in that scene, which belongs to the object in the second scene, which has that CSO inside the building, with the ID of destiny.

It is very simple but can be confusing for the first time, so take a look at the exterior and interior of this door.

In the exterior, the Scene Number To Load is the scene which contains the interior of the building. The Level Manager Id is 0, since this is the first CSO of this Scene and Level Manager ID to Load is 0 as well since that other object is the first CSO of the second scene, which has the interior of the building.

In this case, the exterior zone is the Scene number 46 and the interior of the building is the Scene number 47.

In the Scene number 47, you can see the settings of the other component, which is in this case, is going to travel to the Scene 46. Its Level Manager is 0, which is the address configured in the other scene and its Level Manager ID to Load is 0 too, since this will travel to the above CSO.

In the component **Level Manager Ingame** you can see the field Spawn Player Position Transform which is the reference position and rotation used to place the player on the level once he changes of Scene, so each CSO can be considered as “connected” to other CSO configured in another Scene.

You can see the same example in the second door of this demo example, but in this case, the ID is 1 instead of 0 since this is the second CSO on the level, so the interior points to the exterior object and vice versa.

The **travel station** work in the same way. Once you have all you Scenes on your game, you can configure the component Travel Station System, with the list of Scenes info, each one with the Scene number to travel and the CSO ID to go. For example, if a Scene has three gates, you select one of them as the default position of that zone to appear when the player travels to that Scene (this also works the same in borderlands, having a fixed zone to appear in one zone, even if that zone has many gates).

In this case, you can see how the station has 2 elements, one per scene, pointing to the first door of the Scene, with the ID 0, so if the player travels to the Scene 1 it will appear in the exterior, at the side of the door and it he travels to the Scene 2, it will appear inside the building, at the side of the door too.

Here you can see also in the **Build Settings**, how the Scene numbers are 46 and 47 for this couple of examples, being each one the exterior and the interior zones of this place.

### Test Scene Manager

In order to try the default demo scenes for the scene manager, you can configure the build settings to set the scene index like in the image below, with the same index for each scene:

Using for this the scenes located on this folder:

Once that is configured, open the first scene and play there with entering into the house and returning outside and walking also outside of the perimeter through the big red door behind the player.
