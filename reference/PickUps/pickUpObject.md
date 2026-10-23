# pickUpObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `PickUps/pickUpObject.cs:7`

**概要**: シーン上の拾得物1個を表し、トリガー接触またはボタンで拾得者を判定して`pickupType`経由で取得を実行する。インベントリ追加、HUDアイコン/メッセージ、取得イベント、耐久値、オブジェクト破棄を扱う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Amount | `amount` | `int` | – | 入手できる個数でインベントリへ加算される。 |
| Use Amount Per Unit | `useAmountPerUnit` | `bool` | – | ONにすると1個あたりの量を掛けて加算する。 |
| Amount Per Unit | `amountPerUnit` | `int` | – | 1個あたりに加算するアイテム量。 / 表示条件: `useAmountPerUnit` がオンのとき |
| Pick Up Sound | `pickUpSound` | `AudioClip` | – | 取得したときに再生する効果音クリップ。 |
| Pick Up Sound Audio Element | `pickUpSoundAudioElement` | `AudioElement` | – | 取得音を再生するためのオーディオ要素。 |
| Static Pick Up | `staticPickUp` | `bool` | – | ONにすると物理を止めて近づかないと取れなくなる。 |
| Move To Player On Trigger | `moveToPlayerOnTrigger` | `bool` | true | ONにすると取得時にプレイヤーへ吸い寄せる。 |
| Pick Up Option | `pickUpOption` | `pickUpMode` | – | トリガー接触かボタン操作かで取得方法を選ぶ。 |
| Main Pickup Type | `mainPickupType` | `pickupType` | – | 取得処理を実行する`pickupType`の参照。 |
| Main Pickup Manager Name | `mainPickupManagerName` | `string` | "Pickup Manager" | アイコン登録に使うピックアップマネージャ名。 |

### Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Durability | `useDurability` | `bool` | – | ONにすると耐久値をアイテムへ引き継ぐ。 |
| Max Durability Amount | `maxDurabilityAmount` | `float` | – | アイテムの耐久値の上限を指定する。 / 表示条件: `useDurability` がオンのとき |
| Durability Amount | `durabilityAmount` | `float` | – | 取得時に設定する現在の耐久値。 / 表示条件: `useDurability` がオンのとき |

### Examine Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Be Examined | `canBeExamined` | `bool` | – | ONにすると取得前にオブジェクトを調べられる。 |
| Ignore Examine Object Before Store Enabled | `ignoreExamineObjectBeforeStoreEnabled` | `bool` | – | ONにすると格納前の調べ表示を省略する。 |

### Icon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Pickup Info On Taken | `showPickupInfoOnTaken` | `bool` | true | ONにすると取得時にHUDへ情報を表示する。 |
| Use Pickup Icon On Screen | `usePickupIconOnScreen` | `bool` | true | ONにすると画面上にピックアップアイコンを出す。 |
| Pickup Icon General Name | `pickupIconGeneralName` | `string` | – | ピックアップの種類を決める一般名。 / 表示条件: `usePickupIconOnScreen` がオンのとき |
| Pickup Icon Name | `pickupIconName` | `string` | – | 個別アイコンを選ぶための名前。 / 表示条件: `usePickupIconOnScreen` がオンのとき |
| Use Pickup Icon On Taken | `usePickupIconOnTaken` | `bool` | – | ONにすると取得メッセージにアイコンを付ける。 |
| Pickup Icon | `pickupIcon` | `Texture` | – | 取得メッセージに表示するアイコン画像。 / 表示条件: `usePickupIconOnTaken` がオンのとき |

### Pick Up Used By

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Usable By Anything | `usableByAnything` | `bool` | – | ONにすると誰でもこのピックアップを取得できる。 |
| Usable By Player | `usableByPlayer` | `bool` | true | ONならプレイヤーがこのピックアップを取得できる。 / 表示条件: `usableByAnything` がオフのとき |
| Usable By Vehicles | `usableByVehicles` | `bool` | true | ONなら乗り物がこのピックアップを取得できる。 / 表示条件: `usableByAnything` がオフのとき |
| Usable By Characters | `usableByCharacters` | `bool` | – | ONならAIキャラクターが取得できる。 / 表示条件: `usableByAnything` がオフのとき |
| Player Tag | `playerTag` | `string` | "Player" | プレイヤーとして判定するタグ。 |
| Friend Tag | `friendTag` | `string` | "friend" | 味方キャラクターとして判定するタグ。 |
| Enemy Tag | `enemyTag` | `string` | "enemy" | 敵キャラクターとして判定するタグ。 |

