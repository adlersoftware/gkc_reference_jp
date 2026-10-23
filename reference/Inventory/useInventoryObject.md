# useInventoryObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/useInventoryObject.cs:7`

**概要**: インベントリの必要オブジェクトを使って装置や鍵を解錠するコンポーネント。使用型（メニュー/ボタン/自動/サイド）ごとの選択処理と、解錠イベント・効果音・遅延イベントを管理する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Be Re Used | `canBeReUsed` | `bool` | – | ONにすると使用後も必要数がリセットされ再使用できる。 |
| Use Inventory Type | `useInventoryType` | `useInventoryObjectType` | – | 使用方式を`menu`や`button`などから選ぶ。 |
| Use Objects One By One Using Button | `useObjectsOneByOneUsingButton` | `bool` | true | ONにするとbutton方式で1個ずつ手動で使用する。 / 表示条件: `useInventoryType.enumValueIndex == 1` |
| Inventory Object Action | `inventoryObjectAction` | `string` | – | 検出時に`deviceStringAction`へ表示する操作名。 |
| Disable Object Action After Use | `disableObjectActionAfterUse` | `bool` | – | ONにすると解決後にアイコンとコライダーを無効化する。 |
| Tag To Configure | `tagToConfigure` | `string` | "device" | button方式のときこのオブジェクトに設定するタグ。 |
| Player Tag | `playerTag` | `string` | "Player" | プレイヤーとして判定するタグ。 |
| Vehicle Tag | `vehicleTag` | `string` | "vehicle" | 運転中のドライバーを判定する車両のタグ。 |
| Check Player Inventory While Driving | `checkPlayerInventoryWhileDriving` | `bool` | – | ONにすると運転中のドライバーの所持品も確認する。 |
| Can Use And Use Inventory Pickups On Trigger Enabled | `canUseAndUseInventoryPickupsOnTriggerEnabled` | `bool` | true | ONにすると触れたピックアップを自動で使う。 |
| Remove Inventory Pickup Object On Trigger | `removeInventoryPickupObjectOnTrigger` | `bool` | true | ONにすると使用したピックアップを破壊する。 |

### Message Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Used Message | `objectUsedMessage` | `string` | – | 使用完了時に表示するメッセージ。 / TextArea (3, 10) |
| Use Custom Object Not Found Message | `useCustomObjectNotFoundMessage` | `bool` | – | ONにすると必要オブジェクト不在時の文言を差し替える。 |
| Object Not Found Message | `objectNotFoundMessage` | `string` | – | 必要オブジェクトが見つからないときの表示文言。 / 表示条件: `useCustomObjectNotFoundMessage` がオンのとき / TextArea (3, 10) |

### Object Activated Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enable Object When Activate | `enableObjectWhenActivate` | `bool` | – | ONにすると解決時に指定オブジェクトを有効化する。 |
| Object To Enable | `objectToEnable` | `GameObject` | – | 解決時に有効化するオブジェクト。 / 表示条件: `enableObjectWhenActivate` がオンのとき |
| Use Animation | `useAnimation` | `bool` | – | ONにすると解決時にアニメーションを再生する。 |
| Object With Animation | `objectWithAnimation` | `GameObject` | – | アニメーションを再生するオブジェクト。 / 表示条件: `useAnimation` がオンのとき |
| Animation Name | `animationName` | `string` | – | 再生するアニメーションの名前。 / 表示条件: `useAnimation` がオンのとき |

### Player Inventory Menu Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Open Player Inventory Menu | `openPlayerInventoryMenu` | `bool` | – | ONにすると使用時にプレイヤーの所持品画面を開閉する。 |
| Set New Inventory Panel | `setNewInventoryPanel` | `bool` | – | ONにすると開閉時に所持品パネルを切り替える。 / 表示条件: `openPlayerInventoryMenu` がオンのとき |
| Default Inventory Panel Name | `defaultInventoryPanelName` | `string` | "Default" | 閉じたときに戻す既定の所持品パネル名。 / 表示条件: `openPlayerInventoryMenu` がオンのとき |
| New Inventory Panel Name | `newInventoryPanelName` | `string` | "Inventory On Side" | 開いたときに切り替える所持品パネル名。 / 表示条件: `openPlayerInventoryMenu` がオンのとき |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Info | `showDebugInfo` | `bool` | – | ONにすると処理内容をConsoleに出力する。 |

