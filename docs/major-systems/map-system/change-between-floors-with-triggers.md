# Change between Floors with Triggers

If instead of using vertical distance to know the closest floor where the player is, you can use triggers to change between floors. This can be used better for closed spaces levels, instead of opened.

For this, go to the **Map Creator inspector**, and in the floor that you need, open the **Trigger To Change Floor** list and press the **Add Trigger** button.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F0720nvBqDm0KmGzj20IV%2F0?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FeLlNnKYePmZ33aXd0w7X%2F1?alt=media)

And like before, the gameObjects are created and attached to the proper hierarchy elements.

!\[A picture containing diagram

Description automatically generated]\(/files/8aG9hlPtDbAP3H0gTl3v)

Like this, place this trigger where you want the map floor to be changed to Floor 0. This system is made to use two triggers for a zone, it means, one trigger to change to floor 0 and one trigger to change to floor 1 in every place the floors are changed, both of them close (for example, if the building has two stairs, to walk between both floors, there will be 4 triggers, two for every stair).

This can be appreciated here, in the demo mansion, there are two triggers in the stairs of the hall, one to change to **Floor 1** and another for **Floor 0**. Also, a gizmo is used to show the link from every trigger to its floor.

!\[Diagram

Description automatically generated]\(/files/s4xCjXJyqRiKXyTUugi9)

!\[Diagram

Description automatically generated with medium confidence]\(/files/2zgBIzwrzQrMRyGCRER4)

Once the triggers are placed, go to the **Map System inspector**, go to **Map Settings**, and set to false the option **Get Closest Floor To Player By Distance**.

!\[Graphical user interface, text, application, email

Description automatically generated]\(/files/rtY9VS1sqnFizUUvP3de)

You can add as many triggers as you need for every floor. Also, you can remove any of these triggers with the X button and both the object in the scene and the list are removed.

!\[Graphical user interface, application

Description automatically generated]\(/files/GyDrQIrPKFwTG9tQA5FA)
