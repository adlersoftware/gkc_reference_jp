# Use Inventory Objects

Important: in this explanation, the fuse box is used as an example, but this system can be used to create any type of object where to use inventory objects.

Finally, to use the objects created and configure in the previous steps, follow these steps (in this explanation, the fuse box will be used as an example to unlock a door, and the mesh for the fuse box is already created):

* The parent that contains the fuse box is an empty transform with this configuration:
  * The tag assigned is the device. o The layer assigned is Ignore Raycast.
  * A sphere collider with the trigger option enabled is used to detect if the player is close enough to the fuse box to use the inventory objects on it.  So, it looks like this:

!\[Graphical user interface

Description automatically generated]\(/files/Igmu1IhXC9WLV8KhWHbt)

* Add a Use Inventory Object component to the parent.

!\[Graphical user interface, text, application, email

Description automatically generated]\(/files/jeYbP3YC04cR9DUGxsBt)

* In the Main Settings, set to true the option Disable Object Action After Use. This is used to disable the Device String Action component icon, which will be added after.
* Also, in the option Use Inventory Type, you can configure how the objects used in the fuse box are placed:
  \*
  \*
  \* Menu, the player needs to open, select and use the object.
  \* Button, the player only needs to press the interaction button to use the necessary inventory objects (in case he has them, else a message is shown on the screen to say that the player hasn’t the needed objects).
  \* Automatic, the player only needs to enter the trigger to use the inventory objects in the fuse box.
* Add an event to the list of Unlock Function Call and add the object to use, in this case, add the door to unlock.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FMZwsYaJtHjGX33UPrMJI%2F2?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FCBl4LSy49uMpGArbPtGI%2F3?alt=media)

* Add in the Function field, and set the UnlockDoor function, from the component Door System.

!\[Graphical user interface, text, application, email

Description automatically generated]\(/files/hVIwgjLrm2dREoAXfKly)

* Now, configure the objects to be used from the inventory in this fuse box. For this follow these steps: o Open the Inventory Object To Use Lis.

!\[Graphical user interface, text, application

Description automatically generated]\(/files/YYECsLrkIknTEaywJPvj)

o

Press the button Add Object.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2Fh5Wi4iLIIplNVYMLUfF1%2F6?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FjtEfgsfW2vAzoSuekOAM%2F7?alt=media)

* * Open the new element and configure the values required, name, the amount needed, and the message shown on the screen when the object is used.

!\[Graphical user interface, text, application, email

Description automatically generated]\(/files/3KcjG4HLDpr7aEc8x6Cx)

* * Then, in the field Object Needed, drag and drop the mesh of the inventory object which needs to be used here, in this case, the fuse. The path of these meshes is Assets/Game Kit Controller/Prefabs/Inventory/Mesh

!\[Graphical user interface, application

Description automatically generated]\(/files/4n6nPDYRE5a4OcbiF9vc)

* * Open the Inventory Object Needed List inside the current element that is being configured and press the button Add Object.

!\[Graphical user interface, text, application

Description automatically generated]\(/files/beqFiM38oslvfvsuymMl)

* * Open the new element and, for this case, set to true the option Enable Object.

!\[Graphical user interface, application

Description automatically generated]\(/files/EjE5JcUQrY5jcfLtpAq8)

* * This option activates a gameObject in the level and in this case, the fuse models placed in the fuse box are disabled, so when the player uses a fuse from the inventory, the fuse is activated inside the box. For this example, the gameObject Fuse Model is disabled in the hierarchy. This is the element configured in the Object To Enable Field.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FkRarIbkoSC4icVyoHS00%2F12?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FBd6vhV0BYlFrqmcaae7P%2F13?alt=media)

* * The fuse model needs to be disabled before starting the game.

!\[Graphical user interface, application

Description automatically generated]\(/files/ZvxtgMmJYqqO8xUNV69E)

* * Instead of activating disabled gameObjects, there is an option to instantiate objects in the scene, but this will be explained later.
  * In this case, there are four fuses, so configure the rest of them, like the first one.

!\[Graphical user interface

Description automatically generated]\(/files/ITUV4LqJugYWAEDayGzr)

* * Now, along with the four fuses, the fuse box needs a blue wire to work, so another object needs to be configured, but it is another element different from the fuses. Go to the main Inventory Object Needed List and press the Add Object button to configure the blue wire.

!\[Graphical user interface

Description automatically generated]\(/files/7G8gL1Cnz39HKyhsO8wV)

* * For the blue wire, like for the fuses, configure the name, the message to show on screen and the amount needed and the inventory object mesh to use.

!\[Graphical user interface, text, application, email

Description automatically generated]\(/files/q9ORAlP3piqbXnWIhxUQ)

* * And inside the Inventory Object Needed List, configure the object to active, in this case, a mesh of the wire already placed in the box, like the previous fuses objects.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FErcc7pqlUiiwfGzJWONl%2F18?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F9RudO97MKLo3VWV0dyNN%2F19?alt=media)

* * Like with the Fuses Models configured before, the wire object needs to be disabled.

!\[Graphical user interface, text, application

Description automatically generated]\(/files/3XpLsl9yo4vpZvyc2Msk)

* Finally, add a Device String Action component to the parent, with the next configuration.
* The Device Name and the Device Action are the text shown in the icon of the interaction button on the screen. The Show Icon is the default option to show that icon on the screen. The Show Touch Icon Button is a default option used to show the touch button on mobile devices to use the interaction button.
