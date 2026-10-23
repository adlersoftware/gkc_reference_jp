# climbRopeTriggerMatchSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/climbRopeTriggerMatchSystem.cs:5`

**概要**: 縄登り用の入退場トリガーを、プレイヤーの `climbRopeSystem` に登録/解除するマッチング用コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Movement Zone Active | `movementZoneActive` | `bool` | true | – |
| Check On Trigger Enter | `checkOnTriggerEnter` | `bool` | true | – |
| Check On Trigger Exit | `checkOnTriggerExit` | `bool` | true | – |
| Tag To Check | `tagToCheck` | `string` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Climb Rope Trigger System | `mainClimbRopeTriggerSystem` | `climbRopeTriggerSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 入場で登録、退場で解除するメソッドを呼ぶ。 |
