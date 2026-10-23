# closeCombatSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/closeCombatSystem.cs:7`
- **属性**: `System.Serializable`

**概要**: 近接コンボ攻撃の中核で、`combatTypeInfo` のコンボ進行、ダメージトリガーの有効化、攻撃入力・ガード・被弾イベントを制御する。攻撃の成否に応じてインデックスや待ち時間を更新し、`disableCombat` で戦闘状態を終了する。

**公式ドキュメント抜粋**（[Close Combat System](../../docs/player-controller-components/player-controller/close-combat-system.md)）

> It manages the close combat, usually configured as kicks and punches, managing the different attacks configured on it and the combo logic. It also manages the AI to trigger attacks on the AI characters.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Combat System Enabled | `combatSystemEnabled` | `bool` | – | 近接戦闘の有効無効。オフだと攻撃判定が通らず攻撃できない。 |
| Combat Type ID | `combatTypeID` | `int` | 0 | 使用する`combatTypeInfo`を選ぶID。攻撃リストの切替に使う。 |
| Activate Close Combat System At Start | `activateCloseCombatSystemAtStart` | `bool` | – | 開始時に自動でコンバットモードへ入るか。 |
| Use Delay To Reset Attack Index | `useDelayToResetAttackIndex` | `bool` | – | コンボ終了後、攻撃インデックスのリセットを遅らせるか。 |
| Delay To Reset Attack Index | `delayToResetAttackIndex` | `float` | – | 攻撃インデックスを先頭へ戻すまでの遅延秒数。 / 表示条件: `useDelayToResetAttackIndex` がオンのとき |
| Use Attack Input Stack | `useAttackInputStack` | `bool` | – | 攻撃入力を溜めて順番に再生するか。 |
| Max Amount Of Attack Input Stack | `maxAmountOfAttackInputStack` | `int` | – | 攻撃入力スタックに溜められる最大数。 / 表示条件: `useAttackInputStack` がオンのとき |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Attacks Without Combat Active Enabled | `canUseAttacksWithoutCombatActiveEnabled` | `bool` | – | コンバットモード外でも単発攻撃を出せるようにするか。 |
| Hide Melee Weapons On External Combat | `hideMeleeWeaponsOnExternalCombat` | `bool` | true | 外部戦闘中に近接武器のメッシュを隠すか。 |
| Hide Fire Weapons On External Combat | `hideFireWeaponsOnExternalCombat` | `bool` | – | 外部戦闘中に遠距離武器のメッシュを隠すか。 |
| Ignore Parry On Perfect Block | `ignoreParryOnPerfectBlock` | `bool` | – | コンバットモード中は被弾側のパリィ判定を無効化するか。 |

### Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| General Attack Damage Multiplier | `generalAttackDamageMultiplier` | `float` | 1 | 全攻撃のダメージに掛ける倍率。 |
| Layer Mask To Damage | `layerMaskToDamage` | `LayerMask` | – | 攻撃判定が反応するレイヤー。当たり判定とサーフェス判定に使う。 |
| Place Trigger In Front Of Character On All Attacks | `placeTriggerInFrontOfCharacterOnAllAttacks` | `bool` | – | 全攻撃でダメージトリガーをキャラ前方に配置するか。 |
| Use Custom Ignore Tags | `useCustomIgnoreTags` | `bool` | – | タグ無視リストを当たり判定に適用するか。 / If this option is changed, used the button 'Update Hit Combat Triggers Info' to set the new value |
| Add Force Multiplier | `addForceMultiplier` | `float` | – | 攻撃時に相手へ加える力に掛ける倍率。 |
| Set Can Activate Reaction System Temporally State | `setCanActivateReactionSystemTemporallyState` | `bool` | – | 攻撃ごとにリアクションシステムの一時設定を上書きするか。 |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | 上書き後の値。オンなら攻撃中もリアクションを許可。 / 表示条件: `setCanActivateReactionSystemTemporallyState` がオンのとき |

### Get Health From Attacks And Block Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Get Health From Damaging Objects | `ignoreGetHealthFromDamagingObjects` | `bool` | true | ダメージを与えた相手から体力を回復する処理を無効にするか。 |
| Get Health From Blocks | `getHealthFromBlocks` | `bool` | – | ガード成功時に体力を回復するか。 |
| Health Amount From Blocks | `healthAmountFromBlocks` | `float` | 1 | ガード成功時に回復する体力量。 |
| Get Health From Perfect Blocks | `getHealthFromPerfectBlocks` | `bool` | – | パーフェクトガード時に体力を回復するか。 |
| Health Amount From Perfect Blocks | `healthAmountFromPerfectBlocks` | `float` | 1 | パーフェクトガード時に回復する体力量。 |

