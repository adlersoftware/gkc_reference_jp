# activateActionOnCharactersOnScene

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/activateActionOnCharactersOnScene.cs:5`

**概要**: シーン内の全`playerActionSystem`へ名前指定でカスタムアクションを一括起動するコンポーネント。除外設定・最大距離・リモートイベントに対応する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Action Enabled | `activateActionEnabled` | `bool` | true | – |
| Current Character Action Info Index | `currentCharacterActionInfoIndex` | `int` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

### Character Action Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Action Info List | `characterActionInfoList` | `List<characterActionInfo>` | new List<characterActionInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateActionOnCharacters(string actionName)` | 名前に対応する`characterActionInfo`を選び、除外条件と最大距離を満たすシーン内の各`playerActionSystem`で起動やリモートイベント呼び出しを行う。 |

## 内部型

- `characterActionInfo`（class）
