# Render Terrain in the Map Window

To make the terrain visible in the map system, follow these steps:

* Assign the layer Terrain to the terrain gameObject.
* Inside the **Map System gameObject**, there is a camera, to render the tile meshes created with the map creator. In that camera, add the layer Terrain in the culling mask.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FQjIUqddpBDUi8nSebxwN%2F0?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FyS02wEqPlPqRROVbOtCY%2F1?alt=media)

* Make sure to create at least an empty floor in the **Map System component** in the Character gameObject, it doesn't need to have any map part.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FKBrRIDDy6dyX86yhnYxy%2F2?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2Fea4s74PTfXgfJoARJkPR%2F3?alt=media)

Then, the terrain will be visible in editor mode in the mini window and ingame.

![An open map](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FNe7BBTssfZSJji5Z3o5D%2F4?alt=media)