### Pick Up Taken Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Taken | `useEventOnTaken` | `bool` | – | ONにすると取得時にイベントを実行する。 |
| Event On Taken | `eventOnTaken` | `UnityEvent` | – | ピックアップ取得時に実行するイベント。 / 表示条件: `useEventOnTaken` がオンのとき |
| Use Event On Remaining Amount | `useEventOnRemainingAmount` | `bool` | – | ONにすると取得しきれなかった場合のイベントを有効にする。 / 表示条件: `useEventOnTaken` がオンのとき |
| Event On Remaining Amount | `eventOnRemainingAmount` | `UnityEvent` | – | 取得しきれず残量が残ったときに実行するイベント。 / 表示条件: `useEventOnTaken.boolValue && useEventOnRemainingAmount.boolValue` |
| Send Pickup Finder | `sendPickupFinder` | `bool` | – | ONにすると取得したオブジェクトをイベントで渡す。 |
| Send Pickup Finder Event | `sendPickupFinderEvent` | `eventParameters.eventToCallWithGameObject` | – | 取得者を受け取るためのイベント。 / 表示条件: `sendPickupFinder` がオンのとき |
| Use Remote Event | `useRemoteEvent` | `bool` | – | ONにすると取得者のリモートイベントを呼ぶ。 |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | ONにすると取得処理のログを出力する。 |

