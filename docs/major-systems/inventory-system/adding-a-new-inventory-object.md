# Adding a New Inventory Object

Select the Character gameObject in the GKC\_Prefab.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F33auq5KShIkUjlM5vM6n%2F0?alt=media)

Go to Inventory List Manager inspector and open the inventory list.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FxaJtiDPQ5QUvWzIkT8DM%2F1?alt=media)

Press the button Add Object.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FPL8oKDuvM9avq9Xn0TSB%2F2?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2Fx57JwRMCUCD6XmQWHyPH%2F3?alt=media)

Open the new object and configure the Name and description.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FojBmU9UMzPpiZC71vWBu%2F4?alt=media)

Then, create the mesh used for that inventory object. It needs to have these settings:

* The mesh or meshes used in the object are placed in an empty parent, with a scale (1,1,1).
* That parent needs to use the layer inventory.
* That parent needs a collider adjusted to the object's shape and size. You can add as many collider (box, sphere, capsule) as you need if the objects has a complicated shape, but all these colliders need to be configured in the parent.
* This is not necessary, but the name for the prefab can be the name of the object with Mesh and the end.
* For example, this is the red wire created.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FPpzJBpJ49zz7BMxe9PDG%2F5?alt=media)

Once it is created, drop it to the prefab folder in the path Assets/Game Kit Controller/Prefabs/Inventory/Mesh.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FRMj6u56q5MbaeKvxQawJ%2F6?alt=media)

Go back to the Inventory List Manager, and set the mesh of the new object with the one created previously in the field Inventory Object Mesh.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FelJkjwZmUkXO00MluC4a%2F7?alt=media)
