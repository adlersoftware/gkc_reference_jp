# deviceStringAction

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/deviceStringAction.cs:5`

**概要**: Action System が表示するデバイス名・行動名（`deviceAction`）・アイコン表示状態と、その表示用トランスフォームやフォントサイズを保持する。ほぼ getter/setter のみ。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Device Name | `deviceName` | `string` | – | 使用アイコンに表示するオブジェクト名。 |
| Device Action | `deviceAction` | `string` | – | アイコンに出す操作名で、空文字だと表示されない。 |
| Secondary Device Action | `secondaryDeviceAction` | `string` | – | 状態に応じて切り替える2つ目の操作名。 |
| Reload Device Action On Press | `reloadDeviceActionOnPress` | `bool` | – | 押下時に名前と操作名の表示を再取得する。 |
| Set Using Device State | `setUsingDeviceState` | `bool` | – | 使用時に使用中フラグを切り替えるかどうか。 |
| Use Raycast To Detect Device Parts | `useRaycastToDetectDeviceParts` | `bool` | – | デバイスの部品をレイキャストで検出する。 |
| Ignore Use Only Device If Visible On Camera | `ignoreUseOnlyDeviceIfVisibleOnCamera` | `bool` | true | 画面に映っていなくても使用対象にできる。 |
| Use Fixed Device Icon Position | `useFixedDeviceIconPosition` | `bool` | – | アイコンをデバイス上ではなく画面の固定位置に出す。 |
| Use Custom Device Transform Position | `useCustomDeviceTransformPosition` | `bool` | – | 画面内判定に使う位置を専用トランスフォームにする。 |
| Custom Device Transform Position | `customDeviceTransformPosition` | `Transform` | – | 画面内判定の基準にするトランスフォーム。 / 表示条件: `useCustomDeviceTransformPosition` がオンのとき |
| Check If Obstacle Between Device And Player | `checkIfObstacleBetweenDeviceAndPlayer` | `bool` | – | 間に対象物があると使用候補から外す。 |

### Show/Hide Interaction Icon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hide Icon On Press | `hideIconOnPress` | `bool` | – | 1回押した後にアイコンを隠す。 |
| Disable Icon On Press | `disableIconOnPress` | `bool` | – | 押下後にアイコンを消し、対象リストから外す。 |
| Hide Icon On Use Device | `hideIconOnUseDevice` | `bool` | – | 使用中はアイコンを非表示にする。 |
| Show Icon On Stop Use Device | `showIconOnStopUseDevice` | `bool` | – | 使用終了時にアイコンを再表示する。 |
| Show Icon | `showIcon` | `bool` | – | トリガー内にいる間アイコンを表示する。 |
| Show Touch Icon Button | `showTouchIconButton` | `bool` | – | タッチ用の使用ボタンを表示する。 |

### Multiple Interaction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Multiple Interaction | `useMultipleInteraction` | `bool` | – | 複数の操作名を登録し入力ごとに別動作をさせる。 |

### Text Font Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Text Font Size Active | `setTextFontSizeActive` | `bool` | – | 名前テキストの文字サイズを個別指定する。 |
| Text Font Size | `textFontSize` | `int` | 17 | 名前テキストに使う文字サイズ。 / 表示条件: `setTextFontSizeActive` がオンのとき |

### Min Distance And Angle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Distance To Device | `ignoreDistanceToDevice` | `bool` | – | 距離制限を無視して常に使用可能にする。 |
| Use Custom Min Distance To Use Device | `useCustomMinDistanceToUseDevice` | `bool` | – | プレイヤー側の距離制限値を上書きする。 / 表示条件: `ignoreDistanceToDevice` がオフのとき |
| Custom Min Distance To Use Device | `customMinDistanceToUseDevice` | `float` | – | 使用できる最大距離（メートル単位）。 / 表示条件: `!ignoreDistanceToDevice.boolValue && useCustomMinDistanceToUseDevice.boolValue` |
| Use Custom Min Angle To Use | `useCustomMinAngleToUse` | `bool` | – | 向きの角度制限を有効にする。 |
| Custom Min Angle To Use Device | `customMinAngleToUseDevice` | `float` | – | 使用できる角度差の上限（度）。 / 表示条件: `useCustomMinAngleToUse` がオンのとき |
| Use Relative Direction Between Player And Object | `useRelativeDirectionBetweenPlayerAndObject` | `bool` | – | 角度判定に正面ではなく自分から見た方向を使う。 / 表示条件: `useCustomMinAngleToUse` がオンのとき |
| Remove Device From Player List On Max Distance | `removeDeviceFromPlayerListOnMaxDistance` | `bool` | – | 一定距離を超えたら候補リストから削除する。 |
| Max Distance To Remove Device From Player List | `maxDistanceToRemoveDeviceFromPlayerList` | `float` | – | 候補から外す距離の閾値。 / 表示条件: `removeDeviceFromPlayerListOnMaxDistance` がオンのとき |
| Use Max Distance To Camera Center | `useMaxDistanceToCameraCenter` | `bool` | – | 画面中心からの距離で候補を絞り込む。 |
| Max Distance To Camera Center | `maxDistanceToCameraCenter` | `float` | – | 画面中心からの許容距離（ピクセル）。 / 表示条件: `useMaxDistanceToCameraCenter` がオンのとき |

### Use Custom Icon Button Info Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Icon Button Info | `useCustomIconButtonInfo` | `bool` | – | 使うアイコンボタン情報を名前で指定する。 |
| Custom Icon Button Info Name | `customIconButtonInfoName` | `string` | – | 参照するアイコンボタン情報の名前。 / 表示条件: `useCustomIconButtonInfo` がオンのとき |

### Use Transform Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Transform For String Action | `useTransformForStringAction` | `bool` | – | アイコン位置の基準に専用トランスフォームを使う。 |
| Use Separated Transform For Every View | `useSeparatedTransformForEveryView` | `bool` | – | 三人称と一人称で別々の基準位置を使う。 / 表示条件: `useTransformForStringAction` がオンのとき |
| Transform For Third Person | `transformForThirdPerson` | `Transform` | – | 三人称視点でアイコンを出す位置。 / 表示条件: `useTransformForStringAction.boolValue && useSeparatedTransformForEveryView.boolValue` |
| Transform For First Person | `transformForFirstPerson` | `Transform` | – | 一人称視点でアイコンを出す位置。 / 表示条件: `useTransformForStringAction.boolValue && useSeparatedTransformForEveryView.boolValue` |
| Transform For String Action | `transformForStringAction` | `Transform` | – | アイコン表示に使う基準トランスフォーム。 / 表示条件: `useTransformForStringAction` がオンのとき |
| Action Offset | `actionOffset` | `float` | 1 | デバイス位置からアイコンを上へずらす量。 / 表示条件: `useTransformForStringAction` がオフのとき |
| Use Local Offset | `useLocalOffset` | `bool` | true | ずらす方向を自分自身の上方向に合わせる。 / 表示条件: `useTransformForStringAction` がオフのとき |

### Other Object Info Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Icon Texture | `showIconTexture` | `bool` | – | 使用情報にアイコン画像を表示する。 |
| Icon Texture | `iconTexture` | `Texture` | – | 使用情報に表示するアイコン画像。 / 表示条件: `showIconTexture` がオンのとき |
| Use Object Description | `useObjectDescription` | `bool` | – | 使用情報に説明文を表示する。 |
| Object Description | `objectDescription` | `string` | – | 使用情報に表示する説明文。 / 表示条件: `useObjectDescription` がオンのとき / TextArea (5, 20) |
| Description Font Size | `descriptionFontSize` | `int` | 14 | 説明文に使う文字サイズ。 / 表示条件: `useObjectDescription` がオンのとき |
| Show Object Amount | `showObjectAmount` | `bool` | – | オブジェクトの数量表示を有効にする。 |
| Object Amount | `objectAmount` | `int` | – | 表示するオブジェクトの数量値。 / 表示条件: `showObjectAmount` がオンのとき |
| Use Hold Interaction Button | `useHoldInteractionButton` | `bool` | – | ボタン長押しで使用する方式にする。 |
| Hold Interaction Button Duration | `holdInteractionButtonDuration` | `float` | – | 長押しが必要な時間（秒）。 / 表示条件: `useHoldInteractionButton` がオンのとき |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューにギズモを表示する。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.green | ギズモのラベルに使う文字色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Color | `gizmoColor` | `Color` | Color.white | シーンビューに描く球体の色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | 0.3f | シーンビューに描く球体の半径。 / 表示条件: `showGizmo` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `multipleInteractionNameList` | `List<string>` | new List<string> () | – |
| `iconEnabled` | `bool` | true | – |
| `usingDevice` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getRegularTransformForIcon()` | `useTransformForStringAction` と `transformForStringAction` があればそれを、なければ自身の `transform` を返す。 |
| `useSeparatedTransformForEveryViewEnabled()` | `useTransformForStringAction` と `useSeparatedTransformForEveryView` の論理積を返すだけ。 |
| `getTransformForIconThirdPerson()` | `transformForThirdPerson` を返すだけ。 |
| `getTransformForIconFirstPerson()` | `transformForFirstPerson` を返すだけ。 |
| `setIconEnabledState(bool state)` | `iconEnabled` を `state` に設定するだけ。 |
| `setShowIconState(bool state)` | `showIcon` を `state` に設定するだけ。 |
| `enableIcon()` | `iconEnabled` を真にする `setIconEnabledState(true)` を呼ぶだけ。 |
| `disableIcon()` | `iconEnabled` を偽にする `setIconEnabledState(false)` を呼ぶだけ。 |
| `getDeviceAction()` | `currentDeviceAction` を返すだけ。 |
| `setDeviceAction(string newDeviceAction)` | `deviceAction` と `currentDeviceAction` を `newDeviceAction` に設定する。 |
| `changeActionName(bool state)` | `showingSecondaryAction` を `state` にし、`secondaryDeviceAction` が空でなければ表示名を切替える。 |
| `toggleActionName()` | `showingSecondaryAction` を反転して `changeActionName` を呼ぶだけ。 |
| `checkSetUsingDeviceState()` | `usingDevice` を反転して `checkSetUsingDeviceState` を呼ぶだけ。 |
| `checkSetUsingDeviceState(bool state)` | `setUsingDeviceState` が有効なときだけ `usingDevice` を `state` にする。 |
| `getDeviceName()` | `deviceName` を返すだけ。 |
| `setNewDeviceName(string newName)` | `deviceName` を `newName` に設定するだけ。 |
| `getTextFontSize()` | `setTextFontSizeActive` なら `textFontSize` を、無効なら 0 を返す。 |
