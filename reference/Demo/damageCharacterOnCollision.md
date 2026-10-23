# damageCharacterOnCollision

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Demo/damageCharacterOnCollision.cs:5`

**概要**: 衝突相手のRigidbodyに力を加え、設定に応じて`applyDamage`経由でダメージやキル、押し出しを行うデモ用コンポーネント。`damageEnabled`がfalseの間は衝突処理を早期returnする。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Enabled | `damageEnabled` | `bool` | true | – |
| Add Force To Rigidbodies | `addForceToRigidbodies` | `bool` | true | – |
| Force Amount To Rigidbodies | `forceAmountToRigidbodies` | `float` | 1000 | – |
| Apply Damage When Push Character | `applyDamageWhenPushCharacter` | `bool` | – | – |
| Extra Force On Collision | `extraForceOnCollision` | `float` | – | – |

### Objects To Detect Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Layer To Detect | `useLayerToDetect` | `bool` | – | – |
| Layer To Detect | `layerToDetect` | `LayerMask` | – | – |
| Use Tag To Detect | `useTagToDetect` | `bool` | – | – |
| Tag To Detect List | `tagToDetectList` | `List<string>` | new List<string> () | – |

### Collisions Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Minimum Collision Speed | `useMinimumCollisionSpeed` | `bool` | – | – |
| Minimum Collision Speed | `minimumCollisionSpeed` | `float` | – | – |
| Check Minimum Speed On Main Rigidbody | `checkMinimumSpeedOnMainRigidbody` | `bool` | – | – |
| Minimum Speed On Main Rigidbody | `minimumSpeedOnMainRigidbody` | `float` | – | – |

### Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Kill Character On Collision | `killCharacterOnCollision` | `bool` | true | – |
| Push Character On Collision | `pushCharacterOnCollision` | `bool` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |
| Damage Multiplier | `damageMultiplier` | `float` | 1 | – |
| Apply Fixed Damage Value | `applyFixedDamageValue` | `bool` | – | – |
| Fixed Damage Value | `fixedDamageValue` | `float` | – | – |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | new List<string> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setDamageEnabledState(bool state)` | `damageEnabled`に`state`を代入し、衝突時のダメージ適用の有無を切り替える。 |
| `disableDamage()` | `damageEnabled`をfalseにしてダメージ適用を止めるだけ。 |
| `enableDamage()` | `damageEnabled`をtrueにしてダメージ適用を再開するだけ。 |
