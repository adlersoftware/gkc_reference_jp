# Tutorial - Configure Local Multiplayer

In update 2.9, local multiplayer has been added, with the split-screen system as the current way to configure the cameras. This local multiplayer is in the beta state on 2.9 and will be complete in 3.0. But all the systems work properly without issues or errors, just need some extra additions and checks, like allowing to configure the player's in-game.

For now, the players can only be configured in editor time. For this, follow these steps:

Go to the gameObject called **Player and Menu Management** and to the inspector **Player Characters Manager.**

There, in the field **Current Number Of Players**, configure the number of players to use (for now using only from 1 to 4).

In this example, let's just use 2. After that, in **Camera State To Use**, select the screen camera configuration for the split-screen. For 2 players, there are different options like full screen with left and right side with every player, vertical, with a player on top and the other on the bottom, etc…

You can configure new camera distributions on the **Camera States List**, which configures the amount of main cameras (one per player) and the X, Y, W, and H values of every camera on the screen, setting these values for new players added:

After that, press these buttons in the next order: **Configure Players**, **Set Camera configuration**, **Set Players ID,** and **Assign Map System On Map Creator**. This will add the new players configured in the amount above, configure the split-screen cameras, set the player's ID to manage input for everyone of them, and add them to the main map system manager.

Here you can see the new player added along the previous one:

### Camera Configuration

You can select another type of camera setting, just by selecting a new one in the field **Camera State to Use** and pressing the button **Set Camera Configuration** again. Here are the same players in vertical:

You can also remove players by selecting a lower amount in the field **Current Number of Players** and pressing the above buttons in the same order (and make sure to select the Camera State To Use according to the number of players in the scene). So you can return to having just one player or add more.

In the hierarchy, you can see how the new players are added inside the main parent:

By default, all players are controlled with gamepad, so you will need the same amount of gamepads as players to play with them. There is an option to allow one player to use the keyboard. For this, go to any of the players to the gameObject called **Player Controller**, and in the inspector **Player Input Manager** set to true the field **Use Only Keyboard**.

After that, return to **Player Character Manager** and press **Set Players ID** button again.

Now if you go back to **Player Controller** gameObject and select the inspector **Player Controller**, you can see that the Player ID is 0:

When usually would 1. This is to make the system to know that this player won’t use a gamepad but the keyboard. Follow the same steps to configure the use of gamepad again (set as false the field Use Only Keyboard and press the button Set Players ID again).
