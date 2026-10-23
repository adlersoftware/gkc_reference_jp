# attrackObjectsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/attrackObjectsSystem.cs:7`

**概要**: 照準方向のオブジェクトを引き寄せて保持し、ため撃ちで投げる吸引武器の挙動。掴んだ物のタグ・レイヤー・重力を退避して復元する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attraction Enabled | `attractionEnabled` | `bool` | – | – |
| Attraction Apply Force | `attractionApplyForce` | `bool` | true | – |
| Attraction Radius | `attractionRadius` | `float` | 20 | – |
| Layer To Search | `layerToSearch` | `LayerMask` | – | – |
| Attraction Velocity | `attractionVelocity` | `float` | 10 | – |
| Attraction Force | `attractionForce` | `float` | 1000 | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |
| Max Throw Force | `maxThrowForce` | `float` | 3500 | – |
| Increase Throw Force Speed | `increaseThrowForceSpeed` | `float` | 1500 | – |
| Tag To Locate | `tagToLocate` | `List<string>` | new List<string> () | – |
| Layer To Damage | `layerToDamage` | `LayerMask` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List On Grab Object | `remoteEventNameListOnGrabObject` | `List<string>` | new List<string> () | – |
| Remote Event Name List On Drop Object | `remoteEventNameListOnDropObject` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Carrying Objects | `carryingObjects` | `bool` | – | – |
| Attraction Active | `attractionActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Events On Activate Attraction | `eventsOnActivateAttraction` | `UnityEvent` | – | – |
| Event On Deactivate Attraction | `eventOnDeactivateAttraction` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Power Slider | `powerSlider` | `Slider` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Attraction Position | `attractionPosition` | `Transform` | – | – |
| Player Collider | `playerCollider` | `Collider` | – | – |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |
| Main Player Weapon System | `mainPlayerWeaponSystem` | `playerWeaponSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`があれば停止するだけ。 |
| `setAttractionEnabledState(bool state)` | `attractionEnabled`を設定し、偽のときは`updateSystemCoroutine()`を呼ぶだけ。 |
| `checkGrabObject()` | 既存の`grabObjectsCoroutine`を止め、0.05秒後に掴み処理を行うコルーチンを開始する。 |
| `inputGrabObjects()` | 入力から`checkGrabObject()`を呼び出すだけ。 |
| `inputHoldToLaunchObject()` | 吸引有効かつ保持中で発動から0.5秒過ぎていれば、`addForceToLaunchObjects()`で投擲力を貯める。 |
| `inputReleaseToLaunchObject()` | 保持中なら`dropObjects()`で投げ、吸引状態を切りコルーチンを止めて解除イベントを呼ぶ。 |
| `grabCloseObjects()` | `attractionPosition`周辺の対象タグとRigidbodyを集め、衝突・重力・タグを退避して保持リストに入れる。 |
| `dropObjects()` | カメラ前方の着弾点を求め、保持中の全オブジェクトを`dropObject`で放し、一覧とスライダーを初期化する。 |
| `addForceToLaunchObjects()` | `maxThrowForce`未満なら投擲力を増やし、300超でスライダーへ反映する。 |
| `dropObject(grabbedObject currentGrabbedObject, Vector3 launchDirection)` | 対象の親・タグ・レイヤー・重力を戻し、力が300超なら`launchedObjects`を付けて投げる。 |
| `checkIfDropObject(GameObject objectToCheck)` | 保持リストから一致する物を探し、見つかれば`dropObject`で放して参照を消す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventsOnActivateAttraction` | `UnityEvent` | – |
| `eventOnDeactivateAttraction` | `UnityEvent` | – |

## 内部型

- `grabbedObject`（class）
