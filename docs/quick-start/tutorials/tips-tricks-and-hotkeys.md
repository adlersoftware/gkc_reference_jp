# Tips, Tricks and Hotkeys

## Overview

In this document, you can easily find out where exactly in GKC you’ll find a particular feature. Each feature is described with different keywords but we encourage keeping the words you use to search a feature to a minimum.

Each feature will have its full path written out, but please remember the following formatting as it will help you understand where exactly inside GKC you can find it:

Path **GameObject** *Component* \[Button] {Section Title} Feature

The first Tip is shown in full so you can understand where to go, the rest are more direct.

### Visual Aids

{% tabs %}
{% tab title="Health" %}
![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FR5k9PQVJTPfsiZjVYwKj%2Fimage.png?alt=media\&token=e8067c72-2665-4841-ba2c-291a568d0b95)
{% endtab %}

{% tab title="Shield" %}
![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FzGCrZ7zZzSTtESvj1221%2Fimage.png?alt=media\&token=d4bef384-52a2-4a1a-8af0-46721a88ee9f)
{% endtab %}

{% tab title="Compass" %}
![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FLvAvRArgufUgdtLUAtq7%2F9?alt=media)
{% endtab %}

{% tab title="Player Modes" %}

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Weapon Info Panel" %}
![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FtESUXqEnVl6WKbVrOda3%2Fimage.png?alt=media\&token=bcd59336-8114-4d31-a178-e45a056819b8)
{% endtab %}

{% tab title="Screen Action Panel" %}

{% endtab %}

{% tab title="Quick Access Slots" %}

{% endtab %}

{% tab title="Abilities Dpad" %}

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Initial Inventory List" %}

{% endtab %}

{% tab title="Damage In Screen" %}

{% endtab %}

{% tab title="Show Damage Direction" %}

{% endtab %}
{% endtabs %}

## **Tip #1: Remove Camera Reticle**

Displays a small white dot in the middle of the screen at all times.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 - Character - **Player Camera** - *Player Camera* - \[Settings] - {Use Camera Reticle Settings} - Update Reticle Active State
{% endhint %}

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F1xNmPaR0GvdpgfmkaHgN%2F0?alt=media)

**GameObject (on which the feature is stored):**

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FOXg0skYu035uCDhhrQSr%2F1?alt=media)

*Component (in which you’ll find the feature):*

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FV7NT14Z4c4Jbs9EyoaX2%2F2?alt=media)

\[Button] (if the feature only becomes visible after pressing a button):

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FGgKTX7yvsDP3okoil0r0%2F3?alt=media)

{Section Title} (is useful sometimes for navigation inside crowded gameObject Components):

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FNlGIne7sg6hblLC67JyC%2F4?alt=media)

Feature (the actual feature):

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FnVYRbiaE8hmyfFhv7K7o%2F5?alt=media)

While it is possible to simply hide the camera reticle in the following menu.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 - HUD Elements - HUD and Menus - HUD - Player Info - Health, Energy, Weapons - **Main Camera Reticle**
{% endhint %}

* It is **NOT** actually recommended to deactivate the reticle in this manner.
* This will only deactivate the reticle at the beginning of the runtime, however, there are several features that might bring back the reticle when used.&#x20;
* For example, after using an access panel. Therefore, do not deactivate the reticle UI component, but its feature instead.

## Tip # 2: Scene number for home menu <a href="#guvi40o0f345" id="guvi40o0f345"></a>

Defines the index number of the scene that is loaded when clicking **Exit to Home** on the pause menu.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 **- Character** - *Menu Pause* - Scene Number for Home Menu
{% endhint %}

## Tip # 3: Time Bullet <a href="#ll2e5i78jzrj" id="ll2e5i78jzrj"></a>

When pressing Z, a slow-motion mode is entered until you press Z again.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 **- Character** - *Time Bullet* - Time Bullet By Input Enabled
{% endhint %}

## Tip # 4: Ground detection settings <a href="#nad020kq78wi" id="nad020kq78wi"></a>

Defines which layers GKC will recognize as walkable ground.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 - Character **- Player Controller** - *Player Controller* - {Ground Detection Settings} - Layer
{% endhint %}

* If your character is still walking on water, make sure you set the most parent gameObject of your water to a layer that you excluded here. If prompted, you might have to apply the layer to all children as well.&#x20;
* Sometimes when doing changes to the water, you might have to repeat this step. This behavior has been observed with *Gaia* for example.

## Tip # 5: Increase Walk Speed Enabled <a href="#id-7rqi6ywnav9" id="id-7rqi6ywnav9"></a>

