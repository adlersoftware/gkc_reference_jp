# usingDevicesSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/usingDevicesSystem.cs:11`

**概要**: プレイヤー周囲のデバイス（乗り物・拾得物・スイッチなど）をトリガーやレイキャストで検出し、一覧管理・最寄り選択・`activateDevice` 送信・アイコンやキー表示などのUI更新を行う。

**公式ドキュメント抜粋**（[Using Devices System](../../docs/player-controller-components/player-controller/using-devices-system.md)）

> Used to manage interaction with devices and objects on the game, detecting and storing all of them and setting the current that to use according to the settings, like closer to the player, closer to the center of the screen, the one that is visible on screen, etc...like vehicles, computers, buttons, pickups, chests, etc….

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Devices | `canUseDevices` | `bool` | – | ONにするとデバイス使用の入力を受け付ける。 |
| Use Device Function Name | `useDeviceFunctionName` | `string` | "activateDevice" | 使用時にデバイスへ送る関数名。 |
| Set Current User On Device Function Name | `setCurrentUserOnDeviceFunctionName` | `string` | "setCurrentUser" | 使用者を通知するため送る関数名。 |
| Use Devices Action Name | `useDevicesActionName` | `string` | "Activate Device" | キー表示に使う入力アクション名。 |
| Use Pick Up Amount If Equal To One | `usePickUpAmountIfEqualToOne` | `bool` | – | ONにすると個数1でも所持数を表示する。 |
| Use Only Device If Visible On Camera | `useOnlyDeviceIfVisibleOnCamera` | `bool` | – | ONにするとカメラに映るデバイスだけを対象にする。 |
| Use Device Button Enabled | `useDeviceButtonEnabled` | `bool` | true | ONの間だけデバイス使用ボタンが効く。 |
| Hold Interaction Button Enabled | `holdInteractionButtonEnabled` | `bool` | – | ONにするとデバイス側の長押し設定を使う。 |
| Check If Devices Game Object Detected Not Active | `checkIfDevicesGameObjectDetectedNotActive` | `bool` | – | ONにすると非アクティブなデバイスをリストから除く。 |
| Check If Player Collider Inside Bound Of Device On Exit | `checkIfPlayerColliderInsideBoundOfDeviceOnExit` | `bool` | – | ONにすると退出時も重なり中は解除しない。 |

### Raycast Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | デバイス検出レイキャストのレイヤーマスク。 |
| Raycast Distance | `raycastDistance` | `float` | – | 検出と障害物判定のレイキャスト距離。 |
| Ignore Check If Obstacle Between Device And Player | `ignoreCheckIfObstacleBetweenDeviceAndPlayer` | `bool` | true | ONにするとデバイスとの障害物判定を行わない。 |

### Ignore GameObject List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Game Object List To Ignore | `useGameObjectListToIgnore` | `bool` | – | ONにすると指定オブジェクトを検出対象外にする。 |

### Hold Button To Pick Around Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hold Button To Take Pickups Around | `holdButtonToTakePickupsAround` | `bool` | – | ONにすると長押しで周囲のピックアップをまとめて取る。 / 表示条件: `showAllSettings.boolValue \|\| showIntereactionSettings.boolValue` |
| Hold Button Time | `holdButtonTime` | `float` | 0.5f | まとめ取り判定に必要な長押し時間（秒）。 / 表示条件: `showAllSettings.boolValue \|\| showIntereactionSettings.boolValue && holdButtonToTakePickupsAround.boolValue` |

### Max Distance Interaction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remove Device From Player List On Max Distance | `removeDeviceFromPlayerListOnMaxDistance` | `bool` | – | ONにすると距離超過でリストから外す。 / 表示条件: `showAllSettings.boolValue \|\| showIntereactionSettings.boolValue` |
| Max Distance To Remove Device From Player List | `maxDistanceToRemoveDeviceFromPlayerList` | `float` | – | リストから外す距離のしきい値。 / 表示条件: `showAllSettings.boolValue \|\| showIntereactionSettings.boolValue && removeDeviceFromPlayerListOnMaxDistance.boolValue` |

