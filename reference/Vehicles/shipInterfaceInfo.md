# shipInterfaceInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/shipInterfaceInfo.cs:7`

**概要**: 宇宙船HUDのテキストやバーを毎フレーム更新する船用インターフェース。武器名・弾薬・体力・エネルギー・燃料などを表示する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Interface Enabled | `vehicleInterfaceEnabled` | `bool` | true | – |
| Vehicle | `vehicle` | `GameObject` | – | – |
| Compass Enabled | `compassEnabled` | `bool` | – | – |
| Speed Extra String | `speedExtraString` | `string` | " km/h" | – |

### Compass Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Compass Base | `compassBase` | `RectTransform` | – | – |
| North | `north` | `RectTransform` | – | – |
| South | `south` | `RectTransform` | – | – |
| East | `east` | `RectTransform` | – | – |
| West | `west` | `RectTransform` | – | – |
| Altitude Marks | `altitudeMarks` | `RectTransform` | – | – |

### Other UI Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Interface Canvas | `interfaceCanvas` | `GameObject` | – | – |
| Pitch Value | `pitchValue` | `Text` | – | – |
| Yaw Value | `yawValue` | `Text` | – | – |
| Roll Value | `rollValue` | `Text` | – | – |
| Altitude Value | `altitudeValue` | `Text` | – | – |
| Velocity Value | `velocityValue` | `Text` | – | – |
| Coordinate X Value | `coordinateXValue` | `Text` | – | – |
| Coordinate Y Value | `coordinateYValue` | `Text` | – | – |
| Coordinate Z Value | `coordinateZValue` | `Text` | – | – |
| Level | `level` | `RectTransform` | – | – |
| Altitude Mark Speed | `altitudeMarkSpeed` | `float` | – | – |
| Health Bar | `healthBar` | `Slider` | – | – |
| Energy Bar | `energyBar` | `Slider` | – | – |
| Fuel Bar | `fuelBar` | `Slider` | – | – |
| Weapon Name | `weaponName` | `Text` | – | – |
| Weapon Ammo | `weaponAmmo` | `Text` | – | – |
| Can Land | `canLand` | `Text` | – | – |
| Engines State | `enginesState` | `Text` | – | – |
| Health Content | `healthContent` | `GameObject` | – | – |
| Energy Contet | `energyContet` | `GameObject` | – | – |
| Fuel Content | `fuelContent` | `GameObject` | – | – |
| Weapon Content | `weaponContent` | `GameObject` | – | – |

### Componets

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| HUD Manager | `HUDManager` | `vehicleHUDManager` | – | – |
| Gravity Manager | `gravityManager` | `vehicleGravityControl` | – | – |
| Weapon Manager | `weaponManager` | `vehicleWeaponSystem` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Interface Active | `interfaceActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableInterface(bool state)` | `vehicleInterfaceEnabled`がfalseなら何もせず、trueなら状態を設定してキャンバスを切り替える。 |
| `shipCanLand(bool state)` | `canLand`テキストを着陸可否に応じて「YES」か「NO」にするだけ。 |
| `shipEnginesState(bool state)` | `enginesState`テキストを「ON」か「OFF」にするだけ。 |
