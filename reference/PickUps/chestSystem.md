# chestSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `PickUps/chestSystem.cs:6`

**概要**: プレイヤーが近づいて開くと、設定された中身のピックアップを生成して箱の中に並べる宝箱。開閉アニメ、再補充・再開封の待ち時間、施錠と解錠、開閉イベントを管理する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Random Content | `randomContent` | `bool` | – | 個数と数量を範囲指定からランダムに決めるか。 |
| Refill Chest After Delay | `refillChestAfterDelay` | `bool` | – | 空になった後、補充して再び開けるようにするか。 |
| Time Opened After Empty | `timeOpenedAfterEmpty` | `float` | 1 | 空になってから閉じアニメを始めるまでの待ち時間（秒）。 / 表示条件: `refillChestAfterDelay` がオンのとき |
| Refilled Time | `refilledTime` | `float` | – | 閉じアニメ終了後、再度開けるようになるまでの追加待ち秒数。 / 表示条件: `refillChestAfterDelay` がオンのとき |
| Open Animation Name | `openAnimationName` | `string` | – | 開閉に使う`Animation`クリップ名。 |
| Use Electronic Device Manager | `useElectronicDeviceManager` | `bool` | – | 電子デバイスマネージャー側で開閉を制御する場合はオンにする。 |

### Pickups Trigger Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Pickup Trigger Radius | `setNewPickupTriggerRadius` | `bool` | true | 生成したピックアップの取得トリガー半径を上書きするか。 |
| New Pickup Trigger Radius | `newPickupTriggerRadius` | `float` | 3 | 上書きする取得トリガーの半径。 |
| Enable Pickups Trigger At Start | `enablePickupsTriggerAtStart` | `bool` | true | 生成したピックアップの取得トリガーを開始時から有効にするか。 |
| Main Pickup Manager Name | `mainPickupManagerName` | `string` | "Pickup Manager" | シーンに無い場合に生成するピックアップ管理マネージャー名。 |
| Set Ignore Examine Pickup Object | `setIgnoreExaminePickupObject` | `bool` | – | 生成したピックアップを調べる動作の対象外にするか。 |
| Set Pickups As Get By Trigger Type Enabled | `setPickupsAsGetByTriggerTypeEnabled` | `bool` | – | 生成したピックアップをトリガー取得方式に設定するか。 |

### Locked Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Is Locked | `isLocked` | `bool` | – | 初期状態でロックするか。オンだとColliderが無効になり開けない。 |
| Open When Unlocked | `openWhenUnlocked` | `bool` | – | ロック解除時に自動でチェストを開くか。 / 表示条件: `isLocked` がオンのとき |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Open Chest | `useEventOnOpenChest` | `bool` | – | チェストを開いた時にイベントを呼ぶか。 |
| Event On Open Chest | `eventOnOpenChest` | `UnityEvent` | – | 開いた瞬間に実行するイベント。 / 表示条件: `useEventOnOpenChest` がオンのとき |
| Use Event On Close Chest | `useEventOnCloseChest` | `bool` | – | 空になって閉じる時にイベントを呼ぶか。 |
| Event On Close Chest | `eventOnCloseChest` | `UnityEvent` | – | 閉じる瞬間に実行するイベント。 / 表示条件: `useEventOnCloseChest` がオンのとき |
| Use Event To Send Spawned Objects | `useEventToSendSpawnedObjects` | `bool` | – | 生成したオブジェクトを通知するイベントを使うか。 |
| Event To Send Spawned Objects | `eventToSendSpawnedObjects` | `eventParameters.eventToCallWithGameObject` | – | 生成したオブジェクトを引数に渡すイベント。 / 表示条件: `useEventToSendSpawnedObjects` がオンのとき |
| Event To Send Remain Time To Refill | `eventToSendRemainTimeToRefill` | `eventParameters.eventToCallWithAmount` | – | 補充までの残り時間を通知するイベント。 |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Chest Anim | `chestAnim` | `Animation` | – | 開閉アニメを再生する`Animation`参照。未指定なら自動取得。 |
| Main Collider | `mainCollider` | `Collider` | – | ロック時に無効化されるメインCollider。インタラクション表示に使う。 |
| Map Object Information Manager | `mapObjectInformationManager` | `mapObjectInformation` | – | マップアイコン登録に使う`mapObjectInformation`参照。 |
| Place Where Instantiate Pick Ups | `placeWhereInstantiatePickUps` | `Transform` | – | 生成位置と並べる向きの基準となるTransform。 / 表示条件: `settings` がオンのとき |
| Place Offset | `placeOffset` | `Vector3` | – | 基準Transformから最初の生成位置へのオフセット。 / 表示条件: `settings` がオンのとき |
| Space | `space` | `Vector3` | – | 生成物を並べる間隔。左右・上下・前後の要素で指定。 / 表示条件: `settings` がオンのとき |
| Amount | `amount` | `Vector2` | – | 生成物を並べるグリッドの行数と1行あたりの個数。 / 表示条件: `settings` がオンのとき |
| Pick Up Scale | `pickUpScale` | `float` | – | 生成したピックアップのスケール。 / 表示条件: `settings` がオンのとき |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | 生成位置のギズモを表示するか。 / 表示条件: `settings` がオンのとき |
| Gizmo Color | `gizmoColor` | `Color` | – | 生成位置に描く球ギズモの表示色。 / 表示条件: `settings.boolValue && showGizmo.boolValue` |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | シーンビューでギズモに添えるラベルの文字色。 / 表示条件: `settings.boolValue && showGizmo.boolValue` |
| Gizmo Radius | `gizmoRadius` | `float` | – | 生成位置に描く球ギズモの半径。 / 表示条件: `settings.boolValue && showGizmo.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `chestPickUpList` | `List<chestPickUpElementInfo>` | new List<chestPickUpElementInfo> () | – |
| `managerPickUpList` | `List<pickUpElementInfo>` | new List<pickUpElementInfo> () | – |
| `numberOfObjects` | `int` | – | – |
| `minAmount` | `int` | – | – |
| `maxAmount` | `int` | – | – |
| `settings` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `mainCoroutine` を停止して開封後の監視更新を止める（null なら何もしない）。 |
| `addNewObject(GameObject newObject)` | 生成物を箱の子にし、トリガー半径の変更やトリガー無効化を行って一覧に加え、設定時は生成イベントを送る。 |
| `setCurrentWaitToOpenChestValue(float newValue)` | 開封までの待ち時間を設定し、0より大きければ待機を有効にする。 |
| `getRemainTimeToReopen()` | `refilledTime` から経過時間を引いた再補充までの残り時間を返し、0未満は0に丸める。 |
| `checkEventToSendRemainTimeToRefillOnSaveState()` | セーブ時に再補充までの残り時間を `eventToSendRemainTimeToRefill` で送る。 |
| `openOrCloseChest()` | 待ち時間を確認して開封アニメを再生し、中身を生成して開封イベントを発火、再補充しない設定なら操作を無効化する。 |
| `unlockChest()` | `setLockedState(false)` を呼んで施錠を解除するだけ。 |
| `setLockedState(bool state)` | `isLocked` を反映し、マップ表示の切替と `openWhenUnlocked` 時の即開封を行う。 |
| `getManagerPickUpList()` | `pickUpManager` を検索・生成して `managerPickUpList` をコピーし、更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` で値を反映し、シーンをダーティにして宝箱の設定更新を通知する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnOpenChest` | `UnityEvent` | – |
| `eventOnCloseChest` | `UnityEvent` | – |

## 内部型

- `chestPickUpElementInfo`（class）
- `chestPickUpTypeElementInfo`（class）