### Device Icon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Use Device Icon Enabled | `showUseDeviceIconEnabled` | `bool` | true | ONにすると使用アイコンを表示する。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Use Fixed Device Icon Position | `useFixedDeviceIconPosition` | `bool` | – | ONにするとアイコンを固定位置に表示する。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue && showUseDeviceIconEnabled.boolValue` |
| Device On Screen If Use Fixed Icon Position | `deviceOnScreenIfUseFixedIconPosition` | `bool` | – | ONにすると固定位置を使わず対象の画面位置に出す。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue && showUseDeviceIconEnabled.boolValue` |
| Use Fixed Device Icon Position On FBA | `useFixedDeviceIconPositionOnFBA` | `bool` | – | ONにするとFBA中も固定位置表示にする。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue && showUseDeviceIconEnabled.boolValue` |
| Follow Device Icon Position On FBA If Object On Screen | `followDeviceIconPositionOnFBAIfObjectOnScreen` | `bool` | – | ONにするとFBA中も対象が画面外なら固定位置に残す。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue && showUseDeviceIconEnabled.boolValue` |
| Get Closest Device To Camera Center | `getClosestDeviceToCameraCenter` | `bool` | – | ONにすると画面中心に近いデバイスを選ぶ。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Use Max Distance To Camera Center | `useMaxDistanceToCameraCenter` | `bool` | – | ONにすると画面中心からの距離で絞り込む。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue && getClosestDeviceToCameraCenter.boolValue` |
| Max Distance To Camera Center | `maxDistanceToCameraCenter` | `float` | 20 | 画面中心からこの距離以内のデバイスを対象にする。 / 表示条件: `getClosestDeviceToCameraCenter.boolValue && useMaxDistanceToCameraCenter.boolValue` |
| Default Device Name Font Size | `defaultDeviceNameFontSize` | `int` | 17 | デバイス名の既定フォントサイズ。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Extra Text Start Action Key | `extraTextStartActionKey` | `string` | "[" | キー表示の前に付ける文字列（既定は`[`）。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Extra Text End Action Key | `extraTextEndActionKey` | `string` | "]" | キー表示の後に付ける文字列（既定は`]`）。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Show Current Device Amount | `showCurrentDeviceAmount` | `bool` | true | ONにするとピックアップの所持数を表示する。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Current Device Amount Text Panel | `currentDeviceAmountTextPanel` | `GameObject` | – | 所持数を表示するテキストのパネル。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Current Device Amount Text | `currentDeviceAmountText` | `Text` | – | 所持数の数値を書き込むテキスト。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Show Detected Devices Icon On Screen | `showDetectedDevicesIconOnScreen` | `bool` | – | ONにすると検出した全デバイスにアイコンを出す。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Detected Devices Icon Prefab | `detectedDevicesIconPrefab` | `GameObject` | – | 画面上のデバイスアイコンに使うプレハブ。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Detected Devices Icon Parent | `detectedDevicesIconParent` | `Transform` | – | 生成したデバイスアイコンの親Transform。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Use Min Distance To Use Devices | `useMinDistanceToUseDevices` | `bool` | – | ONにすると距離の上限で使用対象を制限する。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Min Distance To Use Devices | `minDistanceToUseDevices` | `float` | 4 | これを超えると使用対象から外れる距離。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue && useMinDistanceToUseDevices.boolValue` |
| Disable Interaction Touch Button If Not Devices Detected | `disableInteractionTouchButtonIfNotDevicesDetected` | `bool` | – | ONにすると未検出時にタッチボタンを消す。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Keep Interaction Touch Button Always Active | `keepInteractionTouchButtonAlwaysActive` | `bool` | – | ONにするとタッチボタンを常に表示しておく。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Show Interaction Panel If Object Not On Screen | `showInteractionPanelIfObjectNotOnScreen` | `bool` | – | ONにすると対象が画面外でもパネルを表示する。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |

### Icon Button List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Icon Button Info List | `useIconButtonInfoList` | `bool` | – | ONにするとデバイスごとにアイコン情報を切り替える。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue` |
| Default Icon Button Name | `defaultIconButtonName` | `string` | "Default" | 既定で使うアイコン情報の名前。 / 表示条件: `showAllSettings.boolValue \|\| showUISettings.boolValue && useIconButtonInfoList.boolValue` |

