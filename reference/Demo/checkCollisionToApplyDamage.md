# checkCollisionToApplyDamage

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Demo/checkCollisionToApplyDamage.cs:6`

**概要**: 衝突した相手へ、体力へのダメージ・キル・押し出しを設定に応じて行うデモ用コンポーネント。`damageEnabled`がfalseの間は衝突処理の冒頭でreturnし、何もしない。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Enabled | `damageEnabled` | `bool` | true | – |

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

### Damage On Detected Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Kill Detected Object | `killDetectedObject` | `bool` | – | – |
| Apply Damage On Detected Object | `applyDamageOnDetectedObject` | `bool` | – | – |
| Push Character Detected | `pushCharacterDetected` | `bool` | – | – |
| Extra Force On Object Detected | `extraForceOnObjectDetected` | `float` | – | – |
| Ignore Shield On Object Detected | `ignoreShieldOnObjectDetected` | `bool` | – | – |
| Damage Type ID On Object Detected | `damageTypeIDOnObjectDetected` | `int` | -1 | – |
| Can Activate Reaction System Temporally On Object Detected | `canActivateReactionSystemTemporallyOnObjectDetected` | `bool` | – | – |
| Damage Reaction ID On Object Detected | `damageReactionIDOnObjectDetected` | `int` | -1 | – |
| Damage Multiplier On Object Detected | `damageMultiplierOnObjectDetected` | `float` | 1 | – |
| Apply Fixed Damage Value On Object Detected | `applyFixedDamageValueOnObjectDetected` | `bool` | – | – |
| Fixed Damage Value On Object Detected | `fixedDamageValueOnObjectDetected` | `float` | – | – |

### Damage On Object Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Kill Object On Collision | `killObjectOnCollision` | `bool` | – | – |
| Apply Damage On Object | `applyDamageOnObject` | `bool` | – | – |
| Push Character On Collision | `pushCharacterOnCollision` | `bool` | – | – |
| Extra Force On Collision | `extraForceOnCollision` | `float` | – | – |
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
| Use Remote Event On Collision | `useRemoteEventOnCollision` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | new List<string> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Collision | `useEventOnCollision` | `bool` | – | – |
| Event On Collision | `eventOnCollision` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Health Management | `mainHealthManagement` | `healthManagement` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setDamageEnabledState(bool state)` | `damageEnabled`に`state`を代入し、衝突時のダメージ処理の有無を切り替える。 |
| `disableDamage()` | `damageEnabled`をfalseにして衝突時のダメージ処理を止めるだけ。 |
| `enableDamage()` | `damageEnabled`をtrueにして衝突時のダメージ処理を再開するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCollision` | `UnityEvent` | – |
