# GKC Update 3.03-2

### **INTEGRATIONS:**

* Universal AI System
* Randomation
* Edy’s Vehicle System
* Malber’s animal controller (dragon, wolf, birds, etc…)
* Space Combat Kit
* NWH vehicles and water physics
* And with the new general drive/ride system, any vehicle/animal controller from the asset store or custom made will work with GKC without extra steps or code needed for it

### PLAYER CONTROLLER

* &#x20;Improved the ground detection for situations where there are smalls gaps in between the ground, as the characters can move properly on it now.

{% embed url="<https://streamable.com/t0ahj5>" %}

### LOCKED CAMERA

* Added an option on the locked camera system to clamp the aim reticle to a circle. The previous option clamped the movement inside a circle, with this active, the clamp is made inside as well, so the reticle only moves on circles, like most top down/isometric/2.5d games used to do with their aim system based on a reticle direction to aim (ignore the red square, it is from the laser system and that has been adjusted properly.

{% embed url="<https://streamable.com/s39cs7>" %}

* Improved the use of range melee weapons on locked view, like the bow system or the option to fire projectiles from swords, allowing to aim accurately to any direction:

{% embed url="<https://streamable.com/27h8lu>" %}

### WEAPONS

* Added options on the action system to stop shooting and aiming fire weapons when the action is activated, like damage reactions.

{% embed url="<https://streamable.com/42ucba>" %}

*

### ABILITIES SYSTEM

* Added a menu for the abilities system to allow to edit the current abilities configured in the wheel selection, so you can order and organize the abilities which you can select as shortcut easily, in case the player starts to unlock a lot of them or you want to give options to organize it as the player prefers:
* <https://streamable.com/l80eu8>
* Added a new ability example to basically use an holographic target, to get the attention of the AI and maybe put it close to an explosive barrel, so they attack the barrel by accident and die from the explosion:
* <https://streamable.com/hw1ark>
* <https://streamable.com/g4jaia>
* Improved management of the icons on the abilities wheel for how they are scaled and placed according to the active abilities on it through the abilities editor ingame. Also, I added an example of the previous hologram player but this time, it explodes

when it receives damage, killing all AI around it in the process

* <https://streamable.com/smsc61>
* Here some minion summoning using animals instead of human characters:
* <https://streamable.com/h4pb1s>
* Here an example ability to reverse/toggle the player's gravity, similar to the game VVVVVV:
* <https://streamable.com/esq1pk>
* Here a test where the player can control AI on shape shifting mode, with generic models, like animals, through the override/possession system:
* <https://streamable.com/kv24>
* Here an example of the AI pet companion to summon and call to ride, similar to breath of the wild:
* <https://streamable.com/6jqpbb>

### **GENERIC MODEL SYSTEM** (animals, monsters, robots, etc…)

* Added full support of generic models, from animals, to monsters, robots, etc...allowing to configure both as characters to use on AI and player and to turn them ingame or at the start of it and turn back to humanoid shape or remain in that form for any amount of time. They can be also configured as “vehicle” to ride, driven by animations instead of just physics
* Here more progress on the support of generic models and riding animals through the vehicle system, I have finished the main system for it, I just need to improve the controller for the riding animal it self:
* <https://streamable.com/co8gg9>
* Some tests for generic models with the AI, and here some WIP with the AI wandering around and trigger animations on each pause:
* <https://streamable.com/7tbth8>
* They can also use the action system as well, allowing to set the a new category ID value, so according to the current model used for the character (AI or player), the same action can activate an animation for the new model, like howl for the wolf, or attacks for it, instead of the human animations
* Generic models can now activate the close combat as well, along with the reaction system. This has barely needed any addition, working with the current action system, with just a couple of options added to trigger different animations according to the model of the character, so the player can now attack on any other shape and react to damage as well:
* <https://streamable.com/yk4jbj>
* Here a WIP example of the AI with generic models attacking with the close combat system, working in the same way as the humanoid mode, allowing to customize each attack for each character model and getting damage as well:
* <https://streamable.com/7x478l>
* Improved ride system and the animals used for it will be able to perform same actions as the other characters and player, from attacks, to damage reactions, to use the action system, and anything in between:
* <https://streamable.com/orb8ow>
* Added the close combat system on animals to ride too, the ragdolls are also usable on the generic models and more. Here a mix of different elements on animals to ride:
* <https://streamable.com/9jupgg>
* Here more tests with different generic models, like animals, with examples of using the close combat system to trigger attacks on this mode:
* <https://streamable.com/mc01kq>
* Example of the ragdoll on generic models, as I added a generic ragdoll builder like in player and AI, so they will be able to use ragdoll and enter-exit that state:
* <https://streamable.com/0nhfj1>
* Added a generic model creator wizard tool, in order to make the system as easy to configure as possible:
* <https://streamable.com/q37i80>
* Here another example, riding a raccoon ala ant man style haha:
* <https://streamable.com/ncbnff>
* Generic models system is also compatible with the slice system:
* <https://streamable.com/7ycxui>
* Here a preview of the process to configure a new generic model with just a couple of clicks, the rest is mostly configuring the regular movement and jump animations:
* <https://youtu.be/XABt9LvzRaY>
* Here another example of riding an animal, this time, using the powerful deer to attack some poor enemy:
* <https://streamable.com/uynduf>
* Here a test to turn AI into any generic model in runtime through abilities/spells/magic, like a frog, disabling also its attack mode and make them harmless:
* <https://streamable.com/tfykqk>
* Here a test, with animals to ride on regular wander around state, allowing to ride them and in that case, they can follow the rider once he gets off (with options to ignore them after x time, here are just 10 seconds with the player) and repeat the cycle. The option can be disabled to resume the wander state when you get off, or follow the last rider forever
* <https://streamable.com/900q39>
* Also, you can put an inventory bank/bag on them, so they carry any amount of stuff, along your regular inventory

## SHAPE SHIFTING ABILITIES

* As the first step to add support of generic models to allow to use animals, monsters, robots and anything not human as character for player and AI, I have added an example through the abilities system to change the control of any object in game, like shape shifting, starting with vehicles:
* <https://streamable.com/id3e80>
* Here some more examples of the shapeshifting ability used with different objects, like a simple cube, a crate with pickups inside and an explosive barrel::
* <https://streamable.com/05rc9l>
* improvements for the support of generic models for the player and AI and the main structure is already complete, as I am improving different parts of it, which has been basically extending the main player controller component. Here the first results using malbers wolf free pack:
* <https://streamable.com/h2nyit>
* <https://streamable.com/ydh125>
* Improved sphere controller, allowing also to stick and climb on walls taking inspiration of the metroid spider ball mode:
* <https://streamable.com/2lh8ma>
* Here a trigger example which allows to activate/deactivate in runtime the shapeshifting ability of any character:
* <https://streamable.com/fyhcvi>
* Added option on the shape shifting to be ignored by the AI on animal mode:
* <https://streamable.com/zjqyo3>
* Here an example of the AI using abilities or powers to force the shape shifting on any

AI or player during x amount of time (or forever, or until get a certain condition):

* <https://streamable.com/mj45ei>
* Here an option to leave as active the generic model that a character will use for player or AI, so you can see properly on scene the model that will be used for it: ● <https://streamable.com/43jmnk>

**GENERAL RIDE/DRIVE SYSTEM** (Automatic integration with any vehicle/animal controller from the asset store or any external or custom controller)

* Added ride integration with malbers animal controller system from Malbers Animations , which will work on any of its animals packages, it will work with horse anim pro too, so all of his animals which have a character controller configured on them will be able to use it, with all the elements from malbers animals configured on them, attacks, throw fire, etc…
* I have finished the initial testing with this general integration for it. This new ride system can be used on vehicle controllers from the asset store too, so it can be used on any of this type of assets easily, taking just a couple of minutes to set up:
* <https://streamable.com/e38tjl>
* Here a test with birds to ride, through the general ride system and using malbers birds as example for it:
* <https://streamable.com/5yh4tb>
* Edy's Vehicle Physics has been integrated with GKC, it takes just a couple of minutes to adjust the ride system to any external vehicle controller:
* <https://streamable.com/7edtp6>
* Integration with randomation (a very nice vehicle controller with destructible parts) through the general drive/ride system:
* <https://streamable.com/u73p52>
* Here another preview of another integration test that I tried with a vehicle controller using the new general drive/ride system of GKC, this time, for NWH Vehicle Physics
* <https://streamable.com/8uffog>
* Here another test of the general drive/ride system of GKC with dynamic water physics 2 vehicles:
* <https://streamable.com/ndky0n>

### AI

* Added an option on the noise system for the hearing detection of the AI to force a sound to be heard even if the AI option to hear is disabled, so you can make them to notice certain types of noises if you need to, This is used for example on the hologram target, to call their attention in any possible case (of course, it can be disabled):
* <https://streamable.com/tcq04k>
* Here a new test for the generic models, for one AI attacking another AI (I have to configure a couple of tweaks for the attacks rate and target detection for the generic model)
* <https://streamable.com/q5ugmh>
* Here another WIP test of two generic model AI fighting each other (I have to tweak some values of the combat and reactions):
* <https://streamable.com/v6lxzj>
* Here a test that I made with a zombie AI spawning from the ground:
* <https://streamable.com/ypsfse>
* Added the main AI navmesh system to the generic ride/vehicle system, so the animals can move around given a navmesh target to reach. This will be used also for the wander around state on the animals to ride, so they can move around until you ride them. After that, they can return to wander state after x time or follow the last rider, in this case, the player
* <https://streamable.com/c1kzzy>
* Added integration with Universal AI System done and ready, including in the upcoming update 😄
* <https://streamable.com/0lduk1>
* Here an example of the AI turning other AI into zombie state by attacking them, turning them into the enemy faction and spreading the same change to other AI, becoming a high danger for the player pretty fast:
* <https://streamable.com/ihoy4x>
* <https://streamable.com/cg7fmo>
* Here a test for the animal AI (the generic models to ride), with target detection to avoid enemy factions on wander around state (it uses just the AI components, so it will be improved to use all its elements and features in next updates):
* <https://streamable.com/d79alt>
* Improved AI detection and target management, including when the AI has detected it and stills inside its range, so the AI can chase it around corners or behind any other obstacle which blocks the view of the AI or attack from longer distances: ● <https://streamable.com/me96e1>

### INPUT MANAGER

* Here an example to trigger a certain action using a combination of keys input, for example, to activate an ability. In this case, you can set any action to call, including other abilities, and use options to check if the keys are pressed in order and using a max delay to check for the second or third press (the console shows the keys pressed)
* <https://streamable.com/iao7c0>

### OTHERS

* Added a pop up window which only opens the first time that you execute one of the demo scenes of GKC, and only a single time, which is used to show some basic info about the initial setup of the asset and any other relevant message, like the step to import the animations:
* <https://streamable.com/qd05rk>
* Added option to make a character to play an animation through the action system at the start of the game (or when a character/AI is spawned for example):
* <https://streamable.com/fj40rj>
* Added a new option allows to set a direct transition to any animation on the action system, so the animation is played in the next frame, without smooth transition (crossfade), for elements like cutscenes, dialogues, etc.... or just to avoid a smooth transition, and play the animation directly
* Options to configure events when drawing/sheathing a melee weapon, like sounds or animations on the weapon it self, like in the lightsaber:
* <https://streamable.com/sma92j>
* Configured prefab examples to make a simple vendor through dialogue and allow to trigger events by giving inventory objects through the dialogue too like getting a reward of money by giving a wizard a special key from your inventory:
* <https://streamable.com/h0cbwv>
* To use this, I added an option on the dialogue system which allows to configure conditions to trigger one dialogue line or another based on the result of that condition check system, so this is all modular and independent

● ![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FCsSgMOgNBgQ5D0e5dMFi%2F0?alt=media)

* Improved gravity system on 2.5d, to make some small improvements, along with the test of the ability example to reverse the gravity direction of the player like in VVVVVV game:
* <https://streamable.com/gj3s81>
* Added a component to show any stat on screen, it can be used for any value, updating the content text at any moment (the example is the money on the left side, the right side is the default option of the money system it self): ● <https://streamable.com/9jk1qu>

### ISSUES/BUGS FIXED

● Minor adjustments and tweaks, along with polishing and removing of exceptions and issues on very certain circumstances, adding the checks needed to avoid any further

### WALL SLIDE JUMP SYSTEM

* Added an example of wall jump/slide, inspired in mario games and other similar platforms:
* <https://streamable.com/wi02mv>

### SLIDE SYSTEM

* Added new movement to add more dynamic actions on the player, this time, to slide on slopes with a certain inclination, allowing to move left and right, speed up or slow down the movement and jump:
* <https://streamable.com/4ay8ig>
* Here a cool test with the slide system and some additions, like events to activate dust particles, speed settings to move faster or slower on certain surfaces and more, along using wall running, paraglider and other stuff:
* <https://streamable.com/173zcp>
* Here two different examples of how to slide in a very long surface:
* <https://streamable.com/fbgg05>
* By shooting at the spheres, the next slider is activated:
* <https://streamable.com/mkvyry>
* Added an option on the slide system to be used on any moment through input (by detecting if the player is running and uses the crouch action key by default) so instead of crouching, he will start to slide, in the same way as fixed slide zones:
* <https://streamable.com/vg3xq3>
* Improved the slide and teleport systems, now allowing to adhere and rotate to the ground normal when sliding, so you can make movements like this, and adding the same option as the grappling hook points with the teleport system: ● <https://streamable.com/99882f>

### SWIM SYSTEM

* Added new swim system, which allows to both swim and dive and use all the weapons, powers, abilities and anything else on it, including to move faster, use water currents, oxygen, enter-exit on water from ground or climb out of it, detect vehicles to trigger options on it and more
* <https://streamable.com/oi0aef>
* <https://streamable.com/wr1v63>

{% embed url="<https://www.youtube.com/watch?v=tpn26_gjHm4>" %}

* Added trigger events for camera effects underwater, sounds, particles and jump on water or climb to a surface it the player detects one close enough while on the water:
* <https://streamable.com/42irux>
* Here an example of dying from depleted oxygen:
* <https://streamable.com/ifwbju>
* Wind effects works underwater too
* <https://streamable.com/4x5bjg>
* Added options for how vehicles react when entering in water where player can swim/dive, similar to some GTA games, where vehicle interaction is disabled or even explode, along with physics forces for the vehicle underwater:
* <https://streamable.com/y63vn7>
* The swim system zones can send remote events, like deactivating fire on characters when getting in:
* <https://streamable.com/tmesmn>

### BODY MOUNT POINT SYSTEM

* Added improvements for how the characters carry objects on its skeleton, like hands for fire and melee weapons, having a mount point system now. So the adjustment of melee and fire weapons will be much faster and easier now, having to modify just the general mount point of right and left hand once:
* <https://streamable.com/pgs00j>
* I have finished the improved mount points system, which will allow to manage much better how objects are carried inside character's body (player and AI), related to fire and melee weapons and other objects, speeding up the creation of new characters even more
* Here more info of the body mount point system, as it allows to configure any list of parts that are placed in a character (AI or player) and manage them easily, as they are also moved from the current model to the new one when a new model is applied:
* <https://streamable.com/oj38be>
* This is also used by melee and fire weapons, as they are placed inside these mount points now instead of the bones directly, reducing the extra adjustments needed to use these elements in new characters, having all in the proper position out of the box

●

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FdDXDIKqP04Jo8WEMcsah%2F1?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FH2ngRfGCHBnNDP7FXkGX%2F2?alt=media)

●

### TOOLBAR SYSTEM

* Added a new toolbar system which is very customizable and it has many actions as shortcuts in order to make the asset easier and faster to use or simplify some steps, like select main player, focus on a certain component, move the player around, toggle camera view, etc…:

{% embed url="<https://youtu.be/azac7rGsQzc>" %}
