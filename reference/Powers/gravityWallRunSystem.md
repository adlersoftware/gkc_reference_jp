# gravityWallRunSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/gravityWallRunSystem.cs:6`

**概要**: 壁走りシステム。ランボタン長押しで重力方向を壁面へ回し、マテリアル・速度・イベントを切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wall Walk Enabled | `wallWalkEnabled` | `bool` | – | – |
| Wall Walk Rotation Speed | `wallWalkRotationSpeed` | `float` | 10 | – |
| Set Anim Speed Multiplier On Wall Run | `setAnimSpeedMultiplierOnWallRun` | `bool` | true | – |
| Anim Speed Multiplier On Wall Run | `animSpeedMultiplierOnWallRun` | `float` | 2 | – |
| Use Extra Raycast Detection On Wall Walk Enabled | `useExtraRaycastDetectionOnWallWalkEnabled` | `bool` | true | – |
| Stop Gravity Adherence When Stop Run | `stopGravityAdherenceWhenStopRun` | `bool` | true | – |
| Avoid Rigidbodies On Raycast Enabled | `avoidRigidbodiesOnRaycastEnabled` | `bool` | – | – |
| Rotate To Original Normal On Air Enabled | `rotateToOriginalNormalOnAirEnabled` | `bool` | true | – |

### Player Render Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Run Mat | `runMat` | `Material` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Trails Active | `trailsActive` | `bool` | true | – |
| Change Player Materials On Wall Run | `changePlayerMaterialsOnWallRun` | `bool` | – | – |

### Player GameObject List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Game Object List | `playerGameObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| Player Game Object With Child List | `playerGameObjectWithChildList` | `List<GameObject>` | new List<GameObject> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Wall Walk Active | `wallWalkActive` | `bool` | – | – |
| Main Coroutine Active | `mainCoroutineActive` | `bool` | – | – |
| Force Walk Wall Active Externally | `forceWalkWallActiveExternally` | `bool` | – | – |
| Renderer Parts | `rendererParts` | `List<Renderer>` | new List<Renderer> () | – |
| Material List | `materialList` | `List<Material>` | new List<Material> () | – |
| Trails | `trails` | `List<TrailRenderer>` | new List<TrailRenderer> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Wall Walk Start | `useEventOnWallWalkStart` | `bool` | – | – |
| Use Event On Wall Walk End | `useEventOnWallWalkEnd` | `bool` | – | – |
| Event On Wall Walk Start | `eventOnWallWalkStart` | `UnityEvent` | – | – |
| Event On Wall Walk End | `eventOnWallWalkEnd` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Gravity System | `mainGravitySystem` | `gravitySystem` | – | – |
| Main Ragdoll Activator | `mainRagdollActivator` | `ragdollActivator` | – | – |
| Trails Prefab | `trailsPrefab` | `GameObject` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中のメインコルーチンを停止し、稼働フラグを下ろす。 |
| `checkIfActivateWallWalk()` | 走行状態とランボタン長押し時間を監視し、条件を満たすと壁走りを開始または停止する。 |
| `activateWallWalk()` | 壁走り用にトレイルとマテリアルを切り替え、速度を落として開始イベントを発火する。 |
| `stopWallWalk()` | マテリアルと速度を戻し、元の法線方向へ重力を回転させて終了イベントを発火する。 |
| `setAnimSpeedMultiplierOnWallRunValue(float newValue)` | 壁走り中のアニメ速度倍率を設定するだけ。 |
| `setOriginalAnimSpeedMultiplierOnWallRunValue()` | 保存しておいた元のアニメ速度倍率へ戻す。 |
| `isWallWalkActive()` | 壁走り中かどうかを返すだけ。 |
| `setWalkWallEnabledState(bool state)` | 有効化時は監視コルーチンを開始し、無効化時は停止と後始末を行う。 |
| `toggleWalkWallEnabledState()` | 壁走りの有効フラグを反転させて設定し直す。 |
| `disableWalkWallState()` | 壁走り中なら停止し、有効フラグも下ろして監視を止める。 |
| `setForceWalkWallActiveExternallyState(bool state)` | 外部から強制発動させるフラグを設定するだけ。 |
| `enableOrDisableWalkWallExternally(bool state, bool activateRunAction)` | 有効フラグを切り替え、必要なら走行入力の開始や強制停止も行う。 |
| `setMeshesInfo()` | ラグドールの各部位へトレイルを生成して無効化し、描画情報を保存して更新する。 |
| `getMaterialList()` | 未取得なら、各レンダラーのマテリアルをリストへ収集する。 |
| `clearRendererList()` | レンダラーリストを空にするだけ。 |
| `storePlayerRenderer()` | 設定されたオブジェクトとその子からレンダラーを集めてリストへ保存する。 |
| `addplayerGameObjectListFromEditor(GameObject newObject)` | 重複が無ければオブジェクトをリストへ追加し、コンポーネントを更新する。 |
| `storePlayerRendererFromEditor()` | レンダラーを収集してから、エディタ用にコンポーネントを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`で更新し、シーンをダーティにする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnWallWalkStart` | `UnityEvent` | – |
| `eventOnWallWalkEnd` | `UnityEvent` | – |
