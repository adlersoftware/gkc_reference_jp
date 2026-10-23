# sliceSystemUtils

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/Slice System/sliceSystemUtils.cs:10`

**公式ドキュメント抜粋**（[(Optional) Download External Files](../../docs/quick-start/get-started/optional-download-external-files.md)）

> The action system can be used with any type of humanoid animation. To work on this system, example animations from Mixamo were used as placeholders to configure multiple examples of the action system. Due to Mixamo animations can’t be included on asset, you can find the animations used on these examples on the public repository of Game Kit Controller on Github. <https://github.com/sr3888/GKC-Public-Repository These animations are already with the regular settings applied to work on root motion properly (like rotation based on current pose, loop time, adjust speed, etc…). No extra setting is needed to try these examples. All those animations and copyrights belong to Mixamo. You can get those animations and more at the official website of Mixamo: <https://www.mixamo.com// Of course, on this action system, you can use your own animations, from the asset store or any other store or web. Ther…

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static void sliceObject(Vector3 slicePosition, GameObject objectToSlice, Vector3 cutDirection, Material crossSectionMaterial, ref bool objectSliced, ref GameObject object1, ref GameObject object2)` | – |
| `static surfaceToSlice getSurfaceToSlice(GameObject currentSurface)` | – |
| `static void initializeValuesOnHackableComponent(GameObject objectToUse, simpleSliceSystem currentSimpleSliceSystem)` | – |
| `static void setDestructionPending(GameObject objectToUse, bool state)` | – |
| `static void sliceCharacter(GameObject objectToSlice, Vector3 point, Vector3 newNormalInWorldSpaceValue, bool updateLastObjectSpeed, Vector3 lastSpeed)` | – |
| `static GameObject[] shatterObject(GameObject obj, Vector3 shatterPosition, Material crossSectionMaterial = null, bool shaterActive = true)` | – |
| `static EzySlice.Plane getRandomPlane(Vector3 positionOffset, Vector3 scaleOffset)` | – |
| `static void destroyAllSlicedPiecesByRandomString(string stringValue, GameObject mainObjectToIgnore)` | – |
| `static void processObjectToSlice(GameObject objectToCheck, Collider objectCollider, Vector3 slicePosition, Quaternion sliceRotation, float minDelayToSliceSameObject, Vector3 sliceUpDirection, Vector3 sliceRightDirection, Vector3 sliceForwardDirection, float forceToApplyToCutPart, LayerMask targetToDamageLayer, bool randomSliceDirection, bool showSliceGizmo, bool activateRigidbodiesOnNewObjects)` | – |
| `static void sliceCurrentObject(surfaceToSlice currentSurfaceToSlice, GameObject objectToCheck, Collider objectCollider, Material crossSectionMaterial, Vector3 slicePosition, Quaternion sliceRotation, Vector3 sliceUpDirection, Vector3 sliceRightDirection, Vector3 sliceForwardDirection, float forceToApplyToCutPart, float minDelayToSliceSameObject, LayerMask targetToDamageLayer, bool randomSliceDirection, bool showSliceGizmo, bool activateRigidbodiesOnNewObjects)` | – |
| `static void processCharacter(GameObject currentCharacter, Vector3 slicePosition, Quaternion sliceRotation, float minDelayToSliceSameObject, Vector3 sliceUpDirection, Vector3 sliceRightDirection, Vector3 sliceForwardDirection, float forceToApplyToCutPart, LayerMask targetToDamageLayer, bool randomSliceDirection, bool showSliceGizmo, bool activateRigidbodiesOnNewObjects)` | – |
