# Importing GKC

It's really easy to setup Game Kit Controller in your project! Follow the steps below to import the package and get started!

## Step #1: New Project or Existing Project

### New Project

If you are importing GKC into a new project then all you need to do is import the package and leave everything checked.\
\
That's it, you can skip the rest of this page, you're good to start making the game of your dreams!:space\_invader:You can move onto the next section using the button below.

{% content-ref url="/pages/-McMkfQvi5oxkT7npJSU" %}
[Tutorials](/docs/quick-start/tutorials.md)
{% endcontent-ref %}

### Existing Project

If you are importing GKC into an **existing project** then you'll need to **uncheck the option to import the project settings** and then continue onto [**Step #2**](/docs/quick-start/get-started/importing-gkc.md#step-2).

## Step #2: Add Key Mappings to the Input Manager <a href="#step-2" id="step-2"></a>

When importing GKC into an existing project, or if you imported GKC without the project settings then you'll need to add the axes below into the Unity Input Manager (**Edit > Project Settings > Input Manager**) if you want to **support using a gamepad**.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McMKSC8b73op_GA_y0g%2F-McMSlLRIyeAiyv1XbgF%2Fgkc-doc-axes-mappings.png?alt=media\&token=20b68a16-2d8d-4a02-b3e7-0fd92139a331)

These are the key mappings for four players when using local multiplayer *(i.e. same screen multiplayer)*, but you can add just one if you are not going to use the local multiplayer functionality in your game.

{% hint style="danger" %}
**Don't overwrite or remove the default axes** set by Unity when adding the above axes - because these are also used and will be needed by GKC.
{% endhint %}

The key mapping values for each input above are identical for each the variant *(i.e. player/input)*, only the variant names and the joystick number are different.\
\
For example **Horizontal X1** has the **same values** as **Horizontal X2, X3 and X4** with only the **input "Name" and "Joy Num" being different**. On Horizontal X1 the Joy Num is **Joystick 1**, whereas on Horizontal X2 the Joy Num is **Joystick 2** etc. For the full breakdown of input values, you can check out the "*Full Breakdown*" tab of each section below.

### Horizontal X and Vertical Y

{% tabs %}
{% tab title="Overview" %}
![Horizontal X1 (X2, X3, X4) and Vertical Y1 (Y2, Y3, Y4) mappings](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McMKSC8b73op_GA_y0g%2F-McMY2ZjbMcZpXOA0SiE%2Fgkc-doc-axes-horizontal-x-vertical-y.png?alt=media\&token=a197fc6c-71f8-4e49-b97e-f8e4accc1325)
{% endtab %}

{% tab title="Full Breakdown" %}

### Horizontal X

| **Field**       | Horizontal X1 | Horizontal X2 | Horizontal X3 | Horizontal X4 |
| --------------- | ------------- | ------------- | ------------- | ------------- |
| **Name**        | Horizontal X1 | Horizontal X2 | Horizontal X3 | Horizontal X4 |
| **Gravity**     | 0             | 0             | 0             | 0             |
| **Dead**        | 0.19          | 0.19          | 0.19          | 0.19          |
| **Sensitivity** | 1             | 1             | 1             | 1             |
| **Invert**      | -             | -             | -             | -             |
| **Type**        | Joystick Axis | Joystick Axis | Joystick Axis | Joystick Axis |
| **Axis**        | X axis        | X axis        | X axis        | X axis        |
| **Joy Num**     | Joystick 1    | Joystick 2    | Joystick 3    | Joystick 4    |

### Vertical Y

| **Field**       | Vertical Y1                | Vertical Y2                | Vertical Y3                | Vertical Y4                |
| --------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| **Name**        | Vertical Y1                | Vertical Y2                | Vertical Y3                | Vertical Y4                |
| **Gravity**     | 0                          | 0                          | 0                          | 0                          |
| **Dead**        | 0.19                       | 0.19                       | 0.19                       | 0.19                       |
| **Sensitivity** | 1                          | 1                          | 1                          | 1                          |
| **Invert**      | :ballot\_box\_with\_check: | :ballot\_box\_with\_check: | :ballot\_box\_with\_check: | :ballot\_box\_with\_check: |
| **Type**        | Joystick Axis              | Joystick Axis              | Joystick Axis              | Joystick Axis              |
| **Axis**        | Y axis                     | Y axis                     | Y axis                     | Y axis                     |
| **Joy Num**     | Joystick 1                 | Joystick 2                 | Joystick 3                 | Joystick 4                 |
| {% endtab %}    |                            |                            |                            |                            |
| {% endtabs %}   |                            |                            |                            |                            |

### Mouse X and Mouse Y

{% tabs %}
{% tab title="Overview" %}
![Mouse X1 (X2, X3, X4) and Mouse Y1 (Y2, Y3, Y4) mappings](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McMKSC8b73op_GA_y0g%2F-McMZaae9rJtJO5M7Cv5%2Fgkc-doc-axes-mouse-x-mouse-y.png?alt=media\&token=66794630-1733-4380-b8db-ae537e2ba9d7)
{% endtab %}

