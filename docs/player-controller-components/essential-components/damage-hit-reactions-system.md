# Damage Hit Reactions System

The reaction system is called by the damage events of the health system internally, sending the signal of the damage received and position and mount so the system can know the direction and trigger the reaction which is basically to call to the action system of that character.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FtDbErXL6lOoS9uaByrCO%2Fdamagereaction.png?alt=media\&token=45b4fb48-0419-4104-9960-26ce681afeb5)

Each one having a main ID as the current category of reactions so you can have categories for reactions according to the state of the character like reactions from close combat, melee, etc...

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2Fesz1ZpSSbj6js2eAsrZU%2Fdamagereaction2.png?alt=media\&token=c1893294-7e16-4299-92ed-9cd708c773b2)

That is the default reaction type so it follows a similar logic to the melee attack types you have a list of stuff with a type so the system checks for the elements on the current state and triggers the closest to the direction of the attack.

Sending the signal for an action system it self to play that animation
