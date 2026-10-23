# GKC Update 3.03-3A

## **CATEGORIES:**

### PLAYER CONTROLLER

* Added a new character model for the player and AI, having a modular body, which includes many different parts, configured as examples of the new armor/cloth system. allowing to equip any type of equipment for visual elements

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FLSzb2es8RrTCR2yDcYYm%2F0?alt=media)

* Improved a little more the ground adherence, allowing to detect better small gaps and distances to the ground in different states, to move properly on it. Here the max step is 0.6 units and the last step he can't walk on from the ground is 0.7 to show the max height for it available on the example.

{% embed url="<https://streamable.com/58gfp9>" %}

### WEAPONS

* Improved the weapons creator wizard, to allow to set info about the info of the new weapon inventory object, including description, icons, and ammo mesh and icons as well, making the process more automatic now and avoiding any extra step once the weapon (and the inventory objects info for it and its ammo) are created in a couple of clicks:

&#x20;![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FkiAapCvfKcXiNjwiWeyK%2F1?alt=media)

* Added example of weapon which projectiles with a remote event to disable the shape-shifting on an enemy AI
* so if you have a werewolf enemy, if you fire them with a weapon with silver bullets, it returns to human

{% embed url="<https://streamable.com/wjdfpk>" %}

### INVENTORY

* Here is an example of an option to holster the current weapon if its quick access slot is pressed with the weapon already carried (it can be seen on the touch controls as well):

{% embed url="<https://streamable.com/vecvsp>" %}

* I also show there more examples of the close combat system used in any state while carrying fire or melee weapons
* Improved management of the quick access slots, as objects order is saved now, so the objects there will keep their position in between game save/load or scene changes:

{% embed url="<https://streamable.com/yv2u31>" %}

* Of course, not only on weapons but any of the inventory objects on them

### AI

* Here is an example of the return grenade action when the enemy throws a grenade at the player in the first and third person, as the ability system is usable in both views now:

{% embed url="<https://streamable.com/ci5uu6>" %}

* Configured the dual melee weapons on the AI as well, as I didn't have the chance on the recent update:

{% embed url="<https://streamable.com/7hziwe>" %}

* Added an option for the AI which allows them to change between their fire weapons after a random range of wait (in this example is configured around 4-7 seconds):
* <https://streamable.com/ojxi0y>
* Here is an AI dropping his weapons from damage on the arms, falling on the ground due to damage on his feet, and using close combat on the player while using fire weapons

{% embed url="<https://streamable.com/57uozc>" %}

* AI can manage multiple melee weapons and change them in runtime, along with dropping them from damage received on arms as weak points:
* <https://streamable.com/5x7giy>
* Here is a test with an option to hide directly a character inside a hide trigger, removing its info from the detected AI around:
* <https://streamable.com/3bu2wh>

### GENERIC MODEL SYSTEM (animals, monsters, robots, etc…)

Here is a tutorial video to configure generic models on the AI

{% embed url="<https://youtu.be/YKaDpyLL44U>" %}

### VEHICLES

* Configured examples to use the save system to change scenes with vehicles with the general drive/rider system, so external vehicles integrated can move of a scene and save its state as the rest of GKC vehicles:&#x20;

{% embed url="<https://streamable.com/h23grq>" %}

### OTHERS

* Many improvements on workflow and new tools to create or customize many different elements, including the creation of an action system, adding melee weapons, creating armor/cloth pieces, and more.
* Created online doc of GKC which has been published thanks to the huge help of **Tikal.**
* Here is a new test with the new model for GKC, which has already different armor parts, and which I will show some examples of the armor/cloth system work on it during these days:

{% embed url="<https://streamable.com/vy4v4g>" %}

* Here is some more destruction with the Mjolnir weapon example, breaking stuff

{% embed url="<https://streamable.com/b381n5>" %}

### ISSUES/BUGS FIXED

* I fixed a bug on the weapon system on the player due to the action system used on the draw/holster weapon action, when equipping weapons from the inventory menu or dropping them into the quick access slots inventory system, causing the player movement and input to be disabled and not resuming

### MELEE COMBAT SYSTEM