### Object Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Inventory Object Manager | `inventoryObjectManager` | `inventoryObject` | – | インベントリ情報を持つ`inventoryObject`。 |
| Device String Action Manager | `deviceStringActionManager` | `deviceStringAction` | – | 調べ表示に使う`deviceStringAction`。 |
| Main Sphere Collider | `mainSphereCollider` | `SphereCollider` | – | 取得判定に使うトリガー用のコライダー。 |
| Main Collider | `mainCollider` | `Collider` | – | 接触を判定するメインのコライダー。 |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | 取得時にキネマティックへ切り替えるRigidbody。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `takeWithTrigger` | `bool` | true | – |
| `remoteEventList` | `List<string>` | new List<string> () | – |
| `player` | `GameObject` | – | – |
| `vehicle` | `GameObject` | – | – |
| `npc` | `GameObject` | – | – |
| `finder` | `GameObject` | – | – |
| `finderIsPlayer` | `bool` | – | – |
| `finderIsVehicle` | `bool` | – | – |
| `finderIsCharacter` | `bool` | – | – |
| `amountTaken` | `int` | – | – |
| `weaponsManager` | `playerWeaponsManager` | – | – |
| `vehicleHUD` | `vehicleHUDManager` | – | – |
| `playerInventoryManager` | `inventoryManager` | – | – |
| `mainPickupTypeLocated` | `bool` | – | – |
| `inventoryAmountPicked` | `int` | – | – |
| `examiningObject` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activatePickupMovement()` | コルーチンを開始し、`finder`の上方1.5へ毎フレーム移動させ、距離1未満で`pickObject()`を呼ぶ。 |
| `getComponents()` | `amount`が0なら1にし、コンポーネントとアイコンを初期化、`staticPickUp`ならRigidbodyをキネマティック化して半径を1にする。 |
| `playPickupSound()` | `finder`から取得したAudioSourceを設定し、`pickUpSoundAudioElement`を`PlayOneShot`で再生する。 |
| `pickObject()` | 掴まれていれば落とし、`mainPickupType.confirmTakePickup()`で取得処理を行ってから取得時イベントを実行する。 |
| `removePickupFromLevel()` | アイコン登録と調べ中カメラを解除してから、この`gameObject`を`Destroy`する。 |
| `checkEventOnTaken()` | 有効なら取得時イベントと`finder`付きイベントを実行し、`remoteEventList`をリモートイベントへ送る。 |
| `checkEventOnRemainingAmount()` | プレイヤーなら`setInteractionButtonName()`で表示を更新し、`useEventOnRemainingAmount`なら残量イベントを実行する。 |
| `getAmountPicked()` | `useAmountPerUnit`なら`amount`×`amountPerUnit`、そうでなければ`amount`を返す。 |
| `setUpIcon()` | `usePickupIconOnScreen`が有効なら`pickUpManager`を取得/生成し、HUDアイコンを登録して`pickupIconRemoved`をfalseにする。 |
| `pausePickupIconState()` | `pickUpManager`へ自身のアイコンを一時停止状態(true)として通知する。 |
| `resumePickupIconState()` | `pickUpManager`へ自身のアイコンを再開状態(false)として通知する。 |
| `removePickupIcon()` | マネージャー登録と調べ中カメラを解除し、`pickupIconRemoved`をtrueにするだけ。 |
| `removePickupIconAndDisableObject()` | アイコン登録を解除したうえで、アクティブなら`gameObject`を非アクティブにする。 |
| `setCurrentUser(GameObject newObject)` | デバッグ表示の後、`newObject`のColliderで`checkTriggerInfo`を呼び、使用者判定を行う。 |
| `pickObjectByButton()` | 調べ可能で未調べならアイコンを止めて`examiningObject`を立てて戻り、それ以外は取得可否を確認して`takePickupByButton()`を呼ぶ。 |
| `confirmTakePickupByButton()` | 掴まれていれば落としてから`pickObject()`を呼ぶ。 |
| `cancelPickObject()` | 調べ中ならアイコンを再開して`examiningObject`をfalseにし、`electronicDevice`があれば`activateDevice()`を呼ぶ。 |
| `checkTriggerInfoByGameObject(GameObject objectToCheck)` | `objectToCheck`のColliderを取得し、あれば`checkTriggerInfo`を呼ぶ。 |
| `checkTriggerInfo(Collider col)` | 接触相手をプレイヤー・運転中車両・AIの順に判定し、`finder`と`setFinderType`を設定してトリガー取得を実行する。 |
| `confirmTakePickupByTrigger()` | 種別ごとに衝突を無視してRigidbodyをキネマティックにし、移動設定なら移動コルーチン、でなければ`pickObject()`を呼ぶ。 |
| `setFinderType(bool isPlayer, bool isVehicle, bool isCharacter)` | `finderIsPlayer`・`finderIsVehicle`・`finderIsCharacter`の3フラグを設定するだけ。 |
| `tryToPickUpObject()` | 運転中や満杯ならfalseを返し、インベントリに追加できた数だけ`inventoryObjectInfo.amount`と`amount`を減らしてtrueを返す。 |
| `setIgnoreMessagesAndDestroyPickupActiveState(bool state)` | 満杯メッセージを出さずに破棄するかのフラグを設定するだけ。 |
| `setDurabilityInfo(bool state, float newDurabilityAmount, float newMaxDurabilityAmount)` | `useDurability`と現在耐久値・最大耐久値をまとめて設定するだけ。 |
| `setDurabilityAmount(float newDurabilityAmount)` | `durabilityAmount`を設定するだけ。 |
| `setMaxDurabilityAmount(float newMaxDurabilityAmount)` | `maxDurabilityAmount`を設定するだけ。 |
| `setUseDurabilityState(bool state)` | `useDurability`を設定するだけ。 |
| `getLastinventoryAmountPicked()` | 直前にインベントリへ入った数`inventoryAmountPicked`を返すだけ。 |
| `getPickupObjectName()` | `getInventoryInfo()`を呼んだ後、`inventoryObjectInfo.Name`を返し、無ければ空文字を返す。 |
| `activateObjectTrigger()` | `mainSphereCollider`が無効なら有効にして、再び取得できる状態にする。 |
| `showRecieveInfo(string message)` | 表示設定時のみ、プレイヤー/車両のHUDへ`message`と、アイコン使用時は`pickupIcon`を渡す。 |
| `setPickUpAmount(int amountToSet)` | `amount`を設定したうえで`getInventoryInfo()`を呼ぶ。 |
| `getInventoryInfo()` | `inventoryObject`を取得し、初回のみ`setAmount(amount)`で個数を反映する。 |
| `setAmount(int newAmount)` | `storeTotalAmountPerUnit`時は単位数を掛け、`inventoryObjectInfo`の`amount`と`amountPerUnit`を更新する。 |
| `setNewAmount(int newAmount)` | `amount`を設定し、`inventoryObjectManager`があれば`setAmount`、無ければ`getInventoryInfo`を呼ぶ。 |
| `getPickupTrigger()` | `mainSphereCollider`を返すだけ。 |
| `removeDeviceFromListExternalCall(GameObject deviceGameObject)` | `playerFoundList`の各プレイヤーの`usingDevicesSystem`から`deviceGameObject`を一覧解除させる。 |
| `setPickupOptionAsTrigger()` | `pickUpOption`を`trigger`にするだけ。 |
| `setPickupOptionAsButton()` | `pickUpOption`を`button`にするだけ。 |
| `pickObjectAfterXWait(GameObject newPlayer)` | 0.1秒待つコルーチンを開始し、`simpleActionButton`があればそのオブジェクトを、無ければ自身を`newPlayer`に外部使用させる。 |
| `assignPickupElementsOnEditor()` | エディタ用に`objectOnInventory`と`inventoryObject`を結び、`pickupType`を設定してシーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`でこのコンポーネントとシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTaken` | `UnityEvent` | – |
| `eventOnRemainingAmount` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnTriggerEnter(Collider col)`, `OnTriggerExit(Collider col)`

</details>

## 内部型

- `pickUpType`（enum）
- `pickUpMode`（enum）
