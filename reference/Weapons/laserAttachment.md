# laserAttachment

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `laser`
- **ソース**: `Weapons/Attachments/laserAttachment.cs:5`

**概要**: 武器に付けるレーザー照準アタッチメント。カメラ前方へレイを飛ばし、レーザーラインと着弾ドットを描画する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Laser Enabled | `laserEnabled` | `bool` | true | – |
| Laser Rotation Speed | `laserRotationSpeed` | `float` | 20 | – |
| Always Look In Camera Direction | `alwaysLookInCameraDirection` | `bool` | – | – |
| Use Laser Dot | `useLaserDot` | `bool` | – | – |
| Use Laser Dot Icon On Screen | `useLaserDotIconOnScreen` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Message On Contact | `sendMessageOnContact` | `bool` | – | – |
| Contant Functions | `contantFunctions` | `UnityEvent` | new UnityEvent () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Same Object Found | `sameObjectFound` | `bool` | – | – |
| Hitting Surface | `hittingSurface` | `bool` | – | – |
| Laser Can Be Used | `laserCanBeUsed` | `bool` | – | – |
| Hit Point Offset | `hitPointOffset` | `Vector3` | – | – |
| Offset Reference | `offsetReference` | `Transform` | – | – |
| Laser Dot Active | `laserDotActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | – |
| Weapon Manager | `weaponManager` | `playerWeaponSystem` | – | – |
| Ik Weapon Manager | `IkWeaponManager` | `IKWeaponSystem` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Laser Dot | `laserDot` | `GameObject` | – | – |
| Main Laser Dot On Screen System | `mainLaserDotOnScreenSystem` | `laserDotOnScreenSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止するだけ。 |
| `setLaserEnabledState(bool state)` | `laserEnabled`を設定してライン表示・回転・ドットを切り替え、有効時は更新コルーチンを開始する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `contantFunctions` | `UnityEvent` | – |