### Movement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Strafe Mode | `useStrafeMode` | `bool` | – | コンバットモード中にストレイフ移動へ切り替えるか。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Strafe ID Used | `strafeIDUsed` | `int` | – | ストレイフ切替時に使用するID。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Set Previous Strafe Mode On Disable Mode | `setPreviousStrafeModeOnDisableMode` | `bool` | – | モード解除時に以前のストレイフ状態へ戻すか。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Activate Strafe Mode On Lock On Target Active | `activateStrafeModeOnLockOnTargetActive` | `bool` | – | ロックオン中だけストレイフを有効にするか。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Toggle Strafe Mode If Running Active | `toggleStrafeModeIfRunningActive` | `bool` | – | 走り中はストレイフを無効にする連動を行うか。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Player On Ground To Activate Attack | `playerOnGroundToActivateAttack` | `bool` | true | 地上にいる時だけ攻撃を許可するか。オフなら空中攻撃も可。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Check External Controller Behavior Active List | `checkExternalControllerBehaviorActiveList` | `bool` | – | 外部コントローラのビヘイビア中も戦闘を許すかリストで判定する。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Combat Idle ID | `setCombatIdleID` | `bool` | – | コンバットモード中に専用の待機アニメIDへ切り替えるか。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Combat Idle ID | `combatIdleID` | `int` | 1 | コンバット待機に切り替えるアニメID値。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Set Combat Idle After First Attack | `setCombatIdleAfterFirstAttack` | `bool` | – | 最初の攻撃後にコンバット待機へ切り替えるか。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Set Regular Idle After Attack Active | `setRegularIdleAfterAttackActive` | `bool` | – | 攻撃終了後、通常の待機へ戻すか。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Min Wait To Set Regular Id After Attack Active | `minWaitToSetRegularIdAfterAttackActive` | `float` | – | 通常待機へ戻すまでの最小待ち時間（秒）。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue && setRegularIdleAfterAttackActive.boolValue` |
| Keep Combat Idle On FBA Active Enabled | `keepCombatIdleOnFBAActiveEnabled` | `bool` | true | FBA中もコンバット待機を維持するか。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Use Animation Percentage Duration | `useAnimationPercentageDuration` | `bool` | true | ダメージトリガーの発動をアニメ長の割合で指定するか。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |
| Use Animation Percentage Over100 | `useAnimationPercentageOver100` | `bool` | – | その割合を0〜100で指定するか。オフなら0〜1。 / 表示条件: `showAllSettings.boolValue \|\| showMovementSettings.boolValue` |

### Match Attack Position Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Match Target System On Attack | `useMatchTargetSystemOnAttack` | `bool` | – | 攻撃時にターゲットへ位置合わせするか。 / 表示条件: `showAllSettings.boolValue \|\| showMatchPositionSettings.boolValue` |
| Ignore Attack Setting To Match Target | `ignoreAttackSettingToMatchTarget` | `bool` | – | 攻撃側の設定を無視して常に位置合わせするか。 / 表示条件: `showAllSettings.boolValue \|\| showMatchPositionSettings.boolValue && useMatchTargetSystemOnAttack.boolValue` |
| Main Match Player To Target System | `mainMatchPlayerToTargetSystem` | `matchPlayerToTargetSystem` | – | 位置合わせを実行する`matchPlayerToTargetSystem`参照。 / 表示条件: `showAllSettings.boolValue \|\| showMatchPositionSettings.boolValue && useMatchTargetSystemOnAttack.boolValue` |
| Use Main Match Position Offset | `useMainMatchPositionOffset` | `bool` | – | 位置合わせ距離に共通オフセットを使うか。 / 表示条件: `showAllSettings.boolValue \|\| showMatchPositionSettings.boolValue && useMatchTargetSystemOnAttack.boolValue` |
| Main Match Position Offset | `mainMatchPositionOffset` | `float` | – | 共通で使う位置合わせのオフセット距離。 / 表示条件: `showAllSettings.boolValue \|\| showMatchPositionSettings.boolValue && useMatchTargetSystemOnAttack.boolValue` |

