# Configure the Switch Character Companion

This system allows to configure additional characters in the game, setting them as AI which follows the player and can receive orders, like any regular friend AI would do, but in this case, the player can switch the control of these characters, setting the previous controller as AI and ther previous AI as the new controller used by the player. Any number of characters can be configured from 1 to any amount, so this can be used to make games similar to resident evil revelations 2, combining the gameplay with characters with different abilities who need to work together to keep moving in the game.

To configure this, it is the same steps as in the local multiplayer, so check that part of the doc to add 1 or any extra amount of characters.

Once you have done that, in the same **player characters manager** component, set the field **Set Current Character To Control** And AI At Start as true and in the field **Current Character To Control Name**, write the name of the character which will be used as the default player, setting the rest as

AI.

Once the game starts, you can switch between characters. By default, the key to change between characters is . (you can customize these actions keys in the input manager at any moment).
