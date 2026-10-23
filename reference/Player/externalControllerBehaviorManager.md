# externalControllerBehaviorManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/externalControllerBehaviorManager.cs:6`

**概要**: 名前付きの外部コントローラ動作を一括管理するコンポーネント。動作開始時に武器を退避し入力を止め、終了時に武器やIKを復帰させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| External Controller Info List | `externalControllerInfoList` | `List<externalControllerInfo>` | new List<externalControllerInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setExternalControllerActive(string nameToCheck)` | `setExternalControllerState(nameToCheck, true)` を呼ぶだけ。 |
| `setExternalControllerDeactive(string nameToCheck)` | `setExternalControllerState(nameToCheck, false)` を呼ぶだけ。 |
| `setExternalControllerState(string nameToCheck, bool state)` | 名前一致の項目を探し、入力の一時停止、状態イベント、射撃停止・武器退避/IK、近接武器の保持や終了時の描画を行う。 |
| `checkInputListToPauseDuringAction(List<playerActionSystem.inputToPauseOnActionIfo> inputList, bool state)` | state なら各入力の現在状態を保存して無効化し、false なら保存状態が有効だった入力を復帰させる。 |

## 内部型

- `externalControllerInfo`（class）