### Block Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Block Enabled | `blockEnabled` | `bool` | – | ガード機能の有効無効。オフだとガード入力が効かない。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue` |
| General Block Protection Multiplier | `generalBlockProtectionMultiplier` | `float` | 1 | ガード時のダメージ軽減量に掛ける倍率。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Cancel Block Reaction State Name | `cancelBlockReactionStateName` | `string` | "Disable Has Exit Time State" | ガードキャンセル時にオンにするAnimatorのbool名。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Main Melee Combat Block Input Name | `mainMeleeCombatBlockInputName` | `string` | "Block Attack" | ガードに使う入力アクション名。押下判定に使用。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Block Action Name | `blockActionName` | `string` | "Block Close Combat" | ガード中に登録するカスタムアクション名。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Block ID | `blockID` | `int` | – | ガード時に体力側へ渡す被弾リアクションID。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Block Active Previously | `blockActivePreviously` | `bool` | – | 攻撃でガードを解除した際、後で戻すための一時記録。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Use Max Block Range Angle | `useMaxBlockRangeAngle` | `bool` | – | ガード可能な角度制限を使うか。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Max Block Range Angle | `maxBlockRangeAngle` | `float` | – | ガードできる最大の角度（度）。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Block Damage Protection Amount | `blockDamageProtectionAmount` | `float` | – | ガード時に軽減するダメージ量。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Reduced Block Damage Protection Amount | `reducedBlockDamageProtectionAmount` | `float` | – | 軽減量が低下した状態のダメージ軽減量。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Reduced Block Damage Protection Active | `reducedBlockDamageProtectionActive` | `bool` | – | 軽減量の低いガード状態を使用中か。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Can Cancel Block To Start Attack Active | `canCancelBlockToStartAttackActive` | `bool` | – | ガード中に攻撃を始める際、ガード解除用boolを立てるか。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Block Input Paused | `blockInputPaused` | `bool` | – | ガード入力を一時停止するか。オンの間は開始できない。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Use Events On Block Damage | `useEventsOnBlockDamage` | `bool` | – | ガード開始・解除時にイベントを呼ぶか。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Event On Block Activate | `eventOnBlockActivate` | `UnityEvent` | – | ガード開始時に実行するイベント。 / 表示条件: `blockEnabled.boolValue && useEventsOnBlockDamage.boolValue` |
| Event On Block Deactivate | `eventOnBlockDeactivate` | `UnityEvent` | – | ガード解除時に実行するイベント。 / 表示条件: `blockEnabled.boolValue && useEventsOnBlockDamage.boolValue` |
| Use Events On Attack Cant Be Blocked | `useEventsOnAttackCantBeBlocked` | `bool` | – | ガード不能攻撃の時にイベントを呼ぶか。 / 表示条件: `showAllSettings.boolValue \|\| showBlockSettings.boolValue && blockEnabled.boolValue` |
| Event On Attack Cant Be Blocked | `eventOnAttackCantBeBlocked` | `UnityEvent` | – | ガード不能攻撃が当たった時に実行するイベント。 / 表示条件: `blockEnabled.boolValue && useEventsOnAttackCantBeBlocked.boolValue` |

### Surface Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Surface Info Enabled | `checkSurfaceInfoEnabled` | `bool` | true | 打撃サーフェス判定を行うか。オフなら音や演出を出さない。 / 表示条件: `showAllSettings.boolValue \|\| showSurfaceSettings.boolValue` |
| Surface Info On Melee Attack Name For Not Found | `surfaceInfoOnMeleeAttackNameForNotFound` | `string` | "Regular" | サーフェスを検出できなかった時に使うサーフェス名。 / 表示条件: `showAllSettings.boolValue \|\| showSurfaceSettings.boolValue && checkSurfaceInfoEnabled.boolValue` |
| Surface Info On Melee Attack Name For Swing On Air | `surfaceInfoOnMeleeAttackNameForSwingOnAir` | `string` | "Swing On Air" | 空振り時に再生するサーフェス名。 / 表示条件: `showAllSettings.boolValue \|\| showSurfaceSettings.boolValue && checkSurfaceInfoEnabled.boolValue` |

