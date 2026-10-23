# puzzleSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Puzzles/puzzleSystem.cs:7`

**概要**: ドラッグ可能なオブジェクトを掴んで回転や距離変更を行い、所定数配置すると解決するパズル装置。プレイヤー入力とイベントで状態を管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Respawn Dragable Elements | `respawnDragableElements` | `bool` | – | – |
| Respawn Dragable Elements In Original Position | `respawnDragableElementsInOriginalPosition` | `bool` | – | – |
| Respawn Position | `respawnPosition` | `Transform` | – | – |
| Drag Velocity | `dragVelocity` | `float` | 8 | – |
| Layer | `layer` | `LayerMask` | – | – |
| Max Raycast Distance | `maxRaycastDistance` | `float` | – | – |
| Check If Objects To Far From Puzzle Zone | `checkIfObjectsToFarFromPuzzleZone` | `bool` | – | – |
| Max Distance From Puzzle Zone | `maxDistanceFromPuzzleZone` | `float` | – | – |
| Change Hold Distance Speed | `changeHoldDistanceSpeed` | `float` | 2 | – |
| Use Collider Material While Grabbed | `useColliderMaterialWhileGrabbed` | `bool` | – | – |
| Grabbed Collider Material | `grabbedColliderMaterial` | `PhysicsMaterial` | – | – |

### Dragable Elements Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dragable Elements | `dragableElements` | `List<GameObject>` | new List<GameObject> () | – |

### Object ROtation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Freeze Rotation When Grabbed | `freezeRotationWhenGrabbed` | `bool` | – | – |
| Object Can Be Rotated | `objectCanBeRotated` | `bool` | – | – |
| Rotate Speed | `rotateSpeed` | `float` | – | – |
| Horizontal Rotation Enabled | `horizontalRotationEnabled` | `bool` | true | – |
| Vertical Rotation Enabled | `verticalRotationEnabled` | `bool` | true | – |
| Rotate To Camera In Fixed Position | `rotateToCameraInFixedPosition` | `bool` | – | – |
| Rotation Speed | `rotationSpeed` | `float` | – | – |

### Puzzle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reset Objects When Stop Use | `resetObjectsWhenStopUse` | `bool` | – | – |
| Can Reset Objects While Using | `canResetObjectsWhileUsing` | `bool` | – | – |
| Number Objects To Place | `numberObjectsToPlace` | `int` | – | – |
| Disable Object Action After Resolve | `disableObjectActionAfterResolve` | `bool` | – | – |
| Disable Object Trigger After Resolve | `disableObjectTriggerAfterResolve` | `bool` | – | – |
| Wait Delay To Stop Use Puzzle After Resolve | `waitDelayToStopUsePuzzleAfterResolve` | `float` | – | – |

### Camera Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rotate Around Point Enabled | `rotateAroundPointEnabled` | `bool` | – | – |
| Rotate Around Point Speed | `rotateAroundPointSpeed` | `float` | – | – |
| Rotation Point Pivot | `rotationPointPivot` | `Transform` | – | – |
| Rotation Point Camera | `rotationPointCamera` | `Transform` | – | – |
| Camera Position | `cameraPosition` | `Transform` | – | – |
| Use Vertical Rotation Limit | `useVerticalRotationLimit` | `bool` | – | – |
| Use Horizontal Rotation Limit | `useHorizontalRotationLimit` | `bool` | – | – |
| Vertical Rotation Limit | `verticalRotationLimit` | `Vector2` | new Vector2 (-90, 90) | – |
| Horizontal Rotation Limit | `horizontalRotationLimit` | `Vector2` | new Vector2 (-90, 90) | – |

