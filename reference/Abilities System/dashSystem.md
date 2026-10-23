# dashSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/dashSystem.cs:6`

**概要**: 一人称と三人称それぞれのダッシュ設定（速度・継続時間・クールダウン・スタミナ消費・方向別イベント）を保持し、`dashInfo`単位でIDや一時停止状態を切り替える。実行時は入力方向やストレイフ状態からダッシュ方向を決めて移動とカメラを制御する。

**公式ドキュメント抜粋**（[Dash System](../../docs/player-controller-components/essential-components/dash-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dash Enabled | `dashEnabled` | `bool` | true | – |
| Max Time Between Input Press | `maxTimeBetweenInputPress` | `float` | – | – |
| Use Dash Cool Down | `useDashCoolDown` | `bool` | – | – |
| Dash Cool Down Time | `dashCoolDownTime` | `float` | – | – |
| Can Use Dash While Action Active | `canUseDashWhileActionActive` | `bool` | – | – |
| Action Category To Use Dash | `actionCategoryToUseDash` | `List<string>` | new List<string> () | – |

### Dash In First Person Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Dash On First Person | `useDashOnFirstPerson` | `bool` | true | – |
| Dash Duration | `dashDuration` | `float` | – | – |
| Dash Speed | `dashSpeed` | `float` | – | – |
| Dash Camera State | `dashCameraState` | `string` | – | – |
| Time To Disable Dash Camera | `timeToDisableDashCamera` | `float` | – | – |
| Only Dash On Ground | `onlyDashOnGround` | `bool` | – | – |
| Use Double Tap To Dash On First Person Enabled | `useDoubleTapToDashOnFirstPersonEnabled` | `bool` | – | – |

### Dash In Third Person Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Dash On Third Person | `useDashOnThirdPerson` | `bool` | – | – |

### Dash Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Dash ID | `currentDashID` | `int` | – | – |
| Dash Info List | `dashInfoList` | `List<dashInfo>` | new List<dashInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Dash Active | `dashActive` | `bool` | – | – |
| Dash Can Be Used Currently | `dashCanBeUsedCurrently` | `bool` | – | – |
| Dash On Third Person In Transition | `dashOnThirdPersonInTransition` | `bool` | – | – |
| Check Ground Paused | `checkGroundPaused` | `bool` | – | – |
| Override Strafe Mode Active State | `overrideStrafeModeActiveState` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Stamina System | `mainStaminaSystem` | `staminaSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkDoubleTapDash()` | `canUseDash`を満たすとき、一人称/三人称それぞれの二回タップ設定が有効なら`enableDashState`を呼ぶ。 |
| `enableDashState()` | ダッシュを開始し、一人称は速度とカメラ、三人称はスタミナ消費と方向別イベント、共通で移動方向を設定する。 |
| `setOverrideStrafeModeActiveStateResult(bool state)` | `overrideStrafeModeActiveState`に`state`を代入するだけ。 |
| `disableDashState()` | ダッシュを終了し、一人称なら入力上書きの解除、速度の復元、カメラ操作の有効化を行う。 |
| `setDashEnabledState(bool state)` | `dashEnabled`に`state`を代入するだけ。 |
| `inputActivateDashState()` | 有効かつ`canUseDash`を満たすときに`enableDashState`を呼ぶだけ。 |
| `activateDashStateWithoutGroundCheck()` | `checkGroundPaused`をtrueにして接地チェックを飛ばしてからダッシュを起動し、フラグを戻す。 |
| `setCheckGroundPausedState(bool state)` | `checkGroundPaused`に`state`を代入するだけ。 |
| `activateDashStateWithCustomDirection(Vector3 dashDirection)` | カスタム方向`dashDirection`を設定してから、通常のダッシュ起動処理を呼ぶ。 |
| `canUseDash()` | 移動可否、一人称/三人称の設定、クールダウン、接地、ポーズ状態を確認してダッシュ可能かを返す。 |
| `setUseDashOnFirstPersonState(bool state)` | `useDashOnFirstPerson`に`state`を代入するだけ。 |
| `setUseDashOnThirdPersonState(bool state)` | `useDashOnThirdPerson`に`state`を代入するだけ。 |
| `setDashOnThirdPersonInTransitionState(bool state)` | 遷移フラグを設定し、falseなら`disableDashState`でダッシュを終了する。 |
| `checkIfActionToUseOnDashIsOnCategoryList()` | 現在のアクションカテゴリが`actionCategoryToUseDash`に含まれるかを返すだけ。 |
| `setDashOnThirdPersonPausedState(bool state)` | `dashOnThirdPersonPaused`に`state`を代入するだけ。 |
| `setDashInfoOnThirdPersonPausedState(bool state, string dashInfoName)` | 名前が一致する`dashInfo`の`dashOnThirdPersonPaused`を設定するだけ。 |
| `pauseDashInfoOnThirdPerson(string dashInfoName)` | 指定名のダッシュ情報を一時停止にするだけ。 |
| `resumeDashInfoOnThirdPerson(string dashInfoName)` | 指定名のダッシュ情報の一時停止を解除するだけ。 |
| `setDashInfoOnThirdPersonPausedByStaminaState(bool state, string dashInfoName)` | `useStamina`が有効で名前が一致する`dashInfo`の停止フラグだけを設定する。 |
| `pauseByStaminaDashInfoOnThirdPerson(string dashInfoName)` | スタミナ使用ダッシュ情報を停止にするだけ。 |
| `resumeByStaminaDashInfoOnThirdPerson(string dashInfoName)` | スタミナ使用ダッシュ情報の停止を解除するだけ。 |
| `getCurrentDashID()` | `currentDashID`を返すだけ。 |
| `setCurrentDashID(int newValue)` | IDが一致する`dashInfo`を`currentDashInfo`に設定し、他の要素は`isCurrentState`をfalseにする。 |
| `setUseDashOnFirstPersonStateFromEditor(bool state)` | 一人称ダッシュ設定を変更してから`updateComponent`で反映する。 |
| `setUseDashOnThirdPersonStateFromEditor(bool state)` | 三人称ダッシュ設定を変更してから`updateComponent`で反映する。 |

## 内部型

- `thirdPersonStrafeDashDirection`（enum）
- `dashInfo`（class）
