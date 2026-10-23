# magicSpellActionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/magicSpellActionSystem.cs:6`

**概要**: 魔法スペルをリストで管理し、種類名やインデックスで選択して発動コルーチン・遠隔イベント・カスタムアクション・エナジー消費を実行する。魔法システムの開始/終了時にはストレイフモードやしゃがみ状態を保存・復元する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Magic System Enabled | `magicSystemEnabled` | `bool` | true | – |
| Reset Index If Not Attack After Delay | `resetIndexIfNotAttackAfterDelay` | `bool` | – | – |
| Delay To Reset Index After Attack | `delayToResetIndexAfterAttack` | `float` | – | – |
| General Energy Use Multiplier | `generalEnergyUseMultiplier` | `float` | 1 | – |

### Attack Selection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Attack Types | `useAttackTypes` | `bool` | – | – |
| Use Random Attack Index | `useRandomAttackIndex` | `bool` | – | – |
| Use Energy On Magic | `useEnergyOnMagic` | `bool` | – | – |
| Use Next Magic Spell On List For Next Attack Enabled | `useNextMagicSpellOnListForNextAttackEnabled` | `bool` | true | – |
| Avoid Activate Ability If Another In Process Enabled | `avoidActivateAbilityIfAnotherInProcessEnabled` | `bool` | true | – |

### Movement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Strafe Mode | `useStrafeMode` | `bool` | – | – |
| Strafe ID Used | `strafeIDUsed` | `int` | – | – |
| Set Previous Strafe Mode On Disable Magic System | `setPreviousStrafeModeOnDisableMagicSystem` | `bool` | – | – |
| Activate Strafe Mode On Lock On Target Active | `activateStrafeModeOnLockOnTargetActive` | `bool` | – | – |
| Deactivate Strafe Mode On Lock On Target Deactivate | `deactivateStrafeModeOnLockOnTargetDeactivate` | `bool` | – | – |
| Toggle Strafe Mode If Running Active | `toggleStrafeModeIfRunningActive` | `bool` | – | – |
| Set New Crouch ID | `setNewCrouchID` | `bool` | – | – |
| Crouch ID Used | `crouchIDUsed` | `int` | – | – |

### Magic Action List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Magic Spell Action Info List | `magicSpellActionInfoList` | `List<magicSpellActionInfo>` | new List<magicSpellActionInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Previous Strafe Mode | `previousStrafeMode` | `bool` | – | – |
| Previous Strafe ID | `previousStrafeID` | `int` | -1 | – |
| Magic System Active | `magicSystemActive` | `bool` | – | – |
| Current Attack Index | `currentAttackIndex` | `int` | – | – |
| Attack In Process | `attackInProcess` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Attack | `useEventsOnAttack` | `bool` | – | – |
| Event On Attack Start | `eventOnAttackStart` | `UnityEvent` | – | – |
| Event On Attack End | `eventOnAttackEnd` | `UnityEvent` | – | – |
| Use Events On Enable Disable Magic System | `useEventsOnEnableDisableMagicSystem` | `bool` | – | – |
| Event On Enable Magic System | `eventOnEnableMagicSystem` | `UnityEvent` | – | – |
| Event On Disable Magic System | `eventOnDisableMagicSystem` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Other Powers | `mainOtherPowers` | `otherPowers` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableMagicSystem(bool state)` | 魔法システムの有効状態を切り替え、イベントとパワーパネルを更新し、開始/終了時の構え処理を呼ぶ。 |
| `useMagicSpell(string magicTypeName)` | 入力可否と間隔を確認し、`magicTypeName`に合う有効な魔法を選んでエナジーを消費し発動コルーチンを開始する。 |
| `enableMagicByName(string magicName)` | `enableOrDisableMagicByName`で指定魔法を有効にするだけ。 |
| `disableMagicByName(string magicName)` | `enableOrDisableMagicByName`で指定魔法を無効にするだけ。 |
| `enableOrDisableMagicByName(string magicName, bool state)` | 名前が一致する魔法の`magicEnabled`を`state`に設定するだけ。 |
| `setNextAttackIndex()` | `currentAttackIndex`を次へ進め、末尾なら先頭へ戻す。ランダム設定時は乱数で選ぶ。 |
| `setPreviousAttackIndex()` | `currentAttackIndex`を1つ戻し、0以下なら末尾へ回す。ランダム設定時は乱数で選ぶ。 |
| `stopActivateMagicSpellAction()` | `magicCoroutine`があれば停止するだけ。 |
| `stopActivateMagicSpellEvent()` | `magicEventCoroutine`があれば停止するだけ。 |
| `resumeState()` | `attackInProcess`をfalseにして攻撃終了イベントを発火するだけ。 |
| `checkEventsOnAttack(bool state)` | `useEventsOnAttack`時、`state`に応じて開始/終了イベントを発火するだけ。 |
| `checkMagicStateAtStart()` | 現在のストレイフ状態を保存し、設定されたストレイフIDとしゃがみIDへ切り替える。 |
| `checkMagicStateAtEnd()` | 保存したストレイフ状態とIDへ戻し、しゃがみIDを0に戻して各種フラグを初期化する。 |
| `checkLookAtTargetActiveState()` | 魔法有効中にターゲット注視の有無を調べ、設定があればストレイフモードを切り替える。 |
| `checkLookAtTargetDeactivateState()` | `activateStrafeModeOnLockOnTargetActive`が有効ならストレイフモードを解除するだけ。 |
| `canUseInput()` | `playerIsBusy`がfalseならtrueを返すだけ。 |
| `playerIsBusy()` | デバイス使用中・サブメニュー・メニュー表示中ならtrue、ターン制戦闘中はfalseを返す。 |
| `checkEventsOnEnableDisableMagicSystem(bool state)` | 設定が有効なとき、`state`に応じて魔法システムの有効/無効イベントを発火する。 |
| `inputSetNextOrPreviousAttackIndex(bool useNextAttack)` | 魔法有効かつ入力可能なとき、`useNextAttack`に応じて次/前の攻撃インデックスへ動かす。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnAttackStart` | `UnityEvent` | – |
| `eventOnAttackEnd` | `UnityEvent` | – |
| `eventOnEnableMagicSystem` | `UnityEvent` | – |
| `eventOnDisableMagicSystem` | `UnityEvent` | – |

## 内部型

- `magicSpellActionInfo`（class）
