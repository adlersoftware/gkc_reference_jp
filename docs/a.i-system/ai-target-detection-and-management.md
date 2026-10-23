# AI Target Detection and Management

The AI uses two main elements to detect targets, a sphere trigger called “Fov Trigger” used as a range detection, storing all the possible targets inside of it and removing those which exits from it.

The other element is a capsule trigger called “View Trigger” used to detect and check possible threats using a delay for it, instead of identify the target immediately, like the sphere trigger does, so if the target remains inside the capsule trigger x amount of time, the AI will set that possible threat as a target to attack, but if the target exits from that trigger, the AI will lost track of it and return to its regular tasks.

You can edit these triggers to make them bigger or use any other trigger shape instead.

These two triggers send the signal of objects detected to the component “Find Objectives System”, which takes those objects and process it, to see if they are enemies or not to attack, obtaining the faction of the possible targets and checking if they are enemies or not, and activate the attack state according to that.

This component has different settings, including raycast to check targets, minimum distances to start to attack the current target and more.

One important setting is “Avoid enemies”. This is combined with the setting “None” in the field “Attack Type”, which will make this AI to run away from targets that usually would attack, moving in the opposite direction.

The vision range settings allows to configure the total range of view around the AI, taking the forward direction as the center and increasing that vision range to both sides. So you can customize the vision range to be for example 180 degrees, so the AI will see in forward and sides direction, but nothing besides that point, so any target behind the AI won’t be attacked until the direction of the AI or the position of that target reaches a visible range on that view.

The AI can also hear noises, made from firing weapons, steps, explosions, objects dropped or thrown, etc… allowing to also detect decibels, so if a noise has a lower decibel value that the AI can detect, it won’t be able to hear it. When a sound is detected, the AI will go to the position where the noise was caused, to investigate, and after x time, it will return to its previous task, according to the settings configured.

There are also options to configure if the AI can detect any hidden object on a fixed or free place (like inside a locker or in the grass crouching) and if the target is in stealth mode (through an ability for example).

The AI can also wander around, moving to random positions inside a range and with options to avoid to get to far away or move farther in each new position, along with event options, to for example, play random animations in each “rest” delay for the AI while waits to move to the next wander position.

There are also options to configure if the AI returns to the original position where it was located at the start in certain occasions, like after investigating a noise, or losing track of a target, etc...

And other settings allow, for example, make the AI to alert other partners of its faction when a target to attack is located, so the rest of the AI of that faction will also attack that target.

Finally, there are different event options, to be triggered on a target detection or a targe lossed and more similar situations.
