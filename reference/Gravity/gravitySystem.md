# gravitySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `gravityObjectManager`
- **ソース**: `Gravity/gravitySystem.cs:8`

**概要**: プレイヤーの重力方向・無重力モード・自由浮遊モードを管理する中核コンポーネント。サーフェス探索、重力パワー、零重力ルームとの連携、カメラやモデルの回転、イベント発火までを担う。

**公式ドキュメント抜粋**（[Gravity System](../../docs/player-controller-components/player-controller/gravity-system.md)）

> -Gravity System: used to manage the gravity control on the character

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Gravity Power Enabled | `gravityPowerEnabled` | `bool` | – | オンにすると重力パワーを起動できるようになる。 |
| Gravity Power Input Enabled | `gravityPowerInputEnabled` | `bool` | – | プレイヤーの入力で重力パワーを操作できるようにする。 |
| Lift To Search Enabled | `liftToSearchEnabled` | `bool` | – | オンにすると浮上してから再度押した時にサーフェスを探す。 |
| Random Rotation On Air Enabled | `randomRotationOnAirEnabled` | `bool` | – | 空中で方向選択中にモデルをランダムに回転させる。 |
| Layer | `layer` | `LayerMask` | – | サーフェス探索のレイキャストが対象とするレイヤー。 |
| Search Surface Speed | `searchSurfaceSpeed` | `float` | 5 | 重力でサーフェスを探して移動する時の速度の倍率。 |
| Air Control Speed | `airControlSpeed` | `float` | 5 | サーフェス探索中に入力で横移動する時の速度。 |
| Accelerate Speed | `accelerateSpeed` | `float` | 20 | 加速中に重力方向へ追加で加わる速度。 |
| High Gravity Multiplier | `highGravityMultiplier` | `float` | – | 加速中に一時的に適用される重力の倍率。 |
| Rotate To Surface Speed | `rotateToSurfaceSpeed` | `float` | 2 | サーフェスへ向きを回転させる時の補間速度。 |
| Rotate To Regular Gravity Speed | `rotateToRegularGravitySpeed` | `float` | 2 | 通常重力へ戻る時の回転の補間速度。 |
| Preserve Velocity When Disable Gravity Power | `preserveVelocityWhenDisableGravityPower` | `bool` | – | 重力パワー解除時に直前の速度を保持する。 |
| Raycast Distance To Check Below Player | `raycastDistanceToCheckBelowPlayer` | `float` | 10 | プレイヤー下方のサーフェスを調べるレイの距離。 |
| Use Infinite Raycast Distance To Check Below Player | `useInfiniteRaycastDistanceToCheckBelowPlayer` | `bool` | – | 真下を調べるレイを実質無限の距離で飛ばす。 |

### Other Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search New Surface On High Fall Speed | `searchNewSurfaceOnHighFallSpeed` | `bool` | true | 高速で落下した時に新しいサーフェスを自動で探す。 |
| Min Speed To Search New Surface | `minSpeedToSearchNewSurface` | `float` | 15 | 自動探索を始める落下速度のしきい値。 / 表示条件: `searchNewSurfaceOnHighFallSpeed` がオンのとき |
| Pause Search New Surface On High Fall Speed On Reverse Gravity Input | `pauseSearchNewSurfaceOnHighFallSpeedOnReverseGravityInput` | `bool` | true | 重力反転の入力時に高速落下の探索を止める。 / 表示条件: `searchNewSurfaceOnHighFallSpeed` がオンのとき |
| Shake Camera On High Fall Speed | `shakeCameraOnHighFallSpeed` | `bool` | true | 高速で落下している時にカメラを揺らす。 |
| Min Speed To Shake Camera | `minSpeedToShakeCamera` | `float` | 15 | カメラの揺れを始める落下速度のしきい値。 / 表示条件: `shakeCameraOnHighFallSpeed` がオンのとき |
| Check Surface Below On Regular State | `checkSurfaceBelowOnRegularState` | `bool` | – | 通常重力の時も足元のサーフェスを確認する。 |
| Time To Set Null Parent On Air | `timeToSetNullParentOnAir` | `float` | 0.5f | 足元の面を失ってから親を外すまでの秒数。 / 表示条件: `checkSurfaceBelowOnRegularState` がオンのとき |
| Stop Aim Mode When Searching Surface | `stopAimModeWhenSearchingSurface` | `bool` | – | サーフェス探索に入る時にエイムモードを解除する。 |
| Check Gravity Arrow State Active | `checkGravityArrowStateActive` | `bool` | true | 通常重力に戻った時に重力矢印を自動で消す。 |