### Combat Limb List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Explanation | `explanation` | `string` | "Min Time To Play Next Attack field i… | 攻撃設定の説明文。表示用で動作には影響しない。 / 表示条件: `showAllSettings.boolValue \|\| showAttackListSettings.boolValue` / TextArea (3, 10) |

### Stamina Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Stamina On Attack Enabled | `useStaminaOnAttackEnabled` | `bool` | – | 攻撃時にスタミナを消費するか。 / 表示条件: `showAllSettings.boolValue \|\| showAttackListSettings.boolValue` |
| Attack Stamina State Name | `attackStaminaStateName` | `string` | "Close Combat" | 攻撃で消費するスタミナのステート名。 / 表示条件: `showAllSettings.boolValue \|\| showAttackListSettings.boolValue && useStaminaOnAttackEnabled.boolValue` |
| General Stamina Use Multiplier | `generalStaminaUseMultiplier` | `float` | 1 | 攻撃のスタミナ消費量に掛ける倍率。 / 表示条件: `showAllSettings.boolValue \|\| showAttackListSettings.boolValue && useStaminaOnAttackEnabled.boolValue` |
| Main Stamina System | `mainStaminaSystem` | `staminaSystem` | – | スタミナ消費を処理する`staminaSystem`参照。 / 表示条件: `showAllSettings.boolValue \|\| showAttackListSettings.boolValue && useStaminaOnAttackEnabled.boolValue` |

