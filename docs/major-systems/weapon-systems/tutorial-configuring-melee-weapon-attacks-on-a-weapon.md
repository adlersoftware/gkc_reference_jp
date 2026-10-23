# Tutorial - Configuring Melee Weapon Attacks on a Weapon

How to configure the weapon attacks on a weapon itself

These objects are the Melee Weapons themselves. Each one contains its own attack in the **Grab Physical Object Melee Attack System** component.

![The two key locations.](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FabyPuld4rEv9RlfqTgYi%2Fmeleeattack1.png?alt=media\&token=ef3f2e42-df53-4c30-9cc5-b9c94caf6d08)

Under the **Attack List Settings**, there's the **Attack Info List** which has the moves available.

![The Attack List Settings location.](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FCjrih0CxI55jIa0QBjqz%2Fmeleeattack2.png?alt=media\&token=783d1f2d-3eaa-4360-a5d3-e935755a1217)

It also contains the options for **Events** and the size for the damage detection including its offset in case you need to move the position of the trigger.

![Location of the Event Settings and Damage Trigger](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FdENwX1KriYiTey4bQGVI%2Fmeleeattack3.png?alt=media\&token=9a0c8805-2a93-4d67-adfa-2db3fdd0209f)

This is the most important part.  The Attack ability itself.

![Location of the Damage Delay Settings.](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FoW8UPk454RJhBMWbgIyG%2Fmeleeattack4.png?alt=media\&token=48b4d3dc-0fd4-4d8c-8a2e-1b3536651c3c)

On each Attack you have the Damage Trigger Detection which uses a delay to activate the damage detection, using the % values of the animation, so you have a swing animation.

There is a time where the character makes the movement for the attack where he puts the melee weapon on a position and then, it makes the swing, so that is the delay configured before activating the slice.

![Where the delay is located.](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FFkpenAeEQI8SQ3hMzHpP%2Fmeleeattack5.png?alt=media\&token=3d6f2741-75ae-4d23-b274-e61bec3f708f)

So that 0.2 value is the % (20%) where the swing starts, so at that moment, the damage detection is activated.
