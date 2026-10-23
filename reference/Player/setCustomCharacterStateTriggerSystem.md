# setCustomCharacterStateTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Generic Model Controller/setCustomCharacterStateTriggerSystem.cs:5`

**概要**: トリガーに入ったプレイヤーのカスタムキャラクター状態を切り替えるコンポーネント。通常キャラに戻すか、指定名の状態を適用する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Trigger Enabled | `triggerEnabled` | `bool` | true | – |

### Generic Character Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Regular Character | `setRegularCharacter` | `bool` | – | – |
| Custom Character Name To Configure | `customCharacterNameToConfigure` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkCustomCharacterToActivate(GameObject newCharacterGameObject)` | 通常キャラ設定ならカスタム状態を解除し、そうでなければ指定名の状態を設定する。 |
