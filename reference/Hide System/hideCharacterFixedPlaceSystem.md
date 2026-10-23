# hideCharacterFixedPlaceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Hide System/hideCharacterFixedPlaceSystem.cs:6`

**概要**: 固定の隠れ場所で、プレイヤーの隠れ/表示に応じてAI可視状態・FOV・コライダー・状態アイコン・UI・イベントを切り替えるシステム。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Transform | `cameraTransform` | `Transform` | – | 隠れ中に回転を操作するカメラのTransform。 |
| Pivot Transform | `pivotTransform` | `Transform` | – | カメラの水平回転を担当するピボットTransform。 |
| Camera Position Transform | `cameraPositionTransform` | `Transform` | – | 回転範囲ギズモを描く基準になるカメラ位置Transform。 |
| Can Reset Camera Rotation | `canResetCameraRotation` | `bool` | true | `useSpringRotation`時に回転を初期状態へ戻す切替。 |
| Can Reset Camera Position | `canResetCameraPosition` | `bool` | true | `useSpringMovement`時に位置を初期状態へ戻す切替。 |
| Use Character State Icon | `useCharacterStateIcon` | `bool` | true | 隠れ状態をキャラ状態アイコンへ反映するかの切替。 |
| Visible Character State Name | `visibleCharacterStateName` | `string` | "Visible" | 隠れていない時に表示する状態アイコン名。 |
| Not Visible Character State Name | `notVisibleCharacterStateName` | `string` | "Not Visible" | 隠れ中に表示する状態アイコン名。 |
| Check If Detected While Hidden | `checkIfDetectedWhileHidden` | `bool` | – | 隠れ中も敵の検知判定を行い発見で解除する切替。 |

### Camera Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Can Rotate | `cameraCanRotate` | `bool` | true | 隠れ中にマウスでカメラを回転できるかの切替。 |
| Rotation Speed | `rotationSpeed` | `float` | 10 | 隠れ中のマウス入力に対するカメラ回転速度。 |
| Smooth Camera Rotation Speed | `smoothCameraRotationSpeed` | `float` | 5 | カメラ回転を補間して滑らかにする速度。 |
| Use Spring Rotation | `useSpringRotation` | `bool` | – | 入力が止まると回転を初期位置へ戻すかの切替。 |
| Spring Rotation Delay | `springRotationDelay` | `float` | 1 | 回転を戻し始めるまでの待ち時間(秒)。 / 表示条件: `useSpringRotation` がオンのとき |

### Camera Movement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Can Move | `cameraCanMove` | `bool` | true | 隠れ中にカメラを平行移動できるかの切替。 |
| Move Camera Speed | `moveCameraSpeed` | `float` | 10 | 隠れ中のカメラ平行移動の移動速度。 |
| Smooth Move Camera Speed | `smoothMoveCameraSpeed` | `float` | 5 | カメラ移動を補間して滑らかにする速度。 |
| Use Spring Movement | `useSpringMovement` | `bool` | – | 入力が止まると位置を初期位置へ戻すかの切替。 |
| Spring Movement Delay | `springMovementDelay` | `float` | 1 | 位置を戻し始めるまでの待ち時間(秒)。 / 表示条件: `useSpringMovement` がオンのとき |

### Hide/Visible Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hiden Event | `hidenEvent` | `UnityEvent` | new UnityEvent () | 隠れ状態になった時に呼ばれるイベント。 |
| Hide Event Delay | `hideEventDelay` | `float` | – | 隠れイベントを呼ぶまでの遅延秒数。 |
| Visble Event | `visbleEvent` | `UnityEvent` | new UnityEvent () | 隠れ状態から復帰した時に呼ばれるイベント。 |
| Visible Event Delay | `visibleEventDelay` | `float` | – | 復帰イベントを呼ぶまでの遅延秒数。 |

### Camera FOV Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Hidden Fov | `setHiddenFov` | `bool` | – | 隠れ中にカメラのFOVを変更するかの切替。 |
| Hidden Fov | `hiddenFov` | `float` | 20 | 隠れ中に設定するカメラのFOV値。 / 表示条件: `setHiddenFov` がオンのとき |
| Zoom Enabled | `zoomEnabled` | `bool` | – | 隠れ中のズーム操作を有効にするかの切替。 |
| Zoom Speed | `zoomSpeed` | `float` | 10 | ズーム時にFOVが変化する速度。 / 表示条件: `zoomEnabled` がオンのとき |
| Max Zoom | `maxZoom` | `float` | 10 | ズームイン側となるFOV値の下限。 / 表示条件: `zoomEnabled` がオンのとき |
| Min Zoom | `minZoom` | `float` | 90 | ズームアウト側となるFOV値の上限。 / 表示条件: `zoomEnabled` がオンのとき |

