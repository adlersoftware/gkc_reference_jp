# moveCameraToDevice

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/moveCameraToDevice.cs:4`

**概要**: デバイス使用時にプレイヤーカメラを`cameraPosition`へ移動し、終了時に元へ戻すコンポーネント。使用中は操作や武器、HUDを停止する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Movement Active | `cameraMovementActive` | `bool` | true | オンにすると使用中にカメラを`cameraPosition`へ移動させる。 |
| Camera Position | `cameraPosition` | `GameObject` | – | 使用時にメインカメラを親子付けする目標位置のトランスフォーム。 |
| Smooth Camera Movement | `smoothCameraMovement` | `bool` | true | オフにするとカメラ移動を補間せず即座に切り替える。 |
| Use Fixed Lerp Movement | `useFixedLerpMovement` | `bool` | true | オンにすると距離ではなく固定速度でカメラを補間移動する。 / 表示条件: `smoothCameraMovement` がオンのとき |
| Fixed Lerp Movement Speed | `fixedLerpMovementSpeed` | `float` | 2 | 固定補間移動での1秒あたりの補間進行量。 / 表示条件: `smoothCameraMovement.boolValue && useFixedLerpMovement.boolValue` |
| Camera Movement Speed Third Person | `cameraMovementSpeedThirdPerson` | `float` | 1 | 三人称時のカメラ移動速度で、移動時間の計算に使う。 / 表示条件: `smoothCameraMovement` がオンのとき |
| Camera Movement Speed First Person | `cameraMovementSpeedFirstPerson` | `float` | 0.2f | 一人称時のカメラ移動速度で、移動時間の計算に使う。 / 表示条件: `smoothCameraMovement` がオンのとき |
| Ignore Move Camera Function Enabled | `ignoreMoveCameraFunctionEnabled` | `bool` | – | オンにするとこの機器のカメラ移動処理を丸ごと無効にする。 |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Second Move Camera To Device | `secondMoveCameraToDevice` | `bool` | – | オンにするとプレイヤー状態やHUDの切り替えを省く2台目扱いになる。 |
| Disable Player Mesh Game Object | `disablePlayerMeshGameObject` | `bool` | true | オンにすると使用中にプレイヤーのメッシュを非表示にする。 |
| Enable Player Mesh Game Object If First Person Active | `enablePlayerMeshGameObjectIfFirstPersonActive` | `bool` | – | 一人称が有効だった場合、終了後もメッシュ表示を維持する。 |
| Ignore FBA Active If Disable Player Mesh | `ignoreFBAActiveIfDisablePlayerMesh` | `bool` | – | FBAが有効でもプレイヤーメッシュの無効化を適用する。 |
| Ignore Camera Position Adjusment On FBA | `ignoreCameraPositionAdjusmentOnFBA` | `bool` | – | FBA有効時はカメラ位置を動かさず向きだけ合わせる。 |
| Unlock Cursor | `unlockCursor` | `bool` | true | オンにすると使用中にマウスカーソルを表示して操作できる。 |
| Ignore Hide Cursor On Click | `ignoreHideCursorOnClick` | `bool` | – | 使用中はクリックしてもカーソルを隠さない。 / 表示条件: `unlockCursor` がオンのとき |
| Set New Mouse Cursor Controller Speed | `setNewMouseCursorControllerSpeed` | `bool` | – | 使用中だけマウスカーソル速度を別の値に差し替える。 |
| New Mouse Cursro Controller Speed | `newMouseCursroControllerSpeed` | `float` | – | 差し替えるマウスカーソル速度の値。 / 表示条件: `setNewMouseCursorControllerSpeed` がオンのとき |
| Align Player With Camera Position On Start Use Device | `alignPlayerWithCameraPositionOnStartUseDevice` | `bool` | – | 使用開始時にプレイヤーをカメラ位置へ移動させる。 |
| Align Player With Camera Position On Stop Use Device | `alignPlayerWithCameraPositionOnStopUseDevice` | `bool` | – | 使用終了時にプレイヤーをカメラ位置へ移動させる。 |
| Align Player With Camera Rotation On Start Use Device | `alignPlayerWithCameraRotationOnStartUseDevice` | `bool` | – | 使用開始時にプレイヤーの向きをカメラ向きに合わせる。 |
| Align Player With Camera Rotation On Stop Use Device | `alignPlayerWithCameraRotationOnStopUseDevice` | `bool` | – | 使用終了時にプレイヤーの向きをカメラ向きに合わせる。 |
| Custom Align Player Transform | `customAlignPlayerTransform` | `Transform` | – | 位置・回転合わせの基準にするトランスフォーム。未設定ならカメラを使う。 |
| Reset Player Camera Direction | `resetPlayerCameraDirection` | `bool` | – | 使用開始時にカメラの注視角度をリセットする。 |

### HUD Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable All Player HUD | `disableAllPlayerHUD` | `bool` | – | 使用中はプレイヤーHUDをすべて非表示にする。 |
| Disable Secondary Player HUD | `disableSecondaryPlayerHUD` | `bool` | true | `disableAllPlayerHUD`がオフの時、サブHUDのみ隠す。 |
| Disable All Dynamic UI Elements | `disableAllDynamicUIElements` | `bool` | true | 使用中は画面上の動的UI要素をまとめて隠す。 |
| Disable Touch Controls | `disableTouchControls` | `bool` | – | 使用中はタッチ操作のコントロールを無効にする。 |
| Disable Interaction Touch Button On Using Device | `disableInteractionTouchButtonOnUsingDevice` | `bool` | – | 使用中はインタラクション用のタッチボタンを隠す。 |

### Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Keep Weapons If Carrying | `keepWeaponsIfCarrying` | `bool` | – | 武器を持ったまま使用できるようにする。 |
| Draw Weapons If Previously Carrying | `drawWeaponsIfPreviouslyCarrying` | `bool` | – | 使用終了時に以前持っていた武器を再び構えさせる。 / 表示条件: `keepWeaponsIfCarrying` がオンのとき |
| Keep Only If Player Is On First Person | `keepOnlyIfPlayerIsOnFirstPerson` | `bool` | – | 一人称の時だけ武器の保持と再構えを行う。 / 表示条件: `keepWeaponsIfCarrying` がオンのとき |
| Disable Weapons Directly On Start | `disableWeaponsDirectlyOnStart` | `bool` | – | 使用開始時に所持武器を即座に無効化する。 / 表示条件: `keepWeaponsIfCarrying` がオンのとき |
| Disable Weapons Camera | `disableWeaponsCamera` | `bool` | – | 使用中は武器用カメラを無効にする。 |
| Carry Weapon On Lower Position Active | `carryWeaponOnLowerPositionActive` | `bool` | – | フリー操作状態で武器を下段位置に構えさせる。 |
| Ignore Melee Weapon Check | `ignoreMeleeWeaponCheck` | `bool` | – | 使用開始時の掴みオブジェクト破棄判定を省略する。 |

### Camera Rotation On Exit Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Player Camera Rotation On Exit | `setPlayerCameraRotationOnExit` | `bool` | – | 使用終了時に下のトランスフォームの回転をカメラへ適用する。 |
| Player Camera Transform Third Person | `playerCameraTransformThirdPerson` | `Transform` | – | 三人称で終了する時に回転を適用するカメラ側トランスフォーム。 / 表示条件: `setPlayerCameraRotationOnExit` がオンのとき |
| Player Pivot Transform Third Person | `playerPivotTransformThirdPerson` | `Transform` | – | 三人称で終了する時に回転を適用するピボット側トランスフォーム。 / 表示条件: `setPlayerCameraRotationOnExit` がオンのとき |
| Player Camera Transform First Person | `playerCameraTransformFirstPerson` | `Transform` | – | 一人称で終了する時に回転を適用するカメラ側トランスフォーム。 / 表示条件: `setPlayerCameraRotationOnExit` がオンのとき |
| Player Pivot Transform First Person | `playerPivotTransformFirstPerson` | `Transform` | – | 一人称で終了する時に回転を適用するピボット側トランスフォーム。 / 表示条件: `setPlayerCameraRotationOnExit` がオンのとき |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューにこの機器のギズモを表示する。 |
| Gizmo Radius | `gizmoRadius` | `float` | 0.1f | `cameraPosition`に描く球の半径。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.black | エディタのギズモラベルに使う文字色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Length | `gizmoArrowLength` | `float` | 0.3f | ギズモ矢印の先端部分の大きさ。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Line Length | `gizmoArrowLineLength` | `float` | 0.5f | ギズモ矢印として描く線の長さ。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Angle | `gizmoArrowAngle` | `float` | 20 | ギズモ矢印の先端部分の開き角度。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Color | `gizmoArrowColor` | `Color` | Color.white | ギズモ矢印を描画するときの色。 / 表示条件: `showGizmo` がオンのとき |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `moveCamera(bool state)` | `cameraPosition`へカメラを親子付けして移動し、操作停止や武器・HUD・カーソルの切替、終了時の復元を行う。 |
| `hasSecondMoveCameraToDevice()` | `secondMoveCameraToDevice`を`true`にするだけ。 |
| `setCurrentPlayer(GameObject player)` | プレイヤーを保持し、制御・カメラ・武器・頭部トラッキングなど各コンポーネントを取得する。 |
| `enableFreeInteractionState()` | `carryWeaponOnLowerPositionActive`のときだけ、武器の下部携行を有効化し汎用カーソルを無効化する。 |
| `disableFreeInteractionState()` | `carryWeaponOnLowerPositionActive`のときだけ、下部携行を解除し汎用カーソルを有効化する。 |
| `stopMovement()` | カメラ移動コルーチンを停止し、`deviceEnabled`を`false`にする。 |
| `isCameraMoving()` | `movingCamera`を返すだけ。 |
| `setCurrentPlayerUseDeviceButtonEnabledState(bool state)` | `usingDevicesSystem`があれば、使用ボタンの有効状態を`state`に設定する。 |
