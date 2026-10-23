# Honor AI

This page covers the integration of Honor AI and Game Kit Controller.

## What is Honor AI?

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McQr0HehxWZQ3LQRcqD%2F-McQsdMpDbtyWOwBT5U0%2Fgkc-doc-integration-honor-ai-header.png?alt=media\&token=6d99d70f-c526-4a76-b94b-eda713c2d0cf)

**Honor AI** is an utility-based solution for easy creation of various AI agents like monsters, animals, followers, villagers, hunters etc, with just a few clicks!

No matter how experienced you are, you will find Honor AI helpful: less experienced developers will appreciate quick and easy AI setup with just a few clicks, while more advanced users can enjoy well written modular codebase, flexibility and extensibility of the whole system.

What makes Honor AI special is that AI logic isn't hardcoded, but rather designed in AI graphs that can be freely modified to your needs.

Thanks to such a solution Honor AI is the only AI solution on the Asset Store that solves the age-old problem of having to choose between a ready-made product that is inflexible or a low-level framework that doesn't provide game-ready features, as it provides benefits of both, without any compromises!

Honor AI provides you with all of AI essential systems: movement, spatial awareness, perception, combat, relationship, animations, audio, productivity tools and so much more!

{% hint style="info" %}
You can find more information about **Honor AI**, it's documentation and also purchase it over on the [Unity Asset Store](https://assetstore.unity.com/packages/tools/ai/rv-honor-ai-188764).
{% endhint %}

## Integration Steps

These integration steps are also provided **in the Honor AI documentation**.

### Step #1

Extract the `GameKitController.zip` archive file located in the `Integrations` directory of the **Honor AI** asset into the `Game Kit Controller` project directory.

### Step #2

To enable interactions between both assets you'll need to do the following:

1. For your **Honor AI** characters add the `GKCIntegration` component. This will also automatically add the necessary `CharacterFactionManager` component. This should be configured accordingly as per the GKC documentation - `Faction System` field has to be assigned.
2. For your **GKC** AI characters add the `HonorAIIntegration` component and assign all fields.

{% hint style="info" %}
*Note that both assets have their own relationship systems. You need to configure both of them in a consistent way to make sure that they all will recognize each other as enemies, otherwise it will result in a situation where AI from one asset attacks the other but not vice-versa.*
{% endhint %}

{% hint style="success" %}
**That's it!** Game Kit Controller is now integrated with **Honor AI** in your project :partying\_face::raised\_hands:

Is that a zombie horde behind you? Where's a gun when you need one!?! :person\_running::zombie::man\_zombie::zombie::man\_zombie:
{% endhint %}
