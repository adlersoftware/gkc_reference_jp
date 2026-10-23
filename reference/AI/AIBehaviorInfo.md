# AIBehaviorInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Custom AI Behavior/AI Behavior Info.cs:5`

**概要**: カスタムAI行動の基底クラスで、武器・攻撃・ターン制戦闘・乗り物などの状態変更を受け取る窓口を定義する。全メソッドは空の`virtual`で、実際の処理は派生コンポーネントが上書きして実装する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Behavior Enabled | `behaviorEnabled` | `bool` | true | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateAIBehavior()` | 空の`virtual`で、AI行動の有効化要求を受けるだけで何もしない。 |
| `deactivateAIBehavior()` | 空の`virtual`で、AI行動の無効化要求を受けるだけで何もしない。 |
| `updateAI()` | 空の`virtual`で、フレーム更新要求を受けるだけで何もしない。 |
| `updateAIBehaviorState(bool state)` | `state` を受けるだけの空`virtual`で、状態の保持も反映もしない。 |
| `updateAIAttackState(bool state)` | `state` を受けるだけの空`virtual`で、攻撃可否は変更しない。 |
| `updateInsideRangeDistance(bool state)` | `state` を受けるだけの空`virtual`で、射程内判定は変更しない。 |
| `updateAIBehaviorState()` | 引数なし版の空`virtual`で、行動状態の再更新要求を受けるだけ。 |
| `setDrawOrHolsterWeaponState(bool state)` | 武器の抜刀/納刀要求を受けるだけの空`virtual`。 |
| `setAimWeaponState(bool state)` | 武器の照準状態設定要求を受けるだけの空`virtual`。 |
| `setShootWeaponState(bool state)` | 射撃状態の設定要求を受けるだけの空`virtual`。 |
| `setHoldShootWeaponState(bool state)` | 射撃入力の保持要求を受けるだけの空`virtual`。 |
| `dropWeapon()` | 武器を落とす要求を受けるだけの空`virtual`で、実際の処理は持たない。 |
| `checkIfDrawWeaponsWhenResumingAI()` | AI再開時の武器抜刀確認要求を受けるだけの空`virtual`。 |
| `resetBehaviorStates()` | 行動状態のリセット要求を受けるだけの空`virtual`。 |
| `resetAttackState()` | 攻撃状態のリセット要求を受けるだけの空`virtual`。 |
| `stopAim()` | 照準停止の要求を受けるだけの空`virtual`。 |
| `disableOnSpottedState()` | 敵発見状態の無効化要求を受けるだけの空`virtual`。 |
| `updateWeaponsAvailableState()` | 武器の使用可否更新要求を受けるだけの空`virtual`。 |
| `setBehaviorStatesPausedState(bool state)` | 行動状態の一時停止要求を受けるだけの空`virtual`。 |
| `setSystemActiveState(bool state)` | システムの有効状態設定要求を受けるだけの空`virtual`。 |
| `carryingWeapon()` | 常に`false`を返すだけで、武器所持の判定は行わない。 |
| `updateIfCarryingWeapon()` | 武器所持状態の更新要求を受けるだけの空`virtual`。 |
| `setWaitToActivateAttackActiveState(bool state)` | 攻撃開始待ち状態の設定要求を受けるだけの空`virtual`。 |
| `setUseRandomWalkEnabledState(bool state)` | ランダム歩行の有効化要求を受けるだけの空`virtual`。 |
| `setOriginalUseRandomWalkEnabledState()` | ランダム歩行の設定を元に戻す要求を受けるだけの空`virtual`。 |
| `setIgnoreRandomWalkActiveState(bool state)` | ランダム歩行の無視状態設定要求を受けるだけの空`virtual`。 |
| `isAIBehaviorAttackInProcess()` | 常に`false`を返すだけで、攻撃処理中かは判定しない。 |
| `checkNoWeaponsAvailableState()` | 武器が無い状態の確認要求を受けるだけの空`virtual`。 |
| `checkIfDisableCurrentWeaponToChangeAttackMode(string newModeName)` | `newModeName` を受けるだけの空`virtual`で、武器の無効化はしない。 |
| `changeCurrentAttackMode(string newModeName)` | 攻撃モード変更要求を`newModeName` で受けるだけの空`virtual`。 |
| `setIsCurrentCharacterTurn(bool state)` | ターン制戦闘で自キャラの手番かを設定する要求を受けるだけの空`virtual`。 |
| `setAIOnPlayerTeamState(bool state)` | プレイヤー側チームかどうかの設定要求を受けるだけの空`virtual`。 |
| `setCurrentCharacterTurnTarget(GameObject newTarget)` | 手番の対象`newTarget` を受けるだけの空`virtual`。 |
| `stopCurrentAttackInProcess()` | 実行中の攻撃停止要求を受けるだけの空`virtual`。 |
| `setTurnBasedCombatActionActiveState(bool state)` | ターン制戦闘アクションの有効化要求を受けるだけの空`virtual`。 |
| `checkStateOnCharacterDead()` | 死亡時の状態確認要求を受けるだけの空`virtual`。 |
| `checkAIBehaviorStateOnCharacterSpawn()` | スポーン時の行動状態確認要求を受けるだけの空`virtual`。 |
| `checkAIBehaviorStateOnCharacterDespawn()` | デスポーン時の行動状態確認要求を受けるだけの空`virtual`。 |
| `stopAttackState()` | 攻撃状態の停止要求を受けるだけの空`virtual`。 |
| `setAttackEnabledState(bool state)` | 攻撃の有効化要求を受けるだけの空`virtual`。 |
| `setAttackEnabledStateFromEditor(bool state)` | エディタからの攻撃有効化要求を受けるだけの空`virtual`。 |
| `updateCurrentTargetSelectedInfo()` | 現在の対象情報の更新要求を受けるだけの空`virtual`。 |
| `updateAIPassengerBehavior()` | 車両同乗者の行動更新要求を受けるだけの空`virtual`。 |
| `getOffFromVehicle()` | 車両から降りる要求を受けるだけの空`virtual`。 |
| `removeStateOnVehicle()` | 車両乗車状態の解除要求を受けるだけの空`virtual`。 |
| `setAICharacterOnVehicle(GameObject newVehicle)` | 乗車車両`newVehicle` の設定要求を受けるだけの空`virtual`。 |
| `setCurrentPlayerControllerPartner(playerController newPlayerController)` | プレイヤーの相棒`newPlayerController` の設定要求を受けるだけの空`virtual`。 |
