# setCanvasParentSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Menu/setCanvasParentSystem.cs:6`

**概要**: パネルの親を指定先へ付け替え、位置・回転・スケールを初期化する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Panel Scale | `setNewPanelScale` | `bool` | – | – |
| New Panel Scale | `newPanelScale` | `Vector3` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Parent Changed | `useEventOnParentChanged` | `bool` | – | – |
| Event On Parent Changed | `eventOnParentChanged` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Panel To Change | `panelToChange` | `RectTransform` | – | – |
| New Panel Parent | `newPanelParent` | `RectTransform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateParentChange()` | `panelToChange`を`newPanelParent`へ付け替え、位置と回転を初期化しスケール設定後にイベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnParentChanged` | `UnityEvent` | – |