Speeds the walking up over time.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 - Character **- Player Controller** - *Player Controller* - {Walk/Run/Sprint Settings} - Increase Walk Speed Enabled
{% endhint %}

## Tip # 6: Shake Camera On Sprint Third Person <a href="#id-6fbsg9dlxe8w" id="id-6fbsg9dlxe8w"></a>

Adds an extra camera shake to the player when running.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 - Character - Player Controller - Player Controller - {Sprint Settings} - Shake Camera On Sprint Third Person
{% endhint %}

## Tip # 7: Extra Character Mesh Objects <a href="#v3lv2t6jx6vf" id="v3lv2t6jx6vf"></a>

Used in order to hide objects that are not supposed to be visible in first person mode.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 - Character **- Player Controller** - *Player Controller* - \[Advanced] - {Character Mesh Settings} - \[Show/Hide EXTRACHARACTERMESHGAMEOBJECT]
{% endhint %}

* Add as many slots to the list as needed and drag the game objects in here that you don’t want to see in the first person (for example eyelashes, hair, pants, shirt, shoes, etc)

## Tip # 8: Double jump <a href="#t9x79z9gwcfe" id="t9x79z9gwcfe"></a>

Allows the player to do double jumps by pressing the spacebar repeatedly.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 - Character **- Player Controller** - *Player Controller* - \[Advanced] - {Jump Settings} - Enabled Double Jump
{% endhint %}

## Tip # 9: Fall Damage Settings <a href="#iwhu6y4mf72l" id="iwhu6y4mf72l"></a>

Defines how long you can fall before taking damage when hitting the ground.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 - Character **- Player Controller** - *Player Controller* - \[Advanced] - {Fall Damage Settings}
{% endhint %}

![Original settings](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F0KusuRsXKgKKGNA28bjt%2F19?alt=media) ![Example settings (damage from about 3m height)](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FzCuWPUVShWbbPeMX6Ulo%2F20?alt=media)

## Tip # 10: Fall Damage Audio <a href="#id-2mlumx5sf9ca" id="id-2mlumx5sf9ca"></a>

Play a sound when the player receives fall damage (for example “ouch”).

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 - Character **- Player Controller** - *Player Controller* - \[Advanced] - {Fall Damage Settings} - {Event On Fall Damage}
{% endhint %}

