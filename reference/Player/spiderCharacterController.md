# spiderCharacterController

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `vehicleController`
- **ソース**: `Player/Generic Model Controller/spiderCharacterController.cs:5`

**概要**: 蜘蛛型のカスタムキャラクターコントローラ。`vehicleController` を継承し、蜘蛛固有の入力停止フラグを持つ。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Spider | `spider` | `spiderControllerInterface` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jump Input Active | `jumpInputActive` | `bool` | – | – |
| Pause Spider Input | `pauseSpiderInput` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPauseSpiderInputState(bool state)` | `pauseSpiderInput` を設定するだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`Start()`, `inputHoldOrReleaseJump(bool holdingButton)`, `inputHoldOrReleaseTurbo(bool holdingButton)`, `inputSetTurnOnState()`

</details>