### Object Solved Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Unlock Function Call | `unlockFunctionCall` | `UnityEvent` | new UnityEvent () | 解決時に呼び出すUnityEvent。 |
| Use Event On Unlock With Delay | `useEventOnUnlockWithDelay` | `bool` | – | ONにすると解決後に遅延イベントを実行する。 |
| Delay To Activate Event | `delayToActivateEvent` | `float` | – | 遅延イベントを実行するまでの待ち時間（秒）。 / 表示条件: `useEventOnUnlockWithDelay` がオンのとき |
| Event On Unlock With Delay | `eventOnUnlockWithDelay` | `UnityEvent` | – | 指定時間後に実行するUnityEvent。 / 表示条件: `useEventOnUnlockWithDelay` がオンのとき |
| Use Unlock Event From Loading Game | `useUnlockEventFromLoadingGame` | `bool` | – | ONにするとロード復元時にもイベントを実行する。 |
| Unlock Event From Loading Game | `unlockEventFromLoadingGame` | `UnityEvent` | – | ロードで解決済みを復元するとき実行するイベント。 / 表示条件: `useUnlockEventFromLoadingGame` がオンのとき |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Device String Action Manager | `deviceStringActionManager` | `deviceStringAction` | – | 操作名やアイコンを表示する`deviceStringAction`。 |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | 使用音を再生する`AudioSource`。 |
| Main Collider | `mainCollider` | `Collider` | – | トリガー判定に使うコライダー。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `inventoryObjectNeededList` | `List<inventoryObjectNeededInfo>` | new List<inventoryObjectNeededInfo> () | – |
| `objectUsed` | `bool` | – | – |
| `numberOfObjectsUsed` | `int` | – | – |
| `numberOfObjectsNeeded` | `int` | – | – |
| `currentNumberOfObjectsNeeded` | `int` | – | – |
| `playerInventoryMenuOpened` | `bool` | – | – |
| `counter` | `int` | 0 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCanBeUsedState(bool state)` | `canBeUsed`を`state`に設定するだけ。 |
| `getInventoryObjectCanBeUsed()` | `canBeUsed`の現在値を返すだけ。 |
| `activateDevice()` | `button`型かつ未使用時のみ`playerInventoryManager.useCurrentObject()`を呼ぶ。 |
| `useObjectAmountExternallyByName(string inventoryObjectName, int amountUsed)` | 名前指定の照合を強制し、数量1として`useObject`を呼ぶ。 |
| `useSingleObjectExternallyByName(string inventoryObjectName)` | `useObjectAmountExternallyByName`を数量1で呼ぶだけ。 |
| `useObject(int amountUsed, string inventoryObjectName, GameObject inventoryInfoGameObject)` | 必要オブジェクトの使用量を加算し、規定数到達で配置・イベント・効果音を実行して解錠処理へ進む。 |
| `solveThisInventoryObject()` | `solveObject(false)`を呼び、通常の`unlockFunctionCall`で解錠処理を行う。 |
| `solveThisInventoryObjectFromLoadingGame()` | `useUnlockEventFromLoadingGame`の値を渡して`solveObject`を呼ぶ。 |
| `activateEventOnUnlockWithDelay()` | 既存コルーチンを止め、`delayToActivateEvent`秒後にイベントを発火するコルーチンを開始する。 |
| `updateUseInventoryObjectState()` | 再利用可否と使用型に応じ、在庫選択・情報設定・案内解除を呼び分ける。 |
| `setToNullCurrentInventoryObject()` | 使用型が`inventoryOnSide`でなければtrueを返すだけ。 |
| `selectObjectOnInventory()` | 検出済みピックアップか通常選択かを判定し、使用型別の処理へ振り分ける。 |
| `setUseInventoryType(useInventoryObjectType newUseInventoryObjectType)` | `useInventoryType`を新しい値に設定するだけ。 |
| `setOriginalUseInventoryType()` | Startで保存した`originalUseInventoryType`へ戻すだけ。 |
| `useObjectByButton()` | `playerInventoryManager`に使用対象とこのオブジェクトを設定する。 |
| `useObjectByMenu()` | `playerInventoryManager.setCurrentUseInventoryGameObject`で自分を登録するだけ。 |
| `useObjectAutomatically()` | ピックアップ検出時はその情報を、通常時は対象を在庫に設定し`searchForObjectNeed`を呼ぶ。 |
| `setInfoCurrentInventoryObjectToUse()` | 未使用の必要オブジェクトを探し、対象と残り必要数、デバイス表示を更新する。 |
| `getObjectUsedMessage()` | `currentObjectUsedMessage`を返すだけ。 |
| `getCustomObjectNotFoundMessage()` | `objectNotFoundMessage`を返すだけ。 |
| `isCustomObjectNotFoundMessageActive()` | `useCustomObjectNotFoundMessage`を返すだけ。 |
| `isInventoryPlaceUsed()` | `objectUsed`を返すだけ。 |
| `inventoryObjectNeededListContainsObject(GameObject objectToCheck, string inventoryObjectName)` | 未使用の必要リストを名前優先で照合し、一致すれば対象を更新してtrueを返す。 |
| `getInventoryObjectNeededAmount(GameObject objectToCheck, string inventoryObjectName)` | 再使用可能なら1、それ以外は該当オブジェクトの残り必要数を返し、無ければ-1。 |
| `setCharacterDirectly(GameObject newObject)` | 渡したオブジェクトの`Collider`でトリガー入場処理を直接実行する。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | プレイヤー/車両/ピックアップを判定し、入場時に使用対象を選択、退場時に案内を解除する。 |
| `checkIfInventoryPickupIsUsed(inventoryObject inventoryObjectToCheck)` | ピックアップの在庫オブジェクトが必要リストに一致するか調べ、あれば表示名と必要数を更新してtrueを返す。 |
| `removePlayerInventoryInfo()` | `playerInventoryManager`の使用対象登録と選択中オブジェクトを解除する。 |
| `playObjectUsedSound(int index)` | 必要リストの`index`番の効果音を`AudioPlayer.PlayOneShot`で鳴らす。 |
| `setCurrentPlayer(GameObject player)` | `currentPlayer`を設定し、`inventoryManager`と`usingDevicesSystem`を取得して保持する。 |
| `removeCurrentPlayer()` | `currentPlayer`と`playerInventoryManager`をnullにするだけ。 |
| `removeDeviceFromList()` | `usingDevicesSystem`のデバイス一覧からこのオブジェクトを削除する。 |
| `getCurrentAmountUsed()` | 直近に使用した数量`currentAmountUsed`を返すだけ。 |
| `enableOrDisableTrigger(bool state)` | `Collider`と`canBeUsed`を切り替え、無効化時はデバイス一覧からも外す。 |
| `openOrClosePlayerInventoryMenu()` | `openPlayerInventoryMenu`有効時、在庫メニューの開閉を反転しパネル名も切り替える。 |
| `disableInventoryMenu()` | `playerInventoryManager.enableOrDisableInventoryMenu(false)`を呼ぶだけ。 |
| `addInventoryObjectNeededInfo()` | エディタ用に`inventoryObjectNeededList`へ新規要素を追加し、`updateComponent`を呼ぶ。 |
| `addSubInventoryObjectNeededList(int index)` | 指定要素の`inventoryObjectNeededList`へ空のサブ要素を追加して更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーン更新でエディタ表示を更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `unlockFunctionCall` | `UnityEvent` | – |
| `unlockEventFromLoadingGame` | `UnityEvent` | – |
| `eventOnUnlockWithDelay` | `UnityEvent` | – |

## 内部型

- `useInventoryObjectType`（enum）
- `inventoryObjectNeededInfo`（class）
- `inventoryElementNeededInfo`（class）