### Events Settings Close Combat

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | コンバットモード開始・終了時にイベントを呼ぶか。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue` |
| Even On State Enabled | `evenOnStateEnabled` | `UnityEvent` | – | コンバットモード開始時に実行するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue && useEventsOnStateChange.boolValue` |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | コンバットモード終了時に実行するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue && useEventsOnStateChange.boolValue` |

### Events Settings FBA

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On FBA View Change | `useEventOnFBAViewChange` | `bool` | – | FBAの切替時にイベントを呼ぶか。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue` |
| Event On Enable FBA | `eventOnEnableFBA` | `UnityEvent` | – | FBA有効時に実行するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue && useEventOnFBAViewChange.boolValue` |
| Event On Disable FBA | `eventOnDisableFBA` | `UnityEvent` | – | FBA無効時に実行するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventsSettings.boolValue && useEventOnFBAViewChange.boolValue` |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | 四肢の当たり判定位置のギズモを表示するか。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |
| Gizmo Color | `gizmoColor` | `Color` | – | 当たり判定位置に描く球ギズモの色。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue && showGizmo.boolValue` |
| Gizmo Radius | `gizmoRadius` | `float` | – | 当たり判定位置に描く球ギズモの半径。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue && showGizmo.boolValue` |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | シーンビューでギズモに添えるラベルの文字色。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue && showGizmo.boolValue` |

### Current State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | 攻撃処理のデバッグログを出力するか。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | プレイヤー本体の`playerController`参照。移動や状態制御に使う。 / 表示条件: `showComponents` がオンのとき |
| Animator | `animator` | `Animator` | – | 攻撃アニメ再生とAttack ID設定に使うAnimator。 / 表示条件: `showComponents` がオンのとき |
| Main Health | `mainHealth` | `healthManagement` | – | 体力管理。ガード軽減量や被弾リアクションIDを設定する。 / 表示条件: `showComponents` がオンのとき |
| Player Input | `playerInput` | `playerInputManager` | – | 入力参照。ガードキー押下や移動入力の判定に使う。 / 表示条件: `showComponents` がオンのとき |
| Hit Combat Prefab | `hitCombatPrefab` | `GameObject` | – | 四肢の当たり判定を生成する`hitCombat`プレハブ。 / 表示条件: `showComponents` がオンのとき |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | サーフェス別の打撃音を再生するAudioSource。 / 表示条件: `showComponents` がオンのとき |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | 攻撃中の頭部トラッキングを制御する`headTrack`参照。 / 表示条件: `showComponents` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `customTagsToIgnoreList` | `List<string>` | new List<string> () | Tags name list to be ignored by the damage of close combat of this character |
| `attackIDAnimatorName` | `string` | "Attack ID" | – |
| `combatTypeInfoList` | `List<combatTypeInfo>` | new List<combatTypeInfo> () | – |
| `combatLimbList` | `List<combatLimbInfo>` | new List<combatLimbInfo> () | – |
| `currentPlayerMode` | `bool` | – | – |
| `timerCombat` | `float` | 0 | – |
| `combatPlaying` | `bool` | – | – |
| `currentComboInProcessName` | `string` | – | – |
| `previousComboInProcessName` | `string` | – | – |
| `surfaceInfoOnMeleeAttackList` | `List<grabbedObjectMeleeAttackSystem.surfaceInfoOnMeleeAttack>` | new List<grabbedObjectMeleeAttackSyst… | – |
| `blockActive` | `bool` | – | – |
| `attackInputPaused` | `bool` | – | – |
| `attackInputPausedForStamina` | `bool` | – | – |
| `canMoveStatePaused` | `bool` | – | – |
| `rootMotionStateChanged` | `bool` | – | – |
| `headTrackStateChanged` | `bool` | – | – |
| `headTrackLookInOppositeDirectionStateChanged` | `bool` | – | – |
| `showMovementSettings` | `bool` | – | – |
| `showMatchPositionSettings` | `bool` | – | – |
| `showBlockSettings` | `bool` | – | – |
| `showSurfaceSettings` | `bool` | – | – |
| `showCombatLimbListSettings` | `bool` | – | – |
| `showAttackListSettings` | `bool` | – | – |
| `showEventsSettings` | `bool` | – | – |
| `showDebugSettings` | `bool` | – | – |
| `showAllSettings` | `bool` | – | – |
| `showComponents` | `bool` | – | – |
| `externalControllerBehaviorNameListToUseCloseCombat` | `List<string>` | – | – |
| `usingAttacksOnAir` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `disableCurrentAttackInProcess()` | `stopAllAttacks` を呼び、進行中の攻撃を停止するだけ。 |
| `canActivateAttack()` | 次の攻撃までの待ち時間が未設定か経過していれば `true` を返す判定。 |
| `useAttack(string attackName)` | `attackName` のコンボを進め、アニメ再生、遷移判定、移動・IK・重力制御、インデックス更新を行う。 |
| `getCombatTypeInfoByName(string comboName)` | 同 `combatTypeID` 内で `comboName` に一致する型情報を返し、無ければ `null`。 |
| `setAttackStartState(string attackName)` | 攻撃開始処理として開始イベント、対象リムの当たり判定有効化、位置合わせ、スタミナ消費を行う。 |
| `setGeneralStaminaUseMultiplierValue(float newValue)` | `generalStaminaUseMultiplier` を設定するだけ。 |
| `setAttackInputPausedForStaminaState(bool state)` | `attackInputPausedForStamina` を設定するだけ。 |
| `setAttackEndState(string attackName)` | 攻撃終了イベントを発火し、コンボ継続を判定して次攻撃の再生や戦闘終了を行う。 |
| `resetAttacksIndex(int combatTypeIndexToIgnore)` | 指定インデックス以外のコンボ進行を初期化し、他に攻撃が無ければタイマーも 0 にする。 |
| `setDamageDetectedOnTriggerById(int newId)` | `combatLimbList` の `newId` 番の攻撃情報から `checkEventOnDamage` を呼び出す。 |
| `checkEventOnDamage(int combatTypeIndex, int attackIndex, GameObject objectDetected, int combatLimbID)` | ダメージ時イベントとリモートイベントを送り、表面判定と体力回復を処理する。 |
| `resetAttackIdOnAnimator()` | `Attack ID` を 0 に戻すコルーチンを止めて再起動する。 |
| `callEventWithDelay(combatAttackInfo currentCombatAttackInfoEvent, bool playAtStart)` | 既存の遅延処理を止め、開始/終了どちらの遅延でも `eventOnAttackStart` を発火する。 |
| `activateNextAttackIgnoringWaitingTimes()` | 戦闘中なら待ち時間と入力スタックを無視して同コンボの次攻撃を実行する。 |
| `activateAttackWithoutCombatActive(string attackName)` | 一時的に戦闘モードへ入り `attackName` を実行し、失敗時は状態を戻す。 |
| `setCurrentPlayerMode(bool state)` | 戦闘モードを切り替え、トリガー・待機ID・ストレイフ・ガード・FBA・入力スタックを更新する。 |
| `resetIdleStateOnCloseCombat()` | 攻撃後に通常待機へ戻す設定なら、FBA 状態を考慮して待機 ID を 0 に戻す。 |
| `resetAttackInputStack()` | 攻撃入力スタックのリストと有効・完了フラグを初期化する。 |
| `enableOrDisableUseAttackInputStack(bool state)` | `useAttackInputStack` を設定するだけ。 |
| `checkEventsOnStateChange(bool state)` | `useEventsOnStateChange` が有効なら有効化/無効化イベントを発火する。 |
| `checkEventsOnFBAStateChange(bool state)` | FBA 切替イベント設定が有効なら有効/無効イベントを発火する。 |
| `isAttackInProcess()` | `combatPlaying` を返すだけ。 |
| `checkIfFullBodyAwarenessActive()` | 戦闘モード中に FBA 状態を取得し、変化時のみ内部状態を更新する。 |
| `stopActivateDamageTriggerCoroutine()` | `damageTriggerCoroutine` を停止するだけ。 |
| `enableOrDisableTriggers(bool value)` | 全 `combatLimbList` の `trigger` の `enabled` をまとめて設定する。 |
| `enableTriggersIfCombatModeActive()` | `currentPlayerMode` が true のときだけトリガーを有効化する。 |
| `stopCheckEventInfoList()` | `eventInfoListCoroutine` を停止するだけ。 |
| `checkEventInfoList(combatAttackInfo currentCombatAttackInfo)` | 既存のコルーチンを止め、イベント情報リストを遅延実行するコルーチンを開始する。 |
| `stopAllAttacks()` | 戦闘タイマーが残っていれば各コルーチンを止め、`disableCombat` で終了する。 |
| `checkLookAtTargetActiveState()` | ロックオン中なら設定に応じてストレイフモードを有効/無効にする。 |
| `checkLookAtTargetDeactivateState()` | 戦闘モード中ならストレイフモードを無効化するだけ。 |
| `inputAttack(string attackName)` | 入力停止中やスタミナ不足なら無視し、問題なければ `useAttack` を呼ぶ。 |
| `inputSetBlockState(bool state)` | `canUseCombat` を確認してから `setBlockStateWithoutInputCheck` に委譲する。 |
| `setBlockStateWithoutInputCheck(bool state)` | 入力判定を省いてガード状態を設定し、攻撃中はフラグだけ保持して後で再開する。 |
| `setBlockActiveState(bool state)` | ガードアクションと軽減量・角度・リアクションIDを設定し、ガードイベントを送る。 |
| `checkEventsOnBlockDamage(bool state)` | ガード開始/終了イベント設定が有効なら対応するイベントを発火する。 |
| `updateRegularBlockDamageProtectionValue()` | 通常のガード軽減値へ更新するだけ。 |
| `updateReducedBlockDamageProtectionValue()` | 軽減されたガード保護値へ更新するだけ。 |
| `setBlockDamageProtectionValue(bool state)` | 軽減フラグを設定し、ガード中なら体力側の保護量を即時更新する。 |
| `setMeleeAttackInputPausedState(bool state)` | `attackInputPaused` を設定するだけ。 |
| `disableMeleeAttackInputPausedStateWithDuration(float pauseDuration)` | 既存コルーチンを止め、`pauseDuration` 秒だけ攻撃入力を止めるコルーチンを開始する。 |
| `checkIfBlockActive()` | ガード中なら `setBlockActiveState(true)` を再適用するだけ。 |
| `disableBlockInputPausedStateWithDuration(float pauseDuration)` | 指定秒ガード入力を止め、直前までガード中なら 0.3 秒後に再開する。 |
| `setCanCancelBlockToStartAttackActiveState(bool state)` | `canCancelBlockToStartAttackActive` を設定するだけ。 |
| `checkIfBlockInputIsCurrentlyInUse()` | ガード入力を押していなければ `disableBlockStateInProcess` で解除する。 |
| `disableBlockStateInProcess()` | ガード中なら再開フラグを消して `setBlockActiveState(false)` を呼ぶ。 |
| `checkOnAttackBlocked()` | ガード中でブロック時回復が有効なら、最大体力未満のとき回復する。 |
| `checkOnAttackBlockedPerfectly()` | ガード中ならパーフェクトブロック時の回復設定に従い体力を回復する。 |
| `setNoDamageDetectedOnTriggerById(GameObject objectDetected)` | ダメージ無しとして `checkSurfaceFoundOnAttack` をリムID -1 で呼ぶ。 |
| `checkSurfaceFoundOnAttack(bool surfaceLocated, GameObject lastSurfaceDetected, int combatLimbID)` | レイキャストで表面名・位置・法線を求め、表面エフェクト処理へ渡す。 |
| `checkSurfaceFoundOnAttackToProcess(string surfaceName, bool surfaceLocated, Vector3 attackPosition, Vector3 attackNormal, bool ignoreBounceEvent)` | 表面名に一致する設定で効果音、バウンスイベント、パーティクルを再生する。 |
| `setCombatTypeID(int newValue)` | `combatTypeID` を設定するだけ。 |
| `getCombatTypeID()` | `combatTypeID` を返すだけ。 |
| `setNewParentForDamageTriggers(Transform newParent)` | 全ダメージトリガーを新しい親へ移し、位置を 0 にして kinematic 剛体を付ける。 |
| `setOriginalParentForDamageTriggers()` | 元の親・ローカル位置・半径へ戻し、追加した剛体を削除する。 |
| `setUseMatchTargetSystemOnAttackState(bool state)` | `useMatchTargetSystemOnAttack` を設定するだけ。 |
| `setOriginalUseMatchTargetSystemOnAttackState()` | 保存していた元のマッチターゲット設定へ戻すだけ。 |
| `setGeneralAttackDamageMultiplierValue(float newValue)` | `generalAttackDamageMultiplier` を設定するだけ。 |
| `generalAttackDamageMultiplierIncreaseStat(float extraValue)` | `generalAttackDamageMultiplier` に `extraValue` を加算するだけ。 |
| `initializeGeneralAttackDamageMultiplierStatAmount(float newValue)` | `generalAttackDamageMultiplier` を初期値として設定するだけ。 |
| `getGeneralAttackDamageMultiplierValue()` | `generalAttackDamageMultiplier` を返すだけ。 |
| `setPlaceTriggerInFrontOfCharacterOnAllAttacksState(bool state)` | `placeTriggerInFrontOfCharacterOnAllAttacks` を設定するだけ。 |
| `getCombatPrefabs(GameObject combatPrefab)` | `hitCombatPrefab` を差し替え、`updateComponent` でシーンを更新する。 |
| `addCombatPlace(string name, float hitDamage, GameObject limb, colliderPlace limbType)` | 新しいリム情報を作り、`hitCombat` とコライダーを紐付けてリストへ追加する。 |
| `assignBasicCombatTriggers()` | `hitCombatPrefab` から両手両足のトリガーを複製してリム情報を作り、設定を更新する。 |
| `udpateHitCombatInfo()` | 各リムの `hitCombat` に所有者・レイヤー・ダメージ・半径・元の親を再設定する。 |
| `updateHitCombatTriggerRadius(float newValue)` | 全リムの元半径を更新し、球/ボックスコライダーサイズへ反映する。 |
| `removeLimbParts()` | リムのオブジェクトと `hitCombat` を破棄し、リストを空にする。 |
| `enableOrDisableCloseCombatTriggers(bool state)` | 全リムの `hitCombat` のメインコライダーをまとめて有効/無効にする。 |
| `addOrRemoveObjectToIgnoreByHitTriggers(GameObject newObject, bool state)` | 全リムの `hitCombat` に無視対象の追加/削除を指示する。 |
| `enableOrDisableUseAttackInputStackFromEditor(bool state)` | 入力スタック設定を変更し、`updateComponent` でシーンを更新する。 |
| `setCustomIgnoreTagsForCharacterFromEditor()` | プレイヤーのタグを無視タグに設定し、シーンを更新する。 |
| `setUseMatchTargetSystemOnAttackStateFromEditor(bool state)` | マッチターゲット設定を変更し、`updateComponent` でシーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` とダーティシーン更新でエディタ表示を更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `evenOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
| `eventOnEnableFBA` | `UnityEvent` | – |
| `eventOnDisableFBA` | `UnityEvent` | – |
| `eventOnBlockActivate` | `UnityEvent` | – |
| `eventOnBlockDeactivate` | `UnityEvent` | – |
| `eventOnAttackCantBeBlocked` | `UnityEvent` | – |

## 内部型

- `colliderPlace`（enum）
- `combatLimbInfo`（class）
- `combatTypeInfo`（class）
- `combatAttackInfo`（class）
- `damageTriggerActiveInfo`（class）
- `eventInfo`（class）