### Interaction Message Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Interaction Message Game Object | `interactionMessageGameObject` | `GameObject` | – | メッセージを表示するGameObject。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue` |
| Interaction Message Text | `interactionMessageText` | `Text` | – | メッセージ本文を書き込むテキスト。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue` |

### Interaction Actions Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Interaction Actions | `useInteractionActions` | `bool` | – | ONにすると長押し完了時にアクションを実行する。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue` |

### Outline Shader Device Found Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Device Found Shader | `useDeviceFoundShader` | `bool` | – | ONにすると検出中のデバイスに輪郭を付ける。 / 表示条件: `showAllSettings.boolValue \|\| showOutlineShaderSettings.boolValue` |
| Device Found Shader | `deviceFoundShader` | `Shader` | – | 検出中のデバイス輪郭に使うシェーダー。 / 表示条件: `showAllSettings.boolValue \|\| showOutlineShaderSettings.boolValue && useDeviceFoundShader.boolValue` |
| Shader Outline Width | `shaderOutlineWidth` | `float` | – | 輪郭線の太さ（幅）を指定する値。 / 表示条件: `showAllSettings.boolValue \|\| showOutlineShaderSettings.boolValue && useDeviceFoundShader.boolValue` |
| Shader Outline Color | `shaderOutlineColor` | `Color` | – | 輪郭線の色を指定するカラー値。 / 表示条件: `showAllSettings.boolValue \|\| showOutlineShaderSettings.boolValue && useDeviceFoundShader.boolValue` |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | ONにするとAI操作のキャラクターとして扱う。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### Player Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | プレイヤー本体の`playerController`。 / 表示条件: `showComponents` がオンのとき |
| Grab Objects Manager | `grabObjectsManager` | `grabObjects` | – | 掴む処理と連携する`grabObjects`。 / 表示条件: `showComponents` がオンのとき |
| Player Input | `playerInput` | `playerInputManager` | – | キー名とタッチ判定に使う`playerInputManager`。 / 表示条件: `showComponents` がオンのとき |
| Main Camera | `mainCamera` | `Camera` | – | デバイス検出に使うメインカメラ。 / 表示条件: `showComponents` がオンのとき |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | カメラ情報を取得する`playerCamera`。 / 表示条件: `showComponents` がオンのとき |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | レイキャストの起点に使うカメラTransform。 / 表示条件: `showComponents` がオンのとき |
| Main Collider | `mainCollider` | `Collider` | – | プレイヤー自身のコライダー参照。 / 表示条件: `showComponents` がオンのとき |

### Examine Object Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Examine Object Render Texture Panel | `examineObjectRenderTexturePanel` | `GameObject` | – | 拡大表示に使うRenderTextureのパネル。 / 表示条件: `showComponents` がオンのとき |
| Examine Object Blur Panel Parent | `examineObjectBlurPanelParent` | `Transform` | – | 拡大表示時にぼかすUIの親Transform。 / 表示条件: `showComponents` がオンのとき |
| Examine Object Render Camera | `examineObjectRenderCamera` | `Camera` | – | オブジェクト拡大表示用のカメラ。 / 表示条件: `showComponents` がオンのとき |
| Examinate Devices Camera | `examinateDevicesCamera` | `Camera` | – | デバイス観察時に切り替えるカメラ。 / 表示条件: `showComponents` がオンのとき |

