# simpleStrafeAndAimState

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/simpleStrafeAndAimState.cs:5`

**概要**: ストレイフモードとエイム状態をまとめて切り替える補助コンポーネント。元のストレイフIDやカメラ状態を保存し、解除時に復元する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Simple Strafe And Aim Enabled | `simpleStrafeAndAimEnabled` | `bool` | true | – |

### Movement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Strafe Mode | `useStrafeMode` | `bool` | – | – |
| Strafe ID Used | `strafeIDUsed` | `int` | – | – |
| Set Previous Strafe Mode On Disable System | `setPreviousStrafeModeOnDisableSystem` | `bool` | – | – |
| Activate Strafe Mode On Lock On Target Active | `activateStrafeModeOnLockOnTargetActive` | `bool` | – | – |
| Toggle Strafe Mode If Running Active | `toggleStrafeModeIfRunningActive` | `bool` | – | – |
| Set New Crouch ID | `setNewCrouchID` | `bool` | – | – |
| Crouch ID Used | `crouchIDUsed` | `int` | – | – |

### Aim Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Aim State Enabled | `setAimStateEnabled` | `bool` | – | – |

### Third Person Camera State Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Camera State On Third Person | `setNewCameraStateOnThirdPerson` | `bool` | – | – |
| New Camera State On Third Person | `newCameraStateOnThirdPerson` | `string` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Simple Strafe And Aim Active | `simpleStrafeAndAimActive` | `bool` | – | – |
| Previous Strafe Mode | `previousStrafeMode` | `bool` | – | – |
| Previous Strafe ID | `previousStrafeID` | `int` | -1 | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setSimpleStrafeAndAimState(bool state)` | 有効時のみ、フルボディアウェアネス以外で状態を切り替えて `activateState` か `deactivateState` を呼ぶ。 |
| `activateState()` | 元のストレイフ設定を保存し、ストレイフ・エイム・カメラ状態を設定値に合わせて有効化する。 |
| `deactivateState()` | 保存したストレイフIDや移動設定を戻し、エイムとカメラ状態を元に復帰させる。 |
| `checkLookAtTargetActiveState()` | 状態が有効なら、対象を見ているかに応じてストレイフモードを切り替える。 |
| `checkLookAtTargetDeactivateState()` | 状態と `activateStrafeModeOnLockOnTargetActive` が有効ならストレイフモードを解除する。 |
