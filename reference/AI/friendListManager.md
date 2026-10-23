# friendListManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/friendListManager.cs:7`

**概要**: プレイヤーの仲間リストと命令メニューを管理するコンポーネント。仲間の追加/削除、個別・全体命令の送信、メニュー開閉、全滅時のチーム蘇生を担当する。

**公式ドキュメント抜粋**（[Friend List Manager](../../docs/player-controller-components/player-controller/friend-list-manager.md)）

> Used to manage the different friendly AI found by the player, to give orders to it. It can be activated with K by default.

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Open Menu Enabled | `openMenuEnabled` | `bool` | true | – |
| Friend Manager Enabled | `friendManagerEnabled` | `bool` | – | – |
| Menu Panel Name | `menuPanelName` | `string` | "Friend List Manager" | – |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | true | – |
| Used By AI | `usedByAI` | `bool` | – | – |

### Order Info Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Order Info List | `orderInfoList` | `List<orderInfo>` | new List<orderInfo> () | – |

### Order Button Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Order Button List | `orderButtonList` | `List<Button>` | new List<Button> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Call To Friends Order Name | `callToFriendsOrderName` | `string` | "Follow" | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event If System Disabled | `useEventIfSystemDisabled` | `bool` | – | – |
| Event If System Disabled | `eventIfSystemDisabled` | `UnityEvent` | – | – |
| Use Event To Send Friend Added | `useEventToSendFriendAdded` | `bool` | – | – |
| Event To Send Friend Added | `eventToSendFriendAdded` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use Event To Send Friend Removed | `useEventToSendFriendRemoved` | `bool` | – | – |
| Event To Send Friend Removed | `eventToSendFriendRemoved` | `eventParameters.eventToCallWithGameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Menu Opened | `menuOpened` | `bool` | – | – |
| Friends List | `friendsList` | `List<friendInfo>` | new List<friendInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Friends Menu Content | `friendsMenuContent` | `GameObject` | – | – |
| Friend List Content | `friendListContent` | `GameObject` | – | – |
| Friend List Element | `friendListElement` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkEventOnSystemDisabled()` | システム無効イベントが有効なら`eventIfSystemDisabled`を発火するだけ。 |
| `openOrCloseFriendMenu(bool state)` | 可否とポーズ状態を確認して`menuOpened`を更新し、UI・ポーズ・操作を切り替え、運転中は車両カメラも止める。 |
| `openOrCLoseFriendMenuFromTouch()` | 現在の`menuOpened`を反転して`openOrCloseFriendMenu`を呼ぶ。 |
| `closeFriendMenuIfOpen()` | メニューが開いている場合のみ閉じる。 |
| `closeFriendMenu()` | 閉じる要求を`openOrCloseFriendMenu(false)`へ渡すだけ。 |
| `addFriend(GameObject friend)` | 未登録ならリスト要素を生成して名前とTransformを設定し、`friendsList`へ追加して追加イベントを発火する。 |
| `setFriendListName()` | 各仲間要素の名前テキストを「連番.- 名前」に更新するだけ。 |
| `checkIfContains(Transform friend)` | `friendsList`内に同じTransformの仲間がいるかを返す。 |
| `setIndividualOrder(Button pressedButton)` | 押されたボタンのテキストを命令名として、その仲間だけに個別命令を実行する。 |
| `setGeneralOrderByName(string orderName)` | 指定した命令名を全仲間へまとめて適用する。 |
| `setGeneralOrder(Button pressedButton)` | 押されたボタンのテキストを命令名として全体命令を実行する。 |
| `callToFriends()` | `callToFriendsOrderName`(既定Follow)を全体命令として実行する。 |
| `findFriendsInRadius(float radius)` | プレイヤー周囲のコライダーからAIを探し、自身のコライダーを進入扱いで通知して発見させる。 |
| `setCurrentStateText(int index, string state)` | 指定インデックスの仲間の状態テキストを「State: 状態」に更新する。 |
| `removeFriend(Transform friend)` | 一致する仲間のUI要素を破棄してリストから削除し、削除イベントを発火する。 |
| `removeAllFriends()` | 全仲間のUI要素を破棄して`friendsList`を空にする。 |
| `getAllFriendList()` | 仲間のGameObjectリストを返し、リストが空ならnullを返す。 |
| `getClosestByDistanceFriend()` | プレイヤー位置から最も近い仲間のTransformを返し、該当が無ければnullを返す。 |
| `anyFriendOnList()` | `friendsList`が空でないかを返すだけ。 |
| `setUsedByAIState(bool state)` | `usedByAI`フラグを設定するだけ。 |
| `inputOpenOrCloseFriendListMenu()` | メニューが有効で他メニューが開いていなければ、開閉状態を反転して切り替える。 |
| `setFriendManagerEnabledState(bool state)` | `friendManagerEnabled`フラグを設定するだけ。 |
| `resurrectFullTeam()` | 有効時、リスト全員を`applyDamage.resurrectCharacter`で蘇生させる。 |
| `resurrectFullTeamAndPlayer()` | 全仲間を蘇生したうえで、プレイヤー自身も`resurrectCharacter`で蘇生する。 |
| `setOpenMenuEnabled(bool state)` | `openMenuEnabled`フラグを設定するだけ。 |
| `setFriendManagerEnabledStateFromEditor(bool state)` | `friendManagerEnabled`を設定してからコンポーネントを更新する。 |
| `setOpenMenuEnabledFromEditor(bool state)` | `openMenuEnabled`を設定してからコンポーネントを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventIfSystemDisabled` | `UnityEvent` | – |

## 内部型

- `friendInfo`（class）
- `orderInfo`（class）