### Action Screen Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Action Screen | `activateActionScreen` | `bool` | true | – |
| Action Screen Name | `actionScreenName` | `string` | "Use Puzzle System" | – |
| Use Mesh Text For Clues | `useMeshTextForClues` | `bool` | – | – |
| Mesh Text Game Object | `meshTextGameObject` | `GameObject` | – | – |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Puzzle Solved Sound | `usePuzzleSolvedSound` | `bool` | – | – |
| Puzzle Solved Sound | `puzzleSolvedSound` | `AudioClip` | – | – |
| Puzzle Solved Audio Element | `puzzleSolvedAudioElement` | `AudioElement` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Puzzle Solved | `puzzleSolved` | `bool` | – | – |
| Using Puzzle | `usingPuzzle` | `bool` | – | – |
| Current Number Objects Placed | `currentNumberObjectsPlaced` | `int` | – | – |
| Touching | `touching` | `bool` | – | – |
| Moving Object | `movingObject` | `bool` | – | – |
| Current Grabbed Object | `currentGrabbedObject` | `GameObject` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Reset Puzzle | `useEventOnResetPuzzle` | `bool` | – | – |
| Reset Puzzle Event | `resetPuzzleEvent` | `UnityEvent` | – | – |
| Puzzle Solved Event | `puzzleSolvedEvent` | `UnityEvent` | – | – |
| Use Event After Resolve Delay | `useEventAfterResolveDelay` | `bool` | – | – |
| Event After Resolve Delay | `eventAfterResolveDelay` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Electronic Device Manager | `electronicDeviceManager` | `electronicDevice` | – | – |
| Device String Action Manager | `deviceStringActionManager` | `deviceStringAction` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | – | – |
| Gizmo Radius | `gizmoRadius` | `float` | 0.1f | – |
| Gizmo Arrow Length | `gizmoArrowLength` | `float` | 1 | – |
| Gizmo Arrow Line Length | `gizmoArrowLineLength` | `float` | 2.5f | – |
| Gizmo Arrow Angle | `gizmoArrowAngle` | `float` | 20 | – |
| Gizmo Arrow Color | `gizmoArrowColor` | `Color` | Color.white | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `resetObjects()` | 全オブジェクトを初期位置と回転へ戻し、配置数リセットとリセットイベントを行う。 |
| `canBeDragged(GameObject objectToCheck)` | `dragableElements`に含まれるかその子なら該当オブジェクトを返し、無ければnullを返す。 |
| `dropObject()` | 回転固定やコライダー材質を戻し、掴み・移動・回転の各フラグと参照をクリアする。 |
| `checkIfObjectGrabbed(GameObject objectToCheck)` | 掴んでいるオブジェクトと一致すれば`dropObject`を呼ぶだけ。 |
| `startOrStopPuzzle()` | 使用状態を反転し、開始時はプレイヤー登録、終了時は必要ならリセットと回転の復元を行う。 |
| `setCurrentPlayer(GameObject player)` | プレイヤーの管理・カメラ・入力を取得し、このパズルを現在使用中として登録する。 |
| `increaseNumberObjectsPlaced()` | 配置数を1増やし、必要数に達したら`solvePuzzle`を呼ぶ。 |
| `resetNumberObjectsPlaced()` | 配置数を0にするだけ。 |
| `solvePuzzle()` | 解決イベントを発火し、解決済みにして必要ならアイコン削除・トリガー無効・効果音を行う。 |
| `setMainColliderTriggerEnabledState(bool state)` | 解決後にトリガー無効とする設定なら再有効化を拒否しつつ、`mainCollider`を切替える。 |
| `resetCurrentObjectRotation()` | 既存コルーチンを止め、掴んだオブジェクトを初期回転へ戻すコルーチンを開始する。 |
| `removeDeviceFromList()` | プレイヤーの`usingDevicesSystem`からこのオブジェクトをデバイス一覧から外す。 |
| `playSound(AudioElement soundEffect)` | `soundEffect`がnullでなければピッチを確認のうえ`AudioPlayer`で一度再生する。 |
| `inputSetRotateObjectState(bool state)` | 使用中で回転可能なら、回転フラグとRigidbodyの回転固定を`state`に合わせて切替える。 |
| `inputIncreaseObjectHolDistanceByButton(bool state)` | 使用中かつ移動中なら、距離を広げるフラグを`state`に合わせるだけ。 |
| `inputDecreaseObjectHolDistanceByButton(bool state)` | 使用中かつ移動中なら、距離を狭めるフラグを`state`に合わせるだけ。 |
| `inputSetObjectHolDistanceByMouseWheel(bool state)` | 使用中かつ移動中なら、ホイール時刻を記録し`state`に応じて距離変更フラグを立てる。 |
| `inputResetPuzzle()` | 使用中で解決前なら、非把持時は全体リセット、把持中は掴んだ物の回転を戻す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `resetPuzzleEvent` | `UnityEvent` | – |
| `puzzleSolvedEvent` | `UnityEvent` | – |
| `eventAfterResolveDelay` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnTriggerExit(Collider col)`

</details>

## 内部型

- `grabableObjectsInfo`（class）
