# health

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `healthManagement`
- **ソース**: `Health/health.cs:8`

**概要**: キャラクターや車両の体力を管理する`healthManagement`派生コンポーネントで、`healthAmount`の増減、シールド、弱点（部位）ごとのダメージ倍率、被弾・死亡・復活イベント、ヘルスバー表示、ラグドール連携をまとめて扱う。

**公式ドキュメント抜粋**（[Health](../../docs/player-controller-components/player-controller/health.md)）

> It is the main damage detection system, which can be configured on any object that can be damaged, including event options on death, damage, and other states. It has also options to use a shield to avoid damage and allows to detect damage on specific body parts of any object or character, like a hand, arms, chest, head, etc….triggering any event on each part as needed.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Health Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Invincible | `invincible` | `bool` | false | オンにすると被弾しても体力が一切減らない。 |
| Health Amount | `healthAmount` | `float` | 100 | ゲーム開始時点の現在体力の初期値。 / 表示条件: `invincible` がオフのとき |
| Max Health Amount | `maxHealthAmount` | `float` | 100 | 体力の上限値で、0なら`healthAmount`が代用される。 / 表示条件: `invincible` がオフのとき |

### Damage Multiplier Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| General Damage Multipler Enabled | `generalDamageMultiplerEnabled` | `bool` | true | ダメージ倍率機能を有効にするかの切替。 / 表示条件: `invincible` がオフのとき |
| General Damage Multipler Active | `generalDamageMultiplerActive` | `bool` | – | 倍率を実際にダメージへ適用するかの切替。 / 表示条件: `!invincible.boolValue && generalDamageMultiplerEnabled.boolValue` |
| General Damage Multiplier | `generalDamageMultiplier` | `float` | 1 | 受けるダメージに掛ける倍率の値。 / 表示条件: `!invincible.boolValue && generalDamageMultiplerEnabled.boolValue` |

### Regenerate Health Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regenerate Health | `regenerateHealth` | `bool` | – | 体力の自動回復を有効にするかの切替。 / 表示条件: `invincible` がオフのとき |
| Constant Regenerate | `constantRegenerate` | `bool` | – | 毎秒一定量を回復する連続回復モードの切替。 / 表示条件: `!invincible.boolValue && regenerateHealth.boolValue` |
| Regenerate Time | `regenerateTime` | `float` | – | 最後に被弾してから回復を始めるまでの秒数。 / 表示条件: `!invincible.boolValue && regenerateHealth.boolValue` |
| Regenerate Speed | `regenerateSpeed` | `float` | 0 | 連続回復時に1秒あたり回復する体力量。 / 表示条件: `regenerateHealth.boolValue && constantRegenerate.boolValue` |
| Regenerate Amount | `regenerateAmount` | `float` | – | 間欠回復時に1回で回復する体力量。 / 表示条件: `!invincible.boolValue && regenerateHealth.boolValue` |

### Main Shield Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Shield | `useShield` | `bool` | – | シールドシステムを併用するかの切替。 |
| Main Shield System | `mainShieldSystem` | `shieldSystem` | – | ダメージを肩代わりする`shieldSystem`の参照。 / 表示条件: `useShield` がオンのとき |

### Health Stat Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Stats Manager | `playerStatsManager` | `playerStatsSystem` | – | 体力値を同期させる`playerStatsSystem`の参照。 |
| Health Stat Name | `healthStatName` | `string` | "Current Health" | 現在体力を同期するステータス項目の名前。 |
| Max Health Stat Name | `maxHealthStatName` | `string` | "Max Health" | 最大体力を同期するステータス項目の名前。 |

### Damage Hit Reaction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Damage Hit Reaction | `useDamageHitReaction` | `bool` | – | 被弾時のヒットリアクションを有効にする切替。 |
| Send Damage To Reaction System If Shield System Active | `sendDamageToReactionSystemIfShieldSystemActive` | `bool` | – | シールドで防いだ分もリアクションへ送るかの切替。 |
| Main Damage Hit Reaction System | `mainDamageHitReactionSystem` | `damageHitReactionSystem` | – | ヒットリアクションを再生するシステムの参照。 |

### Block Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Damage Blocked | `useEventsOnDamageBlocked` | `bool` | – | ガードで軽減した時のイベント有効切替。 |
| Event On Damage Blocked | `eventOnDamageBlocked` | `eventParameters.eventToCallWithAmount` | – | ガード成功時に軽減後のダメージ量を渡すイベント。 / 表示条件: `useEventsOnDamageBlocked` がオンのとき |

### Others Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Is Character | `objectIsCharacter` | `bool` | true | `applyDamage`でキャラクター扱いと判定させる切替。 |
| Place To Shoot Active | `placeToShootActive` | `bool` | true | 射撃用の目印位置を自動生成するかの切替。 |
| Place To Shoot | `placeToShoot` | `Transform` | – | 敵の照準や死亡時の注視判定に使うTransform。 / 表示条件: `placeToShootActive` がオンのとき |
| Check Damage Receiver On Children Transform | `checkDamageReceiverOnChildrenTransform` | `bool` | – | 子階層の`characterDamageReceiver`を全て登録する切替。 |
| Damage Prefab | `damagePrefab` | `GameObject` | – | 被弾時に再生するダメージエフェクトのプレハブ。 |
| Main Manager Name | `mainManagerName` | `string` | "Health Bar Manager" | 体力バー管理システムを探す時のオブジェクト名。 |
| Send Info To Character Customization On Damage Enabled | `sendInfoToCharacterCustomizationOnDamageEnabled` | `bool` | – | 被弾時に防具耐久値をカスタマイズ側へ送る切替。 |
| Ignore Use Health Amount On Spot | `ignoreUseHealthAmountOnSpot` | `bool` | – | 弱点ごとに持つ残り体力を無視するかの切替。 |
| Use Custom Character Radius | `useCustomCharacterRadius` | `bool` | – | キャラクター半径を独自の値にするかの切替。 |
| Custom Character Radius | `customCharacterRadius` | `float` | – | AIなどが距離判定に使う独自のキャラクター半径。 / 表示条件: `useCustomCharacterRadius` がオンのとき |

### Impact Surface Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Impact Surface | `useImpactSurface` | `bool` | – | 被弾面デカールを個別設定で使うかの切替。 |
| Main Decal Manager Name | `mainDecalManagerName` | `string` | "Decal Manager" | `decalManager`を検索・生成する時の名前。 |