### Interaction Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Touch Button | `touchButton` | `GameObject` | – | タッチ操作で表示する使用ボタン。 / 表示条件: `showComponents` がオンのとき |
| Touch Button Raw Image | `touchButtonRawImage` | `RawImage` | – | タッチボタンのアイコンを表示するRawImage。 / 表示条件: `showComponents` がオンのとき |
| Original Touch Button Raw Image | `originalTouchButtonRawImage` | `Texture` | – | タッチボタンの既定アイコン画像。 / 表示条件: `showComponents` がオンのとき |
| Touch Button Icon | `touchButtonIcon` | `GameObject` | – | タッチ操作時に出すキーアイコン。 / 表示条件: `showComponents` がオンのとき |
| Icon Button | `iconButton` | `GameObject` | – | デバイス上に出す使用アイコン。 / 表示条件: `showComponents` がオンのとき |
| Icon Button Rect Transform | `iconButtonRectTransform` | `RectTransform` | – | 使用アイコンの位置を動かすRectTransform。 / 表示条件: `showComponents` がオンのとき |
| Action Text | `actionText` | `Text` | – | デバイスの操作名を表示するテキスト。 / 表示条件: `showComponents` がオンのとき |
| Key Text | `keyText` | `Text` | – | 操作キー名を表示するテキスト。 / 表示条件: `showComponents` がオンのとき |
| Object Name Text | `objectNameText` | `Text` | – | デバイス名を表示するテキスト。 / 表示条件: `showComponents` がオンのとき |
| Object Image | `objectImage` | `RawImage` | – | デバイスのアイコン画像を表示するRawImage。 / 表示条件: `showComponents` がオンのとき |
| Object Description Text | `objectDescriptionText` | `Text` | – | デバイスの説明文を表示するテキスト。 / 表示条件: `showComponents` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `objectAmountText` | `Text` | – | – |
| `tagsForDevices` | `List<string>` | new List<string> () | – |
| `driving` | `bool` | – | – |
| `iconButtonCanBeShown` | `bool` | true | – |
| `objectToUse` | `GameObject` | – | – |
| `currentVehicle` | `GameObject` | – | – |
| `deviceList` | `List<deviceInfo>` | new List<deviceInfo> () | – |
| `deviceGameObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| `currentDeviceInfo` | `deviceInfo` | – | – |
| `searchingDevicesWithRaycast` | `bool` | – | – |
| `secondaryDeviceFound` | `bool` | – | – |
| `currentDeviceIsPickup` | `bool` | – | – |
| `examiningObject` | `bool` | – | – |
| `interactionActionInfoList` | `List<interactionActionInfo>` | new List<interactionActionInfo> () | – |
| `iconButtonInfoList` | `List<iconButtonInfo>` | new List<iconButtonInfo> () | – |
| `gameObjectListToIgnore` | `List<GameObject>` | new List<GameObject> () | – |
| `multipleInteractionInfoList` | `List<multipleInteractionInfo>` | new List<multipleInteractionInfo> () | – |
| `currenDeviceActionName` | `string` | – | – |
| `holdingInteractionButtonActive` | `bool` | – | – |
| `showIntereactionSettings` | `bool` | – | – |
| `showOutlineShaderSettings` | `bool` | – | – |
| `showEventsSettings` | `bool` | – | – |
| `showOtherSettings` | `bool` | – | – |
| `showDebugSettings` | `bool` | – | – |
| `showAllSettings` | `bool` | – | – |
| `showComponents` | `bool` | – | – |
| `showUISettings` | `bool` | – | – |
| `ignoreIfPlayerMenuActiveState` | `bool` | – | – |
| `ignoreIfUsingDeviceActiveState` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `removeSecondaryDeviceInfo()` | レイキャスト検出と副デバイスの3つの参照をまとめてnullに戻す。 |
| `enableOrDisableIconButton(bool state)` | アイコンボタンの状態が異なる場合だけ `setIconButtonState(state)` を呼ぶ。 |
| `setUseMinDistanceToUseDevicesState(bool state)` | `useMinDistanceToUseDevices` フラグを設定するだけ。 |
| `getclosestDevice(bool activeDevicesIcons, bool checkForCameraDistance)` | 一覧から距離や画面中心で最寄りを選び、遮蔽・角度・距離条件で除外しつつ `objectToUse` とUIを更新して番号を返す。 |
| `setCurrentDeviceStringManagerInfo(deviceInfo deviceToUseInfo)` | 対象の `deviceStringAction` からアクション名・アイコン・説明を取得し、キー表示とアイコン表示可否を更新する。 |
| `checkIfSetNewShaderToDeviceFound(GameObject objectToCheck)` | 対象を現在の検出デバイスとして記録し、輪郭シェーダ設定が有効なら輪郭を付ける。 |
| `checkIfSetOriginalShaderToPreviousDeviceFound(GameObject objectToCheck)` | 見つかっていたデバイスの輪郭を解除し、`currentDeviceToUseFound` をnullにする。 |
| `isCurrentDeviceToUseFound(GameObject objectToCheck)` | `currentDeviceToUseFound` と一致するかを返すだけ。 |
| `setInteractionButtonName()` | `objectToUse` の情報からアクション名・説明・アイコンを取得し、個数表示やフォントサイズ込みでUIへ反映する。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | デバイスのトリガー出入りを判定し、タグや運転状態を確認して一覧への追加/削除、アイコンや現在デバイスの更新を行う。 |
| `addDeviceToListIfNotAlreadyIncluded(GameObject deviceToAdd)` | 一覧に無ければ `addDeviceToList` するだけ。 |
| `addDeviceToList(GameObject deviceToAdd)` | `deviceInfo` を作って `deviceStringAction` の情報を複製し、検出アイコンを生成して一覧へ追加する。 |
| `setIgnoreIfPlayerMenuActiveState(bool state)` | `ignoreIfPlayerMenuActiveState` を設定するだけ。 |
| `setIgnoreIfUsingDeviceActiveState(bool state)` | `ignoreIfUsingDeviceActiveState` を設定するだけ。 |
| `useDevice()` | 現在のデバイスへ長押し/複数インタラクション判定を行い、使用メッセージを送ってUIと輪郭を更新する。 |
| `useCurrentDevice(GameObject currentObjectToUse)` | `objectToUse` を指定オブジェクトに差し替えて `useDevice` を呼ぶだけ。 |
| `setObjectToRemoveAferStopUse(GameObject objectToRemove)` | `objectToRemoveAferStopUse` を設定するだけ。 |
| `checkIfRemoveDeviceFromList()` | デバイス使用終了時に、指定されたオブジェクトを一覧から外して最寄りを再計算する。 |
| `takePickupsAround()` | 周囲の拾得物をまとめて取得し、長押し対象は除外したうえで最寄りデバイスを更新する。 |
| `updateClosestDeviceList()` | `getclosestDevice(false, false)` を呼ぶだけ。 |
| `enableOrDisableTouchButton(bool state)` | `keepInteractionTouchButtonAlwaysActive` でない場合に、タッチボタンの表示を切り替える。 |
| `disableIcon()` | タッチボタンを消し、アイコン表示を許可し、`driving` と `objectToUse` をリセットする。 |
| `setIconButtonCanBeShownState(bool state)` | `iconButtonCanBeShown` フラグを設定するだけ。 |
| `setIconButtonState(bool state)` | アイコンパネルとタッチボタンの表示を切り替え、非表示時は検出アイコンも全て消す。 |
| `getCurrentIconButtonState()` | `iconButtonActive` を返すだけ。 |
| `removeVehicleFromList()` | `currentVehicle` があれば一覧から取り除く。 |
| `setDrivingState(bool state)` | `driving` を設定し、運転中はアイコンを出さないよう `iconButtonCanBeShown` を反転設定する。 |
| `setCurrentVehicle(GameObject vehicle)` | `currentVehicle` を差し替えるだけ。 |
| `removeCurrentVehicle(GameObject vehicle)` | 運転中でなく、指定車両が `currentVehicle` ならnullにする。 |
| `clearDeviceList()` | 検出アイコンを破棄してデバイス一覧を空にする。 |
| `clearDeviceListButOne(GameObject objectToKeep)` | 指定オブジェクト以外のデバイスとアイコンを一覧から削除し、長押しコルーチンも停止する。 |
| `checkDeviceName()` | `objectToUse` のデバイス情報を読み直し、アクション名・名前・アイコン・説明をUIへ再反映する。 |
| `reloadDeviceStringActionOnPlayer(GameObject objectToCheck)` | `objectToUse` と一致する場合のみ `checkDeviceName` で表示を更新する。 |
| `existInDeviceList(GameObject objecToCheck)` | `deviceGameObjectList` に含まれるかを返す。 |
| `removeDeviceFromList(GameObject objectToRemove)` | 一致するデバイスとアイコンを削除し、一覧が空なら現在デバイスの参照もnullにする。 |
| `removeDeviceFromListExternalCall(GameObject objectToRemove)` | 0.01秒待ってから一覧削除と輪郭解除を行うコルーチンを開始する。 |
| `removeDeviceFromListUsingParent(GameObject objectToRemove)` | 指定オブジェクトの子孫にあるデバイスを一覧から取り除く。 |
| `isInTagsForDevicesList(GameObject objectToCheck)` | `tagsForDevices` にタグが含まれるかを返す。 |
| `setExamineteDevicesCameraState(bool state, bool useBlurUIPanel)` | 調査用カメラを切り替え、ブラー用なら別カメラも連動させ、`examiningObject` を設定する。 |
| `getExaminateDevicesCamera()` | `examinateDevicesCamera` を返すだけ。 |
| `isExaminingObject()` | `examiningObject` を返すだけ。 |
| `anyDeviceDetected()` | デバイス一覧に要素があるかを返す。 |
| `getExamineObjectRenderTexturePanel()` | `examineObjectRenderTexturePanel` を返すだけ。 |
| `getExamineObjectBlurPanelParent()` | `examineObjectBlurPanelParent` を返すだけ。 |
| `setKeyText(bool state)` | 操作キー表示テキストを、タッチ操作かどうかと `iconButtonInfo` の設定に応じて更新する。 |
| `setActionAndNameText(string newActionText, string newObjectNameText)` | アクション名とオブジェクト名を設定し、言語設定が有効ならローカライズして反映する。 |
| `setExtraActionInfo(Texture newIcon, string newDescription)` | オブジェクト画像と説明文を設定・表示切替し、タッチボタン用アイコンも更新する。 |
| `updateUIInfo()` | `checkDeviceName` を呼ぶだけ。 |
| `checkShowObjectMessage(string message, float waitTime)` | メッセージ表示コルーチンを開始し、`waitTime` 後に自動で閉じる。 |
| `stopShowObjectMessage()` | メッセージ表示コルーチンを停止し、メッセージUIを閉じる。 |
| `getCurrentDeviceActionText()` | `currentDeviceActionText` を返すだけ。 |
| `hasDeviceToUse()` | `objectToUse` がnullでないかを返す。 |
| `setUseDeviceButtonEnabledState(bool state)` | `useDeviceButtonEnabled` を設定し、`holdingButton` をfalseにする。 |
| `setUseDeviceButtonEnabledStateByCounter(bool state)` | カウンタを増減し、0件のときだけボタンを使用可能にする。 |
| `setPauseUseDeviceButtonForDurationState(float pauseDuration)` | ボタンを `pauseDuration` 秒だけ無効化するコルーチンを開始し、既存のものは停止する。 |
| `stopSetPauseUseDeviceButtonForDurationState()` | 一時停止コルーチンを止めるだけで、フラグは変更しない。 |
| `checkIfPickObjectsAround()` | 長押し時間を超えていれば周囲の拾得物をまとめて取得し、そうでなければ通常の使用を行う。 |
| `checkIfStopUseDeviceIfDrivingVehicle()` | 運転中なら `currentVehicle` を対象に `useCurrentDevice` を呼ぶ。 |
| `checkIfStopUseDevice()` | デバイス使用中なら `useDevice` を呼んで使用を終了させる。 |
| `stopHoldInteractionButtonCoroutine()` | 長押しコルーチンを停止し、スライダーとタイマー表示をリセットする。 |
| `setPauseVehicleGetOffInputState(bool state)` | `pauseVehicleGetOffInput` を設定するだけ。 |
| `ispauseVehicleGetOffInputActive()` | `pauseVehicleGetOffInput` を返すだけ。 |
| `inputActivateDeviceByInteractionNameText(Text interactionNameText)` | 複数インタラクションのテキストと一致する入力名を探し、`inputActivateDeviceByName` を呼ぶ。 |
| `inputActivateDeviceByName(string interactionName)` | 入力名を設定して複数インタラクションを有効にした状態で `inputActivateDevice` を呼び、元に戻す。 |
| `inputActivateDevice()` | ボタンが有効なら `useDevice` を呼び、さらにインタラクションアクションのイベントを発火する。 |
| `inputHoldToPickObjectsAround()` | 拾得物の長押し取得が有効なら、押下時刻を記録して保持状態にする。 |
| `inputReleaseToPickObjectsAround()` | 長押し取得の判定を行い、長押しインタラクション中ならその状態を解除する。 |
| `setUsedByAIState(bool state)` | `usedByAI` を設定するだけ。 |
| `setCanUseDevicesState(bool state)` | `canUseDevices` を設定するだけ。 |
| `setUseDeviceFoundShaderState(bool state)` | `useDeviceFoundShader` を設定するだけ。 |
| `setUseDeviceFoundShaderStateFromEditor(bool state)` | `useDeviceFoundShader` を設定し、エディタ用にコンポーネントを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` でコンポーネントを更新し、シーンをダーティにする。 |

## 内部型

- `deviceInfo`（class）
- `interactionActionInfo`（class）
- `iconButtonInfo`（class）
- `multipleInteractionInfo`（class）
