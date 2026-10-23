# Main Manager Administrator

GKC has many main managers, including the main inventory manager, which handles all the inventory info objects created on the asset, or the faction system to configure the relations between groups of AI and players and if they are enemies, friends, or neutral, and more main systems used to handle different parts of the asset.

This main manager is located on the player prefab parent, on the component Main Manager Administrator, where you can see a list of prefabs assigned there which are the managers themselves. The system automatically drops them on the scene at the start of the game if they haven’t been dropped manually on the editor.

So for this, you can just press the button Add Main Managers to Scene and they will be placed in a new parent object on the hierarchy:

This parent is called Main Managers Prefabs:

Some of these managers are linked to their original prefabs in the project, so you can apply the changes made on them in a scene, like creating a new inventory object, and that info will be applied to the rest of scenes where you have your player prefab placed. You can use the button Update Main Managers Info To Prefabs to update such info.