* Add a new event and drag your gameObject with the attached audio component in here. If you have multiple different audio files that you’d like to be played randomly when taking damage, you can use the script below and call it RandomInjury, attach it to a gameObject, and add your different audio clips to the list.&#x20;
* Then, drag the gameObject into the Event On Fall Damage list and set it to **Randominjury.Injurysound**

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class RandomInjury : MonoBehaviour
{
private AudioSource audioSource;
public AudioClip[] shoot;
private AudioClip shootClip;
void Start()
{
audioSource = gameObject.GetComponent<AudioSource>();
}
public void Injurysound()
{
int index = Random.Range(0, shoot.Length);
shootClip = shoot[index];
audioSource.clip = shootClip;
audioSource.Play();
}
}Land Mark
```

## Tip #11 - Adjusting Land Marks

Displays a blue circle underneath the player when jumping.

{% hint style="info" %}
**LOCATION**

Player And Game Management - Player 1 - Character **- Player Controller** - *Player Controller* - \[Advanced] - {Land Mark Settings} - Use Land Mark
{% endhint %}

## Tip # 11: Disable or Enable Foot Prints <a href="#id-5tfkb445vag0" id="id-5tfkb445vag0"></a>

Creates visible footprints on the ground that fades away slowly.

{% hint style="info" %}

#### **LOCATION**

Player And Game Management - Player 1 - Character **- Player Controller** - *Foot Step Manager* - {Foot Prints Settings} - Use Foot Prints
{% endhint %}

## Tip # 12: Unlock Infinite Slots (Inventory) <a href="#id-5cc1au9ukk1x" id="id-5cc1au9ukk1x"></a>

Change the number of items that can be carried in the inventory.

{% hint style="info" %}

#### **LOCATION**

Player And Game Management - Player 1 - Character **- Player Controller** - *Inventory Manager* - {Inventory Slots Settings} - Infinite Slots
{% endhint %}

You can also change the number of inventory slots here using **Inventory Slots Amount**.

## Tip # 13: Examine Object Before Store Enabled (Inventory) <a href="#s235li6jm0sv" id="s235li6jm0sv"></a>

Displays a spinning preview of an item when picking it up and before adding it to the inventory.&#x20;

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character **- Player Controller** - *Inventory Manager* - \[Examine] - {Examine Object Settings} - Examine Object Before Store Enabled
{% endhint %}

## Tip # 14: Initial Inventory List <a href="#xa16v55n0vpi" id="xa16v55n0vpi"></a>

Configuration for the items available in the inventory and on the player at the start of the game.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character **- Player Controller** - *Inventory Manager* - {Initial Inventory List} - \[Show/Hide INVENTORYLISTMANAGERLIST]
{% endhint %}

* Use this list to add or remove items to your inventory list that will be available at runtime.
* Additionally, you can choose whether or not items are equipped.&#x20;
* If you want to create new items that could be added to your inventory or picked up in the game, use the **Main Inventory Manager** outside the **Player And Game Management** instead.
* Then, you can use the Initial Inventory List if you want the items to be available in the inventory at the start of the game.&#x20;
* If you just started with GKC and want to remove all the weapons after creating the player, remove or disable them here, don’t disable them in the player hierarchy.

## Tip #14: Don't Delete Player Modes, Tweak them <a href="#id-35cepk3umxrt" id="id-35cepk3umxrt"></a>

Used in order to switch between melee, combat, weapon, powers, etc.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character **- Player Controller** - *Player States Manager* - {Players Mode List} - \[Show/Hide PLAYERSMODE]
{% endhint %}

* Don’t delete players mode, instead just open each player mode individually and untick **Mode Enabled**.&#x20;
* There, you also have an option to **Activate Player Mode Events** and **Deactivate Player Mode Events**.&#x20;
* You can use this section to unlock additional features, for example, you can use icons instead of text to indicate the current player mode on screen.&#x20;
* To do the above, just add UI components to your HUD, for example under *Player And Game Management - Player 1 - HUD Elements - HUD and Menus - HUD - Player Info - Player Mode* and disable the Text and the **Current Player Mode Text**.&#x20;
* Then, use **Activate Player Mode Events** and **Deactivate Player Mode Events** in the **Player Modes** settings to activate and deactivate them.

## Tip #15: Inventory Quick Access Slots <a href="#cjnesm2f3cg7" id="cjnesm2f3cg7"></a>

Displays a number of squares at the bottom of the screen with weapons inside.&#x20;

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Essential Components **- Inventory Quick Access Slots** - *Inventory Quick Access Slots System* - Use Inventory Quick Access Slots
{% endhint %}

* You can use the number key on the keyboard in order to switch between different weapons easily without having to equip/unequip them in the inventory.
* If you disable this, you might also want to disable **Show Quick Access Slot Selected Icon**, otherwise, a white line will appear on the screen when switching to a weapon.

## Tip #16: Jump While Swimming <a href="#q4vctrr3du6r" id="q4vctrr3du6r"></a>

Allows a player to jump out of the water.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Non Essential Components - External Controller Behaviours **- Swim System** - *Swim System* - Can Jump When Swimming On Surface
{% endhint %}

## Tip #17: Underwater Camera Effect <a href="#gcg9d3360qon" id="gcg9d3360qon"></a>

Applies a blue blur to the camera when the player is underwater.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Non Essential Components - External Controller Behaviours **- Swim System** - *Swim System* - Use Event On Camera Underwater Effect
{% endhint %}

* You might want to disable this feature if you have an underwater effect generated by a third-party application such as *Gaia*, etc.

## Tip #18: Show Damage Direction <a href="#uz1cw8v4g7xx" id="uz1cw8v4g7xx"></a>

Displays a red cross or x on screen when receiving damage.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Elements Used By Other Components **- Damage On Screen Info System** - *Damage Screen System* - Show Damage Direction
{% endhint %}

## Tip #19: Damage In Screen <a href="#pdekbi9dukpj" id="pdekbi9dukpj"></a>

Displays the amount of damage you've received in the form of a floating number that displays around the player.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Elements Used By Other Components **- Damage On Screen Info System** - *Damage Screen System* - Show Damage Direction
{% endhint %}

## Tip #20: Ignore Gamepad <a href="#hqkcg3lu65i4" id="hqkcg3lu65i4"></a>

If you play your game and GKC is not reacting to your keyboard inputs, check if any external input devices are connected to the PC (for example a controller, a tablet, etc.). If you unplug it and restart the game and it now the controls work, you can follow this step.

{% hint style="info" %}

#### LOCATION

**Player And Game Management -** *Input Manager* - {Gamepad Settings} - Ignore Gamepad
{% endhint %}

## Tip #21: Multi Axes List (Configure Keys) <a href="#tu2y8g63lxtl" id="tu2y8g63lxtl"></a>

Some features cannot simply be disabled, instead, you have to disable the keys that trigger these features. Some of the items in the list below might have an option to be disabled, but as of my current knowledge, they can only be deactivated by disabling the input key

{% hint style="info" %}

#### **LOCATION**

**Player And Game Management -** *Input Manager* - {Multi Input List} - \[Show/Hide MULTIAXESLIST]
{% endhint %}

To disable the following keys navigate to:

/-Key (forward slash): Player Controller - Show/Hide Axes - Simple Kick

\[-Key (left bracket): Player Controller - Show/Hide Axes - Activate Ragdoll in Runtime

CTRL-Key (left control): Player Camera - Show/Hide Axes - Move Away Camera

\#-Key (quote, hash): Player Camera - Show/Hide Axes - Enable-Disable Camera Rotation

Shift-Key (right shift): Player Weapons - Show/Hide Axes - Edit Weapon Attachments

Alt-Key (left alt): Player Weapons - Show/Hide Axes - Weapon Melee Attack

Tip: To find out which feature is assigned to which key, you can go to.

{% hint style="info" %}

#### LOCATION

**Player And Game Management -** *Input Manager* - {Show Current Input Action List Settings} - \[Show Current Input Action List Settings] - \[Show Full Current Input Action List]
{% endhint %}

Now you can see the full available list of keys and their respective features. In order to search for a specific key, use the dropdown “Action Key To Filter” and press the button: \[Show Input Actions Keys By Filter].

## Tip #22: Chapter Info <a href="#uinjk78na4ex" id="uinjk78na4ex"></a>

Defines the name of the current level, for example in save files.

{% hint style="info" %}

#### LOCATION

**Player And Game Management -** *Game Manager* - Chapter Info
{% endhint %}

## Tip #23: Set Initial Position <a href="#id-272osvpt0b6a" id="id-272osvpt0b6a"></a>

By default, your player faces North when going into play mode (North is in the direction of the blue Z editor axis) with the camera also facing North.&#x20;

If you want your player AND camera to face a different direction, use **Set Initial Position**. Don’t rotate the **Player Controller** gameObject, because it will only rotate your player but not your camera.

{% hint style="info" %}

#### LOCATION

**Player And Game Management -** *Set Initial Position At Game Start -* Set Initial Position Enabled (and then define the Rotation Offset)
{% endhint %}

## Tip #24: Screen Action Panel <a href="#nulk2yuho52n" id="nulk2yuho52n"></a>

Disable the UI panel in the bottom left corner stating things like fire/draw weapon, wheel menu, draw/holster weapon, attachments, etc.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Essential Components **- Player Input Panels** - *Player Input Panel System* - {Main Settings} - Screen Action Panels Enabled
{% endhint %}

## Tip #25: Head Bob <a href="#gy0z02o2kajx" id="gy0z02o2kajx"></a>

Disable head bob or change the strength of individual head bobs based on camera state.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Player Camera - Pivot Camera Transform - Main Camera Transform **- Main Camera -** *Head Bob* - Head Bob Enabled
{% endhint %}

Press \[Show/Hide BOBSTATELIST] to change the intensity of the head bob per camera state.

Below is a list of the original settings (left) versus a bit less intense ones (right)

## Tip #26: Compass <a href="#k507ftsnplit" id="k507ftsnplit"></a>

Displays a band with a compass at the top of the screen.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 **- Character -** *Map Systems* - \[Compass Settings] - {Main Settings} - Compass Enabled
{% endhint %}

You could also disable the compass under **Player And Game Management - Player 1 - HUD Elements - HUD and Menus - HUD - Map - Compass Window** however, this would only hide the UI component at runtime. If you want to completely disable UI components and never use them, it’s always better to disable their feature on their respective gameObject inside the Character hierarchy, rather than in the HUD Elements hierarchy.

## Tip #27: Weapon Info Panel <a href="#id-4fxs6bhj8wy5" id="id-4fxs6bhj8wy5"></a>

Displays a weapon info panel (HUD) in the top right corner with the current ammo amount and a weapon thumbnail.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Player Controller - Gravity Center - COM - \*your player\* - \*your player’s bones\* - Player Elements - Player Weapons - \*your weapon\* **- gunModel -** *Player Weapon System* - \[HUD] - {HUD/Hologram On Weapon Settings} - Use Canvas HUD
{% endhint %}

Repeat this on every weapon used in your game

## Tip #28: Hologram On Weapon <a href="#a6asamuspcg9" id="a6asamuspcg9"></a>

Displays a HUD right on the weapon with the current ammo amount.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Player Controller - Gravity Center - COM - \*your player\* - \*your player’s bones\* - Player Elements - Player Weapons - \*your weapon\* **- gunModel -** *Player Weapon System* - \[HUD] - {HUD/Hologram On Weapon Settings} - Use HUD
{% endhint %}

Note: Repeat this on every weapon used in your game

## Tip #29: Projectile Damage <a href="#wacrvnczox93" id="wacrvnczox93"></a>

Defines how much damage a weapon projectile generates on the enemy.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Player Controller - Gravity Center - COM - \*your player\* - \*your player’s bones\* - Player Elements - Player Weapons - \*your weapon\* **- gunModel -** *Player Weapon System* - \[Projectile] - {Projectile Settings} - Projectile Damage
{% endhint %}

Another feature in this section is called Projectiles Per Shot. You might want to change this in parallel to the Projectile Damage, as the two factors will be multiplied.

## Tip #30: Laser Beam, Laser Point <a href="#id-98q0ccpg6m0l" id="id-98q0ccpg6m0l"></a>

Some weapons (for example Assault Rifle) display a visible light beam.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Player Controller - Gravity Center - COM - \*your player\* - \*your player’s bones\* - Player Elements - Player Weapons - \*your weapon\* - gunModel - meshParts - Attachment Systems - Attachment Places - Barrel - Laser
{% endhint %}

Note: Disable the gameObjects in here as needed

## Tip #31: Jump When Hold Ledge <a href="#wn3aruu130xz" id="wn3aruu130xz"></a>

Allows the player to jump off a ledge.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Non Essential Components **- Climb Ledge System** - *Climb Ledge System* - Can Jump When Hold Ledge
{% endhint %}

Alternatively, you can also simply lower the Jump Force When Hold Ledge in here if you just want to reduce the jump height

## Tip #32: Wall Running System <a href="#z2w4rb3mexb9" id="z2w4rb3mexb9"></a>

Allows a player to walk and run on vertical surfaces.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Non Essential Components - External Controller Behaviours **- Wall Running System** - *Wall Running System* - Wall Running Enabled
{% endhint %}

## Tip #33: Abilities Dpad Panel <a href="#kszf3z8lcclz" id="kszf3z8lcclz"></a>

Displays a Dpad UI component on the screen.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Non Essential Components **- Player Abilities System** - *Player Abilities UI System* - Use Dpad Panel
{% endhint %}

This will only disable the UI of the abilities Dpad, not the accessibility of the actual features. You can still use the arrow keys on your keyboard to make use of the abilities themselves. To switch the abilities off completely, disable **Ability List Manager Enabled** in the same gameObject component.

Whilst you could simply disable the Dpad UI element under **Player And Game Management - Player 1 - HUD Elements - HUD and Menus - HUD - Player Info - Health, Energy, Weapons, and More**, I recommend disabling its feature instead (as described above).

## Tip #34: Player Stealth System <a href="#bybdtsi0l0m2" id="bybdtsi0l0m2"></a>

Allows the player to go undetected by enemy AI.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Non Essential Components - Player Abilities System **- Player Stealth System** - *Player Stealth System* - Ability Enabled
{% endhint %}

## Tip #35: Objectives Log <a href="#op0j1a6ufqns" id="op0j1a6ufqns"></a>

Displays an objective log. U-Key.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 **- Character -** *Objective Log System* - Objective Menu Active
{% endhint %}

## Tip #36: Travel Station <a href="#id-2yg96rceuzqk" id="id-2yg96rceuzqk"></a>

Displays a travel station UI menu.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 **- Character -** *Travel Station UI System -* Travel Station UI Active
{% endhint %}

## Tip #37: Experience <a href="#mtr13994xb3m" id="mtr13994xb3m"></a>

Displays an experience system UI.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Essential Components **- Experience-Level-Stat Systems** - *Player Experience System* - Experience System Enabled
{% endhint %}

## Tip #38: Extra Camera Rotation <a href="#u3ay9510j9z6" id="u3ay9510j9z6"></a>

Rotates the camera by a set amount of degrees (180 by default).

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character **- Player Camera** - *Player Camera* - {Set Extra Camera Rotation Settings} - Set Extra Camera Rotation Enabled
{% endhint %}

## Tip #39: Scan Visor <a href="#a56eu1ppyxq3" id="a56eu1ppyxq3"></a>

Activates the scanner system.

{% hint style="info" %}

#### LOCATION

Player And Game Management - Player 1 - Character - Other Player Systems - Elements Used By Other Components **- Scanner System** - *Scanner System* - Scanner System Enabled
{% endhint %}