### Hover Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hover Speed | `hoverSpeed` | `float` | – | ホバー中の上下動の速さを決める値。 |
| Hover Amount | `hoverAmount` | `float` | – | ホバーで上下に動く振幅の大きさ。 |
| Hover Smooth | `hoverSmooth` | `float` | – | ホバーで目標位置へ近づく時の滑らかさ。 |

### Current Normal Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Normal | `currentNormal` | `Vector3` | new Vector3 (0, 1, 0) | プレイヤーが現在立っている面の法線。 |

### Circumnavigation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Circumnavigate Rotation Speed | `circumnavigateRotationSpeed` | `float` | 10 | 球体などを周回する時の回転速度。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue` |
| Use Lerp Rotation | `useLerpRotation` | `bool` | – | 周回時の回転補間を`Lerp`で行う。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue` |
| Tag For Circumnavigate | `tagForCircumnavigate` | `string` | "sphere" | 周回できるサーフェスとして扱うタグ。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue` |
| Tag For Moving Objects | `tagForMovingObjects` | `string` | "moving" | プレイヤーを親子付けする移動オブジェクトのタグ。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue` |
| Check Circumnavigate Surface On Zero Gravity | `checkCircumnavigateSurfaceOnZeroGravity` | `bool` | true | 無重力モードでも周回サーフェスの判定を行う。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue` |
| Check Surface Below Ledge | `checkSurfaceBelowLedge` | `bool` | – | 足場の縁の下にあるサーフェスも探す。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue` |
| Surface Below Ledge Raycast Distance | `surfaceBelowLedgeRaycastDistance` | `float` | 3 | 縁の下を調べるレイが届く距離。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue && checkSurfaceBelowLedge.boolValue` |
| Below Ledge Rotation Speed | `belowLedgeRotationSpeed` | `float` | 10 | 縁の下のサーフェスへ回転する時の速度。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue && checkSurfaceBelowLedge.boolValue` |
| Surface Below Raycast Transform | `surfaceBelowRaycastTransform` | `Transform` | – | 縁の下を調べるレイの開始位置。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue && checkSurfaceBelowLedge.boolValue` |
| Check Surface In Front | `checkSurfaceInFront` | `bool` | – | 進行方向の前方にあるサーフェスも探す。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue` |
| Surface In Front Raycast Distance | `surfaceInFrontRaycastDistance` | `float` | 0.5f | 前方のサーフェスを調べるレイの距離。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue && checkSurfaceInFront.boolValue` |
| Surface In Front Rotation Speed | `surfaceInFrontRotationSpeed` | `float` | 10 | 前方のサーフェスへ回転する時の速度。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue && checkSurfaceInFront.boolValue` |
| Surface In Front Raycast Transform | `surfaceInFrontRaycastTransform` | `Transform` | – | 前方のサーフェスを調べるレイの開始位置。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue && checkSurfaceInFront.boolValue` |
| Gravity Adherence Raycast Parent | `gravityAdherenceRaycastParent` | `Transform` | – | 入力方向に合わせて回してレイの向きを決める親。 / 表示条件: `showAllSettings.boolValue \|\| showCircumnavigationhSettings.boolValue` |