* Configured remote event options on the throw and weapon return and use the already included function to pause all the actions and states on the AI, so you can freeze AI by shoving an axe on its chest haha:

{% embed url="<https://streamable.com/p21q71>" %}

* Tweaked the block animation state on the melee weapons for the upper body, looking better by default now:
* <https://streamable.com/twspw8>

Added another example of a melee weapon, a boomerang, having an option to aim and mark a list of targets to reach, allowing it to be used like in wind waker, to damage, break or send signals to elements to trigger events or functions:

* <https://streamable.com/karxzi>
* Added example of the bow and boomerang to mark targets with the touch buttons, as any button allows to enable the camera drag, so while you perform the aim/shoot/throw/mark, you can rotate the camera with it, to play easily on mobile:
* <https://streamable.com/tm41h7>
* Here is a tutorial to configure new melee attacks on a character and the melee weapons:
* <https://youtu.be/MlqLxtin1Rk>

### TRAVERSAL MOVEMENT ELEMENTS

* Configured an option to allow to use of the weapons while using the slide-on rail traversal action:
* <https://streamable.com/tr66lj>

### CLOSE COMBAT SYSTEM

* Added a cool option on the close combat, which will allow activating close combat attacks on any state, either while using melee or fire weapons, and keep using them, so it will keep the current player's mode, do the attack and keep the weapon on the hands, and chain close combat and fire weapons or melee weapons attacks:

{% embed url="<https://streamable.com/ezy7y8>" %}

* Improved the slice system to allow to configure custom positions to check for objects to slice, so it can be called from events for any position and object on the player, such as the close combat, using the events options to call it:

{% embed url="<https://streamable.com/3prtjy>" %}

* The same action to make a character drop their current weapon activated by remote events from anything, like attacks from close combat, in this case, happening to the player:
* <https://streamable.com/3g0m8o>

### ARMOR/CLOTH SYSTEM

* Added armor/cloth system and the character creation system to customize the aspect of the player, including its visual elements, including blendshapes and accessories

{% tabs %}
{% tab title="Armor Preview" %}
{% embed url="<https://streamable.com/7pkmbc>" %}
{% endtab %}

{% tab title="Armor Preview 2" %}
{% embed url="<https://streamable.com/isowed>" %}
{% endtab %}

{% tab title="Untitled" %}
{% embed url="<https://streamable.com/7dvig1>" %}
{% endtab %}
{% endtabs %}

* It also has options to set different view perspectives according to the zone to edit, like face, head, full body, etc.... with easy settings for it too:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FcKUPzIVh1SrclclHZx0k%2F2?alt=media)

{% embed url="<https://streamable.com/8vyvrl>" %}

* Here is the main armor/cloth system working on the character on the action, allowing to affect both, aspect and stats and other values on the player:
* <https://streamable.com/rgacik>
* In this case, each armor piece increases the max health by 10 units and 370 more if the full armor (7 pieces) are equipped together (base health 100 + (10\*7) + 370 = 500), here is the example for the full armor stats affected:

&#x20;![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FHoZfQ0Ql8mTwpHVZ8vcb%2F3?alt=media)

* <https://streamable.com/adq0j3>
* Added fully functional character creation at the home menu and sent that info to the new game scene, so the player starts with both, the equipment selected and the blend shapes configured:

{% embed url="<https://streamable.com/gc1lhu>" %}

Here is another example of the character creation having now the starting set on the proper customization slots.

{% embed url="<https://streamable.com/oifia0>" %}

* Here is another example of the armor/cloth system during first person, as the character meshes are reactivated temporally in that state.

{% embed url="<https://streamable.com/hkq605>" %}

* Configured the armor/cloth system on the AI, and it allows to send signals from the health system dropping their armor pieces as pickups (or destroy them) in both the AI and player (it can be disabled as needed)

{% embed url="<https://streamable.com/x00wu0>" %}

* Added the options on the armor/cloth system for the values which can be configured on any piece to affect the stats and elements on the character, to affect also to damage types, for either resistances or weakness for it:

● ![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F1UWgmbsqQwXcin6qHact%2F4?alt=media)