### Damage Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Damage Enabled | `useEventOnDamageEnabled` | `bool` | true | 被弾時のイベント呼び出しを有効にする切替。 / 表示条件: `showDamageDeadSettings` がオンのとき |
| Event On Damage | `eventOnDamage` | `UnityEvent` | new UnityEvent () | ダメージを受けた時に呼び出されるイベント。 / 表示条件: `showDamageDeadSettings.boolValue && useEventOnDamageEnabled.boolValue` |
| Use Event On Damage With Attacker | `useEventOnDamageWithAttacker` | `bool` | – | 攻撃者を渡す被弾イベントの有効切替。 / 表示条件: `showDamageDeadSettings` がオンのとき |
| Event On Damage With Attacker | `eventOnDamageWithAttacker` | `eventParameters.eventToCallWithGameObject` | – | 攻撃者オブジェクトを渡す被弾イベント。 / 表示条件: `showDamageDeadSettings.boolValue && useEventOnDamageWithAttacker.boolValue` |
| Use Event On Damage With Amount | `useEventOnDamageWithAmount` | `bool` | – | ダメージ量を渡す被弾イベントの有効切替。 / 表示条件: `showDamageDeadSettings` がオンのとき |
| Event On Damage With Amount | `eventOnDamageWithAmount` | `eventParameters.eventToCallWithAmount` | – | 最終的なダメージ量を渡す被弾イベント。 / 表示条件: `showDamageDeadSettings.boolValue && useEventOnDamageWithAmount.boolValue` |
| Use Event On Damage With Weak Spot Transform | `useEventOnDamageWithWeakSpotTransform` | `bool` | – | 弱点Transformを渡す被弾イベントの有効切替。 / 表示条件: `showDamageDeadSettings` がオンのとき |
| Event On Damage With Weak Spot Transform | `eventOnDamageWithWeakSpotTransform` | `eventParameters.eventToCallWithTransform` | – | 命中した弱点のTransformを渡すイベント。 / 表示条件: `showDamageDeadSettings.boolValue && useEventOnDamageWithWeakSpotTransform.boolValue` |

### Damage Extra Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Extra Damage Functions | `useExtraDamageFunctions` | `bool` | – | ダメージ量に応じた追加イベントの有効切替。 / 表示条件: `showDamageDeadSettings` がオンのとき |
| Event Damage Target Over Time Duration | `eventDamageTargetOverTimeDuration` | `eventParameters.eventToCallWithAmount` | – | 継続ダメージ開始時に継続秒数を渡すイベント。 / 表示条件: `showDamageDeadSettings` がオンのとき |

### Shield Damage Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Damage Shield | `useEventOnDamageShield` | `bool` | – | シールド被弾イベントの有効切替。 / 表示条件: `showDamageDeadSettings.boolValue && useShield.boolValue` |
| Event On Damage Shield | `eventOnDamageShield` | `UnityEvent` | – | シールドがダメージを受けた時に呼ばれるイベント。 / 表示条件: `useShield.boolValue && useEventOnDamageShield.boolValue` |
| Use Event On Damage Shield With Attacker | `useEventOnDamageShieldWithAttacker` | `bool` | – | シールド被弾時に攻撃者も渡すかの切替。 / 表示条件: `useShield.boolValue && useEventOnDamageShield.boolValue` |
| Event On Damage Shield With Attacker | `eventOnDamageShieldWithAttacker` | `eventParameters.eventToCallWithGameObject` | – | シールド被弾時に攻撃者を渡すイベント。 / 表示条件: `useEventOnDamageShield.boolValue && useEventOnDamageShieldWithAttacker.boolValue` |

### Death Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dead Funcion Call | `deadFuncionCall` | `UnityEvent` | new UnityEvent () | 死亡した瞬間に呼び出されるイベント。 / 表示条件: `showDamageDeadSettings` がオンのとき |

### Death Extra Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Extra Dead Functions | `useExtraDeadFunctions` | `bool` | – | 死亡後の追加イベントを有効にするかの切替。 / 表示条件: `showDamageDeadSettings` がオンのとき |
| Delay In Extra Dead Functions | `delayInExtraDeadFunctions` | `float` | – | 死亡後、追加イベントを呼ぶまでの待ち秒数。 / 表示条件: `showDamageDeadSettings.boolValue && useExtraDeadFunctions.boolValue` |
| Extra Dead Function Call | `extraDeadFunctionCall` | `UnityEvent` | new UnityEvent () | 死亡から遅れて呼び出される追加イベント。 / 表示条件: `showDamageDeadSettings.boolValue && useExtraDeadFunctions.boolValue` |

### Event With Attacker On Death Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event With Attacker On Death | `useEventWithAttackerOnDeath` | `bool` | – | 死亡時に攻撃者付きイベントを呼ぶかの切替。 / 表示条件: `showDamageDeadSettings` がオンのとき |
| Event With Attacker On Death | `eventWithAttackerOnDeath` | `eventParameters.eventToCallWithGameObject` | – | 死亡時に攻撃者を渡すイベント。 / 表示条件: `showDamageDeadSettings.boolValue && useEventWithAttackerOnDeath.boolValue` |

### Resurrect Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Resurrect Function Call | `resurrectFunctionCall` | `UnityEvent` | – | 復活処理が走った時に呼ばれるイベント。 / 表示条件: `showDamageDeadSettings` がオンのとき |

### Resurrect After Delay Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Resurrect After Delay Enabled | `resurrectAfterDelayEnabled` | `bool` | – | 死亡から一定時間後に復活させるかの切替。 / 表示条件: `showDamageDeadSettings` がオンのとき |
| Resurrect Delay | `resurrectDelay` | `float` | – | 死亡してから復活イベントを呼ぶまでの秒数。 / 表示条件: `showDamageDeadSettings.boolValue && resurrectAfterDelayEnabled.boolValue` |
| Event To Resurrect After Delay | `eventToResurrectAfterDelay` | `UnityEvent` | – | 指定時間後に復活処理として呼ばれるイベント。 / 表示条件: `showDamageDeadSettings.boolValue && resurrectAfterDelayEnabled.boolValue` |

### Invincible State Change Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Invincible State Change | `useEventsOnInvincibleStateChange` | `bool` | – | 無敵状態の変化イベントを有効にする切替。 / 表示条件: `showDamageDeadSettings` がオンのとき |
| Event On Invicible On | `eventOnInvicibleOn` | `UnityEvent` | – | 無敵状態になった時に呼ばれるイベント。 / 表示条件: `showDamageDeadSettings.boolValue && useEventsOnInvincibleStateChange.boolValue` |
| Event On Invicible Off | `eventOnInvicibleOff` | `UnityEvent` | – | 無敵状態が解除された時に呼ばれるイベント。 / 表示条件: `showDamageDeadSettings.boolValue && useEventsOnInvincibleStateChange.boolValue` |
| Use Event On Damage Received With Temporal Invincibility | `useEventOnDamageReceivedWithTemporalInvincibility` | `bool` | – | 一時無敵中の被弾イベントを有効にする切替。 / 表示条件: `showDamageDeadSettings` がオンのとき |
| Max Delay Between Damage Received And Invincibility State Active | `maxDelayBetweenDamageReceivedAndInvincibilityStateActive` | `float` | – | 一時無敵中の被弾を通知する猶予秒数。 / 表示条件: `showDamageDeadSettings.boolValue && useEventOnDamageReceivedWithTemporalInvincibility.boolValue` |
| Event On Damage Received With Temporal Invincibility | `eventOnDamageReceivedWithTemporalInvincibility` | `UnityEvent` | – | 一時無敵中に被弾した時に呼ばれるイベント。 / 表示条件: `showDamageDeadSettings.boolValue && useEventOnDamageReceivedWithTemporalInvincibility.boolValue` |
| Send Attacker On Event Damage Received With Temporal Invincibility | `sendAttackerOnEventDamageReceivedWithTemporalInvincibility` | `bool` | – | 一時無敵中の被弾通知に攻撃者を渡すかの切替。 / 表示条件: `showDamageDeadSettings.boolValue && useEventOnDamageReceivedWithTemporalInvincibility.boolValue` |
| Event To Send Attacker On Damage Received With Temporal Invincibility | `eventToSendAttackerOnDamageReceivedWithTemporalInvincibility` | `eventParameters.eventToCallWithGameObject` | – | 一時無敵中の被弾時に攻撃者を渡すイベント。 / 表示条件: `useEventOnDamageReceivedWithTemporalInvincibility.boolValue && sendAttackerOnEventDamageReceivedWithTemporalInvincibility.boolValue` |