### Unable To Hide Message Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Message When Unable To Hide | `useMessageWhenUnableToHide` | `bool` | – | 隠れられない時にメッセージを出すかの切替。 |
| Unable To Hide Message | `unableToHideMessage` | `string` | – | 隠れられない時に表示するメッセージ文言。 / 表示条件: `useMessageWhenUnableToHide` がオンのとき / TextArea (1, 10) |
| Show Message Time | `showMessageTime` | `float` | – | メッセージを表示しておく秒数。 / 表示条件: `useMessageWhenUnableToHide` がオンのとき |

### Action Screen Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Action Screen | `activateActionScreen` | `bool` | true | 隠れ操作中にアクション画面を出すかの切替。 |
| Action Screen Name | `actionScreenName` | `string` | "Use Hide System" | 表示するアクション画面の名前。 / 表示条件: `activateActionScreen` がオンのとき |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンにカメラ範囲のギズモを表示する切替。 |
| Gizmo Color | `gizmoColor` | `Color` | – | ギズモ全体の基本色として使う色。 / 表示条件: `showGizmo` がオンのとき |
| Arc Gizmo Radius | `arcGizmoRadius` | `float` | – | 回転可能範囲を示す円弧の半径。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Length | `gizmoArrowLength` | `float` | 1 | 移動範囲を示す矢印の長さを指定。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Angle | `gizmoArrowAngle` | `float` | 20 | 移動範囲を示す矢印の先端角度。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Arrow Color | `gizmoArrowColor` | `Color` | Color.white | 移動範囲を示す矢印に使う描画色。 / 表示条件: `showGizmo` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `rangeAngleX` | `Vector2` | new Vector2 (-90, 90) | – |
| `rangeAngleY` | `Vector2` | new Vector2 (-90, 90) | – |
| `moveCameraLimitsX` | `Vector2` | new Vector2 (-2, 2) | – |
| `moveCameraLimitsY` | `Vector2` | new Vector2 (-2, 2) | – |
| `hidingCharacter` | `bool` | – | – |
| `moveCameraManager` | `moveCameraToDevice` | – | – |
| `electronicDeviceManager` | `electronicDevice` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableHideState()` | 検知中は何もせず、隠れ状態を反転してAI可視・FOV・コライダー・状態アイコン・イベント・UIを切り替える。 |
| `setCharacterState()` | 状態アイコンを使う設定の時、隠れていれば非表示用、そうでなければ表示用のアイコン名を設定する。 |
| `callUnityEvents()` | 既存のイベントコルーチンを止め、隠れ/表示それぞれの遅延後に該当イベントを発火するコルーチンを開始する。 |
| `resetCameraInputValues()` | マウスや移動の入力値、カメラとピボットの回転・位置を初期値にリセットする。 |
| `changeResetCameraTransfrom()` | カメラ回転と位置のリセット可否フラグを反転し、それぞれの最終実行時刻を0にする。 |
| `setCurrentPlayer(GameObject player)` | 対象プレイヤーを設定して各コンポーネント参照を取得し、この隠れ場所をプレイヤー管理側に登録する。 |
| `checkIfDetected()` | プレイヤー未設定なら取得し、隠れていない時に敵から検知されているかを判定してデバイス使用可否を切り替える。 |
| `showUnableToHideMessage()` | メッセージ表示設定とプレイヤーがある時、隠れられない旨のメッセージを表示する。 |
| `inputResetCameraTransform()` | 隠れ中かつカメラ移動中でなければ`changeResetCameraTransfrom`を呼ぶ。 |
| `inputSetIncreaseZoomStateByButton(bool state)` | 隠れ中・カメラ停止中・ズーム有効時のみ、拡大フラグ`increaseZoom`を`state`に合わせる。 |
| `inputSetDecreaseZoomStateByButton(bool state)` | 隠れ中・カメラ停止中・ズーム有効時のみ、縮小フラグ`decreaseZoom`を`state`に合わせる。 |
| `inputSetZoomValueByMouseWheel(bool state)` | 隠れ中・カメラ停止中・ズーム有効時のみ、ホイール使用時刻を更新し、`state`に応じて拡大/縮小フラグを立てる。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `hidenEvent` | `UnityEvent` | – |
| `visbleEvent` | `UnityEvent` | – |
