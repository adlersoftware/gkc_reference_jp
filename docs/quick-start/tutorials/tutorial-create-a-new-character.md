# Tutorial - Create a New Character

How to set up a new Humanoid Character

## Video Tutorial

{% embed url="<https://www.youtube.com/watch?v=lZB_5b4tUm0>" %}

## Written Tutorial

To set your model, follow these steps:

* In the tools bar press **Game Kit Controller** and **Create New Character**.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F0Fgo3V7ttac042rVQaYs%2FPicture11.jpg?alt=media\&token=dd022126-3f21-4531-9b5a-72369be2771f)

* In that window select a humanoid model and press the **Create Player** button. If you are in the Scene window, set the camera in the position where you want to place the player once is created.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FGqW7ZvKsl1K1MedkIPXq%2FPicture12.jpg?alt=media\&token=c9ab9a75-8496-4347-b191-6f5b2b752542)

* The new player will be placed in the scene, in the position where the editor camera is looking.
* This process creates the ragdoll of the new player automatically. Here you can see how it looks.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2Fl1h2At6ANArVPVkdv5xa%2FPicture14.jpg?alt=media\&token=1d003b26-8e20-4d61-a613-0a7651b65d6f)

{% hint style="warning" %}
**IMPORTANT**: the position and rotation of this object, Player 1 and Character and HUD elements must be (0,0,0) for both fields, if you drop the player prefab in the scene, that will be the values by default.
{% endhint %}

• This ragdoll can be configured or removed. For this go to **Ragdoll Builder** inspector, in the GameObject called “Character” and press the button Remove Ragdoll. You can also configure its scale and mass in the option Bone Settings.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FUv9KL3cXgziJeMdWcTDz%2FPicture15.jpg?alt=media\&token=402cab63-3072-4a94-a7be-1444ac7e7790)

* Then you will see the messages in the console about the weapons.
* These messages is to tell the user to configure the correct weapon parent, which is the place where every weapon is parented while is not being used, like the back, the leg, etc… By default, the weapon is placed in the back. To configure a better parent check the next steps.
