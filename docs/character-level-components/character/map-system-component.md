# Map System Component

### SET THE MAP SYSTEM <a href="#toc93279" id="toc93279"></a>

Once a new player has been created, if you want to use the map system, you need to drag and drop the **Map System prefab** (with the same name) in the folder **Assets/Game Kit**

**Controller/Prefabs/Map System**.

Once the hierarchy contains these two elements:

Then, go to **Character** gameObject, **Map System** inspector, and press the button **Add Player to the Map System Creator**, to add this player map system to the main map manager, which is Map Creator.

In the **Map Creator** inspector, you can see how the current player has been added to the main map manager:

Now go back to **Character** gameObject, **Map System** inspector, and press the button **World Map**.

Go to **Building List**, and press the button **Search Building List**. The buildings and floors configured in the Map Creator inspector will be configured automatically.

If you don’t need to use the map system, don’t configure the above steps and it will be disabled.
