# NWH Vehicle Physics 2

This page covers the integration of NWH Vehicle Physics 2 and Game Kit Controller

## What is NWH Vehicle Physics 2?

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F0t4D1U4uEbMrfFcZQ7hQ%2Fimage.png?alt=media&amp;token=6e436931-55da-470d-9779-c45ced02c5ca" alt=""><figcaption></figcaption></figure>

**NWH Vehicle Physics 2** is a complete vehicle simulation package for Unity. Realistic, easy to use, and heavily customizable.

• Easy and fast to set up with all the defaults loaded automatically and a validation system that warns the developer about any setup issues.

• Vehicle setup wizard that creates a functional vehicle from scratch in a few clicks. Multiple presets are available.

• Modular vehicle architecture. Enable or disable parts of the vehicle as they are needed, either manually or through the built-in LOD system.

• Powertrain solver that features excellent performance, stability, and physical accuracy.

• Custom physics sub-stepping solution.

• All aspects of the vehicle are adjustable at runtime - including powertrain, suspension, friction, effects, etc.

{% hint style="info" %}
You can find more information about **NWH Vehicle Physics 2**, and its documentation and also purchase it over on the [Unity Asset Store](https://assetstore.unity.com/packages/tools/physics/nwh-vehicle-physics-2-166252).
{% endhint %}

## Video Tutorial

{% embed url="<https://youtu.be/6y3gdSkTuR4>" %}

## Written Tutorial

Open the scene Racetrack in **NWH** or drop the vehicle prefab you want, drop the GKC player and the rider system object prefab directly inside the vehicle.

If the default controller of **NWH** is on the scene, disable it. Disable all the camera objects from the vehicle, including their audio listener and the camera component of the first camera.

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FvEdazHBKhykiUDF7fAXl%2Fimage.png?alt=media&amp;token=b97892cb-2a4b-4728-ae5f-61455dc9f917" alt=""><figcaption></figcaption></figure>

Drag the **External Rider Controller System** into the scene from the GKC folder and reset it's position. Enable the option on the GKC Rider System to **Use Event On Start Game** and configure the sleep function of the vehicle controller component by dragging the root prefab into the Event Field. Select *VehicleController < Sleep()*.

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FXA3oJnkc7xkkPgucQ44B%2Fimage.png?alt=media&amp;token=b308b6f1-c86f-48c2-b4b4-6dab23a1764b" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2Fer3jNgojsgzypCcKO1NJ%2Fimage.png?alt=media&amp;token=2ee923ad-16ef-41d2-8506-52b1b5a677da" alt=""><figcaption></figcaption></figure>

Configure the events to wake and sleep on the electronic device components by dragging the vehicle prefab to **Event on Start Using Device** and selecting *VehicleController < Awake*. and **Use Event on Stop Using Device** and selecting *VehicleController < Sleep*.&#x20;

Assign the DemoUICanvas (only for the Demo Scene) and set it to *GameObject < Set Active* and enable it.

Create a new GameObject inside the **Vehicle Camera** in the Cameras gameobject of the vehicle and name it *Camera Position*. Select the **External Rider Controller System**, the **Move Camera to Device** component and in *Camera Position*, assign the *Camera Position* gameobject you just created.

Change the **Device Name** and **Device Action** on the **Device String Action** component to what you want. And all is configured to work properly, now it is a matter of adjusting the IK positions and the seat and passenger elements.

Also, move the Steering gameobject from inside the **External Rider Controller System** object to the vehicle mesh. Make sure to unpack the prefab on the rider object. On the vehicle controller, you can adjust the steering wheel max rotation angle so it looks proper with the driver's hands on it through IK.
