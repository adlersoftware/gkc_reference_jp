# remoteEventSearcher

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Event System/remoteEventSearcher.cs:5`

**概要**: 名前で設定を選び、シーン全体または半径内から`remoteEventSystem`を持つオブジェクトを探して、ID/名前条件に合うものへリモートイベントを一斉送信する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remote Events Enabled | `remoteEventsEnabled` | `bool` | true | – |
| Search For Remote Event Socked Enabled | `searchForRemoteEventSockedEnabled` | `bool` | – | – |
| Main Transform Center | `mainTransformCenter` | `Transform` | – | – |

### Remote Event Searcher Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remote Event Searcher Info List | `remoteEventSearcherInfoList` | `List<remoteEventSearcherInfo>` | new List<remoteEventSearcherInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Objects Located List | `objectsLocatedList` | `List<GameObject>` | new List<GameObject> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateRemoteEventSearcher(string remoteEventSearcherName)` | 名前一致の設定を探し、シーン全検索または半径内のオブジェクトへ、ID/名前条件を満たす場合のみリモートイベントを送る。 |

## 内部型

- `remoteEventSearcherInfo`（class）
