# openInitialPopUpWindow

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/openInitialPopUpWindow.cs:11`

**概要**: プレイ開始時に案内用ポップアップウィンドウを開くかどうかを制御するエディタ補助。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Initial Pop Window Enabled | `showInitialPopWindowEnabled` | `bool` | true | – |
| Check For Presets Active | `checkForPresetsActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setShowInitialPopWindowEnabledState(bool state)` | `showInitialPopWindowEnabled`を更新し、`false`にした時は`checkForPresetsActive`も`false`にする。 |
