# simpleGUILayoutStateManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleGUILayoutStateManager.cs:5`

**概要**: シーン内の全`MonoBehaviour`の`useGUILayout`を一括で切り替える。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set State On Start | `setStateOnStart` | `bool` | – | – |
| State On Start | `stateOnStart` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setGUILayoutState(bool state)` | シーン内の全`MonoBehaviour`を取得し、`useGUILayout`が`state`と違うものをまとめて設定する。 |
