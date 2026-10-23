# simpleBreakObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/simpleBreakObject.cs:7`

**概要**: 破壊可能オブジェクト。爆発ダメージ・破片生成・フェード・死亡処理・イベントをまとめて実行し、`fixBrokenObject`で破壊前の状態に戻せる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Break Object Enabled | `breakObjectEnabled` | `bool` | true | – |
| Can Break With Collisions Enabled | `canBreakWithCollisionsEnabled` | `bool` | true | – |
| Min Velocity To Break | `minVelocityToBreak` | `float` | – | – |
| Explosion Sound | `explosionSound` | `AudioClip` | – | – |
| Explosion Audio Element | `explosionAudioElement` | `AudioElement` | – | – |
| Break In Pieces | `breakInPieces` | `bool` | – | – |
| Object Is Kinematic | `objectIsKinematic` | `bool` | – | – |

### Disable Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable Main Object | `disableMainObject` | `bool` | – | – |
| Disable Main Object Mesh | `disableMainObjectMesh` | `bool` | – | – |
| Main Object To Disable | `mainObjectToDisable` | `GameObject` | – | – |
| Remove Pieces Parent | `removePiecesParent` | `bool` | – | – |

### Fade Pieces Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fade Pieces Enabled | `fadePiecesEnabled` | `bool` | – | – |
| Fade Pieces Speed | `fadePiecesSpeed` | `float` | 5 | – |
| Destroy Object After Fade | `destroyObjectAfterFade` | `bool` | – | – |
| Destroy Faded Pieces | `destroyFadedPieces` | `bool` | – | – |
| Time To Remove Pieces | `timeToRemovePieces` | `float` | 3 | – |
| Transparent Shader | `transparentShader` | `Shader` | – | – |
| Default Shader Name | `defaultShaderName` | `string` | "Legacy Shaders/Transparent/Diffuse" | – |
| Color Property Name | `colorPropertyName` | `string` | "_Color" | – |

### Explosion Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Explosion Around Enabled | `useExplosionAroundEnabled` | `bool` | – | – |
| Explosion Damage | `explosionDamage` | `float` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Damage Radius | `damageRadius` | `float` | – | – |
| Explosion Delay | `explosionDelay` | `float` | – | – |
| Can Damage To Object Owner | `canDamageToObjectOwner` | `bool` | – | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |

### Explosion Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Explosion Force To Pieces | `explosionForceToPieces` | `float` | 5 | – |
| Explosion Radius To Pieces | `explosionRadiusToPieces` | `float` | 30 | – |
| Force Mode To Pieces | `forceModeToPieces` | `ForceMode` | ForceMode.Impulse | – |
| Explosion Force | `explosionForce` | `float` | 300 | – |

### Damage Over Time Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Target Over Time | `damageTargetOverTime` | `bool` | – | – |
| Damage Over Time Delay | `damageOverTimeDelay` | `float` | – | – |
| Damage Over Time Duration | `damageOverTimeDuration` | `float` | – | – |
| Damage Over Time Amount | `damageOverTimeAmount` | `float` | – | – |
| Damage Over Time Rate | `damageOverTimeRate` | `float` | – | – |
| Damage Over Time To Death | `damageOverTimeToDeath` | `bool` | – | – |
| Remove Damage Over Time State | `removeDamageOverTimeState` | `bool` | – | – |

### Other Explosion Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Push Characters | `pushCharacters` | `bool` | true | – |
| Kill Objects In Radius | `killObjectsInRadius` | `bool` | – | – |
| Explosion Force Mode | `explosionForceMode` | `ForceMode` | – | – |
| User Layer Mask | `userLayerMask` | `bool` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Apply Explosion Force To Vehicles | `applyExplosionForceToVehicles` | `bool` | true | – |
| Explosion Force To Vehicles Multiplier | `explosionForceToVehiclesMultiplier` | `float` | 0.2f | – |
| Search Closest Weak Spot | `searchClosestWeakSpot` | `bool` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name | `remoteEventName` | `string` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Object Broken | `useEventOnObjectBroken` | `bool` | – | – |
| Event On Object Broken | `eventOnObjectBroken` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Break State Paused | `canBreakStatePaused` | `bool` | – | – |
| Broken | `broken` | `bool` | – | – |
| Fade In Process | `fadeInProcess` | `bool` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Broken Object Pieces Parent | `brokenObjectPiecesParent` | `GameObject` | – | – |
| Spawn Broken Object Pieces Enabled | `spawnBrokenObjectPiecesEnabled` | `bool` | – | – |
| Explosion Particles | `explosionParticles` | `GameObject` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Object Owner | `objectOwner` | `GameObject` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `fixBrokenObject()` | 非表示にしたコライダー/メッシュや対象を復帰させ、`isKinematic`を戻して`broken`をfalseにする。 |
| `activateBreakObject()` | 本体を無効化して爆発・破片生成・死亡処理・破壊イベントを実行し、`broken`を立ててフェードを開始する。 |
| `setCanBreakStatePaused(bool state)` | `canBreakStatePaused`を設定するだけ。 |
| `setObjectOwner(GameObject newObject)` | `objectOwner`を設定するだけ。 |
| `waitToBreak()` | `explosionDelay`が正なら待機してから、0なら即座に`activateBreakObject`を実行する。 |
| `setExplosionValues(float force, float radius)` | `explosionForce`と`damageRadius`を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnObjectBroken` | `UnityEvent` | – |
