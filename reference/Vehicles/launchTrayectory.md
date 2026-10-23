# launchTrayectory

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/launchTrayectory.cs:4`

**概要**: カメラの向きから着弾点をレイキャストし、放物線の軌跡と着地点アイコンをLineRendererで表示する照準補助。2.5D/3Dビューやヘッドトラックにも対応する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Show Line Renderer Enabled | `showLineRendererEnabled` | `bool` | true | – |
| Width | `width` | `float` | – | – |
| Number Of Points | `numberOfPoints` | `float` | – | – |
| Animation Speed | `animationSpeed` | `float` | – | – |
| Tilling Offset | `tillingOffset` | `float` | – | – |
| Animate Texture | `animateTexture` | `bool` | – | – |
| Texture Color | `textureColor` | `Color` | – | – |
| Use Max Distance When No Surface Found | `useMaxDistanceWhenNoSurfaceFound` | `bool` | – | – |
| Max Distance When No Surface Found | `maxDistanceWhenNoSurfaceFound` | `float` | – | – |
| Raycast Checking Enabled | `raycastCheckingEnabled` | `bool` | true | – |
| Check If Locked Camera Active | `checkIfLockedCameraActive` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check For Player Collider | `checkForPlayerCollider` | `bool` | – | – |
| Player Collider | `playerCollider` | `Collider` | – | – |
| Use Hold Throw Arm Animation | `useHoldThrowArmAnimation` | `bool` | – | – |
| Action Active Animator Name | `actionActiveAnimatorName` | `string` | "Action Active" | – |
| Hold Throw Melee Weapon Animator Name | `holdThrowMeleeWeaponAnimatorName` | `string` | "Action ID" | – |
| Hold Throw Melee Weapon Animator ID | `holdThrowMeleeWeaponAnimatorID` | `int` | – | – |
| Set Exit State On Arms Trigger Name | `setExitStateOnArmsTriggerName` | `string` | "Set Exit State On Arms" | – |
| Use Head Track Checking Launch Direction | `useHeadTrackCheckingLaunchDirection` | `bool` | – | – |
| Head Track Body Weight On Aim | `headTrackBodyWeightOnAim` | `float` | 1 | – |

### Show Target Position Icon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Target Position Icon | `showTargetPositionIcon` | `bool` | – | – |
| Target Position Icon | `targetPositionIcon` | `GameObject` | – | – |
| Rotate Target Position Icon | `rotateTargetPositionIcon` | `bool` | – | – |
| Rotate Target Position Icon Speed | `rotateTargetPositionIconSpeed` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Parable Enabled | `parableEnabled` | `bool` | false | – |
| Surface Found | `surfaceFound` | `bool` | – | – |
| Check Body Aim State Active | `checkBodyAimStateActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Shoot Position | `shootPosition` | `Transform` | – | – |
| Character | `character` | `GameObject` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Line Renderer | `lineRenderer` | `LineRenderer` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Raycast Direction | `raycastDirection` | `Vector3` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の軌跡更新コルーチンがあれば停止するだけ（参照は残る）。 |
| `changeParableState(bool state)` | 放物線表示の有効状態を設定し、LineRenderer・更新コルーチン・着地点アイコン・頭トラックを切り替える。 |
| `setMainCameraTransform(Transform newCameraTransform)` | `mainCameraTransform`を差し替えるだけ。 |
| `setShowLineRendererEnabledState(bool state)` | `showLineRendererEnabled`を設定するだけ。 |
