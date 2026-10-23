# playerInputPanelSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/playerInputPanelSystem.cs:6`

**概要**: タッチパネルとアクション画面の表示切替をまとめて管理するコンポーネント。`inputPanelUISystem` を介して画面を出し入れし、ゲームパッド・キーボード別のパネルを切り替える。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Screen Action Panels Enabled | `screenActionPanelsEnabled` | `bool` | true | ONにすると画面上のアクションパネル機能を有効にする。 |
| Instantiate Input Panel UI If Not Found | `instantiateInputPanelUIIfNotFound` | `bool` | true | ONにするとUIシステムが無い場合にプレハブを生成する。 |

### Player Element Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Input | `playerInput` | `playerInputManager` | – | タッチパネル操作を連携するプレイヤー入力の参照。 |
| Pause Manager | `pauseManager` | `menuPause` | – | 生成したパネルのCanvas設定に使うポーズ管理の参照。 |
| Input Panel Prefab | `inputPanelPrefab` | `GameObject` | – | 入力パネルUIを生成するためのプレハブ。 |
| Screen Action Parent | `screenActionParent` | `GameObject` | – | 画面上アクションパネルを格納する親オブジェクト。 |
| Main Input Panel UI System | `mainInputPanelUISystem` | `inputPanelUISystem` | – | 画面アクション情報を保持する入力パネルUIの参照。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `screenActionPanelsActive` | `bool` | true | – |
| `screenActionInfoList` | `List<screenActionInfo>` | new List<screenActionInfo> () | – |
| `touchPanelsInfoList` | `List<touchPanelsInfo>` | new List<touchPanelsInfo> () | – |
| `touchPanelsSchemesInfoList` | `List<touchPanelsSchemesInfo>` | new List<touchPanelsSchemesInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setInputPanelGameObjectActiveState(bool state)` | `mainInputPanelUISystem` が見つかっている場合のみ、入力パネルのGameObject表示を`state`にする。 |
| `getTouchPanelsList()` | `touchPanelsInfoList` をそのまま返すだけ。 |
| `enableTouchPanelByName(string panelName)` | 指定名のタッチパネルを表示するため、`enableOrDisableTouchPanelByName` をtrueで呼ぶだけ。 |
| `disableTouchPanelByName(string panelName)` | 指定名のタッチパネルを非表示にするため、`enableOrDisableTouchPanelByName` をfalseで呼ぶだけ。 |
| `enableOrDisableTouchPanelByName(string panelName, bool state)` | 名前が一致するタッチパネルの表示を`state`にし、最後に`playerInput` のタッチボタン押下状態をリセットする。 |
| `enableTouchPanelSchemeByName(string panelName)` | 指定スキームを現在として記録し、含まれるパネルだけを表示、メインスキームのフラグも更新してタッチボタンをリセットする。 |
| `enableCurrentMainTouchPanelScheme()` | メインゲーム用かつ有効なスキームを探し、`enableTouchPanelSchemeByName` で再適用するだけ。 |
| `enablePreviousTouchPanelScheme()` | `previousTouchPanelsSchemesInfo` があれば、その名前でスキームを再適用するだけ。 |
| `enableOrDisableActionScreen(string actionScreenName)` | `canUseActionPanel` がtrueの時、指定画面のGameObject表示を反転し、現在/前回の画面情報を更新する。 |
| `enableOrDisableActionScreenTemporally(string actionScreenName)` | 現在画面の記録は変えずに、指定アクション画面のGameObject表示だけを反転する。 |
| `enableOrDisableActionScreen(string actionScreenName, bool state)` | 指定画面を`state`にし、ゲームパッド有無で対応GameObjectを選び、親パネルとメイン画面も調整する。 |
| `enableActionScreen(string actionScreenName)` | 指定アクション画面を表示するだけで、非表示側のGameObjectは操作しない。 |
| `disableActionScreen(string actionScreenName)` | 指定アクション画面の全GameObjectを非表示にし、メイン画面ならアクティブフラグもfalseにする。 |
| `enablePreviousActionScreen()` | 前回のアクション画面があれば`enableSingleActionScreen` で復帰し、無ければ現在画面を閉じて記録を消す。 |
| `enableSingleActionScreen(string actionScreenName)` | 指定画面だけを表示し、他のアクション画面のGameObjectを非表示にする排他切替。 |
| `checkEnableMainGameScreenActionPanel()` | 有効なメインゲーム画面パネルを探し、`enableSingleActionScreen` で表示に戻す。 |
| `enableSecondaryActionPanel(string actionScreenName)` | `enableOrDisableSecondaryActionPanel` をtrueで呼ぶだけ。 |
| `disableSecondaryActionPanel(string actionScreenName)` | `enableOrDisableSecondaryActionPanel` をfalseで呼ぶだけ。 |
| `enableOrDisableSecondaryActionPanel(string actionScreenName, bool state)` | 指定画面のサブパネルを、ゲームパッド用か通常用かを選んで`state`にし、もう一方は非表示にする。 |
| `checkDisableMainGameScreenActionPanel()` | 有効なメインゲーム画面パネルのGameObjectをすべて非表示にする。 |
| `checkPanelsActiveOnGamepadOrKeyboard(bool checkKeyboard)` | 表示中のアクション画面について、キーボードなら通常用、ゲームパッドならゲームパッド用GameObjectへ切り替える。 |
| `enableOrDisableScreenActionParent(bool state)` | `screenActionPanelsActive` がtrueの時、タッチ操作中でなければ親GameObjectの表示を`state`にする。 |
| `canUseActionPanel()` | パネルが有効かつアクティブで、タッチ操作中でない場合のみtrueを返す。 |
| `setScreenActionPanelsActiveState(bool state)` | 親GameObjectの表示状態を退避してから`screenActionPanelsActive` を更新し、必要なら親の表示も切り替える。 |
| `setScreenActionPanelsActiveStateFromEditor(bool state)` | `setScreenActionPanelsActiveState` を呼んだ後、`updateComponent` でシーンを更新するだけ。 |
| `setScreenActionPanelsEnabledState(bool state)` | `screenActionPanelsEnabled` を設定し、`updateComponent` でシーンを更新するだけ。 |
| `instantiateInputPanelPrefab()` | UI未設定なら`inputPanelPrefab` を生成し、`searchPlayerInputPanelSystem` で自身を紐付けてキャンバスを設定する。 |
| `setInputPanelUISystem(inputPanelUISystem newInputPanelUISystem)` | `mainInputPanelUISystem` と`screenActionParent` を差し替え、`updateComponent` を呼ぶ。 |
