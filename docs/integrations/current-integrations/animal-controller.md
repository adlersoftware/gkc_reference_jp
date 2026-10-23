# Animal Controller

This page covers the integration of Animal Controller from Malbers

## What is Animal Controller?

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2Fg29ovV5piFCZpASuDfSA%2Fimage.png?alt=media&amp;token=759d1a46-efc8-4b20-afbe-e424517a9b8f" alt=""><figcaption></figcaption></figure>

**Animal Controller(AC)** is an animation framework controller, root-motion or In Place, for any creature or HUMANOID character.&#x20;

**AC** is the base controller for all my Assets, but you can use i*t* on any other asset in the Store.

It was built from the ground up with over 3 years of experience to make all my assets shine even more with a smooth and modular controller.&#x20;

**AC** is based on States and Modes. **States** like *Locomotion, Idle, Jump, Fall, Fly, Swim..* and **Modes** *Like Main Attacks, Secondary Attacks, Hits, Actions, etc.*&#x20;

States are the Animations that contain certain Logic and they cannot overlap each other (Ex: You cannot swim and fly at the same time)

Modes are the Animations that be used while a state Animation is playing (Ex: Attack while flying or Running).

{% hint style="info" %}
You can find more information about **Animal Controller**, and its documentation and also purchase it over on the [Unity Asset Store](https://assetstore.unity.com/packages/tools/animation/animal-controller-148877).
{% endhint %}

## Video Tutorial

{% embed url="<https://www.youtube.com/watch?v=gr_MM2picZ0>" %}

## Written Tutorial

Open the first demo scene (in this example it's *Unka the Dragon*) and drop the *GKC Player* in the scene along with the **Rider System Object**. You can drop this object inside the Malbers animal, and reset its transform value.

### Modify Malbers Input

Next, we need to modify the **Malbers Input** component with some custom code.

Copy the code below to have a function that allows you to *Pause/Resume* the input of the Animal Controller.&#x20;

```
if (inputPaused)
 {
 horizontal = 0;
 vertical = 0;
 upDown = 0;

 RawInputAxis = Vector3.zero;

 return;
}
```

This first part is pasted inside the **SetInput function** at the very top of the script, it starts at line 70.

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FrfwrEsZ4YtNYVIef0CDq%2Fimage.png?alt=media&amp;token=edb84285-d1cb-47c6-a6b3-133740598fdb" alt=""><figcaption><p>Before code insert</p></figcaption></figure>

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FPrwOpI3GCoLwE5GkHrmJ%2Fimage.png?alt=media&amp;token=2ab5dc69-f50b-4c8b-9261-d0bb50cba0a7" alt=""><figcaption><p>After code insert</p></figcaption></figure>

The second code part, below, is pasted directly at the end of the **SetInput function**.

```
public bool inputPaused = true;

public void setInputPausedState(bool state)
{
 inputPaused = state;
}
```

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FrvgkBU6hTkFOBar5rTSZ%2Fimage.png?alt=media&amp;token=191ffcf9-972d-4a01-96d8-4475a4118a8d" alt=""><figcaption><p>Before second code insert</p></figcaption></figure>

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FLiTKm4ru40ZAXbZEbNlQ%2Fimage.png?alt=media&amp;token=b79e927a-1e81-4fd2-b087-ff09abdbe891" alt=""><figcaption><p>After second code insert</p></figcaption></figure>

### Configure GKC Rider System

On the **GKC rider system**, configure the option to use events on start, calling to that function, so the input of the animal is paused from start.

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FuiSEm2QPDP8XTKxUMm3F%2Fimage.png?alt=media&amp;token=365c2e2b-5cdb-464f-9e25-21b100992bd8" alt=""><figcaption></figcaption></figure>

Create an empty game object inside the **CM Brain** of the animal and name it *Main Camera Position*. Disable the *Camera* and *Audio Listener* components of that camera. In the **Rider Seat System** prefab, under the **Move Camera to Devices** component, drag and drop the *Main Camera Position* game object you created in the CM Brain to the *Camera Position* slot.

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F2iandhZ1nx5Mw9g7KbGf%2Fimage.png?alt=media&amp;token=d7a3249b-8436-4d05-be1a-c0f9f5ca8ca0" alt=""><figcaption></figcaption></figure>

### Configure Electron Device Component

On the **Electronic Device** component, we'll configure the Pause/Resume events for the animal. Scroll down to the section, Start/Stop Using Device Settings, and assign your Malbers animal and Look At as in the photo below. Setting setInputPausedState and LookAt in their respective states is needed.

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FMyDOUaglOn3powW9muf8%2Fimage.png?alt=media&amp;token=cceb84b4-2d0e-468f-9733-07c2a1d2b2da" alt=""><figcaption></figcaption></figure>

On *Event on Start Using Device ()* **MalbersInput.setInputPausedState** should be unchecked. That means the animal is not paused on Start. **LookAt.enabled** is checked as that lets the Animal Controller look at targets as usual.

In *Use Event on Stop Using Devic*e, the opposites are selected so that the Animal is Paused on stop and *LookAt* is disabled. Additionally assign the Animal twice, selected MalbersInput.enabled. Checking one, and unchecking the other.

After that you can customize the interaction panel text transform along the Ride positions and IK elements (check the tutorial for [Edy's Vehicle System](/docs/integrations/current-integrations/edys-vehicle-system.md) tutorial for more info) in the Rider Seat System prefab.

That's it! You're ready to ride!