### Events To Send Stats On Save

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Send Current Health Amount | `eventToSendCurrentHealthAmount` | `eventParameters.eventToCallWithAmount` | – | セーブ時などに現在体力を渡すイベント。 / 表示条件: `showDamageDeadSettings` がオンのとき |

### HUD Health Slider Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Health Slider | `healthSlider` | `Slider` | – | プレイヤー体力を表示する`Slider`の参照。 / 表示条件: `showSettings` がオンのとき |
| Use Circle Health Slider | `useCircleHealthSlider` | `bool` | – | 円形の体力ゲージを使うかの切替。 / 表示条件: `showSettings.boolValue && healthSlider.objectReferenceValue` |
| Circle Health Slider | `circleHealthSlider` | `Image` | – | 円形ゲージの塗りに使う`Image`の参照。 / 表示条件: `healthSlider.objectReferenceValue && useCircleHealthSlider.boolValue` |
| Health Slider Text | `healthSliderText` | `Text` | – | 体力値を数値で表示する`Text`の参照。 / 表示条件: `showSettings.boolValue && healthSlider.objectReferenceValue` |
| Hide Health Slider When Not Damage Received | `hideHealthSliderWhenNotDamageReceived` | `bool` | – | 被弾していない時にゲージを隠すかの切替。 / 表示条件: `showSettings.boolValue && healthSlider.objectReferenceValue` |
| Time To Hide Health Slider After Damage | `timeToHideHealthSliderAfterDamage` | `float` | – | 被弾後、ゲージを隠すまでの秒数。 / 表示条件: `healthSlider.objectReferenceValue && hideHealthSliderWhenNotDamageReceived.boolValue` |
| Main Health Slider Parent | `mainHealthSliderParent` | `RectTransform` | – | ゲージ表示時に親にするRectTransform。 / 表示条件: `healthSlider.objectReferenceValue && hideHealthSliderWhenNotDamageReceived.boolValue` |
| Hidden Health Slider Parent | `hiddenHealthSliderParent` | `RectTransform` | – | ゲージ非表示時の退避先RectTransform。 / 表示条件: `healthSlider.objectReferenceValue && hideHealthSliderWhenNotDamageReceived.boolValue` |
| Main Health Slider Transform | `mainHealthSliderTransform` | `RectTransform` | – | 表示と非表示を切り替えるゲージ本体のRectTransform。 / 表示条件: `healthSlider.objectReferenceValue && hideHealthSliderWhenNotDamageReceived.boolValue` |

### Health Slider Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enemy Tag | `enemyTag` | `string` | "enemy" | 敵と判定するタグ名で、名前と色の分岐に使用。 / 表示条件: `showSettings.boolValue && useHealthSlider.boolValue` |
| Friend Tag | `friendTag` | `string` | "friend" | 味方タグ名だが、名前と色の判定は`enemyTag`のみ参照。 / 表示条件: `showSettings.boolValue && useHealthSlider.boolValue` |
| Set Health Bar As Not Visible At Start | `setHealthBarAsNotVisibleAtStart` | `bool` | – | 生成直後に体力バーを非表示にするかの切替。 / 表示条件: `showSettings.boolValue && useHealthSlider.boolValue` |
| Use Health Slide Info On Screen | `useHealthSlideInfoOnScreen` | `bool` | – | 画面内にある間は体力バーを表示し続ける切替。 / 表示条件: `showSettings.boolValue && useHealthSlider.boolValue` |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Damage Receiver | `mainDamageReceiver` | `characterDamageReceiver` | – | ダメージ受け口として使う`characterDamageReceiver`。 / 表示条件: `showSettings` がオンのとき |
| Ragdoll Manager | `ragdollManager` | `ragdollActivator` | – | ラグドール制御を行う`ragdollActivator`の参照。 / 表示条件: `showSettings` がオンのとき |
| Damage In Screen Manager | `damageInScreenManager` | `damageInScreen` | – | 画面にダメージ表示を出すシステムの参照。 / 表示条件: `showSettings` がオンのとき |
| Debug Damage Source Transform | `debugDamageSourceTransform` | `Transform` | – | エディタのダメージ試験に使う発生源Transform。 / 表示条件: `showSettings` がオンのとき |
| Main Inventory Character Customization System | `mainInventoryCharacterCustomizationSystem` | `inventoryCharacterCustomizationSystem` | – | 防具耐久値の更新先となるカスタマイズシステム参照。 / 表示条件: `showSettings` がオンのとき |

### Main Advanced Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Weak Spots In Scanner Mode | `showWeakSpotsInScannerMode` | `bool` | – | スキャナーモード用に弱点メッシュを作る切替。 / 表示条件: `showAdvancedSettings` がオンのとき |
| Scorch Mark Prefab | `scorchMarkPrefab` | `GameObject` | null | 死亡時に地面へ置く焦げ跡のプレハブ。 / 表示条件: `showAdvancedSettings` がオンのとき |
| Weak Spot Mesh | `weakSpotMesh` | `GameObject` | – | 弱点表示に使うメッシュのプレハブ。 / 表示条件: `showAdvancedSettings.boolValue && showWeakSpotsInScannerMode.boolValue` |
| Weak Spot Mesh Alpha Value | `weakSpotMeshAlphaValue` | `float` | – | 弱点メッシュに設定する色のアルファ値。 / 表示条件: `showAdvancedSettings.boolValue && showWeakSpotsInScannerMode.boolValue` / Range (0, 1) |

### Damage On Collision Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Receive Damage From Collisions Enabled | `receiveDamageFromCollisionsEnabled` | `bool` | – | 衝突速度に応じたダメージを受けるかの切替。 / 表示条件: `showAdvancedSettings` がオンのとき |
| Min Time To Receive Damage On Impact | `minTimeToReceiveDamageOnImpact` | `float` | – | 衝突ダメージが再発生するまでの最短秒数。 / 表示条件: `showAdvancedSettings.boolValue && receiveDamageFromCollisionsEnabled.boolValue` |
| Min Velocity To Receive Damage On Impact | `minVelocityToReceiveDamageOnImpact` | `float` | – | ダメージが発生する最小の衝突速度。 / 表示条件: `showAdvancedSettings.boolValue && receiveDamageFromCollisionsEnabled.boolValue` |
| Receive Damage On Impact Multiplier | `receiveDamageOnImpactMultiplier` | `float` | – | 衝突速度に掛けてダメージ量を決める係数。 / 表示条件: `showAdvancedSettings.boolValue && receiveDamageFromCollisionsEnabled.boolValue` |

