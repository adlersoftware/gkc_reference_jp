# simpleShowHideMouseCursor

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Cutscene/simpleShowHideMouseCursor.cs:5`

**概要**: `menuPause` 経由でマウスカーソルとゲームパッドカーソルの表示を切り替える小規模コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Or Hide Mouse Cursor Enabled | `showOrHideMouseCursorEnabled` | `bool` | true | – |
| Enable Gamepad Cursor | `enableGamepadCursor` | `bool` | – | – |
| Search Main Player On Scene Enabled | `searchMainPlayerOnSceneEnabled` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Mouse Cursor Active | `showMouseCursorActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Manager | `pauseManager` | `menuPause` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `showMouseCursor()` | `showOrHideMouseCursor(true)` を呼ぶだけ。 |
| `hideMouseCursor()` | `showOrHideMouseCursor(false)` を呼ぶだけ。 |
| `showOrHideMouseCursor(bool state)` | 有効時、状態が変わるときだけ `menuPause` のカーソル・デバイス・サブメニュー状態を切り替える。 |
