# Dialogue System for Unity

This page covers the integration of Dialogue System for Unity from PixelCrushers

## What is Dialogue System for Unity?

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FU67Xl59C1usovnDRcjWt%2Fimage.png?alt=media&amp;token=133df1d5-ec43-4df5-a412-15e205221b4e" alt=""><figcaption></figcaption></figure>

The powerful, top-rated dialogue system used in **Disco Elysium**, **Lake**, **Suzerain**, **Peglin**, **Jenny LeClue**, and many many more, the **Dialogue System for Unity** makes it easy to add interactive dialogue and quests to your game.&#x20;

It's a complete, robust solution including a visual node-based editor, dialogue UIs, cutscenes, quest logs, save/load, and more.&#x20;

The core is a lean, efficient conversation system. A large collection of included, optional add-ons make it quick and easy to drop conversations into your project and integrate them with other assets.&#x20;

No scripting required. Complete C# source included.

{% hint style="info" %}
You can find more information about **Animal Controller**, and its documentation and also purchase it over on the [Unity Asset Store](https://assetstore.unity.com/packages/tools/animation/animal-controller-148877).
{% endhint %}

## Video Tutorial

{% embed url="<https://www.youtube.com/watch?v=xRMsRyQ8Dk0>" %}

## Written Tutorial

Open the first demo scene from *Dialogue System* asset content. Search the **GKC player prefab** called **"Player and Game Management"** and drop it on the scene, adjust its position and rotation as you need.

Disable the previous player and copy the components **Selector**, and paste it as new on the **Player Controller** gameObject from GKC, on the message that appears, press Add.

And finally, copy and paste the **Dialogue System Events** on the **Player Controller**.

Search the words "Pause Resume" on the project searcher tool and drop that prefab on the scene, disable its collider trigger.

On the **Dialogues System Events**, remove the previous calls on the events of **Conversation Events** and configure the calls to pause and resume the player, with parameters true to pause and false to resume with the function **PauseOrPlayPlayerComponents**.

Finally, go to the **Selector** component, and set a new key for the interaction, like for example E as it is the default key used on interaction in GKC.

And with that, the system is ready to work, pausing the player when the dialogue is in process and resuming it once the dialogue is over, along with the rest of the interactions with the environment.

{% hint style="success" %}
**That's it!** Now you can use Dialogue System conversations in GKC. You can also continue to use GKC dialogue as well in combination!
{% endhint %}