* Added checks to disable all its meshes properly on any external situation, like shape-shifting or any state where the body mesh is disabled.

{% embed url="<https://streamable.com/ow0rfy>" %}

* Added a creator wizard tool to configure new armor/cloth sets, which creates the inventory object pickups and the scriptable objects info for these elements:

&#x20;![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FcROcMsUsgCD7BumyzlRm%2F5?alt=media)

* Here is a preview of the new armor/cloth system to configure the info of a set on a character and using the creator wizard to configure that info as scriptable objects, which will also create inventory objects for them automatically.

{% embed url="<https://youtu.be/IKTJJWIe7w0>" %}

* Here is another example of character creation and customization.

{% embed url="<https://streamable.com/ylia3o>" %}

* Added a tool to get the character meshes of each armor set, so they can be used to create the icons of each inventory object easily
* Added options on the armor set creator to allow to configure on each piece if it contains values for stats, skills, abilities, or damage type resistance/weakness:

&#x20;![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FvPUoLkSisMZSHLgYgNyN%2F6?alt=media)

* Here is an option on the armor/cloth system working on the AI with an option to select a random set on start, so each one can start the game with a randomly selected set, each one with its properties, abilities, stats, and other values.

{% embed url="<https://streamable.com/ono2bj>" %}

### FREE CLIMB SYSTEM

* Added a free climb system, inspired by the **Breath of the Wild**, here are some initial results.

{% embed url="<https://streamable.com/awrrsl>" %}

* It allows to climb on top of surfaces, check for the sides to move around very closed places or corners, animation curves to adjust the movement, and more.

{% embed url="<https://streamable.com/jr3788>" %}

* It includes interaction with the hook, checking of surface for feet, hanging just from hands or place the feet too and more interactions (polished in the process too).

{% embed url="<https://streamable.com/tdu7um>" %}

* It also allows to move on rotating or moving objects.

{% embed url="<https://streamable.com/hdevcu>" %}

* Added option of stamina on the free climb system, with separated values for regular and fast movement on it, so the player will fall if the stamina reaches 0 (and can't grab to the surface either until it starts to refill itself).

{% embed url="<https://streamable.com/ga5lxh>" %}

* Added an option on the climbing system, to slide down the surface, along with moving to the sides too.

{% embed url="<https://streamable.com/4jr2bi>" %}

* Here is also an example of the climb system transitions between the third and first persona and the climb on top action, all the elements of the climb system work on the first person too.

{% embed url="<https://streamable.com/zgbm56>" %}

### LOCALIZATION/LANGUAGE SYSTEM

* here is a regular workflow of the localization system, I have improved some internal parts of it (including being able to use it on builds, as before, it was using functions only available on the editor) along with adding some minor parts inside its editor.

{% embed url="<https://streamable.com/pwbpak>" %}

* Added a few localization elements, improved code on many parts for performance, and tweak some elements

### ACTION SYSTEM

* Added a kind of action system creation wizard tool, so you can set the main info and the system will add automatically the action system on it, so it will be just that and adjust the animator, without extra steps, to make it more automatic:

{% embed url="<https://streamable.com/v05kq9>" %}

* Of course, it can be used on both AI and players, since all of them use the same components

### SAVE SYSTEM

* Added the loading screen scene

{% embed url="<https://streamable.com/txqgxw>" %}

* Here is an example of a vehicle configured through the general drive/rider system to move in between scenes just like the rest of the GKC vehicles (I will show tomorrow an example with UVC for example).

{% embed url="<https://streamable.com/1blxgz>" %}

* Configured the animal to ride examples to be managed through the save system and the scene managers, so they can move between scenes properly as the rest of the dynamic objects.

{% embed url="<https://streamable.com/2qlmkb>" %}

* Here is a test for the scene manager to move objects to ride in between scenes for external vehicle controllers, such as Malbers Animal Controller for example.

{% embed url="<https://streamable.com/rso8jb>" %}

* Configured a garage example to store vehicles there, just by using the regular scene manager and dynamic save system on scene elements:

{% embed url="<https://streamable.com/tbixii>" %}
