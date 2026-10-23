# destroyableObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/destroyableObject.cs:7`

**概要**: 破壊可能オブジェクト。破片化・フェード・破壊音・爆発力を適用し、任意で`setExplosion`による範囲ダメージとイベントを発生させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Explosion Enabled | `explosionEnabled` | `bool` | true | – |
| Destroyed Particles | `destroyedParticles` | `GameObject` | – | – |
| Destroyed Sound | `destroyedSound` | `AudioClip` | – | – |
| Destroyed Audio Element | `destroyedAudioElement` | `AudioElement` | – | – |

### Explosion Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Explosion Force When Destroyed | `useExplosionForceWhenDestroyed` | `bool` | – | – |
| Explosion Radius | `explosionRadius` | `float` | – | – |
| Explosion Force | `explosionForce` | `float` | – | – |
| Explosion Damage | `explosionDamage` | `float` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Kill Objects In Radius | `killObjectsInRadius` | `bool` | – | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |
| Apply Explosion Force To Vehicles | `applyExplosionForceToVehicles` | `bool` | true | – |
| Explosion Force To Vehicles Multiplier | `explosionForceToVehiclesMultiplier` | `float` | 0.2f | – |
| Push Characters On Explosion | `pushCharactersOnExplosion` | `bool` | true | – |
| Search Closest Weak Spot | `searchClosestWeakSpot` | `bool` | – | – |

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

### Detect Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| User Layer Mask | `userLayerMask` | `bool` | – | – |
| Layer | `layer` | `LayerMask` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remove Event Name | `removeEventName` | `string` | – | – |

### Object Pieces Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fade Pieces Enabled | `fadePiecesEnabled` | `bool` | true | – |
| Time To Fade Pieces | `timeToFadePieces` | `float` | – | – |
| Store Renderer Parts | `storeRendererParts` | `bool` | true | – |
| Disable Colliders | `disableColliders` | `bool` | true | – |
| Destroy Object After Face Pieces | `destroyObjectAfterFacePieces` | `bool` | true | – |
| Transparent Shader | `transparentShader` | `Shader` | – | – |
| Default Shader Name | `defaultShaderName` | `string` | "Legacy Shaders/Transparent/Diffuse" | – |
| Color Property Name | `colorPropertyName` | `string` | "_Color" | – |

### Meshes Force Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Meshes Explosion Force | `meshesExplosionForce` | `float` | 500 | – |
| Meshes Explosion Radius | `meshesExplosionRadius` | `float` | 50 | – |
| Meshes Explosion Force Mode | `meshesExplosionForceMode` | `ForceMode` | – | – |

### Extra Pieces Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Extra Parts | `useExtraParts` | `bool` | – | – |
| Extra Parts | `extraParts` | `List<GameObject>` | new List<GameObject> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Object Destroyed | `useEventOnObjectDestroyed` | `bool` | – | – |
| Event On Object Destroyed | `eventOnObjectDestroyed` | `UnityEvent` | – | – |
| Use Event On Object Before Destroyed | `useEventOnObjectBeforeDestroyed` | `bool` | – | – |
| Event On Object Before Destroyed | `eventOnObjectBeforeDestroyed` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Destroyed | `destroyed` | `bool` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Map Information Manager | `mapInformationManager` | `mapObjectInformation` | – | – |
| Destroyed Source | `destroyedSource` | `AudioSource` | – | – |
| Explosion Center | `explosionCenter` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `destroyObject()` | 破片化・破壊音・`applyDamage.setExplosion`による周囲への爆発を実行し、`destroyed`を立てる。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnObjectDestroyed` | `UnityEvent` | – |
| `eventOnObjectBeforeDestroyed` | `UnityEvent` | – |