{% tab title="Full Breakdown" %}

### Mouse X

| **Field**       | Mouse X1             | Mouse X2             | Mouse X3             | Mouse X4             |
| --------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| **Name**        | Mouse X1             | Mouse X2             | Mouse X3             | Mouse X4             |
| **Gravity**     | 0                    | 0                    | 0                    | 0                    |
| **Dead**        | 0.19                 | 0.19                 | 0.19                 | 0.19                 |
| **Sensitivity** | 1                    | 1                    | 1                    | 1                    |
| **Invert**      | -                    | -                    | -                    | -                    |
| **Type**        | Joystick Axis        | Joystick Axis        | Joystick Axis        | Joystick Axis        |
| **Axis**        | 4th axis (Joysticks) | 4th axis (Joysticks) | 4th axis (Joysticks) | 4th axis (Joysticks) |
| **Joy Num**     | Joystick 1           | Joystick 2           | Joystick 3           | Joystick 4           |

### Mouse Y

| **Field**       | Mouse Y1                   | Mouse Y2                   | Mouse Y3                   | Mouse Y4                   |
| --------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| **Name**        | Mouse Y1                   | Mouse Y2                   | Mouse Y3                   | Mouse Y4                   |
| **Gravity**     | 0                          | 0                          | 0                          | 0                          |
| **Dead**        | 0.19                       | 0.19                       | 0.19                       | 0.19                       |
| **Sensitivity** | 1                          | 1                          | 1                          | 1                          |
| **Invert**      | :ballot\_box\_with\_check: | :ballot\_box\_with\_check: | :ballot\_box\_with\_check: | :ballot\_box\_with\_check: |
| **Type**        | Joystick Axis              | Joystick Axis              | Joystick Axis              | Joystick Axis              |
| **Axis**        | 5th axis (Joysticks)       | 5th axis (Joysticks)       | 5th axis (Joysticks)       | 5th axis (Joysticks)       |
| **Joy Num**     | Joystick 1                 | Joystick 2                 | Joystick 3                 | Joystick 4                 |
| {% endtab %}    |                            |                            |                            |                            |
| {% endtabs %}   |                            |                            |                            |                            |

### Left Trigger and Right Trigger

{% tabs %}
{% tab title="Overview" %}
![Left Trigger 1 (2, 3, 4) and Right Trigger 1 (2, 3, 4) mappings](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McMKSC8b73op_GA_y0g%2F-McMa478R4AE4H9Ov8U_%2Fgkc-doc-axes-left-right-trigger.png?alt=media\&token=1090b103-b5aa-412c-b214-ab01ee16e378)
{% endtab %}

{% tab title="Full Breakdown" %}

### Left Trigger

| **Field**       | Left Trigger 1       | Left Trigger 2       | Left Trigger 3       | Left Trigger 4       |
| --------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| **Name**        | Left Trigger 1       | Left Trigger 2       | Left Trigger 3       | Left Trigger 4       |
| **Gravity**     | 1000                 | 1000                 | 1000                 | 1000                 |
| **Dead**        | 0.001                | 0.001                | 0.001                | 0.001                |
| **Sensitivity** | 100                  | 100                  | 100                  | 100                  |
| **Invert**      | -                    | -                    | -                    | -                    |
| **Type**        | Joystick Axis        | Joystick Axis        | Joystick Axis        | Joystick Axis        |
| **Axis**        | 9th axis (Joysticks) | 9th axis (Joysticks) | 9th axis (Joysticks) | 9th axis (Joysticks) |
| **Joy Num**     | Joystick 1           | Joystick 2           | Joystick 3           | Joystick 4           |

### Right Trigger

| **Field**       | Right Trigger 1       | Right Trigger 2       | Right Trigger 3       | Right Trigger 4       |
| --------------- | --------------------- | --------------------- | --------------------- | --------------------- |
| **Name**        | Right Trigger 1       | Right Trigger 2       | Right Trigger 3       | Right Trigger 4       |
| **Gravity**     | 1000                  | 1000                  | 1000                  | 1000                  |
| **Dead**        | 0.001                 | 0.001                 | 0.001                 | 0.001                 |
| **Sensitivity** | 100                   | 100                   | 100                   | 100                   |
| **Invert**      | -                     | -                     | -                     | -                     |
| **Type**        | Joystick Axis         | Joystick Axis         | Joystick Axis         | Joystick Axis         |
| **Axis**        | 10th axis (Joysticks) | 10th axis (Joysticks) | 10th axis (Joysticks) | 10th axis (Joysticks) |
| **Joy Num**     | Joystick 1            | Joystick 2            | Joystick 3            | Joystick 4            |
| {% endtab %}    |                       |                       |                       |                       |
| {% endtabs %}   |                       |                       |                       |                       |

### DPad X and DPad Y

{% tabs %}
{% tab title="Overview" %}
![DPad X1 (X2, X3, X4) and DPad Y1 (Y2, Y3, Y4) mappings](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McMKSC8b73op_GA_y0g%2F-McMawdB9iWhtFfb9ZTP%2Fgkc-doc-axes-dpad-x-dpad-y.png?alt=media\&token=68bec086-7840-477d-aad8-4db410baf794)
{% endtab %}

