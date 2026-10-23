# slideZoneSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/slideZoneSystem.cs:5`

**概要**: スライド（滑走）ゾーンのトリガー。入場時にスライド設定をプレイヤーへ渡し、退場時にスライドを終了させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Slide Zone Active | `slideZoneActive` | `bool` | true | – |
| Slide Speed Multiplier | `slideSpeedMultiplier` | `float` | 1 | – |
| Set Enter State Active | `setEnterStateActive` | `bool` | true | – |
| Set Exit State Active | `setExitStateActive` | `bool` | true | – |
| Just Update Slide Transform | `justUpdateSlideTransform` | `bool` | – | – |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Just Activate Jump State On Slide | `justActivateJumpStateOnSlide` | `bool` | – | – |
| Impulse On Jump | `impulseOnJump` | `Vector3` | – | – |

### Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Just Set Adhere To Surfaces Active State | `justSetAdhereToSurfacesActiveState` | `bool` | – | – |
| Adhere To Surfaces Active State | `adhereToSurfacesActiveState` | `bool` | – | – |
| Set Reset Gravity Direction On Slide Exit Enabled State | `setResetGravityDirectionOnSlideExitEnabledState` | `bool` | – | – |
| Reset Gravity Direction On Slide Exit Enabled State | `resetGravityDirectionOnSlideExitEnabledState` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slide Transform | `slideTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 入場時に各種スライド設定を渡して検出を開始し、退場時に検出停止とTransform解除を行う。 |