### Ragdoll Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Receive Damage Even Dead | `receiveDamageEvenDead` | `bool` | – | 死亡後もダメージを受け続けるかの切替。 / 表示条件: `showAdvancedSettings.boolValue && haveRagdoll.boolValue` |
| Can Be Sedated | `canBeSedated` | `bool` | true | 麻酔や睡眠状態にできるようにするかの切替。 / 表示条件: `showAdvancedSettings.boolValue && haveRagdoll.boolValue` |
| Awake On Damage If Sedated | `awakeOnDamageIfSedated` | `bool` | – | 睡眠中に被弾すると目を覚ますかの切替。 / 表示条件: `haveRagdoll.boolValue && canBeSedated.boolValue` |

### Ragdoll Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Sedate | `useEventOnSedate` | `bool` | – | 睡眠状態の開始と終了イベントの有効切替。 / 表示条件: `haveRagdoll.boolValue && canBeSedated.boolValue` |
| Sedate Start Event | `sedateStartEvent` | `UnityEvent` | – | 睡眠状態に入った時に呼ばれるイベント。 / 表示条件: `canBeSedated.boolValue && useEventOnSedate.boolValue` |
| Sedate End Event | `sedateEndEvent` | `UnityEvent` | – | 睡眠状態から覚めた時に呼ばれるイベント。 / 表示条件: `canBeSedated.boolValue && useEventOnSedate.boolValue` |

### Weak Spots List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Damage Receivers To Custom Transform List | `addDamageReceiversToCustomTransformList` | `bool` | – | 任意のTransformにダメージ判定を追加する切替。 / 表示条件: `showAdvancedSettings` がオンのとき |

### Events On Health Value Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Health Value List | `useEventOnHealthValueList` | `bool` | – | 体力値のしきい値イベントを有効にする切替。 / 表示条件: `showAdvancedSettings` がオンのとき |

### Damage Type ID Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Damage Type Check | `useDamageTypeCheck` | `bool` | – | ダメージタイプ別の耐性処理を有効にする切替。 / 表示条件: `showAdvancedSettings` がオンのとき |
| Check Only Damage Types On Damage Received | `checkOnlyDamageTypesOnDamageReceived` | `bool` | – | リスト外のダメージタイプを無効化するかの切替。 / 表示条件: `showAdvancedSettings.boolValue && useDamageTypeCheck.boolValue` |

### Debug Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Damage Received Debug Info | `showDamageReceivedDebugInfo` | `bool` | – | 受けたダメージの計算内容をログ出力する切替。 / 表示条件: `showDebugSettings` がオンのとき |
| Health Amount To Take On Editor | `healthAmountToTakeOnEditor` | `float` | – | エディタのテストボタンで与えるダメージ量。 / 表示条件: `showDebugSettings` がオンのとき |
| Health Amount To Give On Editor | `healthAmountToGiveOnEditor` | `float` | – | エディタのテストボタンで回復させる体力量。 / 表示条件: `showDebugSettings` がオンのとき |