### Events On Use Gravity Power Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Use Gravity Power State Change | `useEventsOnUseGravityPowerStateChange` | `bool` | – | 重力パワーの使用状態が変わった時にイベントを呼ぶ。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue` |
| Events On Use Gravity Power State Enabled | `eventsOnUseGravityPowerStateEnabled` | `UnityEvent` | – | 重力パワーの使用開始時に呼ぶイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue && useEventsOnUseGravityPowerStateChange.boolValue` |
| Events On Use Gravity Power State Disabled | `eventsOnUseGravityPowerStateDisabled` | `UnityEvent` | – | 重力パワーの使用終了時に呼ぶイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue && useEventsOnUseGravityPowerStateChange.boolValue` |

### Zero Gravity Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start With Zero Gravity Mode | `startWithZeroGravityMode` | `bool` | – | シーン開始時から無重力モードにする。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue` |
| Can Reset Rotation On Zero Gravity Mode | `canResetRotationOnZeroGravityMode` | `bool` | – | 無重力中に回転リセットの入力を使えるようにする。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue` |
| Can Adjust To Forward Surface | `canAdjustToForwardSurface` | `bool` | – | 無重力中に前方のサーフェスへ移動できるようにする。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue` |
| Forward Surface Ray Position | `forwardSurfaceRayPosition` | `Transform` | – | 前方のサーフェスを調べるレイの位置。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue && canAdjustToForwardSurface.boolValue` |
| Max Distance To Adjust | `maxDistanceToAdjust` | `float` | – | 前方のサーフェスへ移動できる最大距離。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue && canAdjustToForwardSurface.boolValue` |
| Reset Rotation Zero Gravity Speed | `resetRotationZeroGravitySpeed` | `float` | – | 無重力での回転リセットの補間速度。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue && canAdjustToForwardSurface.boolValue` |
| Adjust To Forward Surface Speed | `adjustToForwardSurfaceSpeed` | `float` | – | 前方のサーフェスへテレポートする速度。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue && canAdjustToForwardSurface.boolValue` |
| Set On Ground State On Teleport To Surface On Zero Gravity | `setOnGroundStateOnTeleportToSurfaceOnZeroGravity` | `bool` | – | テレポート後に接地状態として扱う。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue` |
| Use Custom Direction On Reset Zero Gravity Rotation | `useCustomDirectionOnResetZeroGravityRotation` | `bool` | – | 回転リセットの目標をカスタム方向にする。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue` |
| Custom Direction On Reset Zero Gravity Rotation | `customDirectionOnResetZeroGravityRotation` | `Vector3` | – | 回転リセットで向くカスタム方向のベクトル。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue && useCustomDirectionOnResetZeroGravityRotation.boolValue` |
| Use Events On Zero Gravity Mode State Change | `useEventsOnZeroGravityModeStateChange` | `bool` | – | 無重力モードの切替時にイベントを呼ぶ。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue` |
| Even On Zero Gravity Mode State Enabled | `evenOnZeroGravityModeStateEnabled` | `UnityEvent` | – | 無重力モードの開始時に呼ぶイベント。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue && useEventsOnZeroGravityModeStateChange.boolValue` |
| Event On Zero Gravity Mode State Disabled | `eventOnZeroGravityModeStateDisabled` | `UnityEvent` | – | 無重力モードの終了時に呼ぶイベント。 / 表示条件: `showAllSettings.boolValue \|\| showZeroGravitySettings.boolValue && useEventsOnZeroGravityModeStateChange.boolValue` |

### Free Floating Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Activate Free Floating Mode | `canActivateFreeFloatingMode` | `bool` | – | 自由浮遊モードを許可するフラグ。 / 表示条件: `showAllSettings.boolValue \|\| showFreeFloatingModeSettings.boolValue` |
| Use Events On Free Floating Mode State Change | `useEventsOnFreeFloatingModeStateChange` | `bool` | – | 自由浮遊モードの切替時にイベントを呼ぶ。 / 表示条件: `showAllSettings.boolValue \|\| showFreeFloatingModeSettings.boolValue` |
| Even On Free Floating Mode State Enabled | `evenOnFreeFloatingModeStateEnabled` | `UnityEvent` | – | 自由浮遊モードの開始時に呼ぶイベント。 / 表示条件: `showAllSettings.boolValue \|\| showFreeFloatingModeSettings.boolValue && useEventsOnFreeFloatingModeStateChange.boolValue` |
| Event On Free Floating Mode State Disabled | `eventOnFreeFloatingModeStateDisabled` | `UnityEvent` | – | 自由浮遊モードの終了時に呼ぶイベント。 / 表示条件: `showAllSettings.boolValue \|\| showFreeFloatingModeSettings.boolValue && useEventsOnFreeFloatingModeStateChange.boolValue` |

### New Gravity At Start Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start With New Gravity | `startWithNewGravity` | `bool` | – | 開始時に`newGravityToStart`の重力へ切り替える。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Use Player Rotation | `usePlayerRotation` | `bool` | – | 開始重力をプレイヤーの向きから決める。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue && startWithNewGravity.boolValue` |
| Adjust Rotation To Surface Found | `adjustRotationToSurfaceFound` | `bool` | – | 開始時に足元の面の法線へ向きを合わせる。 / 表示条件: `startWithNewGravity.boolValue && usePlayerRotation.boolValue` |
| New Gravity To Start | `newGravityToStart` | `Vector3` | – | 開始時に設定する新しい重力方向。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue && startWithNewGravity.boolValue` |

### Gravity Color Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Model Color | `changeModelColor` | `bool` | – | 重力パワー使用中にモデルの色を変える。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Power Color | `powerColor` | `Color` | – | 重力パワー使用中にモデルへ適用する色。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue && changeModelColor.boolValue` |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | AIが操作するキャラクターとして扱う。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | 処理のデバッグログをコンソールへ出力する。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューにデバッグ用のギズモを描く。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |
| Debug Gravity Direction | `debugGravityDirection` | `Vector3` | – | ギズモ表示に使う重力方向の値。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |

