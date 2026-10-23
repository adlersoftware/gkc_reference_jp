# Emerald AI

This page covers the integration of Emerald AI and Game Kit Controller.

## What is Emerald AI?

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McPlJkhjo8vZKHme4Yk%2F-McPrdHVoEFco427xHrj%2Fgkc-doc-integration-emerald-ai-header.png?alt=media\&token=ae15e3e4-c994-46da-90a7-247d4aeb6c8b)

**Emerald AI** allows developers to quickly create engaging dynamic AI with 100's of AAA quality features, all without having to write a single line of code! Emerald's editor is designed to make creating AI easy, yet incredibly customizable.\
\
Emerald caters to all kinds of developers and offers everything users would expect from an all-in-one AI system.

{% hint style="info" %}
You can find more information about **Emerald AI**, and its documentation and also purchase it over on the [Unity Asset Store](https://assetstore.unity.com/packages/tools/ai/emerald-ai-2-0-40199).
{% endhint %}

## Inspector Settings

**Black Horizon Studios** *(The maker of Emerald AI)* has a tutorial video showing the inspector changes needed to integration **Emerald AI** and **Game Kit Controller**.&#x20;

If you'd rather just get a step by step instructions for the inspector changes you can view these in the tab below labelled "Step by Step Instructions".

{% tabs %}
{% tab title="Video Instructions" %}
{% embed url="<https://www.youtube.com/watch?v=miCpkYpyZ_E>" %}

{% hint style="warning" %}
While the video also covers the code changes, these are **now outdated** *(as of GKC v3.03-1+)*, you can find the **up to date code changes needed below**
{% endhint %}
{% endtab %}

{% tab title="Step by Step Instructions" %}

### Step by Step Instructions

Follow these easy steps to get your **Emerald AI NPC** setup to work with **GKC**.

1. Select the NPC with the Emerald AI component attached and change it's Unity tag to **enemy**.
2. Next change the layer of the NPC to **npc**.
   1. If you receive a popup from Unity with the following "**Do you want to set layer npc for all child objects as well?**" Press the **No, this object only** button.
3. In the Emerald AI System component go to the **Detection & Tags** tab and select **Tag Options**.
   1. Change the **Emerald Unity Tag** field to **enemy**.
   2. Then under **Detection Layers** select **player** and **npc**, and deselect anything else, unless it's needed for other parts of your project.

That's it for inspector setting changes, next you'll need to make some script changes as outlined below.
{% endtab %}
{% endtabs %}

## Script Changes

### Part #1

First you'll need to open the **`EmeraldAIPlayerDamage.cs`** script found in the Emerald AI directory  `Assets/Emerald AI/Scripts/Components/` in your favourite editor and **add the following code after** the `DamagePlayerStandard()` method:&#x20;

```csharp
/// <summary>
/// Applies damage to a Game Kit Controller controlled player.
/// </summary>
/// <param name="DamageAmount">The amount of damage to deal to the GKC player.</param>
void DamageGameKitController(int DamageAmount, GameObject attacker)
{
    applyDamage.checkToDamageGKCCharacterExternally (DamageAmount,
    gameObject, attacker);
}

```

Then **in the same file**, add the following **inside** the `SendPlayerDamage` method:

```csharp
// Send damage to GKC player
GameObject targetObject = null;

if (Target != null){
    targetObject = Target.gameObject;
}

DamageGameKitController(DamageAmount, targetObject);
```

You can now save the `EmeraldAIPlayerDamage.cs` script and move onto the next step below.

### Part #2

The next part can be done in two ways, the **first is the recommended way** to add the integration. The **second option isn't recommended** but can be used if you don't want to use inheritance.

{% tabs %}
{% tab title="Recommended" %}

### Recommended Method

Open the **`EmeraldAISystem.cs`** script found in the the Emerald AI directory `Assets/Emerald AI/Scripts/System` in your favourite editor.

First at the top of the script where the class is defined you need to replace **`MonoBehaviour`** inheritance with **`healthManagement`** - At the time of writing this at *line 20*. \
\
The class definition should then look like the following:

```csharp
public class EmeraldAISystem : healthManagement
```

After changing the script inheritance, and in the same script **add the following code after** the `SendEmeraldDamage()` method:

```csharp
/// <summary>
/// Game Kit Controller Integration
///
/// Applies damage to the player via the GKC healthManagement class.
/// </summary>
public override void setDamageWithHealthManagement(float damageAmount,
    Vector3 fromDirection, Vector3 damagePos, GameObject attacker, GameObject projectile,
    bool damageConstant,
    bool searchClosestWeakSpot, bool ignoreShield, bool
    ignoreDamageInScreen, bool damageCanBeBlocked, bool
    canActivateReactionSystemTemporally, int damageReactionID, int damageTypeID)
{
Damage((int)damageAmount, EmeraldAISystem.TargetType.Player);
}
```

{% hint style="success" %}
**That's it!** Congratulations, Game Kit Controller is now integrated with **Emerald AI** in your project :partying\_face::raised\_hands:&#x20;

Now you can hunt that T-Rex down and it'll no longer be invincible to your attacks... although neither will you... *\*PEW\* \*PEW\** :t\_rex::gun:&#x20;
{% endhint %}
{% endtab %}

{% tab title="Not Recommended" %}

### Not Recommended

{% hint style="warning" %}
**Wait!** Before you go further, this is not the best way to integration Emerald AI with GKC. Please consider using the recommended method in the first tab.
{% endhint %}

Open the **`applyDamage.cs`** script found in the the Game Kit Controller directory `Assets/Game Kit Controller/Scripts/Health` in your favourite editor.

First at the top of the script you'll see a few namespaces being included in the script *(before the class definition)*, after the **last one add `using EmeraldAI;`** so that the script now looks something along the lines of:

```csharp
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using EmeraldAI; // Emerald AI Integration

public class applyDamage : MonoBehaviour
{
```

After adding the `EmeraldAI` namespace to the top of the script you will need to **uncomment** **the** **Emerald AI specific code at the bottom** of the **`checkHealth()`** and **`checkCanBeDamaged()`** methods and save the script.

{% hint style="success" %}
**That's it!** If you followed all of the above and uncommented the Emerald AI code then Game Kit Controller is now integrated with Emerald AI in your project :partying\_face:&#x20;
{% endhint %}
{% endtab %}
{% endtabs %}
