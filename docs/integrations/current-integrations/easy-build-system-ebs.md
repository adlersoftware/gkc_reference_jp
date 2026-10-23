# Easy Build System (EBS)

This page covers the integration of Easy Build System (EBS) and Game Kit Controller.

## What is Easy Build System?

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McQXlQkDFkgYtx7EbBH%2F-McQkypAyzbZf77HDlQR%2Fgkc-doc-integration-ebs-header.png?alt=media\&token=e81d54dd-e8fe-4c62-a841-78428fc44591)

**Easy Build System** is an advanced building system, easy to use and expandable. Fast and powerful to suit all of your building needs in all your games, works on any platforms!

Designed to work out-of-the-box, it includes several components like scalable conditions and add-ons, sockets, physics, blueprints, skins, save and load... etc

Support three view modes first, third and top-down view, works with the new Unity Input System and XR. Extend it or to customize it to fit your exact needs, even if you aren't a programmer.

{% hint style="info" %}
You can find more information about **Easy Build System (EBS)**, it's documentation and also purchase it over on the [Unity Asset Store](https://assetstore.unity.com/packages/templates/systems/easy-build-system-v5-3-45394).
{% endhint %}

## Integration Steps

Follow these quick easy steps to integrate **Easy Build System** and **Game Kit Controller**.

### Step #1

Open the scene called "**\[Desktop] First Person - Modular Building Demo**" or any first person demo scenes in the EBS demos directory here: `Assets/Easy Build System/Demos & Add-Ons/Demos` and drop the GKC player prefab into the scene.

{% hint style="info" %}
If the EBS demos directory doesn't exist in your project, you'll need to import them via the EBS package importer *(Tools > Easy Build System > Package Importer > Import Demos & Add-Ons)*.
{% endhint %}

{% hint style="info" %}
The GKC player prefab is located here: \
***`Assets/Game Kit Controller/Prefabs/Player Controller/Player And Game Management.prefab`***
{% endhint %}

### Step #2

Next locate the `Easy Build System - Demo First Person Controller` EBA player controller GameObject in your project hierarchy and **disable it**.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McRfPqA-9d6Nz9bhwQi%2F-McRnG2W750QmU-wT5GV%2Fgkc-doc-integration-ebs-1.png?alt=media\&token=555849c3-6662-4239-b843-4bec06568e30)

### Step #3

Select the `Main Camera` child GameObject of the **Easy Build System - Demo First Person Controller** GameObject. Then locate the `Builder Behaviour` component and **copy it**.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McRfPqA-9d6Nz9bhwQi%2F-McRpcb_AhbxQu21RG8o%2Fgkc-doc-integration-ebs-2.png?alt=media\&token=5769fae3-c576-40c5-9373-bffd45685133)

### Step #4

Next up you want to locate the GKC `Main Camera` GameObject in your project hierarchy *(Player And Game Management > Player Camera > Pivot Camera Transform > Main Camera Transform > Main Camera)* and select the hamburger menu of an existing component, then press "**Paste Component As New**" to paste the `Builder Behaviour` component onto the GKC `Main Camera`.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McRfPqA-9d6Nz9bhwQi%2F-McRsy888dncjXOMP65l%2Fgkc-doc-integration-ebs-3.png?alt=media\&token=fb305598-9727-447b-9905-754c77d2c626)

### Step #5

Still on the GKC `Main Camera` GameObject, got to the bottom of the inspector and press "**Add Component**" then we're going to create a new script, so enter **`GKCInputBehaviour`** and then select "**Create and Add**".

Open the newly created **`GKCInputBehaviour.cs`** script in your preferred editor, **delete any existing content in the script so that it's empty**, and **paste in the code below**.

{% hint style="info" %}
You can also find a text copy of the **GKCInputBehaviour** script in "**Assets/Game Kit Controller/Documentation/Integrations**" in your project.
{% endhint %}

