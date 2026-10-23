# characterActionSystemChecker

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/characterActionSystemChecker.cs:5`

**概要**: `playerActionSystem`を監視し、指定リストのアクションが検出されたら自動で再生するチェッカー。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action System Checker Enabled | `actionSystemCheckerEnabled` | `bool` | true | – |
| Actions To Play Automatically List | `actionsToPlayAutomaticallyList` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Action System | `mainPlayerActionSystem` | `playerActionSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkToPlayActionAutomatically()` | チェッカー有効かつ非アクション中で、現在のアクション名が`actionsToPlayAutomaticallyList`にあれば`playCurrentAnimation`を呼ぶ。 |
