# externalControllerBehavior

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Extra Movements/externalControllerBehavior.cs:5`

**概要**: フリークライムやスライドなど、通常移動とは別にプレイヤーを制御する「外部コントローラ」の基底クラス。既定実装はほぼ空で、派生クラスが各仮想メソッドを上書きして挙動を実装する。

## インスペクター設定

### Behavior Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Behavior Name | `behaviorName` | `string` | – | – |
| External Controller Jump Enabled | `externalControllerJumpEnabled` | `bool` | – | – |

### Disable Other Behaviors Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Be Activated If Others Behaviors Active | `canBeActivatedIfOthersBehaviorsActive` | `bool` | – | – |
| Disable All Others Behaviors On Active | `disableAllOthersBehaviorsOnActive` | `bool` | – | – |
| List Of Behavior To Disable On Active | `listOfBehaviorToDisableOnActive` | `List<string>` | new List<string> () | – |

### Action System Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Custom Action Category ID | `customActionCategoryID` | `int` | -1 | – |
| Regular Action Category ID | `regularActionCategoryID` | `int` | -1 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Behavior Currently Active | `behaviorCurrentlyActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateControllerBehavior()` | 中身が空の仮想メソッドで、派生クラスが毎フレームの挙動更新を実装するためのフック。 |
| `isCharacterOnGround()` | 常にfalseを返す仮想メソッドで、派生クラスが接地判定を上書きする。 |
| `isBehaviorActive()` | 常にfalseを返す仮想メソッドで、派生クラスが有効判定を上書きする。 |
| `setExternalForceActiveState(bool state)` | 中身が空の仮想メソッドで、派生クラスが外力の有効状態を実装する。 |
| `setExternalForceEnabledState(bool state)` | 中身が空の仮想メソッドで、派生クラスが外力の使用可否を実装する。 |
| `updateExternalForceActiveState(Vector3 forceDirection, float forceAmount)` | 中身が空の仮想メソッドで、派生クラスが外力の方向と強さの更新を実装する。 |
| `checkIfActivateExternalForce()` | 中身が空の仮想メソッドで、派生クラスが外力の起動判定を実装する。 |
| `setJumpActiveForExternalForce()` | 中身が空の仮想メソッドで、派生クラスが外力時のジャンプ処理を実装する。 |
| `setExtraImpulseForce(Vector3 forceAmount, bool useCameraDirection)` | 中身が空の仮想メソッドで、派生クラスが追加の力の適用を実装する。 |
| `disableExternalControllerState()` | 中身が空の仮想メソッドで、派生クラスが状態の無効化処理を実装する。 |
| `checkIfResumeExternalControllerState()` | 中身が空の仮想メソッドで、派生クラスが状態の再開処理を実装する。 |
| `checkIfCanEnableBehavior(string behaviorName)` | 名前が空か全無効設定ならtrue、それ以外は無効化対象リストに含まれるかで可否を返す。 |
| `setBehaviorCurrentlyActiveState(bool state)` | `behaviorCurrentlyActive` を設定するだけ。 |
| `isBehaviorCurrentlyActive()` | `behaviorCurrentlyActive` の値を返すだけ。 |
| `setCurrentPlayerActionSystemCustomActionCategoryID()` | 中身が空の仮想メソッドで、派生クラスがアクションカテゴリIDの設定を実装する。 |
| `checkPauseStateDuringExternalForceOrBehavior()` | 中身が空の仮想メソッドで、派生クラスが一時停止時の処理を実装する。 |
| `checkResumeStateAfterExternalForceOrBehavior()` | 中身が空の仮想メソッドで、派生クラスが再開時の処理を実装する。 |
| `checkChangeCameraViewStateOnExternalControllerBehavior()` | 中身が空の仮想メソッドで、派生クラスがカメラ視点の変更処理を実装する。 |
