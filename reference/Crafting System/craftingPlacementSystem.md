# craftingPlacementSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/craftingPlacementSystem.cs:6`

**概要**: カメラからのレイキャストで設置位置を決め、プレビュー生成・回転・設置確定・ステーション接続を扱う。設置中はコルーチンで毎フレーム位置を更新する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Placement Enabled | `placementEnabled` | `bool` | true | – |
| Layer To Place Objects | `layerToPlaceObjects` | `LayerMask` | – | – |
| Layer To Take Objects Back | `layerToTakeObjectsBack` | `LayerMask` | – | – |
| Max Raycast Distance | `maxRaycastDistance` | `float` | – | – |
| Check For Obstacles | `checkForObstacles` | `bool` | – | – |
| Layer For Obstacles | `layerForObstacles` | `LayerMask` | – | – |
| Hit Point Offset | `hitPointOffset` | `float` | – | – |
| Disable Placement Mode On Object Placed | `disablePlacementModeOnObjectPlaced` | `bool` | – | – |
| Placement Active Paused | `placementActivePaused` | `bool` | – | – |
| Use Max Surface Angle To Place Objects | `useMaxSurfaceAngleToPlaceObjects` | `bool` | – | – |
| Max Surface Angle To Place Objects | `maxSurfaceAngleToPlaceObjects` | `float` | – | – |

### Input To Pause On Placement Active Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Custom Input To Pause On Action Info List | `customInputToPauseOnActionInfoList` | `List<playerActionSystem.inputToPauseOnActionIfo>` | new List<playerActionSystem.inputToPa… | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Placement Active | `placementActive` | `bool` | – | – |
| Current Object To Place Mesh | `currentObjectToPlaceMesh` | `GameObject` | – | – |
| Current Object Righ Rotation | `currentObjectRighRotation` | `float` | – | – |
| Current Object Forward Rotation | `currentObjectForwardRotation` | `float` | – | – |
| Object Taken Back | `objectTakenBack` | `bool` | – | – |
| Last Object Taken Back Name | `lastObjectTakenBackName` | `string` | – | – |
| Placing Object Previously Taken | `placingObjectPreviouslyTaken` | `bool` | – | – |
| Current Layer Mask To Place Object | `currentLayerMaskToPlaceObject` | `LayerMask` | – | – |
| Current Object Assigned | `currentObjectAssigned` | `bool` | – | – |
| Ignore Disable Placement Active On Cancel Input Action Active | `ignoreDisablePlacementActiveOnCancelInputActionActive` | `bool` | – | – |
| Toggle Placement Active On Cancel Input Action Active | `togglePlacementActiveOnCancelInputActionActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Enable Placement | `eventOnEnablePlacement` | `UnityEvent` | – | – |
| Event On Disable Placement | `eventOnDisablePlacement` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Crafting System | `mainCraftingSystem` | `craftingSystem` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Player Collider | `mainPlayerCollider` | `Collider` | – | – |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`を`StopCoroutine`で止めるだけ。 |
| `confirmToPlaceObject()` | 選択中オブジェクトを1個消費してプレビュー位置に生成し、設置イベント通知と表面への親子付けを行い、プレビューを破棄する。 |
| `setCurrentObjectToPlaceMesh(GameObject newObject)` | `newObject`を複製して配置プレビューに設定し、位置オフセット・配置レイヤー・回転可否・境界を取得する。 |
| `setOriginalPlacementActivePausedState()` | `Start`で保存した元の`placementActivePaused`状態を復元するだけ。 |
| `setPlacementActivePausedState(bool state)` | 同じ値なら何もせず、解除時は配置中なら配置モードを終了してから`placementActivePaused`を更新する。 |
| `isPlacementActivePaused()` | `placementActivePaused`を返すだけ。 |
| `setPlacementActiveState(bool state)` | 配置モードの開始/終了に伴い、イベント・入力一時停止・全ソケットのライン表示・接続選択状態をまとめて更新する。 |
| `checkInputListToPauseDuringAction(bool state)` | 登録入力リストをtrueで状態保存して無効化し、falseで有効だった入力だけ復帰させる。 |
| `inputRotateObjectToRightOrLeft(bool state)` | 配置中のみ`currentObjectRighRotation`を±90度して270度で折り返し、プレビューをY軸回転する。 |
| `inputRotateObjectToUpOrDown(bool state)` | 配置中のみ`currentObjectForwardRotation`を±90度して270度で折り返し、プレビューをX軸回転する。 |
| `inputConfirmToPlaceObject()` | 取り戻し待ちなら前回のオブジェクトをプレビューに再設定し、そうでなければ`confirmToPlaceObject`を実行する。 |
| `inputConfirmToTakeObjectBackToInventory()` | 注視先の設置オブジェクトを検出し、回収可否を確認してインベントリへ戻し、最後に戻した名前を記録する。 |
| `setIgnoreDisablePlacementActiveOnCancelInputActionActiveState(bool state)` | `ignoreDisablePlacementActiveOnCancelInputActionActive`を設定するだけ。 |
| `setTogglePlacementActiveOnCancelInputActionActiveState(bool state)` | `togglePlacementActiveOnCancelInputActionActive`を設定するだけ。 |
| `inputCancelPlaceObject()` | プレビューがあれば破棄して戻り、なければ無視/トグル設定に従い`mainCraftingSystem`の配置モードを終了する。 |
| `inputConfirmToAttachObjectToSurfaceDetected()` | 取り戻し中でなければ表面取付フラグを一時的に立てて`inputConfirmToPlaceObject`を呼ぶ。 |
| `inputCheckConnectStationInput()` | レイキャストで2つのステーションを選び、接続可否を判定してソケット割当・相互リスト登録・状態チェックを行う。 |
| `inputCheckRemoveStationInput()` | 接続操作中ならライン非表示と選択解除のみ、そうでなければ注視先ステーションの接続を解除する。 |
| `inputSelectNextObjectForPlacement()` | 有効かつ配置中なら`selectNextOrPreviousObjectForPlacement(true)`を呼ぶだけ。 |
| `inputSelectPreviousObjectForPlacement()` | 有効かつ配置中なら`selectNextOrPreviousObjectForPlacement(false)`を呼ぶだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnEnablePlacement` | `UnityEvent` | – |
| `eventOnDisablePlacement` | `UnityEvent` | – |