### Player Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Camera Game Object | `playerCameraGameObject` | `GameObject` | – | プレイヤーカメラのオブジェクト参照。 / 表示条件: `showComponents` がオンのとき |
| Pivot Camera Transform | `pivotCameraTransform` | `Transform` | – | カメラのピボットTransform参照。 / 表示条件: `showComponents` がオンのとき |
| Gravity Center Collider | `gravityCenterCollider` | `SphereCollider` | – | サーフェス探索に使う重力中心の球コライダー。 / 表示条件: `showComponents` がオンのとき |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | プレイヤー制御コンポーネントの参照。 / 表示条件: `showComponents` がオンのとき |
| Powers | `powers` | `otherPowers` | – | パワー管理コンポーネントの参照。 / 表示条件: `showComponents` がオンのとき |
| Player Collider | `playerCollider` | `CapsuleCollider` | – | プレイヤーのカプセルコライダー参照。 / 表示条件: `showComponents` がオンのとき |
| Player Input | `playerInput` | `playerInputManager` | – | 入力軸を取得するプレイヤー入力管理の参照。 / 表示条件: `showComponents` がオンのとき |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | 武器状態を問い合わせる武器管理の参照。 / 表示条件: `showComponents` がオンのとき |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | 移動に使うプレイヤーの`Rigidbody`参照。 / 表示条件: `showComponents` がオンのとき |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | カメラ制御コンポーネントの参照。 / 表示条件: `showComponents` がオンのとき |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | メインカメラのTransform参照。 / 表示条件: `showComponents` がオンのとき |

