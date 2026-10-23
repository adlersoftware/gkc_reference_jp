# Save System for Elements State on Scene

The save system has been improved, allowing now to save the state of objects on scene and keep that info in between games and load/save game and change of scenes, which can be used to keep AI dead, objects spawned on the scene, or pickups taken, doors unlocked or locked, places where inventory objects were used, vehicles moved to different scenes, etc….

For this, there is a main manager which takes all the objects in the scene with a component attached to them, called [**Element On Scene**](/docs/additional-managers/elements-on-scene-manager.md), which allows to set an id value and configure what elements are saved, including position/rotation and events options to initialize the state when the scene is loaded, so if a pickup is taken, that object will be disabled when the scene is loaded, or if an inventory object like a key was used, it will keep that door unlocked through those events, calling the function to unlock on the door.

Here you can see an example of this, with an object having this component and some info, like scene value (which is the scene index from build settings where the object is located) and element ID, to know the id of this object, unique in each one of them.

That logic can be used for any type of object to keep its state in between scenes and loaded games.

To configure this, go to the **Main Manager Prefabs** parent (which you can see more info about it on the section **MAIN MANAGERS ADMINISTRATOR**) and locate the **Elements On Scene Manager** object:

The logic to configure it is very similar to other managers like mission, or dialogue, so in the Element Scene field, configure the scene index from that scene on the respective build settings, in this case, the scene is configured on the index 5, so set that in the Element On Scene Manager component, like here:

Once that is done and that you put the objects and elements you want to use on that scene, press the button Get All Elements On Scene And Assign Info.

That will assign the scene index and an unique ID for each object on scene. If you remove or drop more objects with info to save, make sure to press the button again, to assign the ID to each one.

All the inventory objects and most of the interaction elements have this component attached to them, so you can either disable or remove them in case you don’t want to save that info if your game or certain elements don’t need to.

In the same way, you can attach it to any new object or element that you create to save the state of it, for example, for any simple rigidbody, like a box, to keep the info of its position/rotation or any extra value which requires the initialization through the event options on the component.

The same scene manager examples of the previous pages contains the main save system configured for all the elements on it, allowing to check how it works and to try them ingame, following the same steps to configure the build settings with the scene index and the scenes related to these demo examples.

Another example of this is the prefabs where inventory objects are used, as they have assigned this component too, so they will keep the info in between scenes, allowing to use the events to initialize their values if the inventory objects on them were used or not:

You can see how the events for the object active calls to the solve inventory object element.

And here how the usage of inventory objects when complete, will call to the element on scene info to set it as active:

That will make it to call the element on scene event to initialize the object as already complete, so a door remains unlocked, or a device remains active if energy was given to it to turn it on, and so on. So you can pretty much configure any event call to initialize the GKC elements or your own as well.

A scriptable object also handles prefabs to organize elements which can be spawned ingame for example, pickups, so even if the object was not present on scene on the editor, the system is able to recognize that a certain object was spawned ingame, to remain there if the game is loaded.

So if for example, you break a crate with pickups inside, these pickups can remain there, instead of being removed and the crate can remain destroyed, to avoid using it again.

This scriptable object is assigned on the main element on scene manager, and can be found here:

You can configure any new category or use the current ones to organize the prefabs of this type which can be spawned or picked or destroyed from scene as you need:

And in each category, it is a matter of dropping those prefabs which the element on scene component attached to be recognized as element to save state, like inventory ammo pickups:

For example, this pickup has a prefab ID assigned automatically by the main manager:

So the system is able to locate it and spawn it if needed.

Once the prefabs that you need are placed on the scriptable object, go to the main element on scene manager and press the button Set ID On Elements On Scene Prefabs.

Make sure to do this if you add or remove prefab objects of the main scriptable object.
