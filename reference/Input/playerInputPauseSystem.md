# playerInputPauseSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/playerInputPauseSystem.cs:5`

**概要**: カテゴリ単位で入力アクションを停止・再開し、停止前の有効状態を覚えておくコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Input List During Action Active Always | `pauseInputListDuringActionActiveAlways` | `bool` | true | – |

### Input Category Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Input Category Info List | `inputCategoryInfoList` | `List<inputCategoryInfo>` | new List<inputCategoryInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `pauseInputByCategory(string categoryName)` | 指定カテゴリ内の各入力を無効化し、その前の有効状態を`previousActiveState` に保存する。 |
| `resumeInputByCategory(string categoryName)` | 指定カテゴリ内で停止前に有効だった入力だけを`setPlayerInputMultiAxesState` で再開する。 |

## 内部型

- `inputCategoryInfo`（class）
- `inputInfo`（class）
