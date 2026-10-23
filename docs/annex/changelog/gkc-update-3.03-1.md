# GKC Update 3.03-1

### INTEGRATIONS

* UMA 2
* Honor AI
* Added tutorial videos to configure URP and HDRP with GKC easily

### PLAYER CONTROLLER

* Added quick change direction, to make a turn of 180 degrees when moving from one direction to another quickly, to make the player to feel more dynamic and react better to the input

### PLAYER CAMERA

* New option to use pinch in and out on touch devices, allowing to trigger separate events in both directions, which can be used for different input actions. In this example, I have configured events to trigger the same functions used on the mouse wheel to move the camera closer or farther from the player. The option checks when enough distance has been applied (closer or farther from the initial) for both fingers and also, it checks that no other touch input is pressed, to avoid awkward situations and the minimum distance difference on the fingers to check events
* The pinch system has also an option to simulate two fingers in the unity editor, using the right and left mouse buttons for it, so the right mouse button simulates a fixed finger on screen where you press it and the left button is the one which moves on it

### LOCKED CAMERA

* Improved locked camera system related to the lock-on of targets and the way to manage the different types of camera controls in that view
* New option in locked camera allowing to rotate the camera to left and right separately through input horizontally (Y AXIS), more used for top down or isometric perspectives

### ACTION SYSTEM

* Added ladder system on third person, managed by the action system in most of its elements. It allows now to jump off from the ladder at any moment and even climb at the top if you reach that position with the jump
* Improved option to use the action system in first person, so the camera switches to third person on each action and returns to first person once the action is complete
* Added a tool for the action system, to replace any of the animations used on it in a single click, without need to go to the animator, search the layer, search the animation, then adjust it, etc.... so you can do that very quickly and easily, allowing also to set a new animation speed for the new animation and if it is mirrored or not. The rest is configured automatically.
* Configured an example of the action system (in this case use the bonfire) which activates the dialog system and resumes the action once the dialog is over.
* Configured a new open door examples, so instead of open, enter and close, it just open the door (and it is closed automatically after x time)
* Improved dodge/dash system to use different types of dash/dodge/roll actions that can be configured in a list of different movements and which can be activated by each weapon separately, allowing to asset a type of roll/dodge to each melee weapon

### FIRE WEAPONS

* Configured the slice characters into the plasma cutter, so along meshes, the plasma cutter can slice on characters too, apply damage to any other object and apply physics to the rest of objects
* Configured a sniper rifle weapon example, including a sight UI panel, and some fire values for the projectiles, physics, damage, fire rate, and delay to hit the target according to distance
* Added animation management system for weapons and arms in first person for fire weapons (melee weapons will be added on another update), allowing to use animations and transitions, such as reload, fire, aim, run, walk, draw, holster, etc…, including to manage reload of clips or shells, for regular pistols, rifles, shotguns and any type of weapon/reload type. It is also compatible with any weapons/model/animation pack of the asset store, such as Low poly FPS pack, HQ FPS animated weapons and any other
* Improved the melee hit with a fire weapon, allowing to activate the action system for it instead of using the default option, which uses IK on third person

### MELEE WEAPONS

