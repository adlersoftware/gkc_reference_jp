# playerWeaponsManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/playerWeaponsManager.cs:8`

**概要**: プレイヤーの武器（`IKWeaponSystem`）一覧を保持し、抜刀・納刀、照準、射撃、両手武器、リロード、HUD、アタッチメント、耐久値をまとめて管理する MonoBehaviour。入力系メソッドは入力管理から呼ばれる入口で、Editor 系はインスペクタ操作を補助する。

**公式ドキュメント抜粋**（[Player Weapons Manager](../../docs/player-controller-components/player-controller/player-weapons-manager.md)）

> Used to manage and configure all the weapons used on the character, including changing between them, activate/deactivate each one according to if the player equips them or not, edit its attachments and all the regular actions on fire weapons, like reload, fire, drop or pick weapons, etc.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Single Weapon State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current IK Weapon | `currentIKWeapon` | `IKWeaponSystem` | – | 現在使用中の片手武器コンポーネント。 |

### Dual Weapon State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Right IK Weapon | `currentRightIKWeapon` | `IKWeaponSystem` | – | 二丁持ち時の右手側で使用中の武器。 |
| Current Left Ik Weapon | `currentLeftIkWeapon` | `IKWeaponSystem` | – | 二丁持ち時の左手側で使用中の武器。 |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapons Slots Amount | `weaponsSlotsAmount` | `int` | – | 武器スロットの総数で番号キーの範囲を決める。 / 表示条件: `showMainSettings` がオンのとき |
| Weapons Layer | `weaponsLayer` | `string` | – | 一人称で武器モデルに設定するレイヤー名。 / 表示条件: `showMainSettings` がオンのとき |
| Set Weapon When Picked | `setWeaponWhenPicked` | `bool` | – | 拾った武器をその場で即座に装備する。 / 表示条件: `showMainSettings` がオンのとき |
| Can Grab Objects Carrying Weapons | `canGrabObjectsCarryingWeapons` | `bool` | – | 武器所持中でもオブジェクトを掴めるようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Draw Keep Weapon When Mode Changed | `drawKeepWeaponWhenModeChanged` | `bool` | – | 武器モード切替時に自動で抜刀・納刀する。 / 表示条件: `showMainSettings` がオンのとき |
| Change Weapons With Number Keys Active | `changeWeaponsWithNumberKeysActive` | `bool` | true | 数字キーで武器を切り替えられるようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Change Weapons With Mouse Wheel Active | `changeWeaponsWithMouseWheelActive` | `bool` | true | マウスホイールで武器を切り替えられるようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Change Weapons With Keys Active | `changeWeaponsWithKeysActive` | `bool` | true | キー操作で武器を切り替えられるようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Ignore Use Draw Keep Weapon Animation | `ignoreUseDrawKeepWeaponAnimation` | `bool` | – | 抜刀・納刀アニメーションを無視して即座に構える。 / 表示条件: `showMainSettings` がオンのとき |
| Force Weapon To Use Quick Draw Keep Weapon Active | `forceWeaponToUseQuickDrawKeepWeaponActive` | `bool` | – | 全武器でクイック抜刀・納刀を強制する。 / 表示条件: `showMainSettings` がオンのとき |
| Use Draw Keep Weapon Animation On All Weapons On FBA | `useDrawKeepWeaponAnimationOnAllWeaponsOnFBA` | `bool` | – | フルボディ時も全武器で抜刀アニメを使う。 / 表示条件: `showMainSettings` がオンのとき |

### Empty Ammo Current Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change To Next Weapon If Ammo Empty | `changeToNextWeaponIfAmmoEmpty` | `bool` | – | 弾切れ時に次の武器へ自動で切り替える。 / 表示条件: `showMainSettings` がオンのとき |
| Remove Current Weapon As Not Usable If Ammo Empty Enabled | `removeCurrentWeaponAsNotUsableIfAmmoEmptyEnabled` | `bool` | – | 弾切れの武器を使用不可にして落とす。 / 表示条件: `showMainSettings` がオンのとき |
| Use Event On Empty Ammo On Current Weapon | `useEventOnEmptyAmmoOnCurrentWeapon` | `bool` | – | 弾切れ時にイベントを実行する。 / 表示条件: `showMainSettings` がオンのとき |
| Event On Empty Ammo On Current Weapon | `eventOnEmptyAmmoOnCurrentWeapon` | `UnityEvent` | – | 弾切れ時に呼び出されるイベント。 / 表示条件: `showMainSettings.boolValue && useEventOnEmptyAmmoOnCurrentWeapon.boolValue` |

### Target Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Target To Damage Layer | `targetToDamageLayer` | `LayerMask` | – | 攻撃を当てる対象オブジェクトのレイヤー。 / 表示条件: `showMainSettings` がオンのとき |
| Target For Scorch Layer | `targetForScorchLayer` | `LayerMask` | – | 焦げ跡を付ける対象のレイヤー。 / 表示条件: `showMainSettings` がオンのとき |
| Use Custom Layer To Check | `useCustomLayerToCheck` | `bool` | – | 独自の対象レイヤーで判定を行う。 / 表示条件: `showMainSettings` がオンのとき |
| Custom Layer To Check | `customLayerToCheck` | `LayerMask` | – | 判定に使用する独自のレイヤー。 / 表示条件: `showMainSettings.boolValue && useCustomLayerToCheck.boolValue` |
| Use Custom Ignore Tags | `useCustomIgnoreTags` | `bool` | – | 指定タグのオブジェクトを攻撃対象から除外する。 / 表示条件: `showMainSettings` がオンのとき |

### Weapon HUD Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapons HUD Enabled | `weaponsHUDEnabled` | `bool` | true | 武器HUDの表示を有効にするフラグ。 / 表示条件: `showMainSettings` がオンのとき |
| Disable Weapons HUD After Delay Enabled | `disableWeaponsHUDAfterDelayEnabled` | `bool` | – | 一定時間後に武器HUDを自動で隠す。 / 表示条件: `showMainSettings` がオンのとき |
| Delay To Disable Weapons HUD | `delayToDisableWeaponsHUD` | `float` | 3 | 武器HUDを隠すまでの待ち時間（秒）。 / 表示条件: `showMainSettings.boolValue && disableWeaponsHUDAfterDelayEnabled.boolValue` |
| Show Remain Ammo Text | `showRemainAmmoText` | `bool` | true | HUDの弾数表示に残弾数も併記する。 / 表示条件: `showMainSettings` がオンのとき |

### Weapon Reticle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Cursor Active | `weaponCursorActive` | `bool` | true | 武器用カーソル（レティクル）を表示する。 / 表示条件: `showMainSettings` がオンのとき |
| Use Weapon Cursor Unable To Shoot Third Person | `useWeaponCursorUnableToShootThirdPerson` | `bool` | true | 三人称で射撃不可時に別カーソルを表示する。 / 表示条件: `showMainSettings` がオンのとき |
| Use Weapon Cursor Unable To Shoot First Person | `useWeaponCursorUnableToShootFirstPerson` | `bool` | – | 一人称で射撃不可時に別カーソルを表示する。 / 表示条件: `showMainSettings` がオンのとき |

### Weapon Management Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Fire Weapons Without Aiming | `canFireWeaponsWithoutAiming` | `bool` | – | エイムせずに射撃できるようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Draw Weapon If Fire Button Pressed | `drawWeaponIfFireButtonPressed` | `bool` | – | 射撃ボタンを押すと武器を抜く。 / 表示条件: `showMainSettings` がオンのとき |
| Draw And Aim Weapon If Fire Button Pressed | `drawAndAimWeaponIfFireButtonPressed` | `bool` | – | 射撃ボタンで抜刀とエイムを同時に行う。 / 表示条件: `showMainSettings` がオンのとき |
| Keep Weapon After Delay Third Person | `keepWeaponAfterDelayThirdPerson` | `bool` | – | 三人称で一定時間未使用なら納刀する。 / 表示条件: `showMainSettings` がオンのとき |
| Keep Weapon After Delay First Person | `keepWeaponAfterDelayFirstPerson` | `bool` | – | 一人称で一定時間未使用なら納刀する。 / 表示条件: `showMainSettings` がオンのとき |
| Keep Weapon Delay | `keepWeaponDelay` | `float` | – | 未使用のまま納刀するまでの秒数。 / 表示条件: `showMainSettings.boolValue && keepWeaponAfterDelayThirdPerson.boolValue \|\| keepWeaponAfterDelayFirstPerson.boolValue` |
| Use Quick Draw Weapon | `useQuickDrawWeapon` | `bool` | – | 抜刀・納刀をアニメーションなしで即座に行う。 / 表示条件: `showMainSettings` がオンのとき |
| Time To Stop Aim After Stop Firing | `timeToStopAimAfterStopFiring` | `float` | 0.85f | 射撃停止後にエイムを解除するまでの秒数。 / 表示条件: `showMainSettings` がオンのとき |
| Use Aim Camera On Free Fire Mode | `useAimCameraOnFreeFireMode` | `bool` | – | エイムなし射撃でもエイムカメラを使う。 / 表示条件: `showMainSettings` がオンのとき |
| Pivot Point Rotation Active | `pivotPointRotationActive` | `bool` | – | 武器のピボット点をカメラ方向へ回転させる。 / 表示条件: `showMainSettings` がオンのとき |
| Pivot Point Rotation Speed | `pivotPointRotationSpeed` | `float` | 2 | ピボット点の回転を補間する速度。 / 表示条件: `showMainSettings.boolValue && pivotPointRotationActive.boolValue` |
| Run When Aiming Weapon In Third Person | `runWhenAimingWeaponInThirdPerson` | `bool` | – | 三人称でエイム中も走れるようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Stop Run If Previously Not Running | `stopRunIfPreviouslyNotRunning` | `bool` | – | エイム解除時に元が非走行なら走りを止める。 / 表示条件: `showMainSettings.boolValue && runWhenAimingWeaponInThirdPerson.boolValue` |
| Run Also When Firing Without Aiming | `runAlsoWhenFiringWithoutAiming` | `bool` | – | エイムなし射撃でも走れるようにする。 / 表示条件: `showMainSettings.boolValue && runWhenAimingWeaponInThirdPerson.boolValue` |
| Can Jump While Aiming Third Person | `canJumpWhileAimingThirdPerson` | `bool` | true | 三人称エイム中にジャンプできる。 / 表示条件: `showMainSettings` がオンのとき |
| Can Aim On Air Third Person | `canAimOnAirThirdPerson` | `bool` | true | 空中でもエイムできるようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Stop Aiming On Air Third Person | `stopAimingOnAirThirdPerson` | `bool` | – | 空中にいる間はエイムを解除する。 / 表示条件: `showMainSettings` がオンのとき |
| Ignore Parent Weapon Outside Player Body When Not Active | `ignoreParentWeaponOutsidePlayerBodyWhenNotActive` | `bool` | – | 非使用時に武器を体の外へ付け替えない。 / 表示条件: `showMainSettings` がオンのとき |
| Keep Look At Target Active When Firing Without Aiming | `keepLookAtTargetActiveWhenFiringWithoutAiming` | `bool` | true | エイムなし射撃中もターゲット追従を維持する。 / 表示条件: `showMainSettings` がオンのとき |
| Use Camera Shake On Shoot Enabled | `useCameraShakeOnShootEnabled` | `bool` | – | 射撃時にカメラシェイクを発生させる。 / 表示条件: `showMainSettings` がオンのとき |
| Ignore New Animator Weapon ID Settings | `ignoreNewAnimatorWeaponIDSettings` | `bool` | true | 武器ごとのアニメーター武器ID設定を無視する。 / 表示条件: `showMainSettings` がオンのとき |
| Ignore Upper Body Rotation System | `ignoreUpperBodyRotationSystem` | `bool` | – | 上半身回転システムの制御を無視する。 / 表示条件: `showMainSettings` がオンのとき |
| Ignore Shake Upper Body Enabled | `ignoreShakeUpperBodyEnabled` | `bool` | – | 射撃時の上半身の揺れ演出を無効にする。 / 表示条件: `showMainSettings` がオンのとき |
| Full Body Awareness Weapons Parent Offset Position | `fullBodyAwarenessWeaponsParentOffsetPosition` | `Vector3` | new Vector3 (-0.0941f, -1.68f, 0) | フルボディ時の武器親の位置オフセット。 / 表示条件: `showMainSettings` がオンのとき |
| Override Option To Hide Weapon Mesh When Not Used | `overrideOptionToHideWeaponMeshWhenNotUsed` | `bool` | – | 武器ごとのメッシュ非表示設定を上書きする。 / 表示条件: `showMainSettings` がオンのとき |
| Hide Weapon Mesh When Not Used | `hideWeaponMeshWhenNotUsed` | `bool` | – | 未使用時に武器メッシュを隠す。 / 表示条件: `showMainSettings.boolValue && overrideOptionToHideWeaponMeshWhenNotUsed.boolValue` |

### Dual Wield Fire Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Dual Weapons Enabled | `activateDualWeaponsEnabled` | `bool` | true | 二丁持ち（デュアルウェポン）を有効にする。 / 表示条件: `showMainSettings` がオンのとき |
| Shoot Dual Weapons With Single Input Enabled | `shootDualWeaponsWithSingleInputEnabled` | `bool` | – | 片方の射撃入力で両方の武器を撃つ。 / 表示条件: `showMainSettings` がオンのとき |
| Aim Dual Weapons With Right Shoot Input Enabled | `aimDualWeaponsWithRightShootInputEnabled` | `bool` | – | 右射撃入力で二丁持ちのエイムを行う。 / 表示条件: `showMainSettings` がオンのとき |

### Weapons Collision Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Check Surface Collision Third Person | `ignoreCheckSurfaceCollisionThirdPerson` | `bool` | – | 三人称で武器と壁の衝突判定を無視する。 / 表示条件: `showMainSettings` がオンのとき |
| Ignore Check Surface Collision First Person | `ignoreCheckSurfaceCollisionFirstPerson` | `bool` | – | 一人称で武器と壁の衝突判定を無視する。 / 表示条件: `showMainSettings` がオンのとき |
| Use Extra Collider On Fire Weapon On FBA | `useExtraColliderOnFireWeaponOnFBA` | `bool` | – | フルボディ時に追加コライダーを使う。 / 表示条件: `showMainSettings` がオンのとき |
| Use Extra Collider On Fire Weapons On Third Person | `useExtraColliderOnFireWeaponsOnThirdPerson` | `bool` | – | 三人称でも追加コライダーを使う。 / 表示条件: `showMainSettings` がオンのとき |
| Extra Collider On Fire Weapon On FBA Transform | `extraColliderOnFireWeaponOnFBATransform` | `Transform` | – | 追加コライダーの位置合わせ用トランスフォーム。 / 表示条件: `showMainSettings.boolValue && useExtraColliderOnFireWeaponOnFBA.boolValue \|\| useExtraColliderOnFireWeaponsOnThirdPerson.boolValue` |
| Extra Collider On Fire Weapon On FBA | `extraColliderOnFireWeaponOnFBA` | `BoxCollider` | – | 体とのめり込みを防ぐ追加コライダー。 / 表示条件: `showMainSettings.boolValue && useExtraColliderOnFireWeaponOnFBA.boolValue \|\| useExtraColliderOnFireWeaponsOnThirdPerson.boolValue` |

### Weapons Input Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fire Weapons Input Active | `fireWeaponsInputActive` | `bool` | true | 射撃入力を受け付けるかどうか。 / 表示条件: `showMainSettings` がオンのとき |
| General Weapons Input Active | `generalWeaponsInputActive` | `bool` | true | 武器操作の入力全体を受け付けるか。 / 表示条件: `showMainSettings` がオンのとき |

### Objects Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Durability On Object Enabled | `checkDurabilityOnObjectEnabled` | `bool` | – | 武器の耐久度の管理を有効にする。 / 表示条件: `showMainSettings` がオンのとき |
| Use Event On Durability Empty On Melee Weapon | `useEventOnDurabilityEmptyOnMeleeWeapon` | `bool` | – | 近接武器の耐久切れでイベントを実行する。 / 表示条件: `showMainSettings` がオンのとき |
| Event On Durability Empty On Melee Weapon | `eventOnDurabilityEmptyOnMeleeWeapon` | `UnityEvent` | – | 耐久切れ時に呼び出すイベント。 / 表示条件: `showMainSettings.boolValue && useEventOnDurabilityEmptyOnMeleeWeapon.boolValue` |

### Inventory Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Store Picked Weapons On Inventory | `storePickedWeaponsOnInventory` | `bool` | – | 拾った武器をインベントリに保存する。 / 表示条件: `showMainSettings` がオンのとき |
| Draw Weapon When Picked | `drawWeaponWhenPicked` | `bool` | – | 拾った武器をすぐ手に持たせる。 / 表示条件: `showMainSettings` がオンのとき |
| Draw Picked Weapon Only It Not Previous Weapon Equipped | `drawPickedWeaponOnlyItNotPreviousWeaponEquipped` | `bool` | – | 未装備時のみ拾った武器を抜いて持つ。 / 表示条件: `showMainSettings` がオンのとき |
| Change To Next Weapon When Equipped | `changeToNextWeaponWhenEquipped` | `bool` | – | 装備時にその武器へ切り替える。 / 表示条件: `showMainSettings` がオンのとき |
| Change To Next Weapon When Unequipped | `changeToNextWeaponWhenUnequipped` | `bool` | – | 装備解除時に次の武器へ切り替える。 / 表示条件: `showMainSettings` がオンのとき |
| Not Activate Weapons At Start | `notActivateWeaponsAtStart` | `bool` | – | 開始時に武器を有効化しない設定。 / 表示条件: `showMainSettings` がオンのとき |
| Can Store Any Number Same Weapon | `canStoreAnyNumberSameWeapon` | `bool` | true | 同じ武器を複数所持できるようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Use Ammo From Inventory In All Weapons | `useAmmoFromInventoryInAllWeapons` | `bool` | – | 全武器でインベントリの弾薬を共有する。 / 表示条件: `showMainSettings` がオンのとき |

### Attachment Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Open Weapon Attachments Menu Enabled | `openWeaponAttachmentsMenuEnabled` | `bool` | true | アタッチメント編集メニューを開ける。 / 表示条件: `showMainSettings` がオンのとき |
| Set First Person For Attachment Editor | `setFirstPersonForAttachmentEditor` | `bool` | – | 編集時に一人称視点へ切り替える。 / 表示条件: `showMainSettings` がオンのとき |
| Use Universal Attachments | `useUniversalAttachments` | `bool` | – | アタッチメントを全武器で共有する。 / 表示条件: `showMainSettings` がオンのとき |
| Open Weapon Attachments Menu Paused | `openWeaponAttachmentsMenuPaused` | `bool` | – | メニューを開いたままゲームを止める。 / 表示条件: `showMainSettings` がオンのとき |

### Initial Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Game With Current Weapon | `startGameWithCurrentWeapon` | `bool` | – | 開始時に選択した武器を装備させる。 / 表示条件: `showMainSettings` がオンのとき |
| Draw Initial Weapon Selected | `drawInitialWeaponSelected` | `bool` | true | 開始時に選択武器を抜いて構える。 / 表示条件: `showMainSettings.boolValue && startGameWithCurrentWeapon.boolValue` |
| Start With First Weapon Available | `startWithFirstWeaponAvailable` | `bool` | – | 使用可能な最初の武器で開始する。 / 表示条件: `showMainSettings.boolValue && startGameWithCurrentWeapon.boolValue` |
| Start Game With Dual Weapons | `startGameWithDualWeapons` | `bool` | – | 二丁持ち状態でゲームを開始する。 / 表示条件: `startGameWithCurrentWeapon.boolValue && !startWithFirstWeaponAvailable.boolValue` |
| Start With Random Weapon | `startWithRandomWeapon` | `bool` | – | 開始武器を候補からランダムに選ぶ。 / 表示条件: `!startWithFirstWeaponAvailable.boolValue && avaliableWeaponList.arraySize > 0` |

### Drop Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Drop Weapons | `canDropWeapons` | `bool` | – | 任意の武器を落とせるようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Change To Next Weapon When Drop | `changeToNextWeaponWhenDrop` | `bool` | – | 武器を落としたら次へ切り替える。 / 表示条件: `showMainSettings` がオンのとき |
| Drop Weapon Force Third Person | `dropWeaponForceThirdPerson` | `float` | – | 三人称で武器を投げる力の大きさ。 / 表示条件: `showMainSettings` がオンのとき |
| Drop Weapon Force First Person | `dropWeaponForceFirstPerson` | `float` | – | 一人称で武器を投げる力の大きさ。 / 表示条件: `showMainSettings` がオンのとき |
| Hold Drop Button To Increase Force | `holdDropButtonToIncreaseForce` | `bool` | – | ボタン長押しで投げる力を強める。 / 表示条件: `showMainSettings` がオンのとき |
| Drop Increase Force Speed | `dropIncreaseForceSpeed` | `float` | – | 長押し時の投げる力の増加速度。 / 表示条件: `showMainSettings.boolValue && holdDropButtonToIncreaseForce.boolValue` |
| Max Drop Force | `maxDropForce` | `float` | – | 長押しで増やせる投げる力の上限。 / 表示条件: `showMainSettings.boolValue && holdDropButtonToIncreaseForce.boolValue` |
| Drop Weapon Inventory Objects Pickups | `dropWeaponInventoryObjectsPickups` | `bool` | – | 落とす武器をインベントリ用にする。 / 表示条件: `showMainSettings` がオンのとき |
| Throw Weapon In Camera Direction Enabled | `throwWeaponInCameraDirectionEnabled` | `bool` | – | カメラの向きへ武器を投げ飛ばす。 / 表示条件: `showMainSettings` がオンのとき |
| Check Aim On Throw Weapon State Enabled | `checkAimOnThrowWeaponStateEnabled` | `bool` | – | 投げる際に一時的にエイム状態へ切り替える。 / 表示条件: `showMainSettings` がオンのとき |
| Head Track Body Weight On Aim On Throw Weapon | `headTrackBodyWeightOnAimOnThrowWeapon` | `float` | 1 | 投げる際のヘッドトラックの強さ。 / 表示条件: `showMainSettings.boolValue && checkAimOnThrowWeaponStateEnabled.boolValue` |
| Custom Aim Reticle Name | `customAimReticleName` | `string` | "Reticle 1" | 投げる際に使うカスタムレティクル名。 / 表示条件: `showMainSettings.boolValue && checkAimOnThrowWeaponStateEnabled.boolValue` |

### Death Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Drop Current Weapon When Die | `dropCurrentWeaponWhenDie` | `bool` | – | 死亡時に現在使用中の武器を落とす。 / 表示条件: `showMainSettings` がオンのとき |
| Drop All Weapons When Die | `dropAllWeaponsWhenDie` | `bool` | – | 死亡時に所持武器を全て落とす。 / 表示条件: `showMainSettings` がオンのとき |
| Drop Weapons Only If Using | `dropWeaponsOnlyIfUsing` | `bool` | – | 使用中の武器だけを落とすようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Draw Weapon When Resurrect | `drawWeaponWhenResurrect` | `bool` | – | 復活時に自動で武器を構え直す。 / 表示条件: `showMainSettings` がオンのとき |

### Mark Targets Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Mark Targets | `canMarkTargets` | `bool` | – | ターゲットをマーキングできる。 / 表示条件: `showMainSettings` がオンのとき |

### Aim Assist Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Aim Assist In Third Person | `useAimAssistInThirdPerson` | `bool` | – | 三人称でエイムアシストを行う。 / 表示条件: `showMainSettings` がオンのとき |
| Use Aim Assist In First Person | `useAimAssistInFirstPerson` | `bool` | – | 一人称でエイムアシストを行う。 / 表示条件: `showMainSettings` がオンのとき |
| Use Max Distance To Camera Center Aim Assist | `useMaxDistanceToCameraCenterAimAssist` | `bool` | – | 画面中心からの距離制限を併用する。 / 表示条件: `showMainSettings` がオンのとき |
| Max Distance To Camera Center Aim Assist | `maxDistanceToCameraCenterAimAssist` | `float` | – | アシスト対象の画面中心からの最大距離。 / 表示条件: `showMainSettings.boolValue && useMaxDistanceToCameraCenterAimAssist.boolValue` |
| Use Aim Assist In Locked Camera | `useAimAssistInLockedCamera` | `bool` | true | ロックカメラでもエイムアシストする。 / 表示条件: `showMainSettings` がオンのとき |
| Aim Assist Look At Target Speed | `aimAssistLookAtTargetSpeed` | `float` | 4 | エイムアシストの照準移動速度。 / 表示条件: `showMainSettings` がオンのとき |

### Weapons Stats Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Multiplier Stat | `damageMultiplierStat` | `float` | 1 | 武器ダメージに掛ける倍率の値。 / 表示条件: `showMainSettings` がオンのとき |
| Extra Damage Stat | `extraDamageStat` | `float` | 0 | 武器ダメージに加算する固定値。 / 表示条件: `showMainSettings` がオンのとき |
| Spread Multiplier Stat | `spreadMultiplierStat` | `float` | 1 | 発射時の弾の拡散に掛ける倍率の値。 / 表示条件: `showMainSettings` がオンのとき |
| Fire Rate Multiplier Stat | `fireRateMultiplierStat` | `float` | 1 | 武器の発射レートに掛ける倍率の値。 / 表示条件: `showMainSettings` がオンのとき |
| Extra Reload Speed Stat | `extraReloadSpeedStat` | `float` | 1 | リロード速度に加算する補正値。 / 表示条件: `showMainSettings` がオンのとき |
| Magazine Extra Size Stat | `magazineExtraSizeStat` | `int` | 0 | マガジン容量に加算する弾の数。 / 表示条件: `showMainSettings` がオンのとき |

### Weapons Message Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cant Pick Weapon Message | `cantPickWeaponMessage` | `string` | – | 武器を拾えない時に表示する文言。 / 表示条件: `showMainSettings` がオンのとき / TextArea (1, 5) |
| Cant Drop Current Weapon Message | `cantDropCurrentWeaponMessage` | `string` | – | 武器を落とせない時に表示する文言。 / 表示条件: `showMainSettings` がオンのとき / TextArea (1, 5) |
| Cant Pick Attachment Message | `cantPickAttachmentMessage` | `string` | – | アタッチメントを拾えない時の文言。 / 表示条件: `showMainSettings` がオンのとき / TextArea (1, 5) |
| Weapon Message Duration | `weaponMessageDuration` | `float` | – | メッセージを表示し続ける秒数。 / 表示条件: `showMainSettings` がオンのとき |

### Weapons Mode Active Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | 武器モード切替時にイベントを実行する。 / 表示条件: `showMainSettings` がオンのとき |
| Even On State Enabled | `evenOnStateEnabled` | `UnityEvent` | – | 武器モード有効時に呼ぶイベント。 / 表示条件: `showMainSettings.boolValue && useEventsOnStateChange.boolValue` |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | 武器モード無効時に呼ぶイベント。 / 表示条件: `showMainSettings.boolValue && useEventsOnStateChange.boolValue` |

### Stolen Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapons Can Be Stolen From Character | `weaponsCanBeStolenFromCharacter` | `bool` | true | 他キャラクターに武器を奪われるようにする。 / 表示条件: `showMainSettings` がオンのとき |
| Use Event On Weapon Stolen | `useEventOnWeaponStolen` | `bool` | – | 武器を奪われた時にイベントを実行する。 / 表示条件: `showMainSettings` がオンのとき |
| Event On Weapon Stolen | `eventOnWeaponStolen` | `UnityEvent` | – | 武器を奪われた時に呼ぶイベント。 / 表示条件: `showMainSettings.boolValue && useEventOnWeaponStolen.boolValue` |

### Save/Load Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Load Current Player Weapons From Save File | `loadCurrentPlayerWeaponsFromSaveFile` | `bool` | – | 武器の状態をセーブから読み込む。 / 表示条件: `showMainSettings` がオンのとき |
| Save Current Player Weapons To Save File | `saveCurrentPlayerWeaponsToSaveFile` | `bool` | – | 武器の状態をセーブに書き込む。 / 表示条件: `showMainSettings` がオンのとき |
| Load Weapon Attachments Info From Save File | `loadWeaponAttachmentsInfoFromSaveFile` | `bool` | – | アタッチメント情報をセーブから読み込む。 / 表示条件: `showMainSettings` がオンのとき |
| Save Weapon Attachments Info To Save File | `saveWeaponAttachmentsInfoToSaveFile` | `bool` | – | アタッチメント情報をセーブに書き込む。 / 表示条件: `showMainSettings` がオンのとき |

### Touch Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Swipe Dist | `minSwipeDist` | `float` | – | スワイプで武器を切り替える最小距離。 / 表示条件: `showMainSettings` がオンのとき |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | AI操作キャラとして武器管理を初期化する。 / 表示条件: `showMainSettings` がオンのとき |

### Usable Weapon Prefab List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Usable Weapon Prefab Info List | `useUsableWeaponPrefabInfoList` | `bool` | – | プレハブ一覧から武器を自動生成する。 / 表示条件: `showWeaponsList` がオンのとき |

### Weapon Pocket List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Weapon Pocket Enabled | `useWeaponPocketEnabled` | `bool` | true | 武器ポケットによる持ち替え制限を有効にする。 / 表示条件: `showWeaponsList` がオンのとき |

### Position On Character Offset Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Offset Parent Third Person | `currentOffsetParentThirdPerson` | `Vector3` | – | 三人称武器の親に適用するオフセット値。 / 表示条件: `showWeaponsList` がオンのとき |

### HUD Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapons HUD | `weaponsHUD` | `GameObject` | – | 武器HUDのルートオブジェクト。 / 表示条件: `showElementSettings` がオンのとき |
| Single Weapon HUD | `singleWeaponHUD` | `GameObject` | – | 片手武器用HUDのオブジェクト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Weapon Name Text | `currentWeaponNameText` | `Text` | – | 現在の武器名を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Weapon Ammo Text | `currentWeaponAmmoText` | `Text` | – | 現在の弾数を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Use Remain Ammo Weapon Text | `useRemainAmmoWeaponText` | `bool` | – | 残弾数を別テキストに分けて表示する。 / 表示条件: `showElementSettings` がオンのとき |
| Remain Ammo Weapon Text | `remainAmmoWeaponText` | `Text` | – | 残弾数の表示に使用するテキスト。 / 表示条件: `showElementSettings.boolValue && useRemainAmmoWeaponText.boolValue` |
| Ammo Slider | `ammoSlider` | `Slider` | – | 現在の装弾数を示すスライダー。 / 表示条件: `showElementSettings` がオンのとき |
| Current Weapon Icon | `currentWeaponIcon` | `RawImage` | – | 現在の武器アイコンを表示する画像。 / 表示条件: `showElementSettings` がオンのとき |
| Attachment Panel | `attachmentPanel` | `GameObject` | – | アタッチメント情報の表示パネル。 / 表示条件: `showElementSettings` がオンのとき |
| Attachment Ammo Text | `attachmentAmmoText` | `Text` | – | アタッチメントの弾数を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Attachment Icon | `currentAttachmentIcon` | `RawImage` | – | アタッチメントのアイコン画像。 / 表示条件: `showElementSettings` がオンのとき |
| Dual Weapon HUD | `dualWeaponHUD` | `GameObject` | – | 二丁持ち用HUDのオブジェクト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Right Weapon Ammo Text | `currentRightWeaponAmmoText` | `Text` | – | 右手武器の弾数を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Right Attachment Panel | `rightAttachmentPanel` | `GameObject` | – | 右手武器のアタッチメントパネル。 / 表示条件: `showElementSettings` がオンのとき |
| Rigth Attachment Ammo Text | `rigthAttachmentAmmoText` | `Text` | – | 右手アタッチメントの弾数テキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Right Attachment Icon | `currentRightAttachmentIcon` | `RawImage` | – | 右手アタッチメントのアイコン。 / 表示条件: `showElementSettings` がオンのとき |
| Current Left Weapon Ammo Text | `currentLeftWeaponAmmoText` | `Text` | – | 左手武器の弾数を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Left Attachment Panel | `leftAttachmentPanel` | `GameObject` | – | 左手武器のアタッチメントパネル。 / 表示条件: `showElementSettings` がオンのとき |
| Left Attachment Ammo Text | `leftAttachmentAmmoText` | `Text` | – | 左手アタッチメントの弾数テキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Left Attachment Icon | `currentLeftAttachmentIcon` | `RawImage` | – | 左手アタッチメントのアイコン。 / 表示条件: `showElementSettings` がオンのとき |
| Weapons Parent | `weaponsParent` | `Transform` | – | 武器モデルを格納する親トランスフォーム。 / 表示条件: `showElementSettings` がオンのとき |
| Weapons Transform In First Person | `weaponsTransformInFirstPerson` | `Transform` | – | 一人称時の武器位置の基準トランスフォーム。 / 表示条件: `showElementSettings` がオンのとき |
| Weapons Transform In Third Person | `weaponsTransformInThirdPerson` | `Transform` | – | 三人称時の武器位置の基準トランスフォーム。 / 表示条件: `showElementSettings` がオンのとき |
| Third Person Parent | `thirdPersonParent` | `Transform` | – | 三人称時に武器をぶら下げる親。 / 表示条件: `showElementSettings` がオンのとき |
| First Person Parent | `firstPersonParent` | `Transform` | – | 一人称時に武器をぶら下げる親。 / 表示条件: `showElementSettings` がオンのとき |
| Camera Controller | `cameraController` | `Transform` | – | カメラ制御用トランスフォーム（現在は未使用）。 / 表示条件: `showElementSettings` がオンのとき |
| Weapons Camera | `weaponsCamera` | `Camera` | – | 一人称の武器を描画するカメラ。 / 表示条件: `showElementSettings` がオンのとき |
| Weapon Cursor | `weaponCursor` | `GameObject` | – | 武器カーソルのルートオブジェクト。 / 表示条件: `showElementSettings` がオンのとき |
| Cursor Rect Transform | `cursorRectTransform` | `RectTransform` | – | ロックカメラで使うカーソル位置。 / 表示条件: `showElementSettings` がオンのとき |
| Weapon Cursor Regular | `weaponCursorRegular` | `GameObject` | – | 通常時に表示する武器カーソル。 / 表示条件: `showElementSettings` がオンのとき |
| Weapon Cursor Aiming In First Person | `weaponCursorAimingInFirstPerson` | `GameObject` | – | 一人称エイム時に表示するカーソル。 / 表示条件: `showElementSettings` がオンのとき |
| Weapon Cursor Unable To Shoot | `weaponCursorUnableToShoot` | `GameObject` | – | 射撃不可時に表示するカーソル。 / 表示条件: `showElementSettings` がオンのとき |
| Weapon Custom Reticle | `weaponCustomReticle` | `GameObject` | – | カスタムレティクルのオブジェクト。 / 表示条件: `showElementSettings` がオンのとき |
| Weapons Message Window | `weaponsMessageWindow` | `GameObject` | – | 武器メッセージを表示するウィンドウ。 / 表示条件: `showElementSettings` がオンのとき |
| Main Object Transform Data | `mainObjectTransformData` | `objectTransformData` | – | 武器の位置と回転をコピーするデータ。 / 表示条件: `showElementSettings` がオンのとき |
| Temporal Parent For Weapons | `temporalParentForWeapons` | `Transform` | – | 武器を一時的に親子付けるためのトランスフォーム。 / 表示条件: `showElementSettings` がオンのとき |

### Player Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Manager | `pauseManager` | `menuPause` | – | ポーズメニューやカーソル表示を制御する `menuPause` の参照。 / 表示条件: `showElementSettings` がオンのとき |
| Player Screen Objectives Manager | `playerScreenObjectivesManager` | `playerScreenObjectivesSystem` | – | 目標マーカーを画面やマップに追加するシステムの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | カメラのFOV変更や一人称切替を扱うカメラの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Head Bob Manager | `headBobManager` | `headBob` | – | 発砲時に画面の揺れを加えるヘッドボブの参照。 / 表示条件: `showElementSettings` がオンのとき |
| Player Input | `playerInput` | `playerInputManager` | – | 移動軸やマウス入力を取得する入力管理の参照。 / 表示条件: `showElementSettings` がオンのとき |
| IK Manager | `IKManager` | `IKSystem` | – | 三人称で武器を構えるIK状態を制御する参照。 / 表示条件: `showElementSettings` がオンのとき |
| Player Manager | `playerManager` | `playerController` | – | デバイス使用中かなどプレイヤー状態を見る参照。 / 表示条件: `showElementSettings` がオンのとき |
| Upper Body Rotation Manager | `upperBodyRotationManager` | `upperBodyRotationSystem` | – | 上半身の回転や全身対応状態を制御する参照。 / 表示条件: `showElementSettings` がオンのとき |
| Head Track Manager | `headTrackManager` | `headTrack` | – | 頭部トラッキングの重みを切り替えるための参照。 / 表示条件: `showElementSettings` がオンのとき |
| Grab Objects Manager | `grabObjectsManager` | `grabObjects` | – | 所持中の物を落とす処理に使うグラブ管理の参照。 / 表示条件: `showElementSettings` がオンのとき |
| Player Inventory Manager | `playerInventoryManager` | `inventoryManager` | – | 武器スロットや所持品表示を更新する参照。 / 表示条件: `showElementSettings` がオンのとき |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | デバイスの使用状態を判定するための参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Collider | `mainCollider` | `Collider` | – | 落とした武器との衝突を無視するためのコライダー。 / 表示条件: `showElementSettings` がオンのとき |
| Ragdoll Manager | `ragdollManager` | `ragdollActivator` | – | ラグドールの各コライダーを取得するための参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | 照準やマーキングのレイキャスト起点となる位置。 / 表示条件: `showElementSettings` がオンのとき |
| Main Camera | `mainCamera` | `Camera` | – | 画面座標からレイを作るために使うカメラ。 / 表示条件: `showElementSettings` がオンのとき |
| Main Weapon List Manager | `mainWeaponListManager` | `weaponListManager` | – | 武器選択ウィンドウの表示を扱うリスト管理の参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Simple Sniper Sight System | `mainSimpleSniperSightSystem` | `simpleSniperSightSystem` | – | スナイパースコープの表示を切り替える参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Dynamic Reticle System | `mainDynamicReticleSystem` | `dynamicReticleSystem` | – | 武器ごとの動的レティクル表示を切り替える参照。 / 表示条件: `showElementSettings` がオンのとき |

### IK Hands Transform

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Right Hand Transform | `rightHandTransform` | `Transform` | – | 右手に武器を配置する基準となるトランスフォーム。 / 表示条件: `showElementSettings` がオンのとき |
| Left Hand Transform | `leftHandTransform` | `Transform` | – | 左手に武器を配置する基準となるトランスフォーム。 / 表示条件: `showElementSettings` がオンのとき |
| Right Hand Mount Point | `rightHandMountPoint` | `Transform` | – | 右手で武器を実際に親子付けるマウント位置。 / 表示条件: `showElementSettings` がオンのとき |
| Left Hand Mount Point | `leftHandMountPoint` | `Transform` | – | 左手で武器を実際に親子付けるマウント位置。 / 表示条件: `showElementSettings` がオンのとき |

### Debug Controls

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Log | `showDebugLog` | `bool` | – | 武器の状態遷移をコンソールに出力して確認できる。 / 表示条件: `showDebugSettings` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `carryingWeaponInThirdPerson` | `bool` | – | – |
| `carryingWeaponInFirstPerson` | `bool` | – | – |
| `aimingInThirdPerson` | `bool` | – | – |
| `aimingInFirstPerson` | `bool` | – | – |
| `shootingSingleWeapon` | `bool` | – | – |
| `shootingRightWeapon` | `bool` | – | – |
| `shootingLeftWeapon` | `bool` | – | – |
| `reloadingWithAnimationActive` | `bool` | – | – |
| `lastTimeReload` | `float` | – | – |
| `weaponsHUDCanBeActive` | `bool` | true | – |
| `currentWeaponName` | `string` | – | – |
| `currentRighWeaponName` | `string` | – | – |
| `currentLeftWeaponName` | `string` | – | – |
| `touching` | `bool` | – | – |
| `anyWeaponAvailable` | `bool` | – | – |
| `weaponsList` | `List<IKWeaponSystem>` | new List<IKWeaponSystem> () | – |
| `currentWeaponSystem` | `playerWeaponSystem` | – | – |
| `currentIKWeaponLocated` | `bool` | – | – |
| `customTagsToIgnoreList` | `List<string>` | new List<string> () | – |
| `weaponToStartName` | `string` | – | – |
| `avaliableWeaponList` | `string []` | – | – |
| `weaponToStartIndex` | `int` | – | – |
| `rightWeaponToStartName` | `string` | – | – |
| `leftWeaponToStartName` | `string` | – | – |
| `rightWeaponToStartIndex` | `int` | – | – |
| `leftWeaponToStartIndex` | `int` | – | – |
| `extraRotation` | `float` | – | – |
| `targetRotation` | `float` | – | – |
| `weaponPocketList` | `List<weaponPocket>` | new List<weaponPocket> () | – |
| `weaponsModeActive` | `bool` | – | – |
| `choosedWeapon` | `int` | 0 | – |
| `chooseDualWeaponIndex` | `int` | -1 | – |
| `changingWeapon` | `bool` | – | – |
| `keepingWeapon` | `bool` | – | – |
| `changingDualWeapon` | `bool` | – | – |
| `changingSingleWeapon` | `bool` | – | – |
| `usingFreeFireMode` | `bool` | – | – |
| `aimModeInputPressed` | `bool` | – | – |
| `mainInventoryManagerName` | `string` | "Main Inventory Manager" | – |
| `originalWeaponsCameraFov` | `float` | – | – |
| `originalWeaponsPositionThirdPerson` | `Vector3` | – | – |
| `originalWeaponsRotationThirdPerson` | `Quaternion` | – | – |
| `originalWeaponsPositionFirstPerson` | `Vector3` | – | – |
| `originalWeaponsRotationFirstPerson` | `Quaternion` | – | – |
| `editingWeaponAttachments` | `bool` | – | – |
| `usingDualWeapon` | `bool` | – | – |
| `usingDualWeaponsPreviously` | `bool` | – | – |
| `currentRightWeaponSystem` | `playerWeaponSystem` | – | – |
| `currentLeftWeaponSystem` | `playerWeaponSystem` | – | – |
| `currentRightIKWeaponLocated` | `bool` | – | – |
| `currentLeftIkWeaponLocated` | `bool` | – | – |
| `externalSpreadMultiplier` | `float` | 0 | – |
| `useForwardDirectionOnLaserAttachments` | `bool` | – | – |
| `weaponListCount` | `int` | – | – |
| `usableWeaponPrefabInfoList` | `List<usableWeaponPrefabInfo>` | new List<usableWeaponPrefabInfo> () | – |
| `pivotPointRotationActiveOnCurrentWeapon` | `bool` | – | – |
| `avoidShootCurrentlyActive` | `bool` | – | – |
| `activateWaitOnDrawWeaponWithAnimationOnThirdPerson` | `bool` | – | – |
| `fullBodyAwarenessActive` | `bool` | – | – |
| `fullBodyAwarenessActiveOnStart` | `bool` | – | – |
| `currentPivotCameraTransform` | `Transform` | – | – |
| `showMainSettings` | `bool` | – | – |
| `showElementSettings` | `bool` | – | – |
| `showWeaponsList` | `bool` | – | – |
| `showDebugSettings` | `bool` | – | – |
| `firstPersonActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializePlayerWeaponsValues()` | `weaponsParent` を視点に合わせた親へ付け替え、武器リストを整理して初期武器の有効状態とキー番号を設定する。 |
| `enableOrDisableWeaponsCamera(bool state)` | `weaponsCamera` が未取得なら取り直し、その `enabled` を `state` に切り替えるだけ。 |
| `resetInitialWeaponCheckedOnCharacterSpawn()` | `initialWeaponChecked` を false にして初期武器の再チェックを許可するだけ。 |
| `checkWeaponToSelectOnQuickAccessSlots(string weaponName, bool changeToWeaponWithoutDoubleSelection)` | リロード中や武器移動中でなければ `weaponName` に一致する有効武器を探し、`checkWeaponToChangeByIndex` で切り替えて成否を返す。 |
| `checkPlayerIsNotCarringWeapons()` | 武器が無い場合、またはリロード・武器移動・ポーズ中でなければ true を返す。 |
| `checkInitialWeapon()` | 開始時武器設定に従いランダムや指定名で初期武器を決め、必要なら抜いてスロット表示と選択アイコンを更新する。 |
| `setTouchingMenuPanelState(bool state)` | `fingerPressingTouchPanel` を設定するだけ。 |
| `checkWeaponToChangeByIndex(IKWeaponSystem currentWeaponToCheck, int keyNumberToCheck, int weaponSlotIndex, int weaponIndex)` | 対象武器が二丁か単一かで分岐し、`changeDualWeapons` や `changeSingleWeapon`、`setChangingWeaponState` を呼んで切り替える。 |
| `checkShowWeaponSlotsParentWhenWeaponSelected(int weaponSlotIndex)` | インベントリ使用時のみ `playerInventoryManager.showWeaponSlotsParentWhenWeaponSelected` に転送する。 |
| `checkForDisableFreeFireModeAfterStopFiring()` | 三人称エイム中で射撃後キープ設定がある場合、`lastTimeFired` から一定時間経過で `disableFreeFireModeAfterStopFiring` を呼ぶ。 |
| `disableFreeFireModeAfterStopFiring()` | FBA でなければカメラ体重を戻し、射撃後キープのフラグを下ろして `aimCurrentWeaponInput` でエイムを解除する。 |
| `stopShootingFireWeaponIfActive()` | 武器所持かつ射撃中なら発射とエイムをリセットし、`setHoldShootWeaponState(false)` にして true を返す。 |
| `stopShootingFireWeaponIfActiveWithoutChangingAimState()` | `ignoreDisableAimModeIfActive` を立ててから `stopShootingFireWeaponIfActive` を呼び、エイム状態を変えずに射撃を止める。 |
| `resetWeaponFiringAndAimingIfPlayerDisabled()` | 武器モード中なら `disableFreeFireModeState` を呼び、単一/二丁それぞれの発射を false にして停止する。 |
| `setWeaponsJumpStartPositionState(bool state)` | ジャンプ位置を使う現在武器に `setPlayerOnJumpStartState(state)` を伝える。 |
| `setWeaponsJumpEndPositionState(bool state)` | ジャンプ位置を使う現在武器に `setPlayerOnJumpEndState(state)` を伝える。 |
| `disableWeaponJumpState()` | 二丁/単一の現在武器のジャンプ開始位置・終了位置状態をまとめて false にする。 |
| `setRunningState(bool state)` | `running` を設定するだけ。 |
| `isPlayerRunning()` | `running` を返すだけ。 |
| `isPlayerCrouching()` | `playerManager.isCrouching()` を返すだけ。 |
| `setPlayerRunningState(bool state, IKWeaponSystem IKWeaponToUse)` | 武器に走り状態を伝え、走行時は `newFovOnRun` へ、解除時は元のFOVへカメラFOVを変更し、ズーム中なら解除する。 |
| `disablePlayerRunningState()` | 現在武器が走り状態なら `setPlayerRunningState(false, ...)` を呼んで解除する。 |
| `resetPlayerRunningState()` | `playerRunningWithNewFov` を false にし、メインカメラFOVを元の値へ戻す。 |
| `isPlayerRunningWithNewFov()` | `playerRunningWithNewFov` を返すだけ。 |
| `useMeleeAttack()` | 射撃中でなければ現武器の `walkOrMeleeAttackWeaponPosition()` を呼び、近接攻撃用の位置へ移す。 |
| `checkMeleeAttackExternally()` | 射撃中でなければ現武器の `checkMeleeAttackExternally()` を呼ぶだけ。 |
| `isPlayerCarringWeapon()` | 二丁時は左右両方、単一時は現在武器の `isPlayerCarringWeapon()` を返す。 |
| `currentWeaponIsMoving()` | 二丁時は左右どちらかの `isWeaponMoving()`、単一時は現武器の移動状態を返す。 |
| `isWeaponHandsOnPositionToAim()` | 二丁時は左右、単一時は現武器がエイム位置に手を置いているかを返す。 |
| `isDrawingWeaponInProcess()` | 二丁時は左右、単一時は現武器が武器を抜く途中かどうかを返す。 |
| `isHolsteringWeaponInProcess()` | 二丁時は左右、単一時は現武器が武器をしまう途中かどうかを返す。 |
| `isdrawKeepWeaponAnimationInProcess()` | 二丁時は左右、単一時は現武器で抜き/しまいアニメーション中かどうかを返す。 |
| `checkIfWeaponStateIsBusy()` | 武器が移動中でなく所持済みなら false、それ以外は true を返す。 |
| `currentWeaponWithHandsInPosition()` | 現武器の `thirdPersonWeaponInfo.handsInPosition` を返す。 |
| `currentDualWeaponWithHandsInPosition(bool isRightWeapon)` | `isRightWeapon` に応じて右/左の二丁武器の `handsInPosition` を返す。 |
| `weaponsAreMoving()` | `changingWeapon` か `keepingWeapon` が立っていれば true を返す。 |
| `checkTypeView()` | `playerCameraManager` の一人称状態から `isThirdPersonView` を更新する。 |
| `setFirstPersonViewActiveState(bool state)` | `firstPersonActive` を設定するだけ。 |
| `checkIfFirstPersonActiveExternally()` | `firstPersonActive` を返すだけ。 |
| `isFirstPersonActive()` | `playerCameraManager.isFirstPersonActive()` を返すだけ。 |
| `isFullBodyAwarenessActive()` | `fullBodyAwarenessActive` を返すだけ。 |
| `setFullBodyAwarenessActiveState(bool state, bool settingInEditor, Transform pivotCameraTransform)` | FBA状態を設定し、武器親・手IK・上半身回転・ヘッドトラックを切り替え、射撃用コライダーと武器イベントも更新する。 |
| `updateFBAValues()` | 全武器の `updateFBAValues(true)` を呼び、`updateComponent(true)` で再初期化する。 |
| `checkAutoShootOnTag()` | カメラ前方へレイを飛ばし、対象のタグ/レイヤーが自動射撃対象なら `autoShootOnTagActive` を立て、外れたら解除する。 |
| `checkAvoidShootOnTag()` | カメラ前方の対象タグに応じて `avoidShootCurrentlyActive` を更新し、変化時のみ射撃可否と lower position を切り替える。 |
| `setCurrentWeaponCanMarkTargetsState(bool state)` | `currentWeaponCanMarkTargets` を設定するだけ。 |
| `setCurrentWeaponCanAutoShootOnTagState(bool state)` | `currentWeaponCanAutoShootOnTag` を設定するだけ。 |
| `setCurrentWeaponCanWeaponAvoidShootAtTagState(bool state)` | `currentWeaponCanWeaponAvoidShootAtTag` を設定するだけ。 |
| `checkIfCanMarkTargets()` | 照準先のタグ付きキャラを判定し、未登録なら `playerScreenObjectivesManager` にマーカーを追加して効果音を鳴らす。 |
| `addElementToPlayerList(GameObject obj, bool addMapIcon, bool useCloseDistance, float radiusDistance, bool showOffScreen, bool showMapWindowIcon, bool showDistanceInfo, bool showDistanceOffScreenInfo, string objectiveIconName, bool useCustomObjectiveColor, Color objectiveColor, bool removeCustomObjectiveColor, int buildingIndex, float iconOffset, bool addIconOnRestOfPlayers)` | 引数をそのまま `playerScreenObjectivesManager.addElementToPlayerList` へ渡すだけ。 |
| `removeLocatedEnemiesIcons(GameObject objectToRemove)` | `playerScreenObjectivesManager.removeElementFromListByPlayer` に転送するだけ。 |
| `shootWeapon(bool state)` | ビジーでなければ発射を開始/停止し、カーソル表示・走り解除・`lastTimeFired`・弾薬表示を更新する。 |
| `checkToUpdateInventoryWeaponAmmoText()` | `currentWeaponSystem` のキー番号を渡して `checkToUpdateInventoryWeaponAmmoTextByWeaponNumberKey` を呼ぶ。 |
| `checkToUpdateInventoryWeaponAmmoTextByWeaponNumberKey(int currentWeaponNumberKey)` | インベントリ管理かつ弾薬使用の武器で、スロット常時表示中なら `updateQuickAccesSlotAmount` で残弾表示を更新する。 |
| `shootDualWeapon(bool state, bool rightWeapon, bool shootBothWeapons)` | `rightWeapon`/`shootBothWeapons` に応じて左右の発射を開始/停止し、カーソル・走り・`lastTimeFired`・弾薬表示を更新する。 |
| `setShootingState(bool state)` | 二丁なら左右、単一なら単発の発射フラグを `state` にするだけ。 |
| `isCharacterShooting()` | 二丁なら左右の論理和、単一なら単発フラグを返す。 |
| `isShootingBurst()` | 現在武器の `isShootingBurst()` を返すだけ。 |
| `isTurnBasedCombatActionActive()` | `turnBasedCombatActionActive` を返すだけ。 |
| `setTurnBasedCombatActionActiveState(bool state)` | ターン制フラグを設定し、有効時は全武器の無限弾・リロード無視・弾薬消費無視をまとめて切り替える。 |
| `playerIsBusy()` | デバイス使用中や物理オブジェクト所持、アタッチメント編集、サブメニュー/メニュー表示中なら true を返す。 |
| `setLastTimeFired()` | `lastTimeFired` を現在時刻にし、`playerManager.setLastTimeFiring()` も呼ぶ。 |
| `setLastTimeUsed()` | `lastTimeWeaponUsed` を現在時刻にするだけ。 |
| `getLastTimeFired()` | `lastTimeFired` を返すだけ。 |
| `setLastTimeMoved()` | 二丁/単一の現在武器に `setLastTimeMoved()` を伝える。 |
| `setGamePausedState(bool state)` | `state` は使わず、`setLastTimeFired` と `setLastTimeMoved` で時刻を更新するだけ。 |
| `setUsingDeviceState(bool state)` | `state` は使わず、`setLastTimeFired` と `setLastTimeMoved` で時刻を更新するだけ。 |
| `getLastTimeAimWeapon()` | `lastTimeAimWeapon` を返すだけ。 |
| `cancelReloadIfActive()` | 現武器がリロード中なら `cancelReloadIfActive()` で中断させる。 |
| `setReloadingWithAnimationActiveState(bool state)` | `reloadingWithAnimationActive` を設定し、false のときは `lastTimeReload` を現在時刻にする。 |
| `isReloadingWithAnimationActive()` | `reloadingWithAnimationActive` を返すだけ。 |
| `setLastTimeReload()` | `lastTimeReload` を現在時刻にするだけ。 |
| `getLastTimeReload()` | `lastTimeReload` を返すだけ。 |
| `reloadingActionNotActive()` | `lastTimeReload` から0.8秒経過していなければ false、経過後は0に戻して true を返す。 |
| `setUsingNewWeaponID(bool state)` | `playerManager.setUsingNewWeaponID(state)` に転送するだけ。 |
| `setCurrentWeaponID(int newValue)` | 武器IDを設定し `playerManager.updateWeaponID()` で即時反映させる。 |
| `setCurrentWeaponIDSmoothly(int newValue)` | 武器IDを設定し `playerManager.updateWeaponIDSmoothly()` で補間反映させる。 |
| `setCurrentCrouchID(int newValue)` | `playerManager.setCurrentCrouchIDValue(newValue)` に転送するだけ。 |
| `setIgnoreUpperBodyRotationSystem(bool state)` | `ignoreUpperBodyRotationSystem` を設定するだけ。 |
| `setOriginalCameraBodyWeightValue()` | `headTrackManager` があれば `setOriginalCameraBodyWeightValue()` を呼ぶ。 |
| `isActionActiveInPlayer()` | `playerManager.isActionActive()` を返すだけ。 |
| `activateCustomAction(string actionName)` | `playerManager.activateCustomAction(actionName)` に転送するだけ。 |
| `setHeadBobShotShakeState(IKWeaponSystem.weaponShotShakeInfo newWeaponShotShakeInfo)` | `headBobManager.setShotShakeState` に射撃時のシェイク情報を渡す。 |
| `checkWeaponCameraShake(bool usingRightHandDualWeapon)` | 二丁/単一と視点・武器設定に応じて、`headBobManager` に一人称/三人称の射撃シェイクを設定する。 |
| `isPlayerOnGroundForWeapons()` | 接地中か、はしご・ウォールラン中なら true を返す。 |
| `setPauseCurrentWeaponSwayMovementInputActiveState(bool state)` | `pauseCurrentWeaponSwayMovementInputActive` を設定するだけ。 |
| `setWeaponSway()` | 移動/カメラ入力を取得し、接地・ポーズ・障害物状態を加味して現在武器の `setWeaponSway` に渡す。 |
| `checkNumberInput(int numberAmount)` | `playerInput.checkNumberInput(numberAmount)` の結果を返すだけ。 |
| `isPlayerOnGround()` | `playerOnGround` を返すだけ。 |
| `isPlayerMoving()` | `playerManager.isPlayerMoving(0)` を返すだけ。 |
| `isObstacleToAvoidMovementFound()` | `playerManager.isObstacleToAvoidMovementFound()` を返すだけ。 |
| `drawOrKeepWeaponInput()` | 現在の視点で未所持なら抜き、所持済みならしまうよう `drawOrKeepWeapon` を呼ぶ。 |
| `drawWeaponAIInput()` | 現在の視点で武器を所持していなければ `drawOrKeepWeapon(true)` を呼ぶ。 |
| `keepWeaponAIInput()` | 現在の視点で武器を所持していれば `drawOrKeepWeapon(false)` を呼ぶ。 |
| `drawOrKeepWeapon(bool state)` | 視点別の抜き/しまいを呼び、抜く際は弾薬とスロット表示を更新し、各種使用時刻を記録する。 |
| `aimCurrentWeaponWhenItIsReady(bool state)` | `aimWhenItIsReady` を設定し `stopAimWhenItIsReady` を false にするだけ。 |
| `stopAimCurrentWeaponWhenItIsReady(bool state)` | `stopAimWhenItIsReady` を設定し `aimWhenItIsReady` を false にするだけ。 |
| `drawCurrentWeaponWhenItIsReady(bool state)` | 武器使用中でなければ `drawWhenItIsReady` を設定するだけ。 |
| `keepCurrentWeaponWhenItIsReady(bool state)` | 武器を使用中でなければ `keepWhenItIsReady` を設定するだけ。 |
| `aimCurrentWeaponInput()` | 現在の視点のエイム状態を反転させて `aimCurrentWeapon` を呼ぶ。 |
| `aimCurrentWeapon(bool state)` | 視点別のエイム処理を呼び、`lastTimeFired` と `lastTimeWeaponUsed` を更新する。 |
| `drawOrKeepWeaponThirdPerson(bool state)` | 三人称で抜き/しまいを行い、クイック動作・カーソル・HUD・IK・エイム解除・武器位置をまとめて切り替える。 |
| `weaponReadyToMove()` | 現武器の `drawOrKeepWeaponThirdPerson(carryingWeaponInThirdPerson)` を呼ぶ。 |
| `dualWeaponReadyToMove(bool isRightWeapon)` | `isRightWeapon` に応じて右/左の二丁武器に `drawOrKeepWeaponThirdPerson` を呼ぶ。 |
| `grabWeaponWithNoDrawHand()` | 抜き手アニメーションなしで `IKManager.setIKWeaponState` によりIK武器状態を設定する。 |
| `weaponReadyToMoveDirectlyOnDrawHand()` | 現武器を `placeWeaponDirectlyOnDrawHand` で直接抜き手位置に配置する。 |
| `dualWeaponReadyToMoveDirectlyOnDrawHand(bool isRightWeapon)` | `isRightWeapon` に応じた二丁武器を `placeWeaponDirectlyOnDrawHand` で直接配置する。 |
| `enableOrDisableIKOnHands(bool state)` | 二丁/単一の現在武器の手IKを `state` に切り替える。 |
| `checkIfStopAimIfPlayerCantGetUpFromCrouch()` | しゃがみ解除不可の設定で立てない場合、三人称エイム中ならエイム入力とエイムを解除する。 |
| `aimOrDrawWeaponThirdPerson(bool state)` | 三人称のエイム切替で、手の位置やしゃがみを確認し、カーソル・HUD・IK・回転速度・エイムアシスト・走りを更新する。 |
| `setAimAssistInThirdPersonState()` | 三人称エイムアシスト設定に応じて `playerCameraManager` の注視対象・速度・ロックカメラ用カーソルを設定する。 |
| `setAimAssistInFirstPersonState()` | 一人称エイムアシスト設定に応じて注視速度・最大距離・注視対象の有効状態を設定する。 |
| `drawOrKeepWeaponFirstPerson(bool state)` | 一人称の抜き/しまいを行い、武器カメラ・HUD・弾薬・ズーム時FOV・IK・カーソルを更新する。 |
| `aimOrDrawWeaponFirstPerson(bool state)` | 一人称のエイム切替で、カーソル・HUD・カメラFOV・回転速度・照準状態・エイムアシストを更新する。 |
| `changeCameraFov(bool increaseFov)` | 走りを解除してズームを切り、`increaseFov` なら武器のエイムFOV、そうでなければ元のFOVへカメラを変更する。 |
| `changeWeaponsCameraFov(bool increaseFov, float targetFov, float speed)` | 既存コルーチンを止め、武器カメラFOVを目標値へ `speed` で補間するコルーチンを開始する。 |
| `setCurrentWeaponsParent(bool isFirstPerson)` | 視点切替時に所持武器をクイックでしまい/抜きし、武器親の付け替えとHUD・IK・手位置を更新する。 |
| `enableOrDisableWeaponsMesh(bool state)` | 全武器の `weaponGameObject` を `state` で SetActive する。 |
| `enableOrDisableCurrentWeaponsMesh(bool state)` | 武器使用中のみ、二丁/単一の現在武器の `weaponGameObject` を `state` で SetActive する。 |
| `enableOrDisableAllWeaponsMeshes(bool state)` | 全武器の `enableOrDisableWeaponMesh(state)` を呼ぶ。 |
| `enableOrDisableEnabledWeaponsMesh(bool state)` | 有効化済みの武器のみ `weaponGameObject` を `state` で SetActive する。 |
| `checkIfWeaponEnabledByName(string weaponName)` | `weaponName` と同名で有効な武器があれば true を返す。 |
| `canUseWeapons()` | `weaponsModeActive` を返すだけ。 |
| `chooseNextWeapon(bool isDroppingWeapon, bool checkIfMoreThanOneWeaponAvailable)` | キー番号を1つ進めて有効な次武器を探し `choosedWeapon` を決め、`checkIfChangeWeapon` で切り替える。 |
| `choosePreviousWeapon(bool isDroppingWeapon, bool checkIfMoreThanOneWeaponAvailable)` | キー番号を1つ戻して有効な前武器を探し `choosedWeapon` を決め、`checkIfChangeWeapon` で切り替える。 |
| `checkIfChangeWeapon(bool isDroppingWeapon)` | 所持状況とドロップ設定から切替可否を判断し、二丁はそのまま、単一は即時かクイック切替を選ぶ。 |
| `updateWeaponHUDInfo()` | 二丁/単一に応じて武器名・弾薬テキストと弾薬スライダーを更新し、HUD要素の表示も更新する。 |
| `updateElementsEnabledOnHUD()` | 武器設定に従い武器名・アイコン・弾薬スライダー・弾薬テキストの表示を切り替え、アイコン画像を設定する。 |
| `updateAmmo()` | 二丁/単一それぞれの残弾テキスト（無限時は Inf）と弾薬スライダー値を更新する。 |
| `getWeaponNameByAmmoName(string ammoName)` | 弾薬名（大文字小文字無視）に一致する武器名を返し、無ければ空文字を返す。 |
| `getWeaponAmmoNameByWeaponName(string weaponName)` | 武器名に一致する弾薬名を返し、無ければ空文字を返す。 |
| `getCurrentWeaponName()` | `currentWeaponName` を返すだけ。 |
| `getWeaponOriginalClipSize(string weaponName)` | `weaponName` の武器の初期装弾数を返し、見つからなければ -1 を返す。 |
| `canWeaponsBeStolenFromCharacter()` | `weaponsCanBeStolenFromCharacter` を返すだけ。 |
| `setCanWeaponsBeStolenFromCharacter(bool state)` | `weaponsCanBeStolenFromCharacter` を設定するだけ。 |
| `checkEventOnWeaponStolen()` | `useEventOnWeaponStolen` が有効なら `eventOnWeaponStolen` を発火する。 |
| `enableOrDisableWeaponsHUD(bool state)` | 武器HUD設定に応じて単一/二丁HUDを切り替え、本体表示と遅延非表示を制御して `weaponsHUDActive` を更新する。 |
| `isWeaponsHUDActive()` | `weaponsHUDActive` を返すだけ。 |
| `enableOrDisableHUD(bool state)` | HUDが有効なら本体表示と遅延非表示を制御し、`weaponsHUDCanBeActive` を `state` に更新する。 |
| `setWeaponsHUDEnabledState(bool state)` | `weaponsHUDEnabled` を設定するだけ。 |
| `checkDisableWeaponsHUDAfterDelay(bool state)` | 遅延非表示が有効なら既存コルーチンを止め、`state` なら一定時間後にHUDを消すコルーチンを開始する。 |
| `stopDisableWeaponsHUDAfterDelay()` | `disableWeaponHUDCoroutine` を停止するだけ。 |
| `resetLastAmountOfFiredProjectiles()` | 二丁/単一の現在武器の `resetLastAmountOfFiredProjectiles()` を呼ぶ。 |
| `getLastAmountOfFiredProjectiles()` | 二丁時は右武器の、単一時は現武器の最後の発射プロジェクタイル数を返す。 |
| `getCurrentWeapon()` | 名前が一致する武器を二丁/単一それぞれで探し、`currentIKWeapon` などの参照・名前・アタッチメントHUDを更新する。 |
| `setWeaponByElement(IKWeaponSystem weaponToConfigure)` | 指定武器だけを current にし、`choosedWeapon` を更新して `getCurrentWeapon` を呼ぶ。 |
| `checkAndSetWeaponsAvailable()` | セーブ読込設定を考慮し、最初に見つかった有効武器を current にして `choosedWeapon` を更新し true を返す。 |
| `setNextWeaponAvailableToIndex(int currentIndex)` | 指定インデックスの武器からキー番号を進めて有効武器を探し、見つかれば current にして true を返す。 |
| `setFirstWeaponAvailable()` | 最初に見つかった有効武器を current にし、他の武器は非currentにする。 |
| `setFirstWeaponWithLowerKeyNumber()` | 有効武器のうちキー番号が最小のものを current にし、他の武器は非currentにする。 |
| `checkIfWeaponsAvailable()` | 有効な武器が1つでもあれば true を返す。 |
| `checkIfUsableWeaponsPrefabListActive()` | 実行時生成リストを使用し、かつ要素が1つ以上あれば true を返す。 |
| `moreThanOneWeaponAvailable()` | 有効な武器が2つ以上あれば true を返す。 |
| `checkIfWeaponCanBePicked(string weaponName)` | 必要なら実行時に生成し、同名で未所持（無効）の武器があれば true を返す。 |
| `checkIfWeaponExists(string weaponName)` | `weaponName` と同名の武器がリストにあれば true を返す。 |
| `canStoreAnyNumberSameWeaponState()` | `canStoreAnyNumberSameWeapon` を返すだけ。 |
| `checkIfWeaponIsAvailable(string weaponName)` | `weaponName` と同名で有効な武器があれば true を返す。 |
| `hasAmmoLimit(string weaponName)` | 同名で有効な武器が弾薬上限設定を持つ場合に true を返す。 |
| `hasMaximumAmmoAmount(string weaponName)` | 同名で有効な武器が最大弾薬量に達している場合に true を返す。 |
| `getAmmoAmountToMaximumLimit(string weaponName)` | 同名で有効な武器の上限までの不足弾薬量を返し、無ければ -1 を返す。 |
| `AddAmmo(int amount, string weaponName)` | `weaponName` の武器に `amount` の弾薬を追加し、クイックアクセス枠と弾薬表示を更新する。 |
| `addAmmoToCurrentWeapon(float amount)` | 二丁/単一の現在武器に `amount` を加算し、スロット表示と弾薬表示を更新する。 |
| `addAmmoForAllWeapons(float amount)` | 有効な全武器に `amount` を加算し、各スロット表示を更新して最後に弾薬表示を更新する。 |
| `setKillInOneShootToAllWeaponsState(bool state)` | 全武器の `setKillOneShotState(state)` を呼ぶ。 |
| `enableOrDisableIKOnWeaponsDuringAction(bool state)` | 二丁/単一の現在武器のアクション中IKを `state` に切り替える。 |
| `setActionActiveState(bool state)` | 二丁/単一の現在武器に `setActionActiveState(state)` を伝える。 |
| `enableAllAttachmentsInCurrentWeapon()` | 二丁/単一の現在武器の全アタッチメントを `enableAllAttachments()` で有効化する。 |
| `enableWeaponByName(string weaponName)` | インベントリ管理ならピックアップを試み、そうでなければ `pickWeapon` で武器を有効化する。 |
| `getRightHandTransform()` | `rightHandTransform` を返すだけ。 |
| `getLeftHandTransform()` | `leftHandTransform` を返すだけ。 |
| `getRightHandMountPoint()` | `rightHandMountPoint` を返すだけ。 |
| `getLeftHandMountPoint()` | `leftHandMountPoint` を返すだけ。 |
| `setVisibleToAIState(bool state)` | `playerManager.setVisibleToAIState(state)` に転送するだけ。 |
| `externalForce(Vector3 direction)` | `playerManager.externalForce(direction)` に転送するだけ。 |
| `checkPlayerCanJumpWhenAimingState()` | エイム中ジャンプ不可の設定なら、三人称エイム中はジャンプを禁止し、それ以外は許可する。 |
| `addWeaponToListInRunTime(GameObject weaponObject, bool showDebugInfo, bool addingOnRunTime, bool weaponEnabledState)` | 武器を生成/初期化してプレイヤー・カメラ・手・親を設定し、`weaponsList` に追加、必要ならポケット登録と初期化を行う。 |
| `updateWeaponsParentsInRuntime(Transform parent, Animator mainAnimtor)` | 全武器に手のTransformを再設定し、`updateWeaponParentInRuntime` で新しい親とAnimatorを反映する。 |
| `checkWeaponStateOnEmptyAmmo()` | 弾切れ時に、設定に応じて現在武器をドロップするか `eventOnEmptyAmmoOnCurrentWeapon` を発火する。 |
| `changeToNextWeaponWithAmmo()` | 二丁時は何もせず、弾切れ設定ならドロップ/イベント、そうでなければ弾薬のある次武器を探して切り替える。 |
| `addWeaponToSamePocket(string newWeaponName, string weaponToGetPocket)` | `weaponToGetPocket` が入っているポケットを探し、`newWeaponName` の武器を同じポケットに追加する。 |
| `addWeaponToPocketByPrefab(string newWeaponName, GameObject newWeaponObject)` | ポケット内で同名の武器スロットを `newWeaponObject` に差し替える。 |
| `removeAllWeaponsFromPocketList()` | 全ポケットの武器リストを `Clear()` するだけ。 |
| `removeAllNullWeaponsFromPocketList()` | 全ポケットの武器リストから null 要素を後ろから削除する。 |
| `selectWeaponOnListInEditor(int weaponIndex)` | 範囲内なら `selectObjectInEditor` で該当武器のGameObjectをエディタで選択する。 |
| `selectObjectInEditor(GameObject objectToUse)` | エディタ上で指定した `GameObject` を選択状態にするだけ。 |
| `checkSetExtraRotationCoroutine(bool state)` | 上半身の追加回転を目標角または0へ補間するコルーチンを開始し、非アクティブ時は即時反映する。 |
| `checkDualWeaponShakeUpperBodyRotationCoroutine(float extraAngleValue, float speedValue, bool isRightWeapon)` | 二丁時の発砲の揺れを、左武器では符号を反転して `upperBodyRotationManager` に依頼する。 |
| `checkShakeUpperBodyRotationCoroutine(float extraAngleValue, float speedValue)` | 上半身の揺れを `upperBodyRotationManager` に依頼する。無効フラグが立っていれば何もしない。 |
| `getCurrentWeaponRotation(IKWeaponSystem newWeapon)` | 武器ごとの追加回転・上半身の曲げ倍率・ターゲット可否を現在値として取り込む。 |
| `resetCurrentWeaponRotation(IKWeaponSystem weapon)` | 指定武器の `localEulerAngles` を0に戻すだけ。 |
| `checkUseCustomCameraStateOnAim()` | 武器設定に応じ、三人称エイム用のカスタムカメラ状態を `playerCameraManager` に登録する。 |
| `setIgnoreCrouchWhileWeaponActiveState(bool state)` | `ignoreCrouchWhileWeaponActive` フラグを設定するだけ。 |
| `isIgnoreCrouchWhileWeaponActive()` | `ignoreCrouchWhileWeaponActive` の値を返すだけ。 |
| `setPivotPointRotationActiveOnCurrentWeaponState(bool state)` | `pivotPointRotationActiveOnCurrentWeapon` フラグを設定するだけ。 |
| `isIgnoreNewAnimatorWeaponIDSettings()` | `ignoreNewAnimatorWeaponIDSettings` の値を返すだけ。 |
| `setIgnoreNewAnimatorWeaponIDSettingsState(bool state)` | `ignoreNewAnimatorWeaponIDSettings` フラグを設定するだけ。 |
| `activateOrDeactivateAimMode(bool state)` | エイム開始/終了に合わせ、カメラのエイム状態・上半身IK・回転ポイント・追加回転を切り替える。 |
| `setPauseUpperBodyRotationSystemActiveState(bool state)` | `pauseUpperBodyRotationSystemActive` フラグを設定するだけ。 |
| `setPauseRecoilOnWeaponActiveState(bool state)` | `pauseRecoilOnWeaponActive` フラグを設定するだけ。 |
| `isPauseRecoilOnWeaponActive()` | `pauseRecoilOnWeaponActive` の値を返すだけ。 |
| `setPauseWeaponReloadActiveState(bool state)` | `pauseWeaponReloadActive` フラグを設定するだけ。 |
| `isPauseWeaponReloadActive()` | `pauseWeaponReloadActive` の値を返すだけ。 |
| `setPauseWeaponAimMovementActiveState(bool state)` | `pauseWeaponAimMovementActive` フラグを設定するだけ。 |
| `isPauseWeaponAimMovementActive()` | `pauseWeaponAimMovementActive` の値を返すだけ。 |
| `enableOrDisableWeaponCursor(bool value)` | 視点とエイム状態、サイト使用の有無に応じて通常/エイム用レティクルを切り替え、動的レティクルも更新する。 |
| `checkUpdateReticleActiveState(bool state)` | `playerCameraManager` にレティクル有効状態を通知するだけ。 |
| `checkIfAnyReticleActive()` | いずれかのレティクルが表示中かを判定し、その結果をカメラマネージャへ通知する。 |
| `enableOrDisableWeaponCursorUnableToShoot(bool state)` | 射撃不可カーソルを表示/非表示し、元のレティクル状態を退避・復元する。 |
| `enableOrDisableGeneralWeaponCursor(bool state)` | `weaponCursor` の表示を切り替える。`weaponCursorActive` が偽なら常に非表示にする。 |
| `getGeneralWeaponCursorActiveSelfState()` | `weaponCursor` の `activeSelf` を返す。未設定なら false。 |
| `enableOrDisableRegularWeaponCursor(bool state)` | `weaponCursorRegular` の表示を状態に合わせて切り替えるだけ。 |
| `checkRegularCustomWeaponReticle(GameObject cursorToCheck, bool state, bool weaponReticleActive)` | 武器のカスタムレティクル/動的レティクルの表示とテクスチャを、エイム状態に合わせて切り替える。 |
| `checkIfWeaponIsOnSamePocket(string firstWeaponName, string secondWeaponName)` | 2つの武器が同じポケット（サブポケット）に入っているかを判定して返す。 |
| `pickWeapon(string weaponName)` | 未使用の武器を有効化し、同ポケットの武器を落として装備・持ち替えまで行い、成否を返す。 |
| `setEquippingPickedWeaponActiveState(bool state)` | `equippingPickedWeaponActive` フラグを設定するだけ。 |
| `equipWeapon(string weaponName, bool initializingInventory, bool equippingDualWeapon, string rightWeaponName, string lefWeaponName)` | 武器を有効化して装備し、同ポケットの武器を外して二丁/単品の持ち替えまで行い、`IKWeaponSystem` を返す。 |
| `unequipWeapon(string weaponName, bool unequippingDualWeapon, bool equipSingleWeaponDirectlyIfUsed)` | 指定武器を無効化してメッシュとIKを解除し、必要なら次の武器へ持ち替える。 |
| `checkEquipSingleWeaponAfterRemovingDualWeapon()` | 二丁解除後に装備待ちの単品武器があれば装備し、待機状態をクリアする。 |
| `checkTypeViewBeforeStart()` | `checkTypeView` を呼ぶだけのラッパー。 |
| `setDeadState(bool state)` | 死亡フラグを設定し、死亡時はカーソル固定と武器ドロップ、復活時は武器回転の再取得を行う。 |
| `isDrawWeaponWhenResurrectActive()` | `drawWeaponWhenResurrect` の値を返すだけ。 |
| `dropWeaponCheckingMinDelay()` | リロード中や移動中などを除外し、1秒の間隔を空けて `dropWeapon` を実行する。 |
| `dropWeapon()` | 現在の武器（二丁なら両方）をドロップし、失敗時はメッセージを表示する。 |
| `dropWeaponByBebugButton()` | デバッグボタン用に `dropWeaponCheckingMinDelay` を呼ぶだけ。 |
| `setIgnoreDropWeaponOnDeathState(bool state)` | `ignoreDropWeaponOnDeath` フラグを設定するだけ。 |
| `dropWeaponWhenPlayerDies()` | 死亡時ドロップの設定に従い、現在の武器または全武器をドロップする。 |
| `dropAllWeaponsExternally()` | 全武器ドロップの設定を強制的に有効にしてから `dropWeaponWhenPlayerDies` を実行する。 |
| `dropCurrentWeaponExternally()` | 武器モード中なら `dropWeapon` を呼ぶだけ。 |
| `dropCurrentWeaponExternallyWithoutResultAndDestroyIt()` | ドロップ時の武器プレハブ生成を一時的に抑止して `dropWeapon` を実行する。 |
| `dropCurrentWeapon(IKWeaponSystem weaponToDrop, bool ignoreRagdollCollision, bool checkChangeToNextWeapon, bool dropOnlyWeaponMesh, bool justKeepWeaponWithoutChangeToNext)` | 指定武器を投擲し、メッシュ・HUD・IKを解除して、必要なら次の武器へ切り替える。 |
| `dropCurrentDualWeapon(IKWeaponSystem weaponToDrop, bool ignoreRagdollCollision, bool checkChangeToNextWeapon)` | 二丁武器の両方を投擲し、二丁状態とHUD・IKを解除して、必要なら次の武器へ切り替える。 |
| `launchWeaponRigidbodyWhenDropWeapon(IKWeaponSystem weaponToDrop, bool dropOnlyWeaponMesh, bool ignoreRagdollCollision)` | ドロップ用ピックアップを生成して前方へ投擲し、生成物を `lastWeaponDroppedObject` に記録する。 |
| `getLastWeaponDroppedObject()` | 最後にドロップした武器オブジェクトを返すだけ。 |
| `activateSecondaryAction()` | 二丁時は左右両方、単品時は現在武器の `activateSecondaryAction` を呼ぶ。 |
| `activateSecondaryActionOnDownPress()` | 押下時に、左右または単品武器の `activateSecondaryActionOnDownPress` を呼ぶ。 |
| `activateSecondaryActionOnUpPress()` | 離した時に、左右または単品武器の `activateSecondaryActionOnUpPress` を呼ぶ。 |
| `activateSecondaryActionOnUpHold()` | 長押しを離した時に、左右または単品武器の `activateSecondaryActionOnUpHold` を呼ぶ。 |
| `activateForwardAcion()` | 二丁時は左右、単品時は現在武器の `activateForwardAcion` を呼ぶ。 |
| `activateBackwardAcion()` | 二丁時は左右、単品時は現在武器の `activateBackwardAcion` を呼ぶ。 |
| `disableCurrentWeapon()` | 持ち中の単品武器をしまい、エイム・IK・HUD・カーソル・カメラFOVを元に戻す。 |
| `disableCurrentDualWeapon()` | 二丁武器を両方しまい、二丁状態・エイム・IK・HUDを解除してカメラ設定を戻す。 |
| `checkIfDisableCurrentWeapon()` | 武器所持時、二丁なら `disableCurrentDualWeapon`、単品なら `disableCurrentWeapon` を呼ぶ。 |
| `resetWeaponHandIKWeight()` | `IKManager.resetWeaponHandIKWeight` を呼ぶだけ。 |
| `setGrabbingHandStateOnSingleHand(bool carryingWeapon, bool isRightHand, bool handInPosition)` | 片手の把持状態（武器有無・左右・位置合わせ）を `IKManager` にそのまま渡す。 |
| `getPlayerWeaponsManagerComponents(bool isFirstPerson)` | 武器関連の初期値を取得し、利用可能武器・現在武器・カメラFOV・タッチ判定を設定する。 |
| `getComponents()` | 一人称/三人称の武器トランスフォームの初期位置と回転を保存する。 |
| `resetWeaponsTransformInThirdPersonToPlayerPosition()` | 三人称武器トランスフォームをプレイヤーの位置と回転に合わせる。 |
| `resetWeaponsParentToPlayerPosition()` | `weaponsParent` をプレイヤーの位置と回転に合わせる。 |
| `updateWeaponsParentAndLocalPosition()` | 一人称/三人称（FBA時はピボットカメラ）に応じて `weaponsParent` の親を付け替え、初期値を再取得する。 |
| `getTemporalParentForWeapons()` | `temporalParentForWeapons` を返すだけ。 |
| `getPlayerManagersParentGameObject()` | プレイヤーマネージャの親オブジェクトの `Transform` を返す。 |
| `getWeaponsParent()` | `weaponsParent` を返すだけ。 |
| `getMainCameraTransform()` | 未取得ならカメラマネージャからメインカメラを取得し、その `Transform` を返す。 |
| `getMainCamera()` | 未取得ならカメラマネージャからメインカメラを取得して返す。 |
| `isUsingScreenSpaceCamera()` | `playerCameraManager.isUsingScreenSpaceCamera` を返すだけ。 |
| `isCameraPlacedInFirstPerson()` | `playerCameraManager.isCameraPlacedInFirstPerson` を返すだけ。 |
| `setLockedCameraActiveState(bool state)` | `lockedCameraActive` フラグを設定するだけ。 |
| `isCameraTypeFree()` | `lockedCameraActive` の否定を返すだけ。 |
| `getCurrentNormal()` | `playerManager.getCurrentNormal` を返すだけ。 |
| `isPlayerOnZeroGravityMode()` | `playerManager.isPlayerOnZeroGravityMode` を返すだけ。 |
| `getPlayerGameObject()` | `playerManager` の `GameObject` を返すだけ。 |
| `getMainCanvasSizeDelta()` | `playerCameraManager.getMainCanvasSizeDelta` を返すだけ。 |
| `changeCameraStateInPauseManager(bool state)` | `pauseManager.changeCameraState` を呼ぶだけ。 |
| `checkIfHideWeaponMeshWhenNotUsed(bool currentValue)` | 上書きフラグが有効ならこちらの設定値、無効なら引数の値を返す。 |
| `setWeaponsParent(bool isFirstPerson, bool settingInEditor, bool addingOnRunTime)` | 一人称/三人称に応じて武器の親・レイヤー・メッシュ表示・HUD位置を切り替える。 |
| `setWeaponPartLayer(GameObject weaponPart)` | 現在の視点で `setWeaponPartLayerFromCameraView` を呼ぶだけ。 |
| `setWeaponPartLayerFromCameraView(GameObject weaponPart, bool firstPersonActive)` | FBA以外で、武器パーツ以下のレイヤーを視点に応じて `Default` か武器レイヤーに変更する。 |
| `getExtraColliderOnFireWeaponOnFBA()` | `extraColliderOnFireWeaponOnFBA` を返すだけ。 |
| `pauseExtraColliderOnFireWeaponIfActive(bool state)` | 追加コライダーが有効な場合に、その `enabled` を切り替える。 |
| `isUsingWeapons()` | 一人称または三人称で武器を持っているかを返す。 |
| `isCarryingWeaponInThirdPerson()` | `carryingWeaponInThirdPerson` を返すだけ。 |
| `isCarryingWeaponInFirstPerson()` | `carryingWeaponInFirstPerson` を返すだけ。 |
| `isDrawKeepWeaponWhenModeChangedEnabled()` | `drawKeepWeaponWhenModeChanged` を返すだけ。 |
| `isAimingWeapons()` | 一人称/三人称いずれかでエイム中かを返す。 |
| `isAimingInThirdPerson()` | `aimingInThirdPerson` を返すだけ。 |
| `isAimingInFirstPerson()` | `aimingInFirstPerson` を返すだけ。 |
| `setWeaponToStartGame(string weaponName)` | `setWeaponByName` を呼ぶだけ。 |
| `setWeaponByName(string weaponName)` | 名前一致の武器を現在武器に設定し、`currentIKWeapon` と表示名を更新する。 |
| `getWeaponSystemByName(string weaponName)` | 名前一致の `playerWeaponSystem` を返す。見つからなければ null。 |
| `getWeaponIndexByName(string weaponName)` | 名前一致の武器インデックスを返す。見つからなければ -1。 |
| `changeCurrentWeaponByName(string weaponName)` | 名前一致の武器へ `checkWeaponToChangeByIndex` で持ち替える。 |
| `changeCurrentWeaponByNameCheckingIfReady(string weaponName)` | リロード中や移動中などでなければ、名前一致の武器へ持ち替える。 |
| `enableOrDisableGrabObjectsManager(bool state)` | 武器所持中の掴み許可がある時、掴みマネージャのエイム状態を切り替え、解除時は物を落とす。 |
| `setCanGrabObjectsCarryingWeaponsState(bool state)` | フラグを設定し、三人称エイム中なら掴みマネージャへ即時反映する。 |
| `setOriginalCanGrabObjectsCarryingWeaponsState()` | 保存しておいた元の掴み許可状態に戻すだけ。 |
| `setCarryingPhysicalObjectState(bool state)` | `carryingPhysicalObject` フラグを設定するだけ。 |
| `setShotCameraNoise(Vector2 noiseAmount)` | `playerCameraManager.setShotCameraNoise` に値を渡すだけ。 |
| `setShotCameraNoiseWithDuration(Vector2 noiseAmount, float duration)` | `playerCameraManager` にノイズ量と継続時間を渡すだけ。 |
| `setCameraPositionMouseWheelEnabledState(bool state)` | `playerCameraManager` のマウスホイールによるカメラ位置変更の可否を設定する。 |
| `isCheckDurabilityOnObjectEnabled()` | `checkDurabilityOnObjectEnabled` を返すだけ。 |
| `showCantPickAttacmentMessage(string attachmentName)` | アタッチメント名と取得不可メッセージを合成し、`showObjectMessage` で表示する。 |
| `showObjectMessage(string message, float messageDuration, GameObject messagePanel)` | 既存の表示コルーチンを止め、メッセージパネルに文言を出して指定時間後に閉じる。 |
| `getPlayerWeaponList()` | `weaponsList` をそのまま返すだけ。 |
| `getIKWeaponSystem(string weaponName)` | 名前一致の `IKWeaponSystem` を返す。見つからなければ null。 |
| `setDrawWeaponsPausedState(bool state)` | `drawWeaponsPaused` フラグを設定するだけ。 |
| `setWeaponsModeActive(bool state)` | 武器モードを切り替え、設定に応じて武器の出し入れとイベント通知、インベントリのスロット更新を行う。 |
| `checkIfDrawWeaponWithAnimationAfterAction()` | 三人称で現在武器がある場合、その武器の出しアニメ設定を待機フラグに反映する。 |
| `setActivateWaitOnDrawWeaponWithAnimationOnThirdPersonState(bool state)` | `activateWaitOnDrawWeaponWithAnimationOnThirdPerson` フラグを設定するだけ。 |
| `checkIfDrawSingleOrDualWeapon()` | 直前が二丁なら二丁を出し、そうでなければ現在武器を（アニメ待ちなら遅延して）出す。 |
| `checkIfKeepSingleOrDualWeapon()` | 武器を持っていれば二丁は維持・単品は出し入れし、持っていなければ現在の武器をしまう。 |
| `checkEventsOnStateChange(bool state)` | イベント使用時のみ、状態に応じて有効/無効イベントを発火する。 |
| `isWeaponsModeActive()` | `weaponsModeActive` を返すだけ。 |
| `isActivateDualWeaponsEnabled()` | `activateDualWeaponsEnabled` を返すだけ。 |
| `selectWeaponByName(string weaponName, bool drawSelectedWeapon)` | 名前一致の武器を選択し、必要なら持ち替えまたは出し入れを行う。 |
| `setCurrentRightIkWeaponByName(string weaponName)` | 名前一致の有効な武器を右武器として設定し、フラグを更新する。 |
| `setCurrentLeftIKWeaponByName(string weaponName)` | 名前一致の有効な武器を左武器として設定し、フラグを更新する。 |
| `keepDualWeapons()` | 左右武器の所持フラグを即時 true にしてから、左右の武器を出す処理を呼ぶ。 |
| `drawDualWeapons()` | 左右武器の所持フラグを即時 false にし、条件を満たせば左右の武器を出す。 |
| `drawDualWeaponsIfNotCarryingWeapons()` | 二丁未使用かつ条件を満たす時、在庫または一覧から相手武器を選んで二丁持ちに変更する。 |
| `removeWeaponConfiguredAsDualWeaponState(int keyNumberToSearch)` | 指定キー番号の有効な武器の二丁設定を解除する。 |
| `changeDualWeapons(string rightWeaponName, string lefWeaponName)` | 左右の武器名を設定し、二丁設定・所持状態・持ち替えフラグを更新する。 |
| `changeSingleWeapon(string singleWeaponName)` | 二丁状態を解除して単品へ切り替え、持ち替えフラグを立てる。 |
| `separateDualWeapons()` | 二丁状態と二丁設定を解除し、単品スロット情報を更新する。 |
| `disableDualWeaponStateOnWeapons()` | 左右武器とIKマネージャの二丁状態を解除する。 |
| `updateWeaponSlotInfo()` | 在庫保存時に二丁スロット情報と選択アイコンを更新する。 |
| `updateSingleWeaponSlotInfo()` | 在庫保存時に単品スロット情報と選択アイコンを更新する。 |
| `updateCurrentChoosedDualWeaponIndex()` | 使用中なら二丁/単品に応じた武器キー番号を `chooseDualWeaponIndex` に記録する。 |
| `checkIfWeaponUseAmmoFromInventory()` | 使用中なら、二丁の左右または単品武器の残弾を在庫から取得して設定する。 |
| `setWeaponRemainAmmoFromInventory(playerWeaponSystem weaponSystemToCheck)` | 在庫から残弾を使う武器なら、在庫数を0以上に丸めて残弾へ設定する。 |
| `useAmmoFromInventory(string weaponName, int amountToUse)` | `playerInventoryManager.useAmmoFromInventory` を呼ぶだけ。 |
| `isUseAmmoFromInventoryInAllWeaponsActive()` | `useAmmoFromInventoryInAllWeapons` を返すだけ。 |
| `getAllRemainAmmoOnWeapon(string weaponName)` | 名前一致武器の総残弾を返す。見つからなければ -1。 |
| `getWeaponAmmoAmountFromInventory(string weaponName)` | 名前一致武器の弾薬名で在庫数を返す。見つからなければ -1。 |
| `getNumberOfWeaponsAvailable()` | 有効な武器の数を数えて返す。 |
| `getCurrentWeaponSystem()` | `currentWeaponSystem` を返すだけ。 |
| `getCurrentWeaponTransform()` | 現在武器が有効ならその `Transform` を返し、なければ null。 |
| `isPlayerUsingWeapon(string weaponNameToCheck)` | 指定名が二丁の左右、または現在武器名と一致するかを返す。 |
| `editWeaponAttachmentsByCheckingBusyState()` | 移動・エイム・武器移動などの条件を満たす時だけ `editWeaponAttachments` を呼ぶ。 |
| `editWeaponAttachments()` | メニューやデバイス使用中などを除いてアタッチメント編集の開閉を切り替え、ポーズ状態を更新する。 |
| `openOrCloseWeaponAttachmentEditor(bool state, bool disableHUDWhenEditingAttachments)` | カーソル・HUD・ヘッドトラック・プレイヤー操作などを編集状態に合わせて切り替える。 |
| `cancelWeaponAttachmentEditor(bool disableHUDWhenEditingAttachments)` | 編集中なら編集状態を解除し、カーソルやカメラ・HUDなどを元に戻す。 |
| `setChangeTypeOfViewState()` | `playerCameraManager.changeTypeView` を呼ぶだけ。 |
| `getHeadColliderOnFBA()` | `playerCameraManager.getHeadColliderOnFBA` を返すだけ。 |
| `isEditinWeaponAttachments()` | `editingWeaponAttachments` を返すだけ。 |
| `isAimingWeaponInProcess()` | 武器モード中に、二丁の右または現在武器がエイム処理中かを返す。 |
| `checkPressedAttachmentButton(Button pressedButton)` | 押されたボタンを、二丁時は左右、単品時は現在武器のアタッチメントシステムへ渡す。 |
| `setAttachmentPanelState(bool state)` | `attachmentPanel` の表示を状態に合わせて切り替える。 |
| `setRightWeaponAttachmentPanelState(bool state)` | `rightAttachmentPanel` の表示を状態に合わせて切り替える。 |
| `setLeftWeaponAttachmentPanelState(bool state)` | `leftAttachmentPanel` の表示を状態に合わせて切り替える。 |
| `setAttachmentIcon(Texture attachmentIcon)` | `currentAttachmentIcon` のテクスチャを差し替える。 |
| `setAttachmentPanelAmmoText(string ammoText)` | `attachmentAmmoText` に弾薬テキストを設定する。 |
| `setCurrentWeaponSystemWithAttachment(playerWeaponSystem weaponToConfigure)` | アタッチメント操作用の対象武器を `currentWeaponSystemWithAttachment` に設定する。 |
| `assignCurrentWeaponSystemForAttachmentUsage()` | 現在武器があれば、その武器をアタッチメント操作用の対象に設定する。 |
| `setNumberKey(int newNumberKey)` | 対象武器の `numberKey` を設定する。対象がなければ何もしない。 |
| `setMagazineSize(int magazineSize)` | 対象武器のマガジンサイズを設定する。対象がなければ何もしない。 |
| `setOriginalMagazineSize()` | 対象武器のマガジンサイズを初期値に戻す。対象がなければ何もしない。 |
| `setSilencerState(bool state)` | 対象武器のサイレンサー状態を設定する。対象がなければ何もしない。 |
| `setAutomaticFireMode(bool state)` | 対象武器の自動射撃モードを設定する。対象がなければ何もしない。 |
| `setOriginalAutomaticFireMode()` | 対象武器の自動射撃モードを初期値に戻す。 |
| `setFireRate(float newFireRate)` | 対象武器の連射速度を設定する。対象がなければ何もしない。 |
| `setOriginalFireRate()` | 対象武器の連射速度を初期値に戻す。 |
| `setProjectileDamage(float newDamage)` | 対象武器の弾のダメージを設定する。対象がなければ何もしない。 |
| `setOriginalProjectileDamage()` | 対象武器の弾のダメージを初期値に戻す。 |
| `setBurstModeState(bool state)` | 対象武器のバーストモードを設定する。対象がなければ何もしない。 |
| `setBurstAmount(int newAmount)` | 対象武器のバースト発射数を設定する。対象がなければ何もしない。 |
| `setOriginalBurstMode()` | 対象武器のバースト設定を初期値に戻す。 |
| `setUsingSightState(bool state)` | 対象武器のサイト使用状態を設定する。対象がなければ何もしない。 |
| `setProjectileDamageMultiplier(float multiplier)` | 対象武器のダメージ倍率を設定する。対象がなければ何もしない。 |
| `setSpreadState(bool state)` | 対象武器の拡散状態を設定する。対象がなければ何もしない。 |
| `setOriginalSpreadState()` | 対象武器の拡散状態を初期値に戻す。 |
| `setExplosiveAmmoState(bool state)` | 対象武器の爆発弾設定を切り替える。対象がなければ何もしない。 |
| `setOriginalExplosiveAmmoState()` | 対象武器の爆発弾設定を初期値に戻す。 |
| `setDamageOverTimeAmmoState(bool state)` | 対象武器の継続ダメージ弾設定を切り替える。対象がなければ何もしない。 |
| `setOriginalDamageOverTimeAmmoState()` | 対象武器の継続ダメージ弾設定を初期値に戻す。 |
| `setRemoveDamageOverTimeAmmoState(bool state)` | 対象武器の継続ダメージ解除弾設定を切り替える。対象がなければ何もしない。 |
| `setOriginalRemoveDamageOverTimeAmmoState()` | 対象武器の継続ダメージ解除弾設定を初期値に戻す。ここだけ null チェックがない。 |
| `setSedateAmmoState(bool state)` | 対象武器の鎮静弾設定を切り替える。対象がなければ何もしない。 |
| `setOriginalSedateAmmoState()` | 対象武器の鎮静弾設定を初期値に戻す。 |
| `setPushCharacterState(bool state)` | アタッチメント付き現武器へ `state` を押し出し状態として転送するだけ。 |
| `setOriginalPushCharacterState()` | 現武器の押し出し状態を元の値に戻すよう転送するだけ。 |
| `setNewWeaponProjectile(GameObject newProjectile)` | 現武器の発射物プレハブを `newProjectile` に差し替えるだけ。 |
| `setOriginalWeaponProjectile()` | 現武器の発射物を元のプレハブへ戻すよう転送するだけ。 |
| `setProjectileWithAbilityState(bool newValue)` | 現武器の発射物アビリティ使用状態を `newValue` にするだけ。 |
| `setOriginalProjectileWithAbilityValue()` | 発射物のアビリティ使用状態を元の値へ戻すだけ。 |
| `enableOrDisableInfiniteAmmoOnAllWeapons(bool value)` | 武器リストを数え直し、全武器の `weaponSystemManager` に無限弾薬を設定する。 |
| `setOriginalInfiniteAmmo()` | 全武器の無限弾薬設定を元の値へ戻す。 |
| `setIgnoreReloadAnimationAndDelayActiveStateOnAllWeapons(bool state)` | 全武器にリロードアニメーションと待ち時間を無視する状態を設定する。 |
| `setIgnoreUseAmmoActiveStateOnAllWeapons(bool state)` | 全武器に弾薬消費を無視する状態を設定する。 |
| `pickupAttachment(string weaponName, string attachmentName)` | 同名武器、無ければ共通アタッチメント（両手持ち時は左右）に取得させ結果を返す。 |
| `isUseForwardDirectionOnLaserAttachmentsActive()` | `useForwardDirectionOnLaserAttachments` を返すだけ。 |
| `checkSniperSightUsedOnWeapon(bool state)` | スナイパーサイトシステムへ有効/無効を渡すだけ。 |
| `getIKSystem()` | `IKManager` を返すだけ。 |
| `startOverride()` | `overrideTurretControlState(true)` を呼ぶだけ。 |
| `stopOverride()` | `overrideTurretControlState(false)` を呼ぶだけ。 |
| `overrideTurretControlState(bool state)` | `usedByAI` を `state` の反転値にするだけ。 |
| `setUsedByAIState(bool state)` | `usedByAI` を `state` にするだけ。 |
| `lockOrUnlockCursor(bool state)` | `cursorLocked` を設定し、ポーズ・カメラ・HUD・カーソルなどの関連状態を一括切替する。 |
| `lockCursorAgain()` | カーソルが未ロックの時だけ `lockOrUnlockCursor(true)` を呼ぶ。 |
| `isCursorLocked()` | `cursorLocked` を返すだけ。 |
| `setPlayerControllerCurrentIdleIDValue(int newValue)` | `playerManager` に現在のアイドルIDを設定するだけ。 |
| `setPlayerControllerMovementValues(bool useNewCarrySpeed, float newCarrySpeed)` | `useNewCarrySpeed` が真なら一人称/三人称に応じ移動速度を `newCarrySpeed` にする。 |
| `setPlayerControllerCanRunValue(bool canRun)` | 一人称/三人称に応じ走行可否を `playerManager` に設定する。 |
| `setPlayerControllerMovementOriginalValues()` | 移動速度と走行可否を初期値に戻すよう `playerManager` に依頼する。 |
| `canUseCarriedWeaponsInput()` | 移動可・武器モード・非ビジー・武器を構えている等を満たすか判定する。 |
| `canUseWeaponsInput()` | 移動可・武器モード・非ビジー・武器使用可等を満たすか判定する。 |
| `quickDrawWeaponThirdPersonAction()` | しゃがみを解除し、三人称で武器を構える一連の処理（HUD/IK/カーソル/音）を行う。 |
| `quickKeepWeaponThirdPersonAction()` | 三人称の武器をしまう処理一式（HUD/IK/音/照準解除/カメラ速度復帰）を行う。 |
| `quicChangeWeaponThirdPersonAction()` | 武器をしまって持ち替え、再度構えて切替状態を解除する。 |
| `isUsingFreeFireMode()` | `usingFreeFireMode` か射撃後キープフラグのどちらかが真かを返す。 |
| `isAimingWeaponFromShootingActive()` | `aimingWeaponFromShooting` を返すだけ。 |
| `setAimingWeaponFromShootingState(bool state)` | `aimingWeaponFromShooting` を設定するだけ。 |
| `enableFreeFireModeState()` | キープ系フラグを偽にし、自身とプレイヤーのフリーファイア状態を真にする。 |
| `disableFreeFireModeState()` | フリーファイア関連フラグを偽にし、上半身回転・頭トラッキング・カメラ体重を戻す。 |
| `stopFreeFireOnDrawWeaponWithAnimation()` | フリーファイア中なら連射コルーチンを止め、射撃と照準をリセットする。 |
| `enableOrDisableIKUpperBodyExternally(bool state)` | 上半身IK回転の有効/無効を外部から切替し、曲げ設定と頭トラッキングも更新する。 |
| `setHorizontalMaxAngleDifference(float newValue)` | `upperBodyRotationManager` に水平方向の最大角度差を設定するだけ。 |
| `setVerticalMaxAngleDifference(float newValue)` | `upperBodyRotationManager` に垂直方向の最大角度差を設定するだけ。 |
| `setOriginalHorizontalMaxAngleDifference()` | 水平方向の最大角度差を元の値に戻すだけ。 |
| `setOriginalVerticalMaxAngleDifference()` | 垂直方向の最大角度差を元の値に戻すだけ。 |
| `getPlayerScreenObjectivesManager()` | `playerScreenObjectivesManager` を返すだけ。 |
| `updateCanMoveValue()` | 死亡状態と `playerManager.canPlayerMove()` から `canMove` を更新する。 |
| `canPlayerMove()` | `canMove` を返すだけ。 |
| `isCheckToKeepWeaponAfterAimingWeaponFromShooting()` | `checkToKeepWeaponAfterAimingWeaponFromShooting` を返すだけ。 |
| `setCarryWeaponInLowerPositionActiveState(bool state)` | `carryWeaponInLowerPositionActive` を設定するだけ。 |
| `isCarryWeaponInLowerPositionActive()` | `carryWeaponInLowerPositionActive` を返すだけ。 |
| `currentWeaponUsesHeadLookWhenAiming()` | 両手/単一の現武器の `headLookWhenAiming` を返し、無ければ偽を返す。 |
| `getCurrentWeaponHeadLookSpeed()` | 現武器の `headLookSpeed` を返し、無ければ0を返す。 |
| `getCurrentHeadLookTargetPosition()` | 現武器の `currentHeadLookTarget` の位置を返し、無ければ零ベクトルを返す。 |
| `playerCanAIm()` | リロード中は偽、空中照準可・一人称・地上・照準中なら真を返す。 |
| `disableAimModeInputPressedState()` | `aimModeInputPressed` を偽にするだけ。 |
| `setAimModeInputPressedState(bool state)` | `aimModeInputPressed` を設定するだけ。 |
| `isAimModeInputPressed()` | `aimModeInputPressed` を返すだけ。 |
| `setCurrentWeaponAsOneHandWield()` | 現武器を片手持ちにし、両手武器状態と武器回転を更新する。 |
| `setCurrentWeaponAsTwoHandsWield()` | 現武器を両手持ちにし、両手武器状態と武器回転を更新する。 |
| `updateWeaponListCount()` | `weaponListCount` を `weaponsList` の要素数にするだけ。 |
| `getDamageMultiplierStat()` | `damageMultiplierStat` を返すだけ。 |
| `getExtraDamageStat()` | `extraDamageStat` を返すだけ。 |
| `getSpreadMultiplierStat()` | `spreadMultiplierStat` を返すだけ。 |
| `getFireRateMultiplierStat()` | `fireRateMultiplierStat` を返すだけ。 |
| `getExtraReloadSpeedStat()` | `extraReloadSpeedStat` を返すだけ。 |
| `getMagazineExtraSizeStat()` | `magazineExtraSizeStat` を返すだけ。 |
| `weaponStatIncreaseDamageMultiplierStat(float extraValue)` | `damageMultiplierStat` に加算し、全武器の発射物情報を更新する。 |
| `weaponStatIncreaseExtraDamageStat(float extraValue)` | `extraDamageStat` に加算し、全武器の発射物情報を更新する。 |
| `weaponStatDecreaseSpreadMultiplierStat(float extraValue)` | `spreadMultiplierStat` から減算し、全武器の発射物情報を更新する。 |
| `weaponStatIncreaseFireRateMultiplierStat(float extraValue)` | `fireRateMultiplierStat` に加算し、全武器の発射物情報を更新する。 |
| `weaponStatIncreaseExtraReloadSpeedStat(float extraValue)` | `extraReloadSpeedStat` に加算し、全武器の発射物情報を更新する。 |
| `weaponStatIncreaseMagazineExtraSizeStat(float extraValue)` | `magazineExtraSizeStat` に整数で加算し、全武器の発射物情報を更新する。 |
| `initializeDamageMultiplierStatAmount(float newValue)` | `damageMultiplierStat` を `newValue` にするだけ。 |
| `initializeExtraDamageStatAmount(float newValue)` | `extraDamageStat` を `newValue` にするだけ。 |
| `initializeSpreadMultiplierStatAmount(float newValue)` | `spreadMultiplierStat` を `newValue` にするだけ。 |
| `initializeFireRateMultiplierStatAmount(float newValue)` | `fireRateMultiplierStat` を `newValue` にするだけ。 |
| `initializeExtraReloadSpeedStatAmount(float newValue)` | `extraReloadSpeedStat` を `newValue` にするだけ。 |
| `initializeMagazineExtraSizeStatAmount(float newValue)` | `magazineExtraSizeStat` を整数に変換した `newValue` で設定するだけ。 |
| `setExternalSpreadMultiplier(float newValue)` | `externalSpreadMultiplier` を設定するだけ。 |
| `getExternalSpreadMultiplierValue()` | `externalSpreadMultiplier` を返すだけ。 |
| `updateProjectileInfoValuesOnAllWeapons()` | 0.3秒間隔の制限付きで全武器の発射物情報を更新する。 |
| `renameWeapon(string currentWeaponName, string newWeaponName)` | 名前が一致する武器を1つ見つけて新しい名前にリネームする。 |
| `renameWeaponAmmo(string currentAmmoName, string newAmmoName)` | 全武器に対して弾薬名のリネームを試みる。 |
| `setFireWeaponsInputActiveState(bool state)` | `fireWeaponsInputActive` を設定するだけ。 |
| `setGeneralWeaponsInputActiveState(bool state)` | `generalWeaponsInputActive` を設定するだけ。 |
| `setOpenWeaponAttachmentsMenuPausedState(bool state)` | `openWeaponAttachmentsMenuPaused` を設定するだけ。 |
| `setIgnoreCheckUsingDevicesOnWeaponAttachmentsActiveState(bool state)` | `ignoreCheckUsingDevicesOnWeaponAttachmentsActive` を設定するだけ。 |
| `setUseQuickDrawWeaponState(bool state)` | `useQuickDrawWeapon` を設定するだけ。 |
| `setForceWeaponToUseQuickDrawKeepWeaponActiveState(bool state)` | `forceWeaponToUseQuickDrawKeepWeaponActive` を設定するだけ。 |
| `setOriginalForceWeaponToUseQuickDrawKeepWeaponActiveState()` | 保存された元の値へフラグを戻すだけ。 |
| `isForceWeaponToUseQuickDrawKeepWeaponActive()` | `forceWeaponToUseQuickDrawKeepWeaponActive` を返すだけ。 |
| `setIgnoreUseDrawKeepWeaponAnimationState(bool state)` | `ignoreUseDrawKeepWeaponAnimation` を設定するだけ。 |
| `setOriginalIgnoreUseDrawKeepWeaponAnimationState()` | 保存された元の値へフラグを戻すだけ。 |
| `isIgnoreUseDrawKeepWeaponAnimationActive()` | `ignoreUseDrawKeepWeaponAnimation` を返すだけ。 |
| `isUseDrawKeepWeaponAnimationOnAllWeaponsOnFBAActive()` | `useDrawKeepWeaponAnimationOnAllWeaponsOnFBA` を返すだけ。 |
| `isUseDrawKeepWeaponAnimationActiveOnCurrentWeapon()` | 現武器が抜刀/納刀アニメーション使用設定か返し、無ければ偽。 |
| `setOriginalUseQuickDrawWeaponState()` | `originalUseQuickDrawWeapon` を `useQuickDrawWeapon` に設定するだけ。 |
| `selectFirstWeaponGameObjectOnEditor()` | エディタで武器リストの先頭、無ければ `weaponsParent` を選択する。 |
| `updateDurabilityAmountStateOnAllObjects()` | 耐久チェック有効時、有効な全武器の耐久値を更新する。 |
| `updateDurabilityAmountStateOnObjectByName(string weaponName)` | 名前が一致する有効な武器1つの耐久値を更新する。 |
| `getDurabilityAmountStateOnObjectByName(string weaponName)` | 名前一致武器の耐久値を返し、無効時や不一致時は-1を返す。 |
| `initializeDurabilityValue(float newAmount, string weaponName, int currentObjectIndex)` | 名前一致の有効武器に耐久値とオブジェクトインデックスを初期設定する。 |
| `setInventoryObjectIndex(string weaponName, int currentObjectIndex)` | 名前一致の有効武器にインベントリのオブジェクトインデックスを設定する。 |
| `repairObjectFully(string weaponName)` | 名前が一致する武器の耐久値を全回復させる。 |
| `breakFullDurabilityOnCurrentWeapon()` | 武器所持中なら現武器の耐久値を0にする。 |
| `checkEventOnEmptyDurability()` | 耐久チェック有効時、`eventOnDurabilityEmptyOnMeleeWeapon` を発火する。 |
| `inputSetCurrentWeaponAsOneOrTwoHandsWield()` | 条件を満たす時、現武器の片手/両手持ちを入力でトグルする。 |
| `inputAimWeapon()` | 照準可否を確認し、入力で照準をトグル、未抜刀なら抜刀して照準する。 |
| `inputStartOrStopAimWeapon(bool aimingWeapon)` | 条件を確認したうえで `setAimWeaponState(aimingWeapon)` を呼ぶ。 |
| `stopAimIfActive()` | 照準中なら `setAimWeaponState(false)` を呼ぶだけ。 |
| `setAimWeaponState(bool aimingWeapon)` | 入力フラグを設定し、武器使用中は照準開始/終了、未使用なら抜刀して照準する。 |
| `inputPressDownOrReleaseDropWeapon(bool holdingButton)` | 押下で落下ボタン保持と力の蓄積を開始し、離すと武器を落とす。 |
| `inputHoldDropWeapon()` | 保持中に `currentDropForce` を上限まで増やすだけ。 |
| `inputActivateSecondaryAction()` | 入力可なら現武器の副次アクションを実行する。 |
| `inputActivateSecondaryActionOnPressDown()` | 入力可なら副次アクションの押下時処理を実行する。 |
| `inputActivateSecondaryActionOnPressUp()` | 入力可なら副次アクションの押上時処理を実行する。 |
| `inputActivateSecondaryActionOnPressHold()` | 入力可なら副次アクションの長押し時処理を実行する。 |
| `inputWeaponMeleeAttack()` | 射撃有効かつ入力可なら現武器の近接攻撃を実行する。 |
| `inputLockOrUnLockCursor()` | 武器設定と状態を確認し、可能ならカーソルのロックをトグルする。 |
| `inputHoldOrReleaseShootWeapon(bool holdingButton)` | 条件確認のうえ射撃を開始/停止し、必要ならフリーファイア照準や抜刀も行う。 |
| `setHoldShootWeaponState(bool state)` | 既存の連射コルーチンを止め、真なら連射コルーチンを開始して `holdShootActive` を立てる。 |
| `stopUpdateHoldShootWeaponCoroutine()` | 連射コルーチンを停止し `holdShootActive` を偽にする。 |
| `inputHoldShootWeapon()` | 毎フレーム呼ばれ、条件を再確認して自動武器の射撃継続や武器能力のホールドを処理する。 |
| `inputDrawWeapon()` | 条件確認後、両手武器なら組み合わせを選び、通常は抜刀/納刀の入力処理を行う。 |
| `inputReloadWeapon()` | 入力可なら片手/両手武器の手動リロードを実行する。 |
| `inputNextOrPreviousWeaponByButton(bool setNextWeapon)` | キー切替が有効なら次の武器か前の武器の選択を実行する。 |
| `inputNextOrPreviousWeapnByMouse(bool setNextWeapon)` | マウスホイール切替が有効なら次の武器か前の武器の選択を実行する。 |
| `inputEditWeaponAttachments()` | アタッチメントメニューを開ける状態なら編集処理を呼ぶ。 |
| `inputDrawRightWeapon()` | 両手武器時に右手の武器だけを構える処理を呼ぶ。 |
| `inputDrawLeftWeapon()` | 両手武器時に左手の武器だけを構える処理を呼ぶ。 |
| `drawRightWeapon()` | 左右の武器参照があれば右手武器を選択して構える。 |
| `drawLeftWeapon()` | 左右の武器参照があれば左手武器を選択して構える。 |
| `drawCurrentDualWeaponSelected(bool isRightWeapon)` | 指定した手の武器を現武器にし、IK・構え・HUD・単一武器への移行を処理する。 |
| `inputKeepDualWeapons()` | 両手武器時に片方だけを構える処理を呼ぶ。 |
| `keepDualWeaponAndDrawSingle(bool drawRightWeaponActive)` | 指定した手の武器名と番号を記録し、両手武器を分離する。 |
| `setSelectingWeaponState(bool state)` | `setUsingDualWeaponsState` に委譲して `usingDualWeapon` を設定するだけ。 |
| `setUsingDualWeaponsState(bool state)` | `usingDualWeapon` を設定するだけ。 |
| `isUsingDualWeapons()` | `usingDualWeapon` を返すだけ。 |
| `setChangeWeaponsWithNumberKeysActiveState(bool state)` | `changeWeaponsWithNumberKeysActive` を設定するだけ。 |
| `setChangeWeaponsWithKeysActive(bool state)` | `changeWeaponsWithKeysActive` を設定するだけ。 |
| `setOpenWeaponAttachmentsMenuEnabledState(bool state)` | `openWeaponAttachmentsMenuEnabled` を設定するだけ。 |
| `inputHoldOrReleaseShootRightWeapon(bool holdingButton)` | 設定に応じ、照準の開始/停止か右手武器の射撃押下/離し処理へ振り分ける。 |
| `inputHoldShootRightWeapon()` | 設定を確認し、右手武器の連射処理を呼ぶ。 |
| `inputHoldOrReleaseShootLeftWeapon(bool holdingButton)` | 単一入力設定なら左右両方、そうでなければ左武器の押下/離し射撃を処理する。 |
| `inputHoldShootLeftWeapon()` | 単一入力設定なら左右両方、そうでなければ左武器の連射処理を呼ぶ。 |
| `holdOrReleaseShootRightOrLeftDualWeapon(bool holdingButton, bool isRightWeapon)` | 両手武器の指定手で射撃を開始/停止し、フリーファイア照準や保持コルーチンも制御する。 |
| `holdShootRightOrLeftDualWeapon(bool isRightWeapon)` | 両手武器の毎フレーム連射処理で、条件を再確認し自動射撃や能力ホールドを行う。 |
| `stopUpdateHoldRightShootWeaponCoroutine()` | 右手の連射コルーチンを停止し `holdRightShootActive` を偽にする。 |
| `stopUpdateHoldLeftShootWeaponCoroutine()` | 左手の連射コルーチンを停止し `holdLeftShootActive` を偽にする。 |
| `stopAllCoroutinesOnDeath()` | メッセージ表示・FOV・HUD・回転・連射の各コルーチンをまとめて停止する。 |
| `getMainObjectTransformData()` | `mainObjectTransformData` を返すだけ。 |
| `setIgnoreNewAnimatorWeaponIDSettingsStateFromEditor(bool state)` | 設定を反映してコンポーネントを更新するだけ。 |
| `instantiateUsableWeaponPrefabInfoListFromEditor()` | プレハブ情報が有効でリストが空の時、全プレハブを生成して武器リストを作り直す。 |
| `setWeaponList()` | 子の `IKWeaponSystem` を集めて武器リストを作り直し、各一覧とコンポーネントを更新する。 |
| `getAvailableWeaponListString()` | 有効な武器名の配列を作り、無ければプレハブ情報の名前で代用する。 |
| `getWeaponListString()` | 全武器名を `avaliableWeaponList` に詰め、各開始インデックスを0にする。 |
| `removeWeaponFromList(int weaponIndex)` | 指定武器をリストとポケットから削除し、コンポーネントを更新する。 |
| `clearWeaponList()` | ポケットと武器リストを空にし、各一覧を更新する。 |
| `enableOrDisableWeaponGameObjectList(bool state)` | `weaponsParent` の子を一括で有効/無効化し、武器リストを作り直す。 |
| `removeWeaponsFromPlayerBody()` | 全武器オブジェクトを破棄し、リストとポケットを空にする。 |
| `removeWeaponFromPlayerBodyByName(string weaponName)` | 名前が一致する武器オブジェクトを破棄し、武器リストを作り直す。 |
| `enableOrDisableWeaponsListInRuntime(bool value)` | 全武器の有効状態を実行時に設定する。 |
| `enableOrDisableWeaponsList(bool value)` | 全武器の有効状態を設定し、各コンポーネントと一覧を更新する。 |
| `addPocket()` | 名前が「New Pocket」のポケットを追加するだけ。 |
| `addSubPocket(int index)` | 指定ポケットに「New Subpocket」を追加するだけ。 |
| `removePocket(int index)` | 指定インデックスのポケットを削除するだけ。 |
| `removeSubPocket(int pocketIndex, int subPocketIndex)` | 指定サブポケットを削除するだけ。 |
| `removeWeaponFromSubPocket(int pocketIndex, int subPocketIndex, int weaponIndex)` | 指定サブポケットから指定武器を削除するだけ。 |
| `setCheckDurabilityOnObjectEnabledValueFromEditor(bool state)` | 耐久チェックの有効状態を設定し、コンポーネントを更新する。 |
| `setThirdPersonParent(Transform newParent)` | `thirdPersonParent` を設定し、コンポーネントを更新する。 |
| `setRightHandTransform(Transform handTransform)` | 右手のトランスフォームを設定し、コンポーネントを更新する。 |
| `setLeftHandTransform(Transform handTransform)` | 左手のトランスフォームを設定し、コンポーネントを更新する。 |
| `saveCurrentWeaponListToFile()` | `pauseManager` に武器リストをファイルへ保存させる。 |
| `setCustomIgnoreTagsForCharacterFromEditor()` | `playerManager` のタグを無視タグとして登録し、コンポーネントを更新する。 |
| `setUseQuickDrawWeaponStateFromEditor(bool state)` | `useQuickDrawWeapon` を設定してコンポーネントを更新するだけ。 |
| `setIgnoreUseDrawKeepWeaponAnimationStateFromEditor(bool state)` | `ignoreUseDrawKeepWeaponAnimation` を設定して更新するだけ。 |
| `setForceWeaponToUseQuickDrawKeepWeaponActiveStateFromEditor(bool state)` | `forceWeaponToUseQuickDrawKeepWeaponActive` を設定して更新するだけ。 |
| `setOpenWeaponAttachmentsMenuEnabledStateFromEditor(bool state)` | `openWeaponAttachmentsMenuEnabled` を設定して更新するだけ。 |
| `setCurrentOffsetParentOnThirdPersonOnAllWeapons()` | 全武器の `weaponTransformInfoSystem` に三人称オフセット値を適用する。 |
| `setCurrentOffsetParentThirdPersonValues(Vector3 newValue)` | `currentOffsetParentThirdPerson` を設定するだけ。 |
| `adjustDrawKeepPositionToWeaponPositionOnAllWeapons()` | 全武器の抜刀/納刀位置を武器の位置に合わせて調整する。 |
| `setWeaponMeshScaleOnAllWeapons(float newValue)` | 全武器のメッシュスケールを設定する。 |
| `adjustAllFireWeaponTransformReferencePositionOnAllWeapons(float newValue)` | 全武器の射撃トランスフォーム参照位置を `newValue` で調整する。 |
| `setWeaponsHUDEnabledStateFromEditor(bool state)` | HUDの有効状態を設定してコンポーネントを更新するだけ。 |
| `destroyFirstPersonArmsFromAllWeapons()` | 全武器の一人称用の腕オブジェクトをエディタで破棄する。 |
| `updateComponent(bool updateDirtyScene)` | 自身のコンポーネントを更新し、必要ならシーンをダーティにする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnEmptyAmmoOnCurrentWeapon` | `UnityEvent` | – |
| `eventOnDurabilityEmptyOnMeleeWeapon` | `UnityEvent` | – |
| `evenOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
| `eventOnWeaponStolen` | `UnityEvent` | – |

## 内部型

- `weaponPocket`（class）
- `weaponListOnPocket`（class）
- `usableWeaponPrefabInfo`（class）
