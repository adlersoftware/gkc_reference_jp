# simpleLaser

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `laser`
- **ソース**: `Abilities System/Custom Abilities/simpleLaser.cs:6`

**概要**: カメラから照射するシンプルなレーザー。ヒット判定、ダメージ、レーザードットの表示を扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Laser Enabled | `laserEnabled` | `bool` | true | – |
| Laser Rotation Speed | `laserRotationSpeed` | `float` | 20 | – |
| Use Forward Direction | `useForwardDirection` | `bool` | – | – |
| Use Infinite Raycast Distance | `useInfiniteRaycastDistance` | `bool` | true | – |
| Raycast Distance | `raycastDistance` | `float` | 400 | – |

### Objects To Affect Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Use Objects To Ignore List | `useObjectsToIgnoreList` | `bool` | – | – |
| Objects To Ignore List | `objectsToIgnoreList` | `List<GameObject>` | new List<GameObject> () | – |

### Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Apply Damage Active | `applyDamageActive` | `bool` | – | – |
| Damage Amount | `damageAmount` | `float` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Apply Damage Rate | `applyDamageRate` | `float` | – | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Message On Contact | `sendMessageOnContact` | `bool` | – | – |
| Contact Functions | `contactFunctions` | `UnityEvent` | new UnityEvent () | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Same Object Found | `sameObjectFound` | `bool` | – | – |
| Hitting Surface | `hittingSurface` | `bool` | – | – |
| Laser Can Be Used | `laserCanBeUsed` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hit Point Offset | `hitPointOffset` | `Vector3` | – | – |
| Offset Reference | `offsetReference` | `Transform` | – | – |
| Use Laser Dot | `useLaserDot` | `bool` | – | – |
| Use Laser Dot Icon On Screen | `useLaserDotIconOnScreen` | `bool` | – | – |
| Laser Dot | `laserDot` | `GameObject` | – | – |
| Main Laser Dot On Screen System | `mainLaserDotOnScreenSystem` | `laserDotOnScreenSystem` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setLaserEnabledState(bool state)` | レーザーと `LineRenderer` の表示を切り替え、回転を戻してドット表示と最終ダメージ時刻をリセットする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `contactFunctions` | `UnityEvent` | – |