* Added bow weapon type, with the arrow projectile statsconfigured through the weapon system, so it has all its options and possibilities, including the physics values and the gravity force to describe a parable movement
* The player can also move while using the bow and can holster or draw it at any moment, as it is managed by the same melee weapon system than the other melee weapons, including draw and holster animations
* Improved damage detection for both melee and close combat, for a more accurate detection of surfaces to damage, specially for the close combat system along with adding an option to trigger the damage reaction system on characters with any type of damage received, allowing to configure that in the damage settings
* So you can set if an element that applies damage activates this reaction system (to play animations based on the damage position on the body of a character for example) separately, like firing weapons, close combat, melee combat, collisions with objects, etc...
* New option for the melee/close combat to match the position/rotation of the player with the target that he is attacking, to face both direction and position if close enough.
* There are some options already to select the target to match, like use the movement input to select the next target to attack, so when the attack key is pressed, it takes the movement input along with the camera direction, to calculate the closest target to that direction (inside a range of distance and rotation). Or use the closest target to the screen center, so basically you attack what you look, inside the same ranges options. It has option to just take into account the closest target to the player and inside also a range of max/min distance and rotation of the player respect the target, to it is very customizable
* Added option to carry a single melee weapon at a time
* Added an option on the melee weapon to teleport the player to the current position of the melee weapon when this is thrown in any direction, in a similar way to Final Fantasy XV warp ability
* You can activate it at any moment once the weapon is thrown, or wait for the weapon to find and attach to any surface as well. There is also an option to call (or not) the weapon back to player's hand once the warp is complete
* Add options to the bow system which allows now to easily configure different types of settings for any arrow type. So far, I have configured 3 types, regular, poisonous and explosive, and any other can be configured easily
* Added an option to increase the arrow speed, force and damage according to how much time the player is pulling the bow for the current shoot, increasing these values the longer the player holds the fire (according to multiplier and max values fields)
* Added the option on the bow system to check the surface detected by the arrows, and activate a bounce if the surface type is an obstacle or a hard surface, also allowing to pick the arrows again when they have bounced on such surfaces (this can be disabled, so the arrow bounces, but can't be picked again)
* Added the option to use particles on the slice system, so it can instantiate any type of particles on the position of the slice, like blood on characters or sparks on metal. It works on any other weapon with the slice system, such as the plasma cutter (also, you can pick body parts to throw it to other AI to damage them on collision)
* Added a motorbike sword example (in reference to the chapter of the simpsons where Homer fights with another guy using motorbikes as swords xd)
* Added shield system for the meee combat, which can be carried as inventory objects and you can set if a weapon can use a shield or not, the movement values and damage reaction setting that it uses and block with the shield in free and strafe movement as well
* The shield can be also carried and used without carrying a melee weapon, like in dark souls and similar games
* Also, you can draw or sheathe the shield separately from the melee weapon, so you can toggle its use if you are carrying a shield with the melee weapon, using the quick access slots keys (in this case, by pressing the key 8, as that is the slot where the shield is placed) and the shield is placed on the character's back when the player sheathe the melee weapon as well and vice versa.
* Added shield system for AI as well, and it is also able to use just the shield without melee weapon, so they can just defend.
* Added option to activate the teleport ability on the melee weapon automatically when it detects a surface on the throw action, being almost equal to the warp ability of FFXV

### CLOSE COMBAT SYSTEM

* Added block action on the close combat system, allowing to move while blocking an attack and working in the same way as block on the melee combat system
* Added options to customise sounds, particles and events when detecting different surfaces using the close combat system, working in the same way as the one on the melee combat, and allowing to configure surfaces which can trigger hit damage reactions (or any other animation) when the characters hits or damage it

### DAMAGE REACTION SYSTEM

* Improved damage reaction system, to allow to configure categories of damage reactions, so each mode can have its own reaction animations, so modes like melee or close combat have different damage hit reaction animations, since the character is fighting with different elements. The transition in animations has been improved for this as well
* New option to trigger remote events on the object that has been blocked perfectly, so this can be used for example when the player makes a perfect block, the remote event can change the animation speed on the AI for a few seconds (all configurable) to make it slower and allow more reaction time
* Another option will activate the bullet time in general (or just slow all enemies speed and keep the player speed the same) when he makes a perfect dodge/roll on attack (when the invulnerability time is active and he receives a damage that is avoided from this inside a time range), similar to bayonetta
* New options to configure concrete reactions of a certain attack. For example, the last punch of the combo activates a reaction with an electrocuted animation, the kicks just use the regular damage direction to trigger each reaction according to that (with the last kick activating the push objects, which also pushes the enemy in front) and the first special attack (the multiple and quick punches) activates the stunned reaction
* New option for the damage reaction system, in this case, in the health component. When the AI health decreases, it has events configured to affect the main probability multiplier used to activate damage reaction animations, lowering that amount, so he becomes more resistant to it while he is more and more close to death

### ABILITIES SYSTEM

* Revamped jetpack system and the flying system, using a much better control and animations for it, And now, both modes allow to use powers and weapons without any limit on it, something which couldn't be done before. It uses animations now and like the free floating mode, zero gravity mode and jet pack system, it allows to use the weapons, powers and the rest of abilities on this mode too.
* It is also much smoother now and I want to add some more options for the air control and physics forces applied to it, allowing to have a more free control or a tighter one, according to the user's needs.
* The flying system allows now to move up and down with separated inputs, which is added to the current camera direction, used to move the player up and down as well, so you can combine that for its movement
* Added laser vision ability, similar to superman, including the option to use the slice system as well, to cut through objects, characters, etc…
* Adede ability to spawn objects, which can be used to spawn friendly AI (kind like minions), bombs, vehicles, or any other type of prefab object needed
* Based on the improved option to resurrect dead AI through events/function call, I have also added a simple ability example which can resurrects dead AI inside a radius (using the effect area system and the remote event system, so no extra scripts or class was needed for this), and of course, you can customize tags/layers to check, so you can use it only on friendly AI dead for example
* Added another ability example, a kind of zombie transformation spell, to turn AI enemy into a zombie ally which attacks the rest of enemies, without need of extra code, as it is activated by remote events and the zombie state on the AI
* Added a new ability example taking inspiration from the antigravity grenade from call of duty infinite warfare, as the systems to use that effect was already available (and it is very easy and quick to add new ability with new behaviors and a new simple script for it), by having access to the ragdoll activator component on any character on the scene. So the grenade access to it and plays with its gravity during a certain amount of time
* Added a new ability example allowing to place mines on the ground which can detect any type of target and explode (inspired in one of the weapons of the last of us), like enemies for example. Also, the mine can receive damage as any other object and explode due to it
* Another abilitiy added for manual mines, setting only one at a time, so the second time you press the put mine, it will explode, so you can wait for a certain moment to activate it (the trigger event can be activated, so it can be activated both manually or when detecting a target automatically)
* Added an option to use an animation to throw and pull for the grappling hook, to look more natural, instead of throwing the hook directly in third person (this can be configured to use it or not)
* Added brainwash ability example, to turn enemy AI into friendly AI

### MAGIC/SPELL CASTING MODE

* Configured a magic/spell casting mode example, in a similar way to the melee combat system, allowing to trigger a list of events configured by a category of magic attack, in order to use multiple input keys for different magic spells or attacks, and allowing to the player to keep moving, using separated animations for upper body and lower body
* It allows to configure a list of spells or special attacks to activate in a similar way to the melee or close combat system, allowing to organize the attacks by categories used by the input, so you can set any amount of input for each attack type

### INVENTORY

* Added quick access slots/hotbar system for the inventory, to allow to drop any object on them, from consumables, to fire weapons, melee weapons, regular inventory objects, quest objects, etc.... allowing also to change between melee mode and fire weapons mode directly according to the selected weapon, similar to games like deus ex
* Added option for reordering the inventory grid as you need, by dragging and dropping the slots into any other position
* Added arrows as inventory objects and the option on each bow type to configure if they use arrows from the inventory and which type, so if there are not arrows of x type of that kind of bow, the bow can't be fired. In the other side, you can have some bow with infinite arrows if you need and the arrows can be picked as regular inventory pickups as well
* Melee weapons are now managed as inventory objects as well

### VEHICLES

* Added an option on the vehicle system to set the default camera when enter and exit, so you can set that it always changes to third person view when getting on and set the view of the player for example, viceversa, always set both views in first person, etc... with any combination in between. Here the view changes to 3rd person when getting on and 1st person when getting off

### INTERACTION ELEMENTS

* New option for the interaction system to avoid to use or show an object if there is some obstacle between the player and the object, so for example, if an ammo pickup is inside a closet, even if the interaction trigger is outside the closet, the player can't pick the ammo until he can see the object (for example, by opening the closet)

### INPUT MANAGER

* Added a function to show/hide the touch buttons on screen for touch devices, but keeping the ability to be pressed on screen, which allows to use a gamepad on mobile and keep a clear screen, customizing the controls as its scheme as you need. Here a quick test I made for it

### OTHERS

* Pooling system, which can be used with any type of objects and which has been applied for weapons for now, but it will be also used for the rest of elements in next updates
* Improved hierarchy of the different systems of the player, organizing them by categories, alphabetic order, and if they are essential for the player to work properly or if they can be removed without problem if wanted, to make easier to locate them and customize, remove or disable them
* Also there are some components which were previously attached on the player controller gameObject which has moved to the other hierarchy, so this allows to have only the essential on him and have a cleaner and better organization in the asset
* Added an option on the health bar management system to show the info of the object in the screen directly, similar to how dark souls do it. This allows to also keep showing the other health bars which follow each object on the screen, and also, it will target the closest object to the screen center which has enable the option to show on the top bar of the screen instead of an icon following the object's position
* Added a resurrect event option on the health component and configured an example of it for the AI, as the elements were already included and just needed a couple of additions to reset the AI behavior in order to resurrect properly, so you have unkillable AI or zombie AI for example
* Configured an example of the waypoint camera, the navmesh system of the player and the pause/resume player actions component to configure a "cutscene" where the player walks through a set of positions automatically while the camera moves through waypoints. During that time, player actions are totally paused and they are resumed once the camera reaches its destiny and returns to player view
* Added an option on the dialogue system to allow to configure animations on each dialogue line with options to configure the name of the animation and a delay to activate it. It also allows to activate animations on both NPC and player to play the conversation between them
* Improved workflow on different systems, being more simpler, faster and easier to configure different elements of the asset
* Added and improved editor wizard creator
* Configured multiple templates for the player, so they can be selected with the character creator wizard, from default, to first person, simple version, only melee weapons, etc... as this wizard allows now select from a list of different templates (more types can be added easily without adding code, as this is managed by scriptable objects)

### AI

* Added Zombie AI type example, including a different animation tree for movement, attacks and wander state
* Added the option to create neutral AI on the character creator, so it can be used at any moment along with the friend and enemy AI. By default, this AI won't follow the player or any other faction, neither attack, but with the faction system, you can customize its reaction if attacked
* The AI is able to detect and follow a partner by configuring the faction to set as partner, which can be another AI and not only the player
* Improved brain AI for both melee and close combat systems
* The resurrected/zombie AI is managed by events, changing its attack mode to combat, and setting the ID to use on movement and combat for the value used for the zombie type in the animator. Also, the wandering animations change for zombie style as well
* Also, you can activate this zombie state directly on start on the AI, so it doesn't require to die first to activate it, so you can have both options, to either resurrect or have a zombie ready to use out of the box
* Added an option to configure a maximum range of detection for an AI when is damaged from a distance (previously, that distance didn't have a limit), so you can activate this option and limit how long the AI can detect an attacker from a distance when that attacker makes damage to that AI, for example, with a weapon shoot
* Added example of the execution action for the AI which is activated by default on the wander around state as example to use it (though it can be activated by many ways)

### ISSUES/BUGS FIXED

* Fixed a little bug related to hold an AI companion on ragdoll state, as now it pauses the get up function while the AI is carried.
* Improved performance in general parts of the code in most components, including input, AI, weapons management and more.
* Minor bugs fixed from pickups, inventory, weapons, melee, AI and others.

### INTEGRATIONS

* UMA 2
* Honor AI
* Added tutorial videos to configure URP and HDRP with GKC easily