### Critical Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Type Explanation | `damageTypeExplanation` | `string` | "Damage Resistance as 0 means the dam… | ダメージ耐性値の意味を説明するテキスト。 / 表示条件: `list.isExpanded` / TextArea (3, 20) |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `dead` | `bool` | false | – |
| `delayInDamageFunctions` | `float` | – | – |
| `extraDamageFunctionList` | `List<damageFunctionInfo>` | new List<damageFunctionInfo> () | – |
| `settings` | `enemySettings` | new enemySettings () | – |
| `advancedSettings` | `advancedSettingsClass` | new advancedSettingsClass () | – |
| `sedateActive` | `bool` | – | – |
| `sedateUntilReceiveDamageState` | `bool` | – | – |
| `showSettings` | `bool` | – | – |
| `showAdvancedSettings` | `bool` | – | – |
| `showDamageDeadSettings` | `bool` | – | – |
| `showDebugSettings` | `bool` | – | – |
| `damageReceiverList` | `List<characterDamageReceiver>` | new List<characterDamageReceiver> () | – |
| `customDamageReceiverList` | `List<characterDamageReceiver>` | new List<characterDamageReceiver> () | – |
| `damageReceiverGameObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| `eventOnHealthValueList` | `List<eventOnHealthValue>` | new List<eventOnHealthValue> () | – |
| `damageTypeInfoList` | `List<damageTypeInfo>` | new List<damageTypeInfo> () | – |
| `blockDamageActive` | `bool` | – | – |
| `blockDamageProtectionAmount` | `float` | – | – |
| `impactDecalList` | `string []` | – | – |
| `impactDecalIndex` | `int` | – | – |
| `impactDecalName` | `string` | – | – |
| `currentID` | `int` | – | – |
| `currentSedateDuration` | `float` | – | – |
| `ignoreWeakSpotsActive` | `bool` | – | – |
| `customTransformListDamageReceiver` | `List<Transform>` | new List<Transform> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setUseEventOnDamageEnabledState(bool state)` | `useEventOnDamageEnabled`を設定するだけの薄いセッター。 |
| `setIgnoreSetShieldStateActive(bool state)` | `setShieldState`系の呼び出しを無視させる`ignoreSetShieldStateActive`フラグを設定する。 |
| `setShieldState(bool state)` | 無視フラグ中は何もせず、`useShield`を設定して有効時はシールド開始と最大値同期、無効時は`disableShield`を呼ぶ。 |
| `setOriginalUseShieldState()` | `originalUseShieldState`の値で`setShieldState`を呼び直す復元用メソッド。 |
| `setUseShieldState(bool state)` | シールドシステムを触らず`useShield`だけを設定する（無視フラグ中は何もしない）。 |
| `setShieldStateAndCheckEventsForShieldState(bool state)` | `setShieldState`の後に`checkEventsForShieldState`を呼び、状態変化イベントを確認する。 |
| `checkEventsForShieldState()` | シールドシステムがあれば`mainShieldSystem.checkEventsForShieldState`に委譲する。 |
| `addDamageReceiversToRagdoll()` | ラグドールの全非トリガーColliderに`characterDamageReceiver`を追加し、レシーバー一覧を再構築する。 |
| `removeDamageReceiversFromRagdoll()` | `customDamageReceiverList`のダメージレシーバーを破棄してリストを空にし、コンポーネントを更新する。 |
| `setDamage(float damageAmount, Vector3 fromDirection, Vector3 damagePosition, GameObject attacker, GameObject projectile, bool damageConstant, bool searchClosestWeakSpot, bool ignoreShield, bool ignoreDamageInScreen, bool damageCanBeBlocked, bool canActivateReactionSystemTemporally, int damageReactionID, int damageTypeID)` | `damageAmount`・`attacker`・`ignoreShield`・`damageTypeID`を受け、無敵/ブロック/シールド/弱点/倍率を判定して`healthAmount`を減算し、死亡処理まで行う中核。 |
| `enableUseCustomStateHealthAmountOnSpotEnabledState(string weakSpotName)` | `weakSpotName`の弱点の`useCustomStateHealthAmountOnSpotEnabled`をtrueにする薄いラッパー。 |
| `disableUseCustomStateHealthAmountOnSpotEnabledState(string weakSpotName)` | `weakSpotName`の弱点の`useCustomStateHealthAmountOnSpotEnabled`をfalseにする薄いラッパー。 |
| `setUseCustomStateHealthAmountOnSpotEnabledState(bool state, string weakSpotName)` | 名前で弱点を検索し`useCustomStateHealthAmountOnSpotEnabled`を設定する（見つからなければ何もしない）。 |
| `enableUseHealthAmountOnSpotState(string weakSpotName)` | `weakSpotName`の`useHealthAmountOnSpot`をtrueにする薄いラッパー。 |
| `disableUseHealthAmountOnSpotState(string weakSpotName)` | `weakSpotName`の`useHealthAmountOnSpot`をfalseにする薄いラッパー。 |
| `setUseHealthAmountOnSpotState(bool state, string weakSpotName)` | 名前で弱点を検索し`useHealthAmountOnSpot`を設定する（見つからなければ何もしない）。 |
| `setCurrentWeakSpotNameToAdjust(string weakSpotName)` | 後続のID設定で使う`currentWeakSpotNameToAdjust`に弱点名を保存するだけ。 |
| `setCurrentCustomStateHealthAmountOnSpotID(int newID)` | 保存済みの弱点名があればID指定版へ転送し、`currentWeakSpotNameToAdjust`を空に戻す。 |
| `setCurrentCustomStateHealthAmountOnSpotID(int newID, string weakSpotName)` | 名前で弱点を検索し`currentCustomStateHealthAmountOnSpotID`を設定する。 |
| `setSendFunctionWhenDamageStateOnWeakSpot(string weakSpotName, bool state)` | 名前で弱点を検索し`sendFunctionWhenDamage`を設定する。 |
| `setDrivingState(bool state)` | `driving`フラグを設定するだけの薄いセッター。 |
| `setDrivingRemotelyState(bool state)` | `drivingRemotely`フラグを設定するだけの薄いセッター。 |
| `setIgnoreIfCharacterDrivingOnDamageReceiverState(bool state)` | `ignoreIfCharacterDrivingOnDamageReceiver`フラグを設定するだけの薄いセッター。 |
| `isDamageReactionPaused()` | `mainDamageHitReactionSystem`の被弾リアクション停止状態を返す。 |
| `setUseEventOnHealthValueListState(bool state)` | `useEventOnHealthValueList`を設定するだけの薄いセッター。 |
| `setOriginalUseEventOnHealthValueListState()` | `originalUseEventOnHealthValueList`の値へ戻す復元用メソッド。 |
| `checkEventOnHealthValueList(bool receivingDamage)` | 体力値イベント一覧を走査し、被弾/回復の別と`minDamageToReceive`（割合指定可）を満たすものを一度だけ発火する。 |
| `setEventOnHealthValueEnabledState(bool state, string stateName)` | 名前が一致する体力値イベントの`eventEnabled`を設定して抜ける。 |
| `setEventOnHealthValueEnabledState(string stateName)` | 名前一致の体力値イベントを有効化する薄いラッパー。 |
| `setEventOnHealthValueDisabledState(string stateName)` | 名前一致の体力値イベントを無効化する薄いラッパー。 |
| `getLastDamageTime()` | 最後にダメージを受けた時刻`lastDamageTime`を返す。 |
| `damageSpot(int elementIndex, float damageAmount)` | 指定弱点の位置（無ければ自身の位置）を被弾位置として、自身を攻撃者に`setDamage`を呼ぶ。 |
| `checkIfEnabledStateCanChange(bool state)` | `receiveDamageEvenDead`でなければコンポーネントの`enabled`を切り替える。 |
| `setDamageTargetOverTimeWithAmountAndDurationAndRate(string amountAndDurationAndRateString)` | 「amount;duration;rate」形式の文字列を解析し、遅延0.5秒で継続ダメージを開始する。 |
| `setDamageTargetOverTimeToDeath(float damageOverTimeAmount)` | 0.5秒遅延・毎0.4秒・死亡するまで続く継続ダメージを開始する。 |
| `setDamageTargetOverTimeState(float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, int damageTypeID)` | 既存の継続ダメージを止め、指定パラメータで継続ダメージのコルーチンを開始する。 |
| `stopDamageOverTime()` | 継続ダメージのコルーチンを停止し`receivingDamageOverTimeActive`をfalseにする。 |
| `setDamageOrHealthTargetWithDelay(float waitAmount, float valueAmount, int damageTypeID)` | 既存を止めて、指定秒後に回復（正値）またはダメージ（負値）を与えるコルーチンを開始する。 |
| `stopDamageOrHealthTargetWithDelay()` | 遅延ダメージ/回復のコルーチンを停止する。 |
| `sedateCharacter(Vector3 position, float sedateDelay, bool useWeakSpotToReduceDelay, bool sedateUntilReceiveDamage, float sedateDuration)` | ラグドールがあり`canBeSedated`なら、弱点で遅延を短縮して鎮静状態と継続時間を設定し`ragdollManager`へ渡す。 |
| `sedateCharacter(float sedateDuration)` | 自身の位置・遅延0・弱点短縮なしで5引数版を呼ぶラッパー。 |
| `sedateCharacterUntilReceiveDamage(float sedateDuration)` | 被弾まで鎮静が続く設定で5引数版を呼ぶラッパー。 |
| `getCurrentSedateDuration()` | 現在の鎮静継続時間`currentSedateDuration`を返す。 |
| `setSedateState(bool state)` | `sedateActive`を設定し、死亡中でなければ鎮静開始/終了イベントを発火する。 |
| `isReceiveDamageFromCollisionsEnabled()` | 衝突ダメージの有効フラグ`receiveDamageFromCollisionsEnabled`を返す。 |
| `setImpactReceivedInfo(Vector3 impactVelocity)` | 有効かつクールダウン経過かつ最低速度超過なら、速度×係数の一定ダメージを与えて時刻を記録する。 |
| `setRagdollImpactReceivedInfo(Vector3 impactVelocity, Collider impactCollider)` | ラグドールがあれば`ragdollManager.setImpactReceivedInfo`へ委譲する。 |
| `characterIsOnRagdollState()` | ラグドールが存在しアクティブならtrueを返す。 |
| `getMainRagdollActivator()` | `ragdollManager`（`ragdollActivator`）を返す。 |
| `canRagdollReceiveDamageOnImpact()` | `advancedSettings.ragdollCanReceiveDamageOnImpact`を返す。 |
| `updateSlider(float value)` | スライダー表示を内部更新し、`playerStatsManager`があれば体力ステータスも更新する。 |
| `updateSliderWithoutUpdatingStatManager(int statId, float value)` | ステータスマネージャーを更新せずスライダー表示のみ更新する（`statId`は未使用）。 |
| `updatePlayerStatsManagerValue()` | `playerStatsManager`があれば体力ステータス値を現在の`healthAmount`で更新する。 |
| `updatePlayerStatesManagerMaxHealthValue()` | `playerStatsManager`があれば最大体力ステータス値を現在の最大値で更新する。 |
| `updateSliderMaxValue(float newMaxValue)` | スライダーとヘルスバーの最大値を更新し、スライダー非表示チェックを走らせる。 |
| `removeHealthSlider()` | 死亡時にヘルスバーを削除する設定なら`healthBarManager`から対象スライダーを外す。 |
| `checkHideHealthSliderParent()` | 被弾後にスライダーを隠すコルーチンを再開始する。 |
| `isPlayerMenuActive()` | プレイヤーメニューが開いているかを返す。 |
| `getHealth(float amount)` | ダメージ表示UIに回復量を出してから`addHealth`を呼ぶ。 |
| `addHealth(float amount)` | 死亡していなければ加算して最大値でクランプし、スライダー更新と体力値イベント確認を行う。 |
| `addHealthWithoutUpdatingStatManager(int statId, float amount)` | `playerStatsManager`を更新せずに体力を加算し、最大値クランプ・スライダー更新・イベント確認を行う。 |
| `updateHealthAmountWithoutUpdatingStatManager(int statId, float amount)` | 死亡していなければ体力を指定値に置き換え、クランプ・スライダー更新・イベント確認を行う。 |
| `updateMaxHealthAmountWithoutUpdatingStatManager(int statId, float newAmount)` | 最大体力を設定し、`lastIncreaseMaxHealthAmount`とスライダー最大値を更新する。 |
| `updateRegenerateAmountWithoutUpdatingStatManager(int statId, float newAmount)` | `regenerateAmount`を設定するだけの薄いセッター。 |
| `setHealthAmountOnMaxValue()` | 最大体力までの差分を`addHealth`で加算して満タンにする。 |
| `clampHealthAmountToMaxHealth()` | 体力を0〜最大値にクランプしてスライダーを更新する。 |
| `setSliderInfo(string name, Color color)` | ヘルスバーに名前と色を設定し、`characterName`と割当済みフラグを更新する。 |
| `updateNameWithAlly()` | 設定値の味方名と味方色で`setSliderInfo`を呼ぶ。 |
| `updateNameWithEnemy()` | 設定値の敵名と敵色で`setSliderInfo`を呼ぶ。 |
| `hacked()` | ハッキング扱いで味方名・味方色にスライダー表示を変更する。 |
| `resurrect()` | 体力を最大に戻して`dead`を解除し、スライダー・復活イベント・弱点体力・イベントフラグを復元する。 |
| `setResurrectAfterDelayEnabledState(bool state)` | `resurrectAfterDelayEnabled`を設定するだけの薄いセッター。 |
| `setPauseResurrectCheckState(bool state)` | 復活遅延チェックの一時停止フラグを設定し、`lastTimeDead`を現在時刻にする。 |
| `resurrectFromExternalCall()` | 死亡中なら復活イベント`eventToResurrectAfterDelay`を発火する。 |
| `setSliderVisibleState(bool state)` | ヘルスバーがあればスライダーの表示状態を切り替える。 |
| `setSliderVisibleStateForPlayer(GameObject player, bool state)` | 指定プレイヤー向けにスライダーの表示状態を切り替える。 |
| `setSliderLocatedState(bool state)` | ヘルスバーの配置状態を切り替える。 |
| `setSliderLocatedState(GameObject player, bool state)` | 指定プレイヤー向けにヘルスバーの配置状態を切り替える。 |
| `getHealthID()` | この体力コンポーネントのヘルスバーID`currentID`を返す。 |
| `getClosesWeakSpotIndex(Vector3 collisionPosition)` | 無視・体力切れでない弱点の中から指定位置に最も近いもののインデックスを返す（無ければ-1）。 |
| `checkIfDamagePositionIsCloseEnoughToWeakSpotByName(Vector3 collisionPosition, List<string> weakSpotNameList, float maxDistanceToWeakSpot)` | 名前が一覧に含まれ指定距離内にある弱点が存在すればtrueを返す。 |
| `checkIfWeakSpotListContainsTransform(Transform transformToCheck)` | 無視されていない弱点のいずれかが指定Transformを使っていればtrueを返す。 |
| `activateEventToSendCurrentHealthAmount()` | 現在の体力値を引数に`eventToSendCurrentHealthAmount`を発火する。 |
| `getMaxHealthAmount()` | 最大体力`maxHealthAmount`を返す。 |
| `getAuxHealthAmount()` | 補助体力値`auxHealthAmount`を返す。 |
| `addAuxHealthAmount(float amount)` | 補助体力値`auxHealthAmount`に加算するだけ。 |
| `getHealthAmountToLimit()` | 最大体力と補助体力の差（回復可能量）を返す。 |
| `pushFullCharacter()` | ラグドール中なら腰に上方向の力を加え、そうでなければ全身を前上方向へ押す。 |
| `pushCharacterWithoutForce()` | ラグドールへ力を加えずに押す処理を`ragdollManager`へ委譲する。 |
| `pushCharacterWithoutForceXAmountOfTime(float newValue)` | 指定時間、力を加えずにキャラクターを押す処理を委譲する。 |
| `pushFullCharacterXAmountOfTime(float newValue, Vector3 direction)` | 指定時間・指定方向へ全身を押す処理を委譲する。 |
| `TakeDamage(float damage)` | `takeHealth`へそのまま渡すエイリアス。 |
| `killCharacter()` | 現在体力分のダメージをシールド無視・弱点検索なしで与えて即死させる。 |
| `killByButton()` | ボタン用に、一定ダメージ扱いかつシールド無視で現在体力分のダメージを与える。 |
| `killByButtonWithoutRagdollForce()` | ラグドールの力を一時的に切ってから`killByButton`を実行し、設定を戻す。 |
| `killCharacter(Vector3 fromDirection, Vector3 damagePos, GameObject attacker, GameObject projectile, bool damageConstant)` | 指定方向・位置・攻撃者・発射物で現在体力分のダメージを与える。 |
| `takeHealth(float damageAmount)` | 自身を攻撃者とし、シールドを無視してダメージを与える。 |
| `takeHealthWithoutDamageReaction(float damageAmount)` | 被弾リアクションを一時停止してからダメージを与え、元の停止状態に戻す。 |
| `takeConstantDamage(float damageAmount)` | 一定ダメージとして（シールドは有効のまま）ダメージを与える。 |
| `takeConstantDamageWithoutShield(float damageAmount)` | 一定ダメージとしてシールドを無視してダメージを与える。 |
| `takeDamageFromDebugDamageSourceTransform(float damageAmount)` | `debugDamageSourceTransform`の向きと位置を使ってダメージを与える（未設定なら何もしない）。 |
| `getShieldSystem()` | `mainShieldSystem`を返す。 |
| `getShieldAmountToLimit()` | シールド有効時はシールドの上限までの残量を返し、無効時は-1を返す。 |
| `addAuxShieldAmount(float amount)` | シールド有効時、`mainShieldSystem`の補助シールド量に加算する。 |
| `callExtraDeadFunctions()` | `delayInExtraDeadFunctions`待ってから`extraDeadFunctionCall`を発火するコルーチンを開始する。 |
| `getPlaceToShoot()` | 射撃位置`placeToShoot`を返す。 |
| `getTransformToAttachWeaponsByClosestPosition(Vector3 positionToCheck)` | 指定位置に最も近い弱点の武器取付Transform（ボーン指定時はボーン）を返す（無ければnull）。 |
| `getClosestWeakSpotPositionToPosition(Vector3 positionToCheck, List<string> weakListNameToCheck, bool checkWeakListName, float maxDistanceToBodyPart)` | 名前条件と最大距離で絞った弱点のうち最も近い位置を返し、無ければ`-Vector3.one`を返す。 |
| `updateDamageReceivers()` | 各弱点Transform上のレシーバーに自身を設定して登録し、ダメージ倍率を反映する。 |
| `activateAllEventsOnEmptyHealthAmountOnWeakSpotsList()` | 無視されていない全弱点の体力切れイベント`eventOnEmtpyHealthAmountOnSpot`を発火する。 |
| `activateAllEventsOnDamageWeakSpotsList()` | 無視されていない全弱点の`damageFunction`を発火する。 |
| `getImpactListInfo()` | デカールマネージャーを用意してインパクト名一覧を`impactDecalList`へ複製する。 |
| `getDecalImpactIndex()` | `impactDecalIndex`を返す。 |
| `isUseImpactSurfaceActive()` | `useImpactSurface`を返す。 |
| `getCharacterName()` | 名前が未設定ならタグで敵/味方を判定して設定し、`characterName`を返す。 |
| `addObjectAsNewCharacterDamageReceiver(GameObject newObject)` | 対象に`characterDamageReceiver`を追加（既存なら再利用）して自身を設定し、一覧に登録する。 |
| `setCustomTransformListDamageReceiver()` | `customTransformListDamageReceiver`の各Transformにレシーバーを付けて登録し、リストを空にする。 |
| `updateCharacterDamageReceiverOnObject()` | レシーバー一覧をクリアし、子階層の全`characterDamageReceiver`を再登録して設定を反映する。 |
| `addDamageReceiverToObject()` | 自身のGameObjectに`mainDamageReceiver`を確保してキャラクターを設定する。 |
| `setHumanoidWeaKSpots(bool clearPreviousWeakSpotList)` | Animatorのヒューマノイドボーンから弱点を作成、または既存弱点をボーンへ再リンクする。 |
| `resetWeakSpotDamageMultipliers()` | 全弱点の`damageMultiplier`を1、`killedWithOneShoot`をfalseに戻す。 |
| `addWeakSpot(Transform spotTransform, string spotName, float damageMultiplier, bool killedInOneShot, HumanBodyBones newHumanBodyBone)` | 名前・Transform・倍率・一撃フラグ・ボーンを指定して弱点を新規追加する。 |
| `enableOverrideAndActivateInvincibleState()` | 上書きフラグを立ててカウンタを増やし、無敵状態を有効にする。 |
| `disableOverrideAndActivateInvincibleState()` | カウンタを減らし0になったら上書きフラグを解除して無敵を解く。 |
| `setInvincibleState(bool state)` | 無敵値を設定し、解除時は時間限定無敵のフラグを戻してから状態変化イベントを発火する。 |
| `setInvincibleStateDuration(float invincibleDuration)` | 継続ダメージを止めたうえで、指定時間だけ無敵になるコルーチンを開始する。 |
| `setInvincibleStateDurationWithoutDisableDamageOverTime(float invincibleDuration)` | 継続ダメージは止めずに、指定時間だけ無敵になるコルーチンを開始する。 |
| `setCheckEventsOnTemporalInvincibilityActiveState(bool state)` | 時間限定無敵中の被弾イベント確認フラグを設定し、有効時は時刻を記録する。 |
| `checkEventsOnInvicibleStateChange(bool state)` | 設定が有効なら無敵オン/オフのイベントを発火する。 |
| `stopSetInvincibleStateDurationCoroutine()` | 無敵時間コルーチン`invincibleDurationCoroutine`を停止する。 |
| `initializeHealthAmount(float newValue)` | `healthAmount`を代入するだけの薄い初期化。 |
| `checkLastIncreaseMaxHealthAmount()` | 直前の最大体力増加が正なら満タンに、そうでなければ最大値でクランプする。 |
| `increaseMaxHealthAmount(float newAmount)` | 最大体力を加算し、スライダー最大値・ステータス・体力を最大まで更新する。 |
| `increaseMaxHealthAmountByMultiplier(float amountMultiplier)` | 最大体力を倍率で乗算し、スライダー最大値・ステータス・体力を最大まで更新する。 |
| `initializeMaxHealthAmount(float newValue)` | `maxHealthAmount`を代入するだけの薄い初期化。 |
| `setRegenerateHealthState(bool state)` | `regenerateHealth`を設定するだけの薄いセッター。 |
| `setConstantRegenerateState(bool state)` | `constantRegenerate`を設定するだけの薄いセッター。 |
| `initializeRegenerateAmount(float newValue)` | `regenerateAmount`を代入するだけの薄い初期化。 |
| `increaseRegenerateAmount(float newValue)` | `regenerateAmount`に加算するだけ。 |
| `increaseRegenerateAmountByMultiplier(float amountMultiplier)` | `regenerateAmount`に倍率を掛けるだけ。 |
| `checkIfMaxHealth()` | 現在体力が最大体力以上かを返す。 |
| `setShield(float shieldAmount)` | シールド有効時、`mainShieldSystem.getShield`でシールド量を加算する。 |
| `getHealthAmountToPick(float amount)` | 上限までの不足量を計算し、実際に補助体力へ加算した量を返す。 |
| `setGeneralDamageMultiplerActiveState(bool state)` | 倍率機能が有効な場合のみ`generalDamageMultiplerActive`を設定する。 |
| `setGeneralDamageMultiplierValue(float newValue)` | `generalDamageMultiplier`を設定するだけの薄いセッター。 |
| `setOriginalDamageMultiplierValue()` | `originalGeneralDamageMultiplier`の値へ倍率を戻す。 |
| `characterHasWeakSpotList()` | 弱点リストを使用する設定か（`useWeakSpots`）を返す。 |
| `setUseWeakSpotsActiveState(bool state)` | `advancedSettings.useWeakSpots`を設定するだけの薄いセッター。 |
| `setOriginalUseWeakSpotsActiveState()` | `originalUseWeakSpots`の値へ弱点使用設定を戻す。 |
| `setActivateRagdollOnDamageReceivedState(bool state)` | `activateRagdollOnDamageReceived`を設定するだけの薄いセッター。 |
| `setOriginalActivateRagdollOnDamageReceivedState()` | 保存しておいた元のラグドール有効化設定へ戻す。 |
| `setSliderOffset(float newValue)` | `settings.sliderOffset.y`を設定するだけの薄いセッター。 |
| `addDamageReceiverGameObjectList(GameObject newObject)` | `damageReceiverGameObjectList`に未登録なら追加する。 |
| `removeDamageReceiverGameObjectList(GameObject newObject)` | `damageReceiverGameObjectList`から該当オブジェクトを削除する。 |
| `clearDamageReceiverGameObjectList()` | `damageReceiverGameObjectList`を空にする。 |
| `setAllyNewNameIngame(string newName)` | `settings.allyName`を設定するだけの薄いセッター。 |
| `setEnemyNewNameIngame(string newName)` | `settings.enemyName`を設定するだけの薄いセッター。 |
| `enableOrDisableDamageTypeInfo(string damageTypeName, bool state)` | 名前一致のダメージタイプの`damageTypeEnabled`を設定する。 |
| `increaseDamageTypeInfo(string damageTypeName, float extraValue)` | 名前一致のダメージタイプの`damageTypeResistance`に加算する。 |
| `setObtainHealthOnDamageTypeState(string damageTypeName, bool state)` | 名前一致のダメージタイプの`obtainHealthOnDamageType`を設定する。 |
| `setEventOnHealthValueEnabledStateFromEditor(string stateName)` | 体力値イベントを有効化してから`updateComponent`でシーンを更新するエディタ用メソッド。 |
| `setEventOnHealthValueDisabledStateFromEditor(string stateName)` | 体力値イベントを無効化してから`updateComponent`を呼ぶエディタ用メソッド。 |
| `setResurrectAfterDelayEnabledStateFromEditor(bool state)` | `resurrectAfterDelayEnabled`を設定して`updateComponent`を呼ぶエディタ用メソッド。 |
| `initializeHealthAmountFromEditor(float newValue)` | `initializeHealthAmount`の後に`updateComponent`を呼ぶエディタ用メソッド。 |
| `initializeMaxHealthAmountFromEditor(float newValue)` | `initializeMaxHealthAmount`の後に`updateComponent`を呼ぶエディタ用メソッド。 |
| `updatePlayerStatsManagerValueFromEditor()` | `playerStatsManager.updateStatValueFromEditor`で体力値をエディタ更新する。 |
| `updatePlayerStatesManagerMaxHealthValueFromEditor()` | 最大体力ステータスを`updateStatValueFromEditor`でエディタ更新する。 |
| `setAllyNewName(string newName)` | `settings.allyName`を設定し、再生中でなければ`updateComponent`を呼ぶ。 |
| `setEnemyNewName(string newName)` | `settings.enemyName`を設定し、再生中でなければ`updateComponent`を呼ぶ。 |
| `setUseShieldStateFromEditor(bool state)` | `setUseShieldState`の後に`updateComponent`を呼ぶエディタ用メソッド。 |
| `enableUseHealthAmountOnSpotStateFromEditor(string weakSpotName)` | `enableUseHealthAmountOnSpotState`の後に`updateComponent`を呼ぶエディタ用メソッド。 |
| `disableUseHealthAmountOnSpotStateFromEditor(string weakSpotName)` | `disableUseHealthAmountOnSpotState`の後に`updateComponent`を呼ぶエディタ用メソッド。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`でコンポーネントとシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnDamageReceivedWithTemporalInvincibility` | `UnityEvent` | – |
| `eventOnInvicibleOn` | `UnityEvent` | – |
| `eventOnInvicibleOff` | `UnityEvent` | – |
| `eventOnDamage` | `UnityEvent` | – |
| `eventOnDamageShield` | `UnityEvent` | – |
| `deadFuncionCall` | `UnityEvent` | – |
| `extraDeadFunctionCall` | `UnityEvent` | – |
| `resurrectFunctionCall` | `UnityEvent` | – |
| `sedateStartEvent` | `UnityEvent` | – |
| `sedateEndEvent` | `UnityEvent` | – |
| `eventToResurrectAfterDelay` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`addAuxHealthAmountWithHealthManagement(float amount)`, `changePlaceToShootPosition(bool state)`, `characterHasWeakSpotListWithHealthManagement()`, `checkIfDamagePositionIsCloseEnoughToWeakSpotByNameWithHealthManagement(Vector3 collisionPosition, List<string> weakSpotNameList, float maxDistanceToWeakSpot)`, `checkIfDamageReceiverBelongsToThisCharacter(GameObject objectToCheck)`, `checkIfDeadWithHealthManagement()`, `checkIfMaxHealthWithHealthManagement()`, `checkIfWeakSpotListContainsTransformWithHealthManagement(Transform transformToCheck)`, `explodeVehicleIfCharacterCurrentlyDriving()`, `getAuxHealthAmountWithHealthManagement()`, `getCharacterOrVehicleWithHealthManagement()`, `getCharacterRootMotionTransform()`, `getCharacterWeakSpotListWithHealthManagement()`, `getCharacterWithHealthManagement()`, `getClosestWeakSpotPositionToPositionWithHealthManagement(Vector3 positionToCheck, List<string> weakListNameToCheck, bool checkWeakListName, float maxDistanceToBodyPart)`, `getCurrentHealthAmount()`, `getCurrentHealthAmountWithHealthManagement()`, `getCurrentShieldAmount()`, `getDamageReceiverColliderList()`, `getDecalImpactIndexWithHealthManagement()`, `getHealthAmountToPickWithHealthManagement(float amount)`, `getMaxHealthAmountWithHealthManagement()`, `getPlaceToShootGameObjectWithHealthManagement()`, `getPlaceToShootWithHealthManagement()`, `isBlockDamageActiveState()`, `isCharacterInRagdollState()`, `isCharacterWithHealthManagement()`, `isDead()`, `isUseImpactSurfaceActiveWithHealthManagement()`, `isUseShieldActive()`, `killCharacterIfCurrentlyDrivingVehicle()`, `killCharacterWithHealthManagement()`, `killCharacterWithHealthManagement(GameObject projectile, Vector3 direction, Vector3 position, GameObject attacker, bool damageConstant)`, `removeDamagetTargetOverTimeStateWithHealthManagement()`, `sedateCharacterithHealthManagement(Vector3 position, float sedateDelay, bool useWeakSpotToReduceDelay, bool sedateUntilReceiveDamage, float sedateDuration)`, `setBlockDamageActiveState(bool state)`, `setBlockDamageProtectionAmount(float newValue)`, `setBlockDamageRangleAngleState(bool useMaxBlockRangeAngleValue, float maxBlockRangeAngleValue)`, `setDamageOrHealthTargetWithDelayWithHealthManagement(float waitAmount, float valueAmount, int damageTypeID)`, `setDamageReactionPausedState(bool state)`, `setDamageTargetOverTimeStateWithHealthManagement(float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, int damageTypeID)`, `setDamageWithHealthManagement(float damageAmount, Vector3 fromDirection, Vector3 damagePos, GameObject attacker, GameObject projectile, bool damageConstant, bool searchClosestWeakSpot, bool ignoreShield, bool ignoreDamageInScreen, bool damageCanBeBlocked, bool canActivateReactionSystemTemporally, int damageReactionID, int damageTypeID)`, `setHealWithHealthManagement(float healAmount)`, `setHitReactionBlockIDValue(int newBlockID)`, `setIgnoreParryActiveState(bool state)`, `setIgnoreWeakSpotsActiveState(bool state)`, `setPlaceToShootLocalPosition(Vector3 newValue)`, `setPlaceToShootPositionOffset(float newValue)`, `setPlayerMenuActiveState(bool state)`, `setShieldWithHealthManagement(float shieldAmount)`, `updateOriginalSliderOffset()`, `updateSliderOffset(float value)`

</details>

## 内部型

- `enemySettings`（class）
- `advancedSettingsClass`（class）
- `weakSpot`（class）
- `damageFunctionInfo`（class）
- `eventOnHealthValue`（class）
- `damageTypeInfo`（class）
- `customStateHealthAmountOnSpotInfo`（class）
