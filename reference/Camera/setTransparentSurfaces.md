# setTransparentSurfaces

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Others/setTransparentSurfaces.cs:6`

**概要**: プレイヤーとカメラの間にあるサーフェスを検出し、マネージャ経由で一時的に透明化するコンポーネント。プレイヤーIDごとに透明化対象を管理する。

**公式ドキュメント抜粋**（[Set Transparent Surfaces](../../docs/player-controller-components/player-camera/set-transparent-surfaces.md)）

> Used to detect objects between the player and the main camera with a certain layer configured on it (Transparent Mesh), allowing to keep collisions with them but seeing through them and fade their meshes to keep the player visible on screen. This is used on certain objects of the scene in different games, like columns, certain walls, trees, etc…. and in most games with an isometric or top-down view.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Surface Enabled | `checkSurfaceEnabled` | `bool` | true | – |
| Check Surface Active At Start | `checkSurfaceActiveAtStart` | `bool` | – | – |
| Check Surface Active | `checkSurfaceActive` | `bool` | – | – |
| Locked Camera Active | `lockedCameraActive` | `bool` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Capsule Cast Radius | `capsuleCastRadius` | `float` | 0.3f | – |
| Use Custom Shader | `useCustomShader` | `bool` | – | – |
| Custom Shader | `customShader` | `Shader` | – | – |
| Main Manager Name | `mainManagerName` | `string` | "Set Transparent Surfaces Manager" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Surface Found | `surfaceFound` | `bool` | – | – |
| Surface Found Previously | `surfaceFoundPreviously` | `bool` | – | – |
| Player Is Using Devices | `playerIsUsingDevices` | `bool` | – | – |
| Player Is Using Devices Previously | `playerIsUsingDevicesPreviously` | `bool` | – | – |
| Current Surface Game Object Found List | `currentSurfaceGameObjectFoundList` | `List<GameObject>` | new List<GameObject> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Start Check Surface | `useEventsOnStartCheckSurface` | `bool` | – | – |
| Event On Start Check Surface | `eventOnStartCheckSurface` | `UnityEvent` | – | – |
| Use Events On Stop Check Surface | `useEventsOnStopCheckSurface` | `bool` | – | – |
| Event On Stop Check Surface | `eventOnStopCheckSurface` | `UnityEvent` | – | – |
| Use Event On Surface Found | `useEventOnSurfaceFound` | `bool` | – | – |
| Event On Surface Found | `eventOnSurfaceFound` | `UnityEvent` | – | – |
| Use Event On No Surface Found | `useEventOnNoSurfaceFound` | `bool` | – | – |
| Event On No Surface Found | `eventOnNoSurfaceFound` | `UnityEvent` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Sphere Color | `sphereColor` | `Color` | Color.green | – |
| Cube Color | `cubeColor` | `Color` | Color.blue | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Player ID | `playerID` | `int` | – | – |
| Ray Origin Position Free Camera | `rayOriginPositionFreeCamera` | `Transform` | – | – |
| Ray Target Position Free Camera | `rayTargetPositionFreeCamera` | `Transform` | – | – |
| Ray Origin Position Locked Camera | `rayOriginPositionLockedCamera` | `Transform` | – | – |
| Ray Target Position Locked Camera | `rayTargetPositionLockedCamera` | `Transform` | – | – |
| Set Transparent Surfaces Manager | `setTransparentSurfacesManager` | `setTransparentSurfacesSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkSurfacesToRemove()` | 検出リスト内のサーフェスから、自プレイヤーIDの登録をマネージャ経由で外す。 |
| `changeSurfacesToTransparentOrRegularTemporaly(bool state)` | 検出済みかつ自プレイヤーIDが登録されたサーフェスだけを、一時的な透明/通常状態に切り替える。 |
| `setCheckSurfaceActiveState(bool state)` | 有効時のみ有効フラグを更新し、停止時は登録解除、開始/停止に応じてイベントを発火する。 |
| `setLockedCameraActiveState(bool state)` | `lockedCameraActive` を設定するだけ。 |
| `setCheckSurfaceEnabledState(bool state)` | `checkSurfaceEnabled` を設定するだけ。 |
| `setCheckSurfaceEnabledStateFromEditor(bool state)` | `checkSurfaceEnabled` を設定してからコンポーネントを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartCheckSurface` | `UnityEvent` | – |
| `eventOnStopCheckSurface` | `UnityEvent` | – |
| `eventOnSurfaceFound` | `UnityEvent` | – |
| `eventOnNoSurfaceFound` | `UnityEvent` | – |
