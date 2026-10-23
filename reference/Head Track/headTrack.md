# headTrack

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `OnAnimatorIKComponent`
- **ソース**: `Head Track/headTrack.cs:7`

**概要**: アニメータのLookAtを使い、プレイヤーの頭と体を注視対象やカメラ方向へ向けるコンポーネント。対象リストから最近傍を選び、重みを補間してIKを更新する。

**公式ドキュメント抜粋**（[Head Track](../../docs/player-controller-components/player-controller/head-track.md)）

> It manages the head and upper body orientation to make them look to a certain position, with certain clamp limits and according to the forward direction of the character, using IK for both body parts.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Track Enabled | `headTrackEnabled` | `bool` | true | ヘッドトラック全体を有効にする。 |
| Update IK Enabled | `updateIKEnabled` | `bool` | true | IKの更新を毎フレーム行うかどうか。 |
| Head | `head` | `Transform` | – | 注視に使う頭ボーンのTransform参照。 / 表示条件: `headTrackEnabled` がオンのとき |
| Head Weight | `headWeight` | `float` | 1 | 頭の向きを目標方向へ向ける強さ。 / 表示条件: `headTrackEnabled` がオンのとき / Range (0, 1) |
| Body Weight | `bodyWeight` | `float` | 0.4f | 上半身も目標方向へ向ける強さ。 / 表示条件: `headTrackEnabled` がオンのとき / Range (0, 1) |
| Rotation Speed | `rotationSpeed` | `float` | 3 | 視線方向を目標へ補間する速度。 / 表示条件: `headTrackEnabled` がオンのとき |
| Weight Change Speed | `weightChangeSpeed` | `float` | 2 | 頭と体の重みを変化させる速度。 / 表示条件: `headTrackEnabled` がオンのとき |
| Use Time To Change Target | `useTimeToChangeTarget` | `bool` | – | 注視対象の切り替えに間隔を設ける。 / 表示条件: `headTrackEnabled` がオンのとき |
| Time To Change Target | `timeToChangeTarget` | `float` | – | 注視対象を切り替える間隔の秒数。 / 表示条件: `headTrackEnabled.boolValue && useTimeToChangeTarget.boolValue` |
| Obstacle Layer | `obstacleLayer` | `LayerMask` | – | 注視対象を遮る障害物のレイヤー。 / 表示条件: `headTrackEnabled` がオンのとき |
| Use Head Track Target | `useHeadTrackTarget` | `bool` | – | 専用の目標Transformを注視先として使う。 / 表示条件: `headTrackEnabled` がオンのとき |
| Head Track Targe Transform | `headTrackTargeTransform` | `Transform` | – | 頭の向きを合わせる目印のTransform参照。 / 表示条件: `headTrackEnabled.boolValue && useHeadTrackTarget.boolValue` |

### Look Camera Direction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Look In Camera Direction | `lookInCameraDirection` | `bool` | – | カメラの向きを注視方向として使う。 |
| Camera Target To Look | `cameraTargetToLook` | `Transform` | – | カメラ方向を注視する時の目標位置。 / 表示条件: `lookInCameraDirection` がオンのとき |
| Camera Head Weight | `cameraHeadWeight` | `float` | 1 | カメラ注視の時に使う頭の重み。 / 表示条件: `lookInCameraDirection` がオンのとき / Range (0, 1) |
| Camera Body Weight | `cameraBodyWeight` | `float` | 0.4f | カメラ注視時に使う上半身の重み。 / 表示条件: `lookInCameraDirection` がオンのとき / Range (0, 1) |
| Camera Range Angle X | `cameraRangeAngleX` | `Vector2` | new Vector2 (-90, 90) | カメラ注視の縦方向の角度制限。 / 表示条件: `lookInCameraDirection` がオンのとき |
| Camera Range Angle Y | `cameraRangeAngleY` | `Vector2` | new Vector2 (-90, 90) | カメラ注視の横方向の角度制限。 / 表示条件: `lookInCameraDirection` がオンのとき |
| Max Distance To Head To Look At Camera Target | `maxDistanceToHeadToLookAtCameraTarget` | `float` | 1 | カメラ注視を許す頭とカメラの距離の上限。 / 表示条件: `lookInCameraDirection` がオンのとき |
| Look In Opposite Direction Out Of Range | `lookInOppositeDirectionOutOfRange` | `bool` | – | 範囲外の時は逆方向の目標を見る。 / 表示条件: `lookInCameraDirection` がオンのとき |
| Look In Opposite Direction Extra Range | `lookInOppositeDirectionExtraRange` | `float` | 20 | 逆方向の注視へ切り替える角度の余裕。 / 表示条件: `lookInCameraDirection.boolValue && lookInOppositeDirectionOutOfRange.boolValue` |
| Opposite Camera Target To Look | `oppositeCameraTargetToLook` | `Transform` | – | 範囲外で見る逆方向の目標Transform。 / 表示条件: `lookInCameraDirection.boolValue && lookInOppositeDirectionOutOfRange.boolValue` |
| Opposite Camera Target To Look Parent | `oppositeCameraTargetToLookParent` | `Transform` | – | 逆方向の注視用に回転させる親Transform。 / 表示条件: `lookInCameraDirection.boolValue && lookInOppositeDirectionOutOfRange.boolValue` |
| Opposite Camera Parent Rotation Speed | `oppositeCameraParentRotationSpeed` | `float` | – | 逆方向の注視用の親を回す速度。 / 表示条件: `lookInCameraDirection.boolValue && lookInOppositeDirectionOutOfRange.boolValue` |
| Look Behind If Moving | `lookBehindIfMoving` | `bool` | – | 後退して移動中に背後を振り返る。 / 表示条件: `lookInCameraDirection.boolValue && lookInOppositeDirectionOutOfRange.boolValue` |
| Look Behind Rotation Speed | `lookBehindRotationSpeed` | `float` | – | 背後を振り返る時の親の回転速度。 / 表示条件: `lookInOppositeDirectionOutOfRange.boolValue && lookBehindIfMoving.boolValue` |
| Use Dead Zone | `useDeadZone` | `bool` | – | 振り返りに遊びの角度を設ける。 / 表示条件: `lookInCameraDirection.boolValue && lookInOppositeDirectionOutOfRange.boolValue` |
| Dead Zone Look Behind | `deadZoneLookBehind` | `float` | 10 | 振り返りを始める角度のしきい値。 / 表示条件: `lookInOppositeDirectionOutOfRange.boolValue && useDeadZone.boolValue` |