### Gravity Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Gravity Center | `gravityCenter` | `Transform` | – | 回転させるモデル中心のTransform参照。 / 表示条件: `showComponents` がオンのとき |
| Cursor | `cursor` | `GameObject` | – | 方向選択中に画面へ出すカーソルのオブジェクト。 / 表示条件: `showComponents` がオンのとき |
| Arrow | `arrow` | `GameObject` | – | 重力方向を示す矢印のオブジェクト参照。 / 表示条件: `showComponents` がオンのとき |
| Player Renderer | `playerRenderer` | `Renderer` | – | 色変更の対象になるプレイヤーの描画参照。 / 表示条件: `showComponents` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `materialToChange` | `List<bool>` | new List<bool> () | – |
| `powerActivated` | `bool` | – | – |
| `recalculatingSurface` | `bool` | – | – |
| `searchingSurface` | `bool` | – | – |
| `searchingNewSurfaceBelow` | `bool` | – | – |
| `searchAround` | `bool` | – | – |
| `dead` | `bool` | – | – |
| `firstPersonView` | `bool` | – | – |
| `regularGravity` | `Vector3` | new Vector3 (0, 1, 0) | – |
| `gravityPowerActive` | `bool` | – | – |
| `zeroGravityModeOn` | `bool` | – | – |
| `freeFloatingModeOn` | `bool` | – | – |
| `circumnavigateCurrentSurfaceActive` | `bool` | – | – |
| `hovering` | `bool` | – | – |
| `turning` | `bool` | – | – |
| `updateCurrentNormalByExternalTransformActive` | `bool` | – | – |
| `allowCircumnavigationOnAllSurfacesWithIgnoretagList` | `bool` | – | – |
| `circumnavigationOnAllSurfacesWithIgnoretagList` | `List<string>` | new List<string> () | – |
| `choosingDirection` | `bool` | – | – |
| `currentSetGravityManager` | `setGravity` | – | – |
| `showCircumnavigationhSettings` | `bool` | – | – |
| `showZeroGravitySettings` | `bool` | – | – |
| `showFreeFloatingModeSettings` | `bool` | – | – |
| `showEventsSettings` | `bool` | – | – |
| `showOtherSettings` | `bool` | – | – |
| `showDebugSettings` | `bool` | – | – |
| `showAllSettings` | `bool` | – | – |
| `showComponents` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setAllowCircumnavigationOnAllSurfacesWithIgnoretagListState(bool state)` | 無視タグリスト以外の全サーフェスを周回可能にするフラグを設定するだけ。 |
| `setCircumnavigationOnAllSurfacesWithIgnoretagList(List<string> newList)` | 周回を許可しないタグのリストを設定し、空でなければ有効フラグを立てる。 |
| `setUpdateCurrentNormalByExternalTransformState(bool state, Transform newTransform, bool ignoreRecalculateSurfaceValue)` | 外部Transformの上方向を法線として使い続ける状態を切替え、解除時は`regularGravity`に近ければ現在法線へ反映する。 |
| `setIgnoreRecalculateSurfaceState(bool state)` | サーフェス再計算を無視するフラグを設定するだけ。 |
| `checkOnGroundOrAirState()` | プレイヤーの接地判定を取得して`onGroundOrOnAir`へ渡し、接地時はカメラ揺れ停止や法線再計算の状態を更新する。 |
| `activateGravityPower()` | 重力パワーを有効にし、設定に応じて浮上・空中停止かカメラ前方へのサーフェス探索を始める。 |
| `deactivateGravityPower()` | 重力パワーを解除し、法線が`regularGravity`と異なれば通常重力へ回転、速度保持や色・カメラ設定も戻す。 |
| `checkKeepWeapons()` | 3人称で武器を構えている場合に武器の保持状態を確認させる。 |
| `checkKeepPower()` | 3人称でパワーの照準中なら`deactivateAimMode`で照準を解除する。 |
| `changeMovementVelocity(bool value)` | エア移動の加速状態を切替え、加速時はカメラFOV・重力倍率・カメラ揺れを強める。 |
| `addParent(GameObject obj)` | 移動オブジェクトを親にして一緒に動くようにし、回転中は`externalGravityCenter`側を親にする。 |
| `removeParent()` | 親を解除して自由に動けるようにし、回転中は`externalGravityCenter`を親に戻す。 |
| `setExternalGravityCenterAsParent()` | `externalGravityCenter`をプレイヤーとカメラの親に設定するだけ。 |
| `setFatherDetectedAsParent()` | 検出済みの`fatherDetected`をプレイヤーとカメラの親に設定する。 |
| `setNullParent()` | プレイヤーとカメラの親を`null`にする。 |
| `setNewParent(Transform newParent)` | プレイヤーとカメラのTransformの親を指定Transform(`null`可)に設定する。 |
| `setCorrectParent()` | 親に追従中なら`fatherDetected`、そうでなければ`null`を親に設定し直す。 |
| `changeCameraView(bool state)` | 一人称視点フラグを設定し、一人称時は重力矢印を非表示にする。 |
| `canRotatePlayer()` | サーフェス探索中にプレイヤーを回転してよいか、武器やパワーの照準状態から判定して返す。 |
| `changeOnTrigger(Vector3 dir, Vector3 right)` | トリガーから重力方向と右軸を渡してサーフェス探索を開始し、色変更やカメラ揺れも有効にする。 |
| `stopGravityPower()` | 車両搭乗時などに重力パワーを停止し、回転・速度・カメラ状態を通常へ戻す。 |
| `checkRotateToSurface(Vector3 normal, float rotSpeed)` | 既存の回転コルーチンを止めて、指定法線へプレイヤーを回す`rotateToSurface`を開始する。 |
| `stopRotateToSurfaceCoroutine()` | サーフェス回転コルーチンを停止する。 |
| `rotateToSurface(Vector3 normal, float rotSpeed)` | `externalGravityCenter`を親にしてプレイヤーとカメラを指定法線へ補間回転し、速度保持や接地判定まで行う。 |
| `isCharacterRotatingToSurface()` | サーフェスへ回転中かどうかを返す。 |
| `checkRotateToSurfaceWithoutParent(Vector3 normal, float rotSpeed)` | 親を使わない回転コルーチンを停止してから開始する。 |
| `stopRotateToSurfaceWithOutParentCoroutine()` | 親なしサーフェス回転コルーチンを停止する。 |
| `rotateToSurfaceWithOutParent(Vector3 normal, float rotSpeed)` | 親を付けずにプレイヤー・カメラ・重力中心を指定法線へ補間回転し、速度保持時は2倍で復元する。 |
| `setNormal(Vector3 normal)` | 親を使わず即座にプレイヤーとカメラを法線へ向け、色と重力パワー状態を更新する。 |
| `setCurrentNormal(Vector3 newValue)` | 現在の法線`currentNormal`を設定するだけ。 |
| `getRegularGravity()` | 通常重力の法線`regularGravity`を返す。 |
| `updateCurrentRotatingNormal(Vector3 newNormal)` | 回転用の法線`currentRotatingNormal`を更新するだけ。 |
| `getCurrentRotatingNormal()` | 回転用の法線を返す。 |
| `checkRotateCharacter(Vector3 normal)` | 角度差があるか通常重力なら、メッシュ回転コルーチンを止めて開始する。 |
| `rotateCharacter(Vector3 normal)` | 重力中心(メッシュ)を法線方向へ補間回転し、零ベクトルなら通常の向きへ戻す。 |
| `changeGravityDirectionDirectlyInvertedValue(Vector3 gravityDirection, bool preserveVelocity)` | 渡された方向を反転して`changeGravityDirectionDirectly`を呼ぶ。 |
| `changeGravityDirectionDirectly(Vector3 gravityDirection, bool preserveVelocity)` | 回転中でなければ速度を止めて指定法線へ直接回転させ、色とパワー状態を更新する。 |
| `setCurrentSetGravityManager(setGravity currentSetGravity)` | 使用中の`setGravity`を記録し、nullでないかのフラグも更新する。 |
| `setCurrentGravityCenterPoint(Transform newTransform)` | 重力中心点のTransformを設定し、nullでないかのフラグも更新する。 |
| `getCurrentSetGravityManager()` | 現在使用中の`setGravity`を返す。 |
| `changeColor(bool state)` | `changeModelColor`が有効なら色変更コルーチンを開始する。 |
| `changeColorCoroutine(bool value)` | パワー色か白へ、対象マテリアルの`_Color`を補間して変更する。 |
| `setMeshCharacter(SkinnedMeshRenderer currentMeshCharacter)` | キャラクターのRendererを差し替えてコンポーネントを更新する。 |
| `death(bool state)` | 死亡フラグを設定し、死亡時は重力パワー解除・ホバー停止・メッシュ回転リセットを行う。 |
| `setGravityArrow(GameObject obj)` | 重力矢印オブジェクトを設定するだけ。 |
| `setGravityArrowState(bool state)` | 重力矢印の表示を切替え、状態フラグも更新する。 |
| `setFirstPersonView(bool state)` | 一人称視点フラグを設定するだけ。 |
| `isCurcumnavigating()` | 周回可能なサーフェスを検出中か返す。 |
| `isGravityPowerActive()` | 重力パワーが有効か返す。 |
| `startOverride()` | 上書き開始として`usedByAI`をfalseにする。 |
| `stopOverride()` | `overrideTurretControlState(false)`で`usedByAI`をtrueに戻す。 |
| `overrideTurretControlState(bool state)` | `usedByAI`を`state`の否定に設定するだけ。 |
| `isZeroGravityModeOn()` | 無重力モードが有効か返す。 |
| `toggleZeroGravityModeOnState()` | 無重力モードのオン/オフを反転する。 |
| `setZeroGravityModeOnState(bool state)` | 無重力モードを設定し、解除時は法線が通常と異なれば重力パワーを解除してイベントを発火する。 |
| `setZeroGravityModeOnStateWithOutRotation(bool state)` | 回転を伴わずに無重力モードを設定し、状態変化イベントのみ発火する。 |
| `disableFreeFloatingModeOnIfActive()` | 自由浮遊モードが有効なら解除する。 |
| `setfreeFloatingModeOnState(bool state)` | 無重力中や不可時は無視し、自由浮遊モードを設定してイベントを発火する。 |
| `checkEventsOnFreeFloatingModeStateChange(bool state)` | イベント有効時、状態に応じて自由浮遊モードのUnityEventを発火する。 |
| `checkEventsOnZeroGravityModeStateChange(bool state)` | イベント有効時、状態に応じて無重力モードのUnityEventを発火する。 |
| `checkEventsOnUseGravityPowerStateChange(bool state)` | イベント有効時、重力パワー使用状態のUnityEventを発火する。 |
| `setPowerActivateState(bool state)` | パワー起動フラグを設定し、重力パワー使用イベントを発火する。 |
| `changeFreeFloatingModeOnState()` | 自由浮遊モードのオン/オフを反転する。 |
| `setfreeFloatingModeOnStateWithDelay(float delayAmount, bool state)` | 既存の遅延コルーチンを止め、指定秒後に自由浮遊モードを設定するコルーチンを開始する。 |
| `stopSetfreeFloatingModeOnStateWithDelayCoroutine()` | 遅延設定コルーチンを停止する。 |
| `setfreeFloatingModeOnStateWithDelayCoroutine(float delayAmount, bool state)` | `delayAmount`秒待ってから自由浮遊モードを設定する。 |
| `setCanActivateFreeFloatingModeState(bool state)` | 自由浮遊モードを許可するフラグを設定するだけ。 |
| `rotateCharacterInZeroGravityMode(Vector3 normal, float rotSpeed)` | 既存の回転コルーチンを止め、無重力用の回転コルーチンを開始する。 |
| `rotateCharacterInZeroGravityModeCoroutine(Vector3 normal, float rotSpeed)` | カメラ基準でプレイヤーを法線へ補間回転し、重力中心も正立に戻す。 |
| `teleportPlayer(Vector3 teleportPosition, float teleportSpeed, Vector3 normal, float rotSpeed)` | 既存のテレポートを止め、指定位置・速度・法線でテレポートコルーチンを開始する。 |
| `stopTeleporting()` | テレポートコルーチンを止めてプレイヤー操作を戻す。 |
| `setPlayerControlState(bool state)` | プレイヤー操作を有効/無効にし、速度ゼロ化・物理マテリアル・接地判定の一時停止を切替える。 |
| `isTeleportInProcess()` | テレポート中か返す。 |
| `setGravityPowerEnabledState(bool state)` | 重力パワーを許可するフラグを設定するだけ。 |
| `setGravityPowerState(bool enablePower)` | 死亡・デバイス使用・無効時以外で、重力パワーの起動/解除を実行する。 |
| `disableGravityPowerIfOnAir()` | 方向選択中か探索中なら重力パワーを解除する。 |
| `enableCameraShake()` | カメラ揺れが許可されていれば揺れを開始し、状態を立てる。 |
| `disableCameraShake()` | 揺れ中かつ許可時のみカメラ揺れを止める。 |
| `setCameraShakeCanBeUsedState(bool state)` | カメラ揺れの可否を設定し、不可なら揺れを停止する。 |
| `setGravityPowerInputEnabledState(bool state)` | 重力パワー入力の有効フラグを設定するだけ。 |
| `inputSetGravityPowerState(bool enablePower)` | 入力が有効なら`setGravityPowerState`を呼ぶだけ。 |
| `inputChangeGravitySpeed(bool increaseSpeed)` | 死亡・デバイス使用・無効時以外で、加速の開始/停止を`changeMovementVelocity`へ渡す。 |
| `inputAdjustToSurfaceOnZeroGravity()` | 無重力で空中・非回転時に前方レイキャストし、通常重力でなければヒット面へテレポートする。 |
| `setCustomDirectionOnResetZeroGravityRotationValue(Vector3 newValue)` | 零重力回転リセット時のカスタム方向を設定するだけ。 |
| `setCustomDirectionOnResetZeroGravityRotationValue(Transform newTransform)` | Transformの上方向をカスタム方向として設定する。 |
| `inputResetRotationOnZeroGravity()` | 無重力で空中・非回転時、通常重力かカスタム方向へキャラクターを回転させる。 |
| `inputToggleReverseGravity()` | 重力が通常でなければ解除、通常なら反転方向へ直接変更し、必要なら高速落下探索を止める。 |
| `setCurrentZeroGravityRoom(zeroGravityRoomSystem gravityRoom)` | 現在の無重力ルームを設定し、室内フラグを更新する。 |
| `isPlayerInsiderGravityRoom()` | プレイヤーが無重力ルーム内にいるか返す。 |
| `getCurrentZeroGravityRoom()` | 現在の無重力ルームを返す。 |
| `getCurrentSurfaceBelowPlayer()` | プレイヤー下のサーフェスTransformを返す。 |
| `addObjectToCurrentZeroGravityRoomSystem(GameObject objectToAdd)` | 無重力ルーム内なら、そのルームにオブジェクトを追加する。 |
| `setCircumnavigateSurfaceState(bool state)` | 周回フラグを設定し、解除時は周回検出や親を解除して再計算を止める。 |
| `setCheckSurfaceInFrontState(bool state)` | 前方サーフェス確認フラグを設定するだけ。 |
| `setCheckSurfaceBelowLedgeState(bool state)` | 下の縁確認フラグを設定するだけ。 |
| `setUsedByAIState(bool state)` | AI使用フラグ`usedByAI`を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `evenOnFreeFloatingModeStateEnabled` | `UnityEvent` | – |
| `eventOnFreeFloatingModeStateDisabled` | `UnityEvent` | – |
| `evenOnZeroGravityModeStateEnabled` | `UnityEvent` | – |
| `eventOnZeroGravityModeStateDisabled` | `UnityEvent` | – |
| `eventsOnUseGravityPowerStateEnabled` | `UnityEvent` | – |
| `eventsOnUseGravityPowerStateDisabled` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`getCurrentNormal()`, `getGravityCenter()`, `isPlayerSearchingGravitySurface()`, `isSearchingSurface()`, `isUsingRegularGravity()`, `onGroundOrOnAir(bool state)`

</details>