```csharp
using EasyBuildSystem.Features.Scripts.Core.Base.Builder;
using EasyBuildSystem.Features.Scripts.Core.Base.Builder.Enums;
using EasyBuildSystem.Features.Scripts.Core.Base.Manager;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class GKCInputBehaviour : MonoBehaviour
{
    #region Fields

    public bool UseShortcuts = true;

    public KeyCode BuilderPlacementModeKey = KeyCode.E;
    public KeyCode BuilderDestructionModeKey = KeyCode.R;
    public KeyCode BuilderEditionModeKey = KeyCode.T;

    public KeyCode BuilderValidateModeKey = KeyCode.Mouse0;
    public KeyCode BuilderCancelModeKey = KeyCode.Mouse1;

    public int SelectedIndex { get; set; }

    public bool buildModeEnabled = true;

    #endregion

    #region Methods

    private void Update ()
    {
        if (!buildModeEnabled) {
            return;
        }

        if (UseShortcuts) {
            if (Input.GetKeyDown (BuilderPlacementModeKey))
                BuilderBehaviour.Instance.ChangeMode (BuildMode.Placement);

            if (Input.GetKeyDown (BuilderDestructionModeKey))
                BuilderBehaviour.Instance.ChangeMode (BuildMode.Destruction);

            if (Input.GetKeyDown (BuilderEditionModeKey))
                BuilderBehaviour.Instance.ChangeMode (BuildMode.Edition);

            if (BuilderBehaviour.Instance.CurrentMode != BuildMode.Placement)
                UpdatePrefabSelection ();

            if (Input.GetKeyDown (BuilderCancelModeKey))
                BuilderBehaviour.Instance.ChangeMode (BuildMode.None);
        }

        if (BuilderBehaviour.Instance.CurrentMode == BuildMode.Placement) {
            if (IsPointerOverUIElement ())
                return;

            if (Input.GetKeyDown (BuilderValidateModeKey))
                BuilderBehaviour.Instance.PlacePrefab ();

            float WheelAxis = Input.GetAxis ("Mouse ScrollWheel");

            if (WheelAxis > 0)
                BuilderBehaviour.Instance.RotatePreview (BuilderBehaviour.Instance.SelectedPrefab.RotationAxis);
            else if (WheelAxis < 0)
                BuilderBehaviour.Instance.RotatePreview (-BuilderBehaviour.Instance.SelectedPrefab.RotationAxis);

            if (Input.GetKeyDown (BuilderCancelModeKey))
                BuilderBehaviour.Instance.ChangeMode (BuildMode.None);
        } else if (BuilderBehaviour.Instance.CurrentMode == BuildMode.Edition) {
            if (IsPointerOverUIElement ())
                return;

            if (Input.GetKeyDown (BuilderValidateModeKey))
                BuilderBehaviour.Instance.EditPrefab ();

            if (Input.GetKeyDown (BuilderCancelModeKey))
                BuilderBehaviour.Instance.ChangeMode (BuildMode.None);
        } else if (BuilderBehaviour.Instance.CurrentMode == BuildMode.Destruction) {
            if (IsPointerOverUIElement ())
                return;

            if (Input.GetKeyDown (BuilderValidateModeKey)) {
                if (BuilderBehaviour.Instance.CurrentRemovePreview != null) {
                    BuilderBehaviour.Instance.DestroyPrefab ();
                }
            }

            if (Input.GetKeyDown (BuilderCancelModeKey))
                BuilderBehaviour.Instance.ChangeMode (BuildMode.None);
        }
    }

    private void UpdatePrefabSelection ()
    {
        float WheelAxis = Input.GetAxis ("Mouse ScrollWheel");

        if (WheelAxis > 0) {
            if (SelectedIndex < BuildManager.Instance.Pieces.Count - 1)
                SelectedIndex++;
            else
                SelectedIndex = 0;
        } else if (WheelAxis < 0) {
            if (SelectedIndex > 0)
                SelectedIndex--;
            else
                SelectedIndex = BuildManager.Instance.Pieces.Count - 1;
        }

        if (SelectedIndex == -1)
            return;

        if (BuildManager.Instance.Pieces.Count != 0)
            BuilderBehaviour.Instance.SelectPrefab (BuildManager.Instance.Pieces[SelectedIndex]);
    }

    /// <summary>
    /// Check if the cursor is above a UI element or if the circular menu is open.
    /// </summary>
    private bool IsPointerOverUIElement ()
    {
        if (Cursor.lockState == CursorLockMode.Locked)
            return false;

        if (EventSystem.current == null)
            return false;

        PointerEventData EventData = new PointerEventData (EventSystem.current)
        {
            position = new Vector2 (Input.mousePosition.x, Input.mousePosition.y)
        };

        List<RaycastResult> Results = new List<RaycastResult> ();
        EventSystem.current.RaycastAll (EventData, Results);
        return Results.Count > 0;
    }

    public void setBuildModeEnabledState (bool state)
    {
        buildModeEnabled = state;

        if (!buildModeEnabled) {
            BuilderBehaviour.Instance.ChangeMode (BuildMode.None);
        }
    }

    #endregion
}

```

Save the `GKCInputBehaviour.cs` script and return to Unity. You should now see something like the following:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McS-U2JzeuvnL79Jz8b%2F-McS0ICk_9gQo5_qPl-A%2Fgkc-doc-integration-ebs-4.png?alt=media\&token=b0784304-7a66-4754-86b4-6bf8c8e28e45)

### Step #6

Next we're going to link up the Player Mode that'll be used when the player wants to enter build mode.

First select the **`Player Controller`** GameObject in your project hierarchy and locate the "**Player Modes List**" in the "**Player States Manager**" component.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McS-U2JzeuvnL79Jz8b%2F-McS5gga62ORX4U4EJoC%2Fgkc-doc-integration-ebs-5.png?alt=media\&token=b796e1c5-2c09-493c-a741-f5bd4cbb26a4)

Now you need to create **two new events** in the player mode you want the player to have the ability to build in. We're going to use an existing one for this example called "**Simple Mode**", but you can add a new player mode, or use another existing one if you'd prefer.

Expand your selected mode and add a new event to the "**Activate Player Mode Event**" list and one to the "**Deactivate Player Mode Event**" list. The function for both new events should be set to **`GKCInputBehaviour.setBuildModeEnabledState`** - Now tick the checkbox in the "**Activate Player Mode Event**" list and leave the checkbox unticked in the "**Deactivate Player Mode Event**" list.

Finally drag the **`Main Camera`** GameObject into the object field in both events you just created.&#x20;

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McS5jqGjmyTC1a4BEbf%2F-McS9-I9UDR5_bC4tTRr%2Fgkc-doc-integration-ebs-6.png?alt=media\&token=769d28dd-b7ed-4dc1-950c-cdf956976e63)

{% hint style="success" %}
**That's it!** Game Kit Controller is now integrated with **Easy Build System (EBS)** in your project. Hit play and change the player mode *("H" key by default)* to the mode you added the events to above:partying\_face::raised\_hands:

Now if you'd excuse me, I have to go finish building my dream home that I'll never actually own in real life... but who needs real life when you can build anything you want in GKC!:hotel::sunrise\_over\_mountains::sunglasses:&#x20;
{% endhint %}

{% hint style="info" %}
*Note: A future version of the Easy Build System and Game Kit Controller integration will allow deeper integration with other systems of GKC like the inventory.*
{% endhint %}
