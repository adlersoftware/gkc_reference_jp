# Creating a new Map Creator and adding Map Parts

If you want to use the map system, you need to drag and drop the Map System prefab (with the same name) in the folder **Assets/Game Kit Controller/Prefabs/Map System**.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FLOPVsaNsv3tyG8LnlrFM%2F0?alt=media)

Once the hierarchy contains these two elements:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F2qFMao0b4CjhcaKHLIpe%2F1?alt=media)

Inside the hierarchy of the **Map System** gameObject, go to **Floor List** and to **Map Creator** inspector.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FBvWUpYX6u1iM2OIPxILr%2F2?alt=media)

Go to **Floors List** and press **Add Floor** button.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F7ePR2n4hxPxxTqTAR0Yf%2F3?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FC50mOaBukbBLUfEywf4s%2F4?alt=media)

This element will contain all the map parts for the same floor. At the same time, every map part contains a group of empty transforms which are used as a vertex to create the map part mesh, like a room, a corridor, a wall, etc…

In the hierarchy, you can see that inside the **Floor List** transform, a new transform has been added as a parent to that floor, and inside that floor, the first map part.

!\[Graphical user interface, text, application

Description automatically generated]\(/files/0XXQNiECAPGh7k7AozYR)

Open the first element of the floor list, which already contains the first map part, to the **Map Tile Builder inspector**, and press the button Add Transform in the Vertex Position list.

![ ](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FwxDsiFHlwllFr3ETzxQL%2F6?alt=media)

For example, if you press this button 4 times, 4 empty transforms will be attached inside the **MapPart-001**, used as the vertex for the mesh that will be created.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FbisbHF6AFvExbvZESct8%2F7?alt=media)

For an easy workflow, in the **Map Tile Builde**r, go to **Gizmo Settings** and enable the **Use Handle For Vertex** and configure the radius as you need.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F2Nn37qCGo4lYOUnTjDVM%2F8?alt=media)

You can also move the transform 001 to 004 to place the vertex to make the shape that you need.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FLOkrhVKYf8kXw1W8j8AJ%2F9?alt=media)

You can add as many vertexes as you need, to make rooms or places simple, for example, squares or rectangles to circular rooms, hexagonal, etc…, just press the button Add Transform.

<img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FuHfHLHt9LROfmRLXgu9F%2F10?alt=media" alt="" data-size="original">

When the game starts, the shape is created, looking like this:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FzTOxUStF6I4fQZeMsLj4%2F11?alt=media)

You can remove any of these vertexes by pressing the X button and both the object in the scene and in the list are removed.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FcH6WbFLFxOHx15EFs6dr%2F12?alt=media)
