# Tutorial - Create New Melee Weapon

How to Create a New Melee Weapon for your character with the Wizard.

## Video Tutorial

{% embed url="<https://youtu.be/ad7bN_dE3ZI>" %}

## Written Tutorial

Drop the weapon mesh on the scene and make sure to remove any collider on it and also check that the static field is false on the object.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F7z6jGAqjbRP0IyBgBh8w%2F0?alt=media)

Create a new transform inside the weapon and move it out of it, reset the rotation of the object and place the mesh inside, so you can center the weapon mesh on the center of the new parent.

Remember to set the setting global on the unity top bar setting for the step, so you can see the actual pivot position of the objects.

Open the menu to create a new melee weapon on Game Kit Controller bar settings on the top side of the Unity, and drop the new object there.

!\[Graphical user interface

Description automatically generated]\(/files/APxcZGhNeI7VUEnGl6Y9)

Enable the option to create inventory info, set a unique name for the weapon, set a new image and press Create Object button.

Select the weapon type that is closer to the type of weapon that you want to use like a sword, axe, bow, etc.… so it will have similar settings to it.

Enable the option to create inventory info, set a unique name for that weapon, set a new image and press Create Object button.

Once created, you can search it on the search tool of the project window, and drop the physical object in the scene, to adjust some elements on it.

You can adjust the box collider of the weapon object along with adjusting the weapon mesh, so its handle is centered on the pivot of the weapon, to be carried properly.

!\[A picture containing text

Description automatically generated]\(/files/6AEyUcvCcWFuP0X3KXLF)

With that, the weapon is ready to use, in this example, the weapon is placed in the mount point of the hand, so in most cases, it won’t need many adjustments.

But each weapon can be adjusted to each character, for this, go to the melee weapon system and use the melee weapon adjust tool.

First, enable the edit weapon to transform values in-game and the show gizmo option then uses the gizmo to adjust rotation/position in place and press the Copy Transform Values button.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FM3KiPI2OSrtehL95lOHq%2F3?alt=media)

Once that is done, stop the game and press the Paste Transform values button. Now, play the scene and try, the weapon should adjust as you configured now.

Same as carrying on hand, the sheathed weapon position/rotation can be adjusted. Sheath the weapon (Using the Y key by default) and follow the same steps as before.

The process is the same, adjusting the gizmo of the weapon on the character so it is carried there when is not in the player's hands, so adjust, copy, stop the game, and paste.

And all done after that, the weapon is also stored in the player’s inventory.

You can also search the weapon inventory object instead, using the search tool on the project window.

Just like before, you can adjust the collider of the inventory object, to adjust it to the size of the weapon and apply the settings to the prefab (remember to apply the settings in the previous one too).
