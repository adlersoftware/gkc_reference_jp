# Tutorial - Add Action System By Input

## Youtube Tutorial

{% embed url="<https://youtu.be/AEAc-5BR_VQ>" %}
Youtube Tutorial
{% endembed %}

## Written Tutorial

Add a new action on the input and configure the event to activate the animation action by going clicking on the root of the prefab (**Player and Game Management**), then the **Input Manager** component.

![Input Manager Window](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FczdXPaapTrGDxWNcWee6%2F0?alt=media)

Scroll down to the section **Multi-Input List** and open the **Multi Axes List** menu.

![Multi Input List](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FqrSx8eq5EBLsDDqiwnV2%2F1?alt=media)

Then open **Player Controller** in the **Multi-Input List** and select **Add Action** to add a new one. In this tutorial, we’ll be creating the action, Simple Kick. You can also put a Keyboard and/or Joystick input to activate the action here.

![Simple Kick Action](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F3ZZlb0cqnjXKWeW0M9FN%2F2?alt=media)

Next, navigate to the **Player Controller** game object on the player character and scroll down to the **Player Input Manager**.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FKEOAufkhX06I12MuaQ3h%2F3?alt=media)

Then scroll down to **Multi Axes List** and select the **Player Controller** section as we did on the **Player and Game Management** component. Click **Add Action** as before, except now on the Axe dropdown, you will see the Simple Kick Action we made. Select that. Set the Button Press Type to Get Key Down to have it execute when the input key is pressed down.

Click the plus under **Button Event** to add a new Event and drag the **Player Action System** prefab for the hierarchy into the field to assign it.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FmhrHmjUn9kcCF8JVo2bV%2F4?alt=media)

Select No Function, go to **playerActionSystem** and select **activateCustomAction** (string). For the string enter in our new action, Simple Kick.

Next, we’ll configure the action values to play a specific animation using its name and duration as main parameters. First, we’ll go back to the **Player Action System** game object and add a new game object named Simple Kick that will hold our settings for Simple Kick.

Add a game object under **Player Action System** and add the **Action System** component to it.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FpCK1Ab8JTUpdsBYbtq3q%2F5?alt=media)

Scroll down to the **Action Info List** and click **Add Action**. The Name and Action Name are our action, Simple Kick. For this example, we’ll enable **Pause Player Actions Input** so that other inputs are recognized while the action is active. Then we’ll enable **Resume Player After Action** so that the player regains control after the Action is finished.

Now we need to add an animation to our action. Open the **Animator** window and make sure you have the Base Layer selected. Click the state machine **New Actions**, right-click the canvas and add a new **State Machine**. Name it Simple Kick.

Open the new state machine we just created and add a **New State**. This will be named, you guessed it, Simple Kick. Add a kicking animation to the Motion field. There’s one included in the Mixamo Animation package, Sword and Shield Kick. Note the Animation Time of your kick animation, we’ll be using that later.

Add a transition from Simple Kick to the state **Main Movement>Grounded>Grounded**. Select the transition and uncheck **Has Exit Time**. Under Conditions add the Action Active parameter and set it to false.

Navigate to **the Custom Action State Info Settings** and open the **Custom Action State Info List**.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F04DHR7SH46pN78hlIDQ6%2F6?alt=media)

Add a new state by increasing the Size by one. There are 46 in this example, so we’ll increase it to 47. The name is our action, Simple Kick, like the rest of the fields. For **Main Action System**, we’ll drag our Simple Kick game object that we just added to assign it.

Go back to the Simple Kick action we added under **Player Action System**, and **under Action Main Settings**, set the **Animation Duration** to our kick animation. In our example, it’s 1.2. Next check **Action Uses Movement**.

![
](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F97pXVOzUnLYCRYXKRBNL%2F7?alt=media)

That’s it! The input will now call this new custom action we made, taking care of pausing and resuming the rest of the states, input, and actions of the character.

Now, let’s add some interaction and flourish to our kick. We’ll configure a component to push objects in front of the player that is kicked using the events options of the action. Including any needed delays.

Under the **Player Controller** game object, select the **Push Objects on Running Slide** game object and duplicate it. We’ll rename it to **Simple Kick Push**.

Return to the Simple Kick game object under the **Player Action System**. Under **Event Info List** click Add Event. In Element 0, we’ll set the **Delay to Activate** to 0.5. Add a new event in **Event To Use** and drag the **Simple Kick Push** game object into our field. Select the Function pushObjectsPower > setPowerEnabledState (bool) and check it.

Add another Event to the **Event Info List**. Element 1 will have a **Delay to Activate** of 1. Drag over the **Simple Kick Push** again into the field. Select the same function as before, setPowerEnabledState, and leave it unchecked.

![
](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FQdu26SsGRKPIihDPap4Z%2F8?alt=media)

That’s it! Happy Kicking!
