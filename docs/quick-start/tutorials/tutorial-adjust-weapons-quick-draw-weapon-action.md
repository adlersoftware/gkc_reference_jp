# Tutorial - Adjust Weapons Quick Draw Weapon Action

How to adjust weapons for the the Quick Draw Weapon Action

## Overview

In the third-person view, there is an option on weapons that allows making a quick draw of the weapon placing it directly on the dominant player’s hand. There is also an option to carry a weapon on the player’s dominant hand when he is not aiming, without IK.

For both options, it is necessary to adjust the position of the weapon on the player’s dominant hand, since every model has a different bone orientation, this needs to be done manually if you use any of the above options (there are a **few weapons using these options by default, like the shotgun, laser miner, double shotgun, homing missiles, spear launcher, and laser shooter**).

This is a very quick and easy step, with the next steps:

* Select the weapon that you want to adjust in the hierarchy, open the **IK Weapon System** inspector and press the button **Show Element Settings:**
* Press the button **Show Third Person Settings** and **Show Single Weapon Settings**. ● The option to use the quick draw weapon is in **Quick Draw Settings**:
* And the option to carry a weapon on the player’s dominant hand while not aiming is in

### **Deactivate IK If Not Aiming Settings:**

* This is also where the hand position is adjusted to place the weapon on it while not aiming it
* To adjust the position, press play, draw the weapon which you are adjusting, aim the weapon and then stop aiming. You may see that the weapon is placed in an incorrect position and rotation when the player draws the weapon. Don’t worry, this is why these steps are being done:
* Without keeping the weapon, press the button **Copy Weapon Position In Hand**
* Stop the game and press the button **Paste Weapon Position In Hand**

And that is it, the weapon now will be placed properly on player’s hand when the quick draw action is enabled on that weapon, looking like this when the player draws that weapon with the position adjusted:

The quick draw can be also used without deactivating the IK system on player’s arms, like for example, the double shotgun, which by default is configured like that:

This weapon has the option to make a quick draw enabled and deactivate IK option disabled, so the weapon is first placed in the player’s dominant hand and then moved to a walk position, like in the capture above.

For this, set to false the field **Deactivate IK If Not Aiming**, located in the same part that is has been used for this explanation:
