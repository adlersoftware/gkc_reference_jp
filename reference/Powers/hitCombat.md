# hitCombat

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/hitCombat.cs:6`

**概要**: 近接攻撃の当たり判定コンポーネント。手足のトリガーで相手を検出し、ダメージ・押し出し・力を適用する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hit Damage | `hitDamage` | `float` | 5 | – |
| Damage Multiplier | `damageMultiplier` | `float` | 1 | – |
| Configure Damage As Constant | `configureDamageAsConstant` | `bool` | – | – |
| Ignore Shield | `ignoreShield` | `bool` | – | – |
| Can Activate Reaction System Temporally | `canActivateReactionSystemTemporally` | `bool` | – | – |
| Damage Reaction ID | `damageReactionID` | `int` | -1 | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |
| Layer Mask | `layerMask` | `LayerMask` | – | – |
| Check Trigger Surfaces | `checkTriggerSurfaces` | `bool` | – | – |
| Check Objects With Multiple Damage Receivers Enabled | `checkObjectsWithMultipleDamageReceiversEnabled` | `bool` | true | – |

### Ignore Tags Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Ignore Tags | `useIgnoreTags` | `bool` | – | – |
| Tags To Ignore List | `tagsToIgnoreList` | `List<string>` | new List<string> (new string [] { "en… | – |

### Objects Detected Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Message On Damage Detected | `sendMessageOnDamageDetected` | `bool` | true | – |
| Message On Damage Detected Name | `messageOnDamageDetectedName` | `string` | "setDamageDetectedOnTriggerById" | – |
| Use Custom Object To Send Message | `useCustomObjectToSendMessage` | `bool` | – | – |
| Custom Object To Send Message | `customObjectToSendMessage` | `GameObject` | – | – |
| Send Message On Surface With No Damage Detected | `sendMessageOnSurfaceWithNoDamageDetected` | `bool` | – | – |
| Message On Surface With No Damage Detected Name | `messageOnSurfaceWithNoDamageDetectedName` | `string` | "setNoDamageDetectedOnTriggerById" | – |
| Store Detected Object On List | `storeDetectedObjectOnList` | `bool` | – | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Surfaces For Decals | `checkSurfacesForDecals` | `bool` | – | – |
| Raycast Distance | `raycastDistance` | `float` | – | – |

### Push Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Force Multiplier | `addForceMultiplier` | `float` | – | – |
| Force Mode | `forceMode` | `ForceMode` | ForceMode.Impulse | – |
| Apply Impact Force To Vehicles | `applyImpactForceToVehicles` | `bool` | true | – |
| Impact Force To Vehicles Multiplier | `impactForceToVehiclesMultiplier` | `float` | 0.2f | – |
| Use Push Character | `usePushCharacter` | `bool` | – | – |
| Push Character Function Name | `pushCharacterFunctionName` | `string` | "pushCharacter" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Currently Enabled | `currentlyEnabled` | `bool` | – | – |
| Current Combat Type Index | `currentCombatTypeIndex` | `int` | – | – |
| Current Attack Index | `currentAttackIndex` | `int` | – | – |
| Damage Applied In Last Attack | `damageAppliedInLastAttack` | `bool` | – | – |
| Trigger Id | `triggerId` | `int` | – | – |
| Detect Surface State Active | `detectSurfaceStateActive` | `bool` | – | – |
| Use Cast All Damage Detection | `useCastAllDamageDetection` | `bool` | – | – |
| Detected Object List | `detectedObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| Ignore Detected Objects On List | `ignoreDetectedObjectsOnList` | `bool` | – | – |
| Custom Force Amount | `customForceAmount` | `float` | – | – |
| Custom Force To Vehicles Multiplier | `customForceToVehiclesMultiplier` | `float` | – | – |
| Custom Force Mode | `customForceMode` | `ForceMode` | – | – |
| Custom Force Mode Active | `customForceModeActive` | `bool` | – | – |
| Ignore Object List Active | `ignoreObjectListActive` | `bool` | – | – |
| Object To Ignore List | `objectToIgnoreList` | `List<GameObject>` | new List<GameObject> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Detect Surface State Active | `eventOnDetectSurfaceStateActive` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Player | `currentPlayer` | `GameObject` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Main Box Collider | `mainBoxCollider` | `BoxCollider` | – | – |
| Main Sphere Collider | `mainSphereCollider` | `SphereCollider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 有効時のみ`isEnter`が真なら、接触したオブジェクトを`checkObjectDetected`へ渡す。 |
| `checkObjectDetection(GameObject objectDetected, bool isTrigger)` | 除外リスト・タグ・レイヤー・自分自身・トリガー設定を判定し、攻撃対象になり得るかを返す。 |
| `checkObjectDetected(GameObject objectDetected, bool isTrigger)` | 検出対象をリストへ登録し、デカール・ダメージ・押し出し・力を順に適用、検出イベントも発火する。 |
| `checkDamageToApplyOnObject(GameObject objectToDamage)` | `activateDamage`でダメージを与え、送信設定に応じてメッセージ送信や最終攻撃フラグを更新する。 |
| `checkPushCharactersOnObject(GameObject objectToDamage)` | 押し出しが有効なら、対象キャラへプレイヤー前方ベクトルで押し出しメッセージを送る。 |
| `setCustomForceDirection(Vector3 newValue)` | 次回攻撃で力を加える方向を設定するだけ。 |
| `setCustomForceAmount(float newValue)` | 次回攻撃で使う力の量`customForceAmount`を設定するだけ。 |
| `setCustomForceMode(ForceMode newForceMode)` | `customForceMode`を設定し、カスタム`ForceMode`を有効化する。 |
| `removeCustomForceMode()` | カスタム`ForceMode`の有効フラグを下ろすだけ。 |
| `setIgnoreForcesToApplyOnAttackActiveState(bool state)` | 攻撃時に力を適用しないフラグを設定するだけ。 |
| `setCustomForceToVehiclesMultiplier(float newValue)` | 乗り物へ加える力の倍率を設定するだけ。 |
| `setAddForceMultiplierValue(float newValue)` | 通常攻撃で加える力の倍率`addForceMultiplier`を設定するだけ。 |
| `checkForceToApplyOnObject(GameObject objectToDamage)` | 対象の`Rigidbody`へ方向と量から求めた力を加え、乗り物には専用倍率を掛ける。 |
| `checkDecalsToApplyOnObject(GameObject objectToDamage)` | 本体はコメントのみで何もせず、デカール適用処理は未実装。 |
| `getLastSurfaceDetected()` | 直前に検出したサーフェスの`GameObject`を返すだけ。 |
| `setLastSurfaceDetected(GameObject newSurface)` | 直前検出サーフェスとして設定するだけ。 |
| `getOwner(GameObject ownerObject)` | `currentPlayer`を設定し、メインコライダーを取得して所有者との衝突を無視する。 |
| `getMainCollider()` | メインコライダーを取得して返す。 |
| `setMainColliderEnabledState(bool state)` | メインコライダーが存在すれば、その`enabled`を指定状態に切り替える。 |
| `reloadMainColliderEnabled()` | メインコライダーを一度無効化してから再度有効化する。 |
| `setCurrentState(bool value)` | 有効フラグを設定し、押し出し・ダメージ・力の各フラグをリセットして検出リストを空にする。 |
| `setIgnoreDetectedObjectsOnListState(bool state)` | 検出済みリストを無視するフラグを設定するだけ。 |
| `setConfigureDamageAsConstant(bool state)` | ダメージを一定値として扱うフラグを設定するだけ。 |
| `setUseCastAllDamageDetectionState(bool state)` | 真なら球/ボックス範囲を即座に全検出して処理し、フラグを戻す。 |
| `setNewHitDamage(float newValue)` | 1回の攻撃の基本ダメージ`hitDamage`を設定するだけ。 |
| `setIgnoreShieldState(bool state)` | シールドを無視するフラグを設定するだけ。 |
| `setCurrentExtraDamageValue(float extraDamageValue)` | ダメージ倍率を設定し、0以下なら1に補正する。 |
| `activePushCharacterOnce()` | 次の1回だけキャラを押し出すフラグを立てるだけ。 |
| `deactivatePushCHaracterOnce()` | 1回限りの押し出しフラグを下ろすだけ。 |
| `setUsePushCharacterState(bool state)` | 常時キャラ押し出しの有効フラグを設定するだけ。 |
| `setCurrentAttackInfoIndex(int combatTypeIndex, int attackIndex)` | 現在のコンバット種別と攻撃のインデックスを設定するだけ。 |
| `getDamageAppliedInLastAttackState()` | 直前の攻撃でダメージが入ったかどうかを返すだけ。 |
| `setDetectSurfaceStateActive(bool state)` | サーフェス検出イベントの発火待ちフラグを設定するだけ。 |
| `isDetectSurfaceStateActive()` | サーフェス検出イベント待ちかどうかを返すだけ。 |
| `activateDamage(GameObject objectToDamage)` | `applyDamage.checkCanBeDamaged`を呼び出し、ダメージ適用の可否を返す。 |
| `getLastDamageApplied()` | 直近攻撃のダメージ量（基本値×倍率）を返す。 |
| `setCustomDamageCanBeBlockedState(bool state)` | ダメージがブロック可能かを設定し、デバッグ時のみログを出す。 |
| `setTriggerId(int newValue)` | トリガーIDを設定するだけ。 |
| `setTriggerIdOnEditor(int newValue)` | トリガーIDを設定してから、エディタ用にコンポーネントを更新する。 |
| `setCheckTriggerSurfacesState(bool state)` | トリガー同士の接触も検出するかを設定するだけ。 |
| `setCustomObjectToSendMessage(GameObject newObject)` | メッセージ送信先のカスタムオブジェクトを設定するだけ。 |
| `setCustomLayerMask(LayerMask newLayerMask)` | 検出に使う`LayerMask`を設定するだけ。 |
| `setCustomTagsToIgnore(List<string> newTagList)` | 無視タグ一覧を設定し、nullならタグ無視を無効化してリストを空にする。 |
| `setSendMessageOnDamageDetectedState(bool state)` | ダメージ検出時のメッセージ送信フラグを設定するだけ。 |
| `setCanActivateReactionSystemTemporallyState(bool state)` | リアクションシステムの一時有効化フラグを設定するだけ。 |
| `setNewDamageReactionID(int newValue)` | ダメージリアクションIDを設定するだけ。 |
| `setNewDamageTypeID(int newValue)` | ダメージ種別IDを設定するだけ。 |
| `setNewSphereColliderTriggerRadius(float newValue)` | 球コライダーがあれば、その半径を新しい値に変更する。 |
| `setNewBoxColliderTriggerSize(Vector3 newValue)` | ボックスコライダーがあれば、そのサイズを新しい値に変更する。 |
| `addOrRemoveObjectToIgnore(GameObject newObject, bool state)` | 対象を無視リストへ追加/削除し、リストが空かどうかで無視有効フラグを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`でこのコンポーネントを更新し、シーンをダーティにする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnDetectSurfaceStateActive` | `UnityEvent` | – |
