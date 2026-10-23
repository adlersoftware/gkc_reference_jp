# changeGlobalGravityPower

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/New Powers Behaviors/changeGlobalGravityPower.cs:5`

**概要**: カメラ前方の面の法線に合わせて、レベル全体の重力方向を変えるパワー。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Power Enabled | `powerEnabled` | `bool` | true | – |
| Layer | `layer` | `LayerMask` | – | – |
| Change Global Gravity On Secondary Power Active | `changeGlobalGravityOnSecondaryPowerActive` | `bool` | – | – |
| Change Gravity On Vehicles | `changeGravityOnVehicles` | `bool` | – | – |
| Change Gravity On Character | `changeGravityOnCharacter` | `bool` | – | – |
| Push NPCS | `pushNPCS` | `bool` | – | – |
| Message Name To Send | `messageNameToSend` | `string` | "pushCharacter" | – |
| Ignore Tag List | `ignoreTagList` | `List<string>` | new List<string> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Powers Manager | `powersManager` | `otherPowers` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Gravity Manager | `gravityManager` | `gravitySystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activatePower()` | カメラ前方の静的コライダーに当たると、その法線方向へ`Physics.gravity`を変更する。 |
| `activateSecondaryPower()` | 重力変更に加え、設定に応じてキャラ・乗り物の向きやNPCの押し出しも行う。 |
