# brainwashAIState

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/brainwashAIState.cs:5`

**概要**: キャラクターを洗脳して陣営・タグ・名前・パートナーを変更するステートで、`GKC_Utils`の処理へ設定を渡す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Faction To Configure | `factionToConfigure` | `string` | "Friend Soldiers" | – |
| Set New Name | `setNewName` | `bool` | – | – |
| New Name | `newName` | `string` | – | – |
| AI Is Friend | `AIIsFriend` | `bool` | – | – |
| New Tag | `newTag` | `string` | "friend" | – |
| Follow Partner On Trigger Enabled | `followPartnerOnTriggerEnabled` | `bool` | true | – |
| Set Player As Partner | `setPlayerAsPartner` | `bool` | true | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Events | `useRemoteEvents` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | new List<string> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Game Object | `characterGameObject` | `GameObject` | – | – |
| New Partner Game Object | `newPartnerGameObject` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateState()` | 対象が設定済みなら、陣営やタグ等の設定を`GKC_Utils`の洗脳処理へ渡して実行する。 |
| `setnewPartnerGameObject(GameObject newObject)` | `newPartnerGameObject`を`newObject`に設定するだけ。 |
