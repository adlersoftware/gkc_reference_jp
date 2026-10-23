# FAQ

Frequently Asked Questions about Game Kit Controller.

## Why is the player or AI falling into the ground or missing animations? <a href="#player-or-ai-falling-into-the-ground" id="player-or-ai-falling-into-the-ground"></a>

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McMCQgUtFo6dM0xByk5%2F-McMFOXf_ZcqG7mcSP-7%2FGKC_missing_animations.png?alt=media\&token=6a557f9b-910b-4a0b-a8fc-410621bb0bf0)

GKC uses Mixamo animations as placeholders for the base action system animations. Mixamo animations can't be included with the GKC package on the Unity Asset Store - which is what causes this issue.\
\
You will need to download and import these animations separately from one of the following links:&#x20;

* [Mixamo Placeholder Animations \[Google Drive\]](https://drive.google.com/file/d/1xefUnZHPeEQhk7UQEO4xxSVwlRCYyBXr/view?usp=sharing) ***\*Recommended***
* [Mixamo Placeholder Animations \[GitHub\]](https://github.com/sr3888/GKC-Public-Repository)

These animations are already configured to work on root motion properly (*like rotation based on current pose, loop time, adjust speed, etc…*). No extra changes are needed, just import the package and hit play.

{% hint style="warning" %}
If this issue still happens after importing the animation package, save your project and restart Unity. Everything should work after that.
{% endhint %}

{% hint style="info" %}
All these animations and copyrights belong to Mixamo. You can get these animations and more at the official Mixamo website: [https://www.mixamo.com/](https://www.mixamo.com/#/)
{% endhint %}

## Can I switch out the vehicle, character models and such? <a href="#switch-out-the-models" id="switch-out-the-models"></a>

**Of course**, most of the prefabs in the asset are made to be easy to replace their models with new ones. For example, in vehicles, all the meshes are a child of the Chassis GameObject.

## Can I make a suggestion, integration or feature request? <a href="#make-a-feature-request" id="make-a-feature-request"></a>

**Sure!** We have channels dedicated to just this over on our [Discord server](https://discord.gg/kUpeRZ8). Come on by and let us know what you have in mind:raised\_hands:&#x20;

## Can I use a terrain generation asset to create the level / map with your asset? <a href="#can-i-use-a-terrain-generation-asset" id="can-i-use-a-terrain-generation-asset"></a>

**Yes**, you shouldn't have any problems using other assets to create the level scene or terrain. The collision detection with them will work without issues. If you find this isn't the case though, give us a shout on our Discord server.

## How do I setup Game Kit Controller and HDRP? <a href="#gkc-and-hdrp" id="gkc-and-hdrp"></a>

Using GKC with **Unity**’**s** High Definition Render Pipeline (**HDRP**) only requires making a few adjustments to your project. This is covered in the tutorial video below:

{% embed url="<https://www.youtube.com/watch?v=CIDdd2ImnW4>" %}

## How do I setup Game Kit Controller and URP? <a href="#gkc-and-urp" id="gkc-and-urp"></a>

Using GKC with **Unity**’**s** Universal Render Pipeline (**URP**) only requires making a few adjustments to your project. This is covered in the tutorial video below:

{% embed url="<https://www.youtube.com/watch?v=FiWUDliXyrA>" %}

## **Can I add/edit the vehicles weapons? Or use other Unity Assets in combination with it… i.e. a cannon or a laser or rockets?** <a href="#can-i-add-or-edit-the-vehicles" id="can-i-add-or-edit-the-vehicles"></a>

Absolutely, the vehicle weapons, like powers and player weapons are totally customizable and have a huge amount of options including the following:

* Physics based, Impact settings, Fire rate, Speed
* Automatic / Single Firing modes
* Projectile settings
  * Explosive or non-explosive projectile
  * Explosion radius
  * Force
  * Number of projectiles to fire per-shot
  * Position
  * Create shells
  * Object penetration
  * Sound and particle options
  * Target tracking and heat seeking projectiles
  * Projective movement in a straight line, or using a trajectory
* The list goes on....&#x20;

This same configuration is used for weapon for player, vehicles, NPC with weapons and powers. And just like the vehicle meshes, you can change the weapon mesh easily as well.
