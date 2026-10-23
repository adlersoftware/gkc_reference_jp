# customCharacterControllerBaseBuilder

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Generic Model Controller/customCharacterControllerBaseBuilder.cs:5`

**概要**: カスタムキャラクターコントローラへ設定リストを適用するビルダー。設定ごとの UnityEvent を呼び、対象コンポーネントを更新する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Custom Character Controller Base | `mainCustomCharacterControllerBase` | `customCharacterControllerBase` | – | 設定リスト適用後に更新する対象のキャラクター制御。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `settingsInfoCategoryList` | `List<buildPlayer.settingsInfoCategory>` | new List<buildPlayer.settingsInfoCate… | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `adjustSettingsFromEditor()` | `adjustSettings()` を呼ぶだけ。 |
| `adjustSettings()` | カテゴリごとに設定リストを適用し、最後にコントローラのコンポーネントを更新する。 |
| `adjustSettingsFromList(List<buildPlayer.settingsInfo> settingsList)` | 有効な設定のイベントを送って対象を更新し、最後にシーンをダーティにする。 |