{% tab title="Full Breakdown" %}

### DPad X

| **Field**       | DPad X1              | DPad X2              | DPad X3              | DPad X4              |
| --------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| **Name**        | DPad X1              | DPad X2              | DPad X3              | DPad X4              |
| **Gravity**     | 0                    | 0                    | 0                    | 0                    |
| **Dead**        | 0.2                  | 0.2                  | 0.2                  | 0.2                  |
| **Sensitivity** | 1                    | 1                    | 1                    | 1                    |
| **Invert**      | -                    | -                    | -                    | -                    |
| **Type**        | Joystick Axis        | Joystick Axis        | Joystick Axis        | Joystick Axis        |
| **Axis**        | 6th axis (Joysticks) | 6th axis (Joysticks) | 6th axis (Joysticks) | 6th axis (Joysticks) |
| **Joy Num**     | Joystick 1           | Joystick 2           | Joystick 3           | Joystick 4           |

### DPad Y

| **Field**       | DPad Y1                    | DPad Y2                    | DPad Y3                    | DPad Y4                    |
| --------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| **Name**        | DPad Y1                    | DPad Y2                    | DPad Y3                    | DPad Y4                    |
| **Gravity**     | 0                          | 0                          | 0                          | 0                          |
| **Dead**        | 0.2                        | 0.2                        | 0.2                        | 0.2                        |
| **Sensitivity** | 1                          | 1                          | 1                          | 1                          |
| **Invert**      | :ballot\_box\_with\_check: | :ballot\_box\_with\_check: | :ballot\_box\_with\_check: | :ballot\_box\_with\_check: |
| **Type**        | Joystick Axis              | Joystick Axis              | Joystick Axis              | Joystick Axis              |
| **Axis**        | 7th axis (Joysticks)       | 7th axis (Joysticks)       | 7th axis (Joysticks)       | 7th axis (Joysticks)       |
| **Joy Num**     | Joystick 1                 | Joystick 2                 | Joystick 3                 | Joystick 4                 |
| {% endtab %}    |                            |                            |                            |                            |
| {% endtabs %}   |                            |                            |                            |                            |

### Mouse Left Click

{% tabs %}
{% tab title="Overview" %}
![Mouse Left Click mapping](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McMKSC8b73op_GA_y0g%2F-McMb2f2fo8m24-9h24F%2Fgkc-doc-axes-mouse-left-click.png?alt=media\&token=04ed104c-9057-4f8b-8f00-fa266510d0f6)
{% endtab %}

{% tab title="Full Breakdown" %}

| **Field**           | Mouse Left Click              |
| ------------------- | ----------------------------- |
| **Name**            | Mouse Left Click              |
| **Positive Button** | mouse 0                       |
| **Gravity**         | 1000                          |
| **Dead**            | 0.001                         |
| **Sensitivity**     | 1000                          |
| **Invert**          | -                             |
| **Type**            | Key or Mouse Button           |
| **Axis**            | X axis                        |
| **Joy Num**         | Get Motion from all Joysticks |
| {% endtab %}        |                               |
| {% endtabs %}       |                               |

After finishing adding the above key mappings then you will have the input for four players configured. This will allow up to four players to use the local multiplayer system.

{% hint style="info" %}
This step will no longer be necessary in the future and adding the key mappings will be handled by an in-editor setup wizard:man\_mage:
{% endhint %}

## Step #3: Add Tags and Layers

When importing GKC into an existing project, or if you imported GKC without the project settings then you'll need to add the tags and layers used by this asset.

You can add the below tags and layers by going into the Unity Tags and Layers settings (**Edit > Project Settings > Tags and Layers**).

### Tags

| Tag No | Tag Value |
| ------ | --------- |
| Tag 0  | box       |
| Tag 1  | sphere    |
| Tag 2  | moving    |
| Tag 3  | enemy     |
| Tag 4  | friend    |
| Tag 5  | device    |
| Tag 6  | inventory |
| Tag 7  | vehicle   |

### Layers

| Layer No | Layer Value          |
| -------- | -------------------- |
| #1       | gravityObjects       |
| #2       | Armor Surface        |
| #3       | turrets              |
| #4       | player               |
| #5       | radar                |
| #6       | Scanner              |
| #7       | vehicle              |
| #8       | inventory            |
| #9       | npc                  |
| #10      | weapons              |
| #11      | device               |
| #12      | Terrain              |
| #13      | Point\&Click         |
| #14      | Dynamic Split Screen |
| #15      | Transparent Mesh     |

{% hint style="info" %}
This step will no longer be necessary in the future, adding the tags and layers will be handled by an in-editor setup wizard:man\_mage:
{% endhint %}

{% hint style="success" %}
**That's it!** You've completed importing GKC into your project and you can **now start making the game of your dreams using Game Kit Controller**!:space\_invader:
{% endhint %}
