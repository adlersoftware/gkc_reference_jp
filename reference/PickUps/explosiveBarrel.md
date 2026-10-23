# explosiveBarrel

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `PickUps/explosiveBarrel.cs:6`

**概要**: 衝突速度やダメージで爆発する爆発性の樽。範囲ダメージ、爆風、破片生成、フェード削除、遅延爆発を設定でき、プレイヤーが把持している間は衝突爆発を止められる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Break In Pieces | `breakInPieces` | `bool` | – | – |
| Can Damage To Explosive Barrel Owner | `canDamageToExplosiveBarrelOwner` | `bool` | true | – |
| Explosion Force To Barrel Pieces | `explosionForceToBarrelPieces` | `float` | 5 | – |
| Explosion Radius To Barrel Pieces | `explosionRadiusToBarrelPieces` | `float` | 30 | – |
| Force Mode To Barrel Pieces | `forceModeToBarrelPieces` | `ForceMode` | ForceMode.Impulse | – |

### Explosion/Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Explosion Damage | `explosionDamage` | `float` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Damage Radius | `damageRadius` | `float` | – | – |
| Min Velocity To Explode | `minVelocityToExplode` | `float` | – | – |
| Explosion Delay | `explosionDelay` | `float` | – | – |
| Explosion Force | `explosionForce` | `float` | 300 | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |

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

### Audio Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Explosion Sound | `explosionSound` | `AudioClip` | – | – |
| Explosion Audio Element | `explosionAudioElement` | `AudioElement` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name | `remoteEventName` | `string` | – | – |

### Fade or Remove Broken Pieces

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fade Broken Pieces | `fadeBrokenPieces` | `bool` | true | – |
| Remove Broken Pieces Enabled | `removeBrokenPiecesEnabled` | `bool` | true | – |
| Time To Remove | `timeToRemove` | `float` | 3 | – |
| Default Shader Name | `defaultShaderName` | `string` | "Legacy Shaders/Transparent/Diffuse" | – |
| Use Custom Shader | `useCustomShader` | `bool` | – | – |
| Custom Shader | `customShader` | `Shader` | – | – |
| Color Property Name | `colorPropertyName` | `string` | "_Color" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Can Explode | `canExplode` | `bool` | true | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Broken Barrel | `brokenBarrel` | `GameObject` | – | – |
| Explosion Particles | `explosionParticles` | `GameObject` | – | – |
| Transparent Shader | `transparentShader` | `Shader` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `explodeBarrel()` | 表示とコライダーを無効化して範囲ダメージと爆発を発生させ、破片の生成と爆風、死亡処理を行って破棄コルーチンを開始する。 |
| `canExplodeState(bool state)` | `canExplode` を設定するだけ（把持中に衝突爆発を止める用途）。 |
| `setExplosiveBarrelOwner(GameObject newBarrelOwner)` | 爆発の発生源となる `barrelOwner` を設定するだけ。 |
| `getBarrelRigidbody()` | `mainRigidbody` が未設定なら自身の `Rigidbody` を取得して保持する。 |
| `setBarrelRigidbody(Rigidbody rigidbodyToUse)` | `mainRigidbody` を指定された `Rigidbody` に差し替えるだけ。 |
| `waitToExplode()` | `explosionDelay` が0より大きければ遅延コルーチンを開始し、そうでなければ即座に爆発させる。 |
| `setExplosionValues(float force, float radius)` | 爆発の威力 `explosionForce` とダメージ半径 `damageRadius` をまとめて設定する。 |