### Range Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Head Range Rotation | `useHeadRangeRotation` | `bool` | true | 注視方向を角度範囲の中に制限する。 / 表示条件: `headTrackEnabled` がオンのとき |

### Targets To Ignore Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Targets To Ignore List | `useTargetsToIgnoreList` | `bool` | – | 無視リストに入れた対象は注視しない。 / 表示条件: `headTrackEnabled` がオンのとき |

### Player Element

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Animator | `animator` | `Animator` | – | 頭ボーンを取得するAnimator参照。 / 表示条件: `headTrackEnabled` がオンのとき |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | プレイヤー制御コンポーネントの参照。 / 表示条件: `headTrackEnabled` がオンのとき |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | カメラ制御コンポーネントの参照。 / 表示条件: `headTrackEnabled` がオンのとき |
| IK Manager | `IKManager` | `IKSystem` | – | 頭のIK重みを参照するIKシステム。 / 表示条件: `headTrackEnabled` がオンのとき |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | 注視方向をシーンビューにギズモ表示する。 / 表示条件: `headTrackEnabled` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | 0.2f | 頭の位置に描くギズモ球の半径。 / 表示条件: `headTrackEnabled.boolValue && showGizmo.boolValue` |
| Arc Gizmo Radius | `arcGizmoRadius` | `float` | – | 角度範囲を示す円弧ギズモの半径。 / 表示条件: `headTrackEnabled.boolValue && showGizmo.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `rangeAngleX` | `Vector2` | new Vector2 (-90, 90) | – |
| `rangeAngleY` | `Vector2` | new Vector2 (-90, 90) | – |
| `playerCanLookState` | `bool` | – | – |
| `lookTargetList` | `List<headTrackTarget>` | new List<headTrackTarget> () | – |
| `targetsToIgnoreList` | `List<GameObject>` | new List<GameObject> () | – |
| `customHeadTrackToLookInfoList` | `List<customHeadTrackToLookInfo>` | new List<customHeadTrackToLookInfo> () | – |
| `currentHeadWeight` | `float` | – | – |
| `currentBodyWeight` | `float` | – | – |
| `originalCameraBodyWeight` | `float` | – | – |
| `cameraBodyWeightTarget` | `float` | – | – |
| `useSmoothHeadTrackDisable` | `bool` | – | – |
| `headTrackActiveWhileAiming` | `bool` | – | – |
| `currentLookTargetLocated` | `bool` | – | – |
| `temporalDirectionToLook` | `Vector3` | – | – |
| `headTrackPaused` | `bool` | – | – |
| `positionToLookFound` | `bool` | – | – |
| `fullBodyAwarenessActive` | `bool` | – | – |
| `lookTargetLocated` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setSmoothHeadTrackDisableState(bool state)` | `useSmoothHeadTrackDisable`を設定するだけ。 |
| `setExternalHeadTrackPauseActiveState(bool state)` | `externalHeadTrackPauseActive`を設定するだけ。 |
| `setHeadTrackSmoothPauseState(bool state)` | 外部ポーズとスムーズ停止のフラグを同時に設定するだけ。 |
| `updateHeadTrack()` | `animator`へ現在の頭・体の重みと注視位置を設定してLookAtを反映する。 |
| `setPauseCanLookStateWithDuration(float newDuration)` | 指定時間だけ`ignorePlayerCanLookTemporallyActive`を立てるコルーチンを開始する。 |
| `playerCanLook()` | エイム状態やFBA、頭IKの重みなどから頭トラック可能かを判定して返す。 |
| `setFullBodyAwarenessActiveState(bool state)` | FBAフラグを設定し、解除時は対象がいれば注視を再開させる。 |
| `getLookPosition()` | 頭位置から対象の可視性と範囲を判定し、最近傍対象やカメラ方向への注視点を補間して返す。 |
| `setCanUseHeadTrackOnLockedCameraActiveState(bool state)` | `canUseHeadTrackOnLockedCameraActive`を設定するだけ。 |
| `isTargetOnHeadRange(Vector3 direction)` | `direction`の水平・垂直角度が現在の視野範囲内ならtrueを返す。 |
| `lerpWeights(float headWeightTarget, float bodyWeightTarget)` | 頭と体の重みを目標値へ`weightChangeSpeed`で補間する。 |
| `getClosestTarget()` | 注視対象リストを掃除し、一定間隔で最も近い対象をカレントに選ぶ。 |
| `checkHeadTrackTarget(headTrackTarget target)` | 無視リストに無ければ対象をリストへ追加し、ポーズを解除して注視を有効化する。 |
| `removeHeadTrackTarget(headTrackTarget target)` | 対象をリストから外し、空になれば注視対象なしの状態にする。 |
| `setHeadTransform(Transform headTransform)` | 頭ボーン参照`head`を差し替えるだけ。 |
| `searchHead()` | `animator`からHeadボーンを取得して`head`に設定し、コンポーネントを更新する。 |
| `setCameraBodyWeightValue(float newValue)` | `cameraBodyWeightTarget`を設定するだけ。 |
| `setOriginalCameraBodyWeightValue()` | `cameraBodyWeightTarget`を保存済みの初期値へ戻すだけ。 |
| `getHeadTrackTargetTransform()` | `headTrackTargeTransform`を返すだけ。 |
| `getHeadTrackTargetParent()` | `headTrackTargetParent`を返すだけ。 |
| `getOriginalHeadTrackTargetPosition()` | `originalHeadTrackTargetTransformPosition`を返すだけ。 |
| `setHeadTrackEnabledState(bool state)` | `headTrackEnabled`を設定するだけ。 |
| `setOriginalHeadTrackEnabledState()` | `headTrackEnabled`を保存済みの初期値へ戻すだけ。 |
| `isHeadTrackEnabled()` | `headTrackEnabled`を返すだけ。 |
| `setHeadTrackActiveWhileAimingState(bool state)` | `headTrackActiveWhileAiming`を設定するだけ。 |
| `setHeadWeight(float newValue)` | 頭の重み`headWeight`を設定するだけ。 |
| `setBodyWeight(float newValue)` | 体の重み`bodyWeight`を設定するだけ。 |
| `setLookInOppositeDirectionOutOfRangeValue(bool state)` | `lookInOppositeDirectionOutOfRange`を設定するだけ。 |
| `setOriginalLookInOppositeDirectionOutOfRangeValue()` | `lookInOppositeDirectionOutOfRange`を保存済みの初期値へ戻すだけ。 |
| `setNewCameraTargetToLook(Transform newCameraTargetToLook)` | `newCameraTargetToLook`がnullでなければ`cameraTargetToLook`を差し替える。 |
| `setNewCameraTargetToLookAndAdjustDirectionToPrevious(Transform newCameraTargetToLook)` | 新ターゲットに旧ターゲットの位置と回転を引き継がせてから`cameraTargetToLook`を差し替える。 |
| `setCustomHeadTrackToLookInfoByName(string nameToSearch)` | 一覧から`nameToSearch`に一致する情報を探し、設定に応じて注視ターゲットを差し替える。 |
| `setOriginalCameraTargetToLook()` | 保存済みの`originalCameraTargetToLook`へ戻すだけ。 |
| `setHeadTrackEnabledStateFromEditor(bool state)` | `headTrackEnabled`を設定し、`updateComponent`で反映する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`を呼ぶだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`updateOnAnimatorIKState()`

</details>

## 内部型

- `customHeadTrackToLookInfo`（class）
