# remoteEventSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Event System/remoteEventSystem.cs:6`

**概要**: 名前付きのリモートイベントを、引数なし/float/bool/GameObject/Transform/stringの`UnityEvent`に割り当てて発火する仕組み。イベント単位の有効・無視・発動後無効化と全体の有効状態を管理する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remote Events Enabled | `remoteEventsEnabled` | `bool` | true | オンにするとリモートイベントの呼び出しを受け付ける。 |
| Remote Event System Name | `remoteEventSystemName` | `string` | – | リモートイベント検索で対象を絞り込むための識別名。 |
| Remote Event System ID | `remoteEventSystemID` | `int` | – | リモートイベント検索で対象を絞り込むための識別ID。 |

### Remote Events On Start Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Remote Events On Start | `activateRemoteEventsOnStart` | `bool` | – | オンにすると開始時に指定イベントをまとめて実行する。 |

### Object Searcher

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name To Search | `objectSearcherName` | `string` | "" | イベント一覧を名前で絞り込むための検索文字列。 |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | オンにするとイベント実行時に名前をログ出力する。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `remoteEventsOnStartList` | `List<string>` | new List<string> () | – |
| `eventInfoList` | `List<eventInfo>` | new List<eventInfo> () | – |
| `objectSearchResultList` | `List<string>` | new List<string> () | – |
| `searchObjectsActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `callRemoveEvent(string eventName)` | 名前は削除だが中身は`callRemoteEvent`を呼ぶだけで、指定名のイベントを通常発火する。 |
| `callRemoteEvent(string eventName)` | 有効時、名前が一致する有効かつ無視でない要素を探し、`useRegularEvent`なら`UnityEvent`を呼び、必要なら無効化する。 |
| `callRemoteEventWithAmount(string eventName, float amount)` | 名前一致かつ`useAmountOnEvent`の要素の`eventToActiveAmount`に`amount`を渡して呼ぶ。 |
| `callRemoteEventWithBool(string eventName, bool state)` | 名前一致かつ`useBoolOnEvent`の要素の`eventToActiveBool`に`state`を渡して呼ぶ。 |
| `callRemoteEventWithGameObject(string eventName, GameObject objectToSend)` | 名前一致かつ`useGameObjectOnEvent`の要素の`eventToActiveGameObject`に`objectToSend`を渡して呼ぶ。 |
| `callRemoteEventWithTransform(string eventName, Transform transformToSend)` | 名前一致かつ`useTransformOnEvent`の要素の`eventToActiveTransform`に`transformToSend`を渡して呼ぶ。 |
| `callRemoteEventWithString(string eventName, string strintParameter)` | 名前一致かつ`useStringOnEvent`の要素の`eventToActivateString`に文字列を渡して呼ぶ。 |
| `setEnabledEventState(string eventName)` | `setEnabledOrDisabledEventState(true, eventName)`を呼ぶだけのラッパー。 |
| `setDisabledEventState(string eventName)` | `setEnabledOrDisabledEventState(false, eventName)`を呼ぶだけのラッパー。 |
| `setEnabledOrDisabledEventState(bool state, string eventName)` | 名前が一致する最初の要素の`eventEnabled`を設定して抜ける。 |
| `setIgnoreEventActiveState(string eventName)` | `setIgnoreEventState(true, eventName)`を呼ぶだけのラッパー。 |
| `setIgnoreEventDeactiveState(string eventName)` | `setIgnoreEventState(false, eventName)`を呼ぶだけのラッパー。 |
| `setIgnoreEventState(bool state, string eventName)` | `FindIndex`で名前一致の要素を探し、見つかれば`ignoreEventActive`を設定する。 |
| `setRemoteEventsEnabledState(bool state)` | `remoteEventsEnabled`を設定するだけの薄いセッター。 |
| `getRemoteEventSystemName()` | `remoteEventSystemName`を返すゲッター。 |
| `getRemoteEventSystemID()` | `remoteEventSystemID`を返すゲッター。 |
| `clearObjectsSearcResultList()` | 検索結果と検索名を空にし、`searchObjectsActive`と各要素の`pauseVisibleOnEditor`を偽にして更新する。 |
| `showObjectsBySearchName()` | `objectSearcherName`を小文字化し、名前が部分一致/一致する要素名を重複なく`objectSearchResultList`に集める。 |
| `setEnabledEventStateFromEditor(string eventName)` | 有効化を適用した後に`updateComponent`を呼ぶエディタ用ラッパー。 |
| `setDisabledEventStateFromEditor(string eventName)` | 無効化を適用した後に`updateComponent`を呼ぶエディタ用ラッパー。 |
| `setRemoteEventsEnabledStateFromEditor(bool state)` | 全体の有効状態を設定してから`updateComponent`を呼ぶエディタ用関数。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`を呼んでシーン更新をマークする。 |

## 内部型

- `eventInfo`（class）
