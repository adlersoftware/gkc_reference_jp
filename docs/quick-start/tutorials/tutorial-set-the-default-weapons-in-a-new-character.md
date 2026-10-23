# Tutorial - Set the Default Weapons in a New Character

To manage the player’s weapons, go to **Player Controller** gameObject, and to the inspector **Player Weapons Manager**.

<details>

<summary>If You Use The Inventory to Store and Manage Weapons</summary>

* Open **Inventory Manager** inspector in Player Controller gameObject and open the Initial

### Inventory List:

* In that list, you can configure the initial inventory in the player at the start of the game. You can add, remove, set as equipped, and set if the inventory object will be added at the start or not (to avoid removing an object from the list to not being included in the inventory of the player at the start). By default, all the weapons available in the player are included.
* To include every weapon, press the button O to enable or disable if the weapon will be in the inventory at the start or not (the field **Add Inventory Object** will be as true or false):
* To set that weapon as equipped at the start of the game (so the player can carry and fire that weapon), press the button E, and the field **Is Equipped** will be set to true or false:
* Currently, the revolver is configured to be added to the inventory and equipped.

Do this setting with the rest of the weapons, so you can add as many as you need or remove by setting Add Inventory Object as false, so the player starts with no weapons, but he can add weapons later in the game using the weapons pickups.

For this example, only the revolver has been added and equipped, so you can see that the inventory object is included in the Inventory List, below the Inventory Manager List, in the same inspector.

The rest of empty slots are configured according to inventory space configured in the inspector, in this case, 20 slots with a limit of 10 units per slot.

</details>

<details>

<summary>If You Don't Use Weapons</summary>

#### **IF YOU DON’T NEED TO USE THE WEAPONS**, follow these steps:

* In the **Player Weapons Manager** inspector, press the button **Show Weapon List**.
* Open the **Weapons List**:
* Press the button **Disable All Weapons** or **Clear Weapon List**.
* After this, you can also remove the weapons gameObjects from the player, located inside his body. The image below shows where they are located in the hierarchy. Remove all the objects inside the gameObject Player Weapons.
* Also, make sure to remove the weapons objects configured in the **Inventory Manager** inspector in the Player Controller gameObject, to avoid adding weapons that doesn’t exist in the player body anymore.

</details>

<details>

<summary>If You Use Weapons</summary>

#### **IF YOU NEED TO USE THE WEAPONS**, follow these steps:

* Press the button Show Settings in the **Player Weapons Manager** inspector.
* In the Inventory Settings, set to false the field **Store Picked Weapons On Inventory**:
* Now, press the button **Show Weapon List**.
* You can now press **Enabled** (or disabled) option in every weapon to make it usable in game (else the weapon model in the player is disabled, but you can use it if you pick the weapon in the level, but you first need to complete these steps to avoid problems. You can remove every weapon in the list, as explained below, so even if the player finds that weapon to pick in the level, he will be unable to use it).
* Go to **Inventory Manager** inspector in the Player Controller gameObject and in the

Inventory Equip Settings, set to false the field Store Picked Weapons On Inventory:

* Finally, return to **Player Weapons Manager** inspector. You can assign in every weapon where it will be attached inside the player’s body (the back, the legs, the waist and by default is the back), so if the weapon is in the leg, it is placed inside of it. To this, go to any weapon (by selecting any weapon in the above list).
* Go to gunModel inside the weapon, and open the inspector **Player Weapon System**.
* Press the button **Show Weapon Settings**, go to section **Weapon Components** and set the bone that you want in the label **Weapon Parent** (for example in the demo, the pistols are parented in every leg and the rest of weapons in the back of the player).

Like this, the weapons can be activated and used in the player without manage them through the inventory, so you can use them similar to games like Doom (2016) which hasn’t an inventory.

Also, for there are two types of weapons pickups, one to just activate the weapons and other to store them as inventory.

The first type can be found in the prefabs folder **Prefabs/Player Weapons/Weapons**:

The second type can be found in the prefabs folder **Prefabs/Inventory/Usable/Weapons**:

So according to the type of weapons management that you use in your project, use the proper weapon pickup prefabs.

</details>
