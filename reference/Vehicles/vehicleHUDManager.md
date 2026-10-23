# vehicleHUDManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `healthManagement`
- **ソース**: `Vehicles/vehicleHUDManager.cs:8`

**概要**: 車両の体力・ブースト（エネルギー）・燃料の値と対応する`Slider`を保持し、被弾・破壊処理やHUD更新、乗降・カメラ・入力の各マネージャへの委譲をまとめる`healthManagement`派生コンポーネント。自爆・射出・ホーンなどの車両操作APIも公開する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Name | `vehicleName` | `string` | – | 車両名。スキャナーやマップ表示での識別に使われる。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Destroyed Sound | `destroyedSound` | `AudioClip` | – | 破壊時に再生する`AudioClip`。爆発音などを設定。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Destroyed Audio Element | `destroyedAudioElement` | `AudioElement` | – | 破壊音の再生方法やイベント名をまとめた`AudioElement`。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Destroyed Source | `destroyedSource` | `AudioSource` | – | 破壊音を再生する`AudioSource`を指定する。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Health Percentage Damage Particles | `healthPercentageDamageParticles` | `float` | – | 体力がこの割合（%）以下になると損傷パーティクルを表示。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Place To Shoot | `placeToShoot` | `Transform` | – | 武器やデカールの照準・着弾基準になるTransform。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Can Set Turn On State | `canSetTurnOnState` | `bool` | – | 運転中にエンジンのON/OFF入力を許可するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Auto Turn On When Get On | `autoTurnOnWhenGetOn` | `bool` | – | 搭乗した時にエンジンを自動でONにするトグル。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Vehicle Radius | `vehicleRadius` | `float` | – | 車両の概算半径。AIの接近判定や出現位置の計算に使う。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Layer For Obstacles On Get Off | `layer` | `LayerMask` | – | 降車時の障害物判定レイキャスト用のレイヤーマスク。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Layer For Passengers | `layerForPassengers` | `LayerMask` | – | 乗車トリガーとして反応させるレイヤーを指定。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Passengers Parent | `passengersParent` | `Transform` | – | 乗車したキャラクターを親子付けするTransform。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Can Unlock Cursor | `canUnlockCursor` | `bool` | – | 運転中にカーソルロックを解除できるようにするトグル。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |

### HUD Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable Player HUD Enabled | `disablePlayerHUDEnabled` | `bool` | true | 搭乗中にプレイヤー側のHUDを非表示にするトグル。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Show Vehicle HUD | `showVehicleHUD` | `bool` | true | 運転中に車両HUD（体力・速度など）を表示するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue` |
| Show Vehicle Speed | `showVehicleSpeed` | `bool` | true | 車両HUDに現在速度の表示を出すかどうか。 / 表示条件: `showAllSettings.boolValue \|\| showMainSettings.boolValue && showVehicleHUD.boolValue` |

### Health Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Invincible | `invincible` | `bool` | – | 無敵状態。オンならダメージを受けず体力バーも隠れる。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue` |
| Health Amount | `healthAmount` | `float` | – | 現在の体力値。ゲーム開始時の初期値にもなる。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue && !invincible.boolValue` |
| Max Health Amount | `maxHealthAmount` | `float` | 100 | 体力の最大値。0なら開始時に`healthAmount`を採用。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue && !invincible.boolValue` |

### Regenerate Health Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regenerate Health | `regenerateHealth` | `bool` | – | 体力を時間経過で自動回復させるトグル。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue && !invincible.boolValue` |
| Constant Health Regenerate | `constantHealthRegenerate` | `bool` | – | オンなら毎秒回復、オフなら一定間隔ごとの回復。 / 表示条件: `!invincible.boolValue && regenerateHealth.boolValue` |
| Regenerate Health Time | `regenerateHealthTime` | `float` | – | 最後にダメージを受けてから回復を始めるまでの秒数。 / 表示条件: `!invincible.boolValue && regenerateHealth.boolValue` |
| Regenerate Health Speed | `regenerateHealthSpeed` | `float` | – | 毎秒回復する体力量。定常回復の時に使う。 / 表示条件: `regenerateHealth.boolValue && constantHealthRegenerate.boolValue` |
| Regenerate Health Amount | `regenerateHealthAmount` | `float` | – | 1回の回復で加算する体力量。間隔回復の時に使う。 / 表示条件: `!invincible.boolValue && regenerateHealth.boolValue` |
| Destroyed | `destroyed` | `bool` | – | 破壊済みかどうかの状態。実行時に自動で更新される。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue && !invincible.boolValue` |

### Energy Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Use Boost | `vehicleUseBoost` | `bool` | true | ブーストを使うか。有効時はHUDにエネルギーを表示。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue` |
| Infinite Boost | `infiniteBoost` | `bool` | – | ブーストを消費せず常に満タンで使えるようにする。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue && vehicleUseBoost.boolValue` |
| Boost Amount | `boostAmount` | `float` | – | 現在のブースト量。開始時の初期値にもなる。 / 表示条件: `vehicleUseBoost.boolValue && !infiniteBoost.boolValue` |
| Max Boost Amount | `maxBoostAmount` | `float` | – | ブーストの最大値。0なら開始時に`boostAmount`を採用。 / 表示条件: `vehicleUseBoost.boolValue && !infiniteBoost.boolValue` |
| Boost Use Rate | `boostUseRate` | `float` | – | ブースト使用中に1秒あたり消費する量。 / 表示条件: `vehicleUseBoost.boolValue && !infiniteBoost.boolValue` |

### Regenerate Boost Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regenerate Boost | `regenerateBoost` | `bool` | – | ブーストを時間経過で自動回復させるトグル。 / 表示条件: `vehicleUseBoost.boolValue && !infiniteBoost.boolValue` |
| Constant Boost Regenerate | `constantBoostRegenerate` | `bool` | – | オンなら毎秒回復、オフなら一定間隔ごとの回復。 / 表示条件: `!infiniteBoost.boolValue && regenerateBoost.boolValue` |
| Regenerate Boost Time | `regenerateBoostTime` | `float` | – | 最後にブーストを使ってから回復を始めるまでの秒数。 / 表示条件: `!infiniteBoost.boolValue && regenerateBoost.boolValue` |
| Regenerate Boost Speed | `regenerateBoostSpeed` | `float` | – | 毎秒回復するブースト量。定常回復の時に使う。 / 表示条件: `regenerateBoost.boolValue && constantBoostRegenerate.boolValue` |
| Regenerate Boost Amount | `regenerateBoostAmount` | `float` | – | 1回の回復で加算するブースト量。間隔回復の時に使う。 / 表示条件: `!infiniteBoost.boolValue && regenerateBoost.boolValue` |

### Fuel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Use Fuel | `vehicleUseFuel` | `bool` | – | 燃料を消費するか。オフなら燃料なしでも走行できる。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue` |
| Infinite Fuel | `infiniteFuel` | `bool` | – | 燃料を消費せず常に満タンで走れるようにするトグル。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue && vehicleUseFuel.boolValue` |
| Fuel Amount | `fuelAmount` | `float` | – | 現在の燃料量。開始時の初期値にもなる。 / 表示条件: `vehicleUseFuel.boolValue && !infiniteFuel.boolValue` |
| Max Fuel Amount | `maxFuelAmount` | `float` | 100 | 燃料の最大値。0なら開始時に`fuelAmount`を採用。 / 表示条件: `vehicleUseFuel.boolValue && !infiniteFuel.boolValue` |
| Fuel Use Rate | `fuelUseRate` | `float` | – | 走行中に1秒あたり消費する燃料量。 / 表示条件: `vehicleUseFuel.boolValue && !infiniteFuel.boolValue` |
| Start With Gas Tank Empty | `startWithGasTankEmpty` | `bool` | – | 開始時に燃料を0にし、ガソリンタンクを有効にする。 / 表示条件: `vehicleUseFuel.boolValue && !infiniteFuel.boolValue` |

### Regenerate Fuel Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regenerate Fuel | `regenerateFuel` | `bool` | – | 燃料を時間経過で自動回復させるトグル。 / 表示条件: `vehicleUseFuel.boolValue && !infiniteFuel.boolValue` |
| Constant Fuel Regenerate | `constantFuelRegenerate` | `bool` | – | オンなら毎秒回復、オフなら一定間隔ごとの回復。 / 表示条件: `!infiniteFuel.boolValue && regenerateFuel.boolValue` |
| Regenerate Fuel Time | `regenerateFuelTime` | `float` | – | 燃料の消費から回復を始めるまでの待ち秒数。 / 表示条件: `!infiniteFuel.boolValue && regenerateFuel.boolValue` |
| Regenerate Fuel Speed | `regenerateFuelSpeed` | `float` | – | 毎秒回復する燃料量。定常回復の時に使う。 / 表示条件: `regenerateFuel.boolValue && constantFuelRegenerate.boolValue` |
| Regenerate Fuel Amount | `regenerateFuelAmount` | `float` | – | 1回の回復で加算する燃料量。間隔回復の時に使う。 / 表示条件: `!infiniteFuel.boolValue && regenerateFuel.boolValue` |
| Gas Tank Game Object | `gasTankGameObject` | `GameObject` | – | 燃料補給タンクのGameObject。空の状態で有効化される。 / 表示条件: `vehicleUseFuel.boolValue && !infiniteFuel.boolValue` |

### Main Stats Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Health Stat Name | `healthStatName` | `string` | "Health" | 体力バーを識別するステータス名。回復処理の判定に使う。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue` |
| Energy Stat Name | `energyStatName` | `string` | "Energy" | ブーストバーを識別するステータス名。回復処理の判定に使う。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue` |
| Fuel Stat Name | `fuelStatName` | `string` | "Fuel" | 燃料バーを識別するステータス名。回復処理の判定に使う。 / 表示条件: `showAllSettings.boolValue \|\| showVehicleStats.boolValue` |

### Damage Receiver List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Weak Spots | `useWeakSpots` | `bool` | – | 弱点ごとの倍率や即死設定を使うトグル。 / 表示条件: `showAllSettings.boolValue \|\| showAdvancedSettings.boolValue` |
| Ignore Use Health Amount On Spot | `ignoreUseHealthAmountOnSpot` | `bool` | – | 弱点ごとの残量を無視し、車両本体の体力へ直接ダメージ。 / 表示条件: `showAllSettings.boolValue \|\| showAdvancedSettings.boolValue` |

### Use Custom Vehicle Parts To Destroy Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Vehicle Parts To Destroy | `useCustomVehiclePartsToDestroy` | `bool` | – | 破壊時に分解するパーツを独自リストで指定するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showAdvancedSettings.boolValue` |
| Custom Vehicle Parts Explosion Force | `customVehiclePartsExplosionForce` | `float` | 500 | 独自パーツを吹き飛ばす爆発の強さ。 / 表示条件: `showAllSettings.boolValue \|\| showAdvancedSettings.boolValue && useCustomVehiclePartsToDestroy.boolValue` |
| Custom Vehicle Parts Explosion Radius | `customVehiclePartsExplosionRadius` | `float` | 50 | 独自パーツの爆発が影響する半径。 / 表示条件: `showAllSettings.boolValue \|\| showAdvancedSettings.boolValue && useCustomVehiclePartsToDestroy.boolValue` |
| Custom Vehicle Parts Explosion Force Mode | `customVehiclePartsExplosionForceMode` | `ForceMode` | ForceMode.Impulse | 独自パーツ爆発の`ForceMode`（加速の与え方）。 / 表示条件: `showAllSettings.boolValue \|\| showAdvancedSettings.boolValue && useCustomVehiclePartsToDestroy.boolValue` |
| Use Event On Custom Vehicle Parts | `useEventOnCustomVehicleParts` | `bool` | – | 独自パーツの破壊時にイベントを呼ぶトグル。 / 表示条件: `showAllSettings.boolValue \|\| showAdvancedSettings.boolValue && useCustomVehiclePartsToDestroy.boolValue` |
| Event On Custom Vehicle Parts | `eventOnCustomVehicleParts` | `UnityEvent` | – | 独自パーツの破壊時に実行するイベント。 / 表示条件: `useCustomVehiclePartsToDestroy.boolValue && useEventOnCustomVehicleParts.boolValue` |

### Main Settings Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check On Collision Enter Only Externally | `checkOnCollisionEnterOnlyExternally` | `bool` | – | 通常の衝突判定を止め、外部呼び出し時のみ処理する。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |

### Damage and Fade Vehicle Pieces Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Damage Particles | `useDamageParticles` | `bool` | true | 体力が低下した時に火災・煙パーティクルを出すトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Damage Particles | `damageParticles` | `GameObject` | – | 損傷時に使う火災・煙パーティクルを含むGameObject。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && useDamageParticles.boolValue` |
| Use Destroyed Particles | `useDestroyedParticles` | `bool` | true | 破壊時に爆発パーティクルを生成するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Destroyed Particles | `destroyedParticles` | `GameObject` | – | 破壊時に生成する爆発パーティクルのプレハブ。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && useDestroyedParticles.boolValue` |
| Remove Pieces When Destroyed | `removePiecesWhenDestroyed` | `bool` | true | 破壊後に車両パーツを消滅させるトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Fade Vehicle Pieces On Destroyed | `fadeVehiclePiecesOnDestroyed` | `bool` | true | パーツ消滅時に透明化してフェードさせるトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Time To Fade Pieces | `timeToFadePieces` | `float` | 3 | 破壊後、パーツのフェードや消滅を始めるまでの秒数。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Destroyed Mesh Shader | `destroyedMeshShader` | `Shader` | – | フェード用に差し替える透明シェーダー。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Default Shader Name | `defaultShaderName` | `string` | "Legacy Shaders/Transparent/Diffuse" | `destroyedMeshShader`未設定時に使うシェーダー名。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Color Property Name | `colorPropertyName` | `string` | "_Color" | フェードで透明度を操作するシェーダープロパティ名。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Set Colliders On All Vehicle Mesh Parts | `setCollidersOnAllVehicleMeshParts` | `bool` | true | 破壊時に全メッシュパーツへコライダーと剛体を付けるトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |

### Eject/Self Destruction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Self Destruct | `canUseSelfDestruct` | `bool` | – | 運転中に自爆入力を許可するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Can Stop Self Destruction | `canStopSelfDestruction` | `bool` | – | 自爆の途中停止を許可する設定（実行コードでは未参照）。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && canUseSelfDestruct.boolValue` |
| Self Destruct Delay | `selfDestructDelay` | `float` | – | 自爆入力から爆発までの待ち時間（秒）。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && canUseSelfDestruct.boolValue` |
| Eject Passenger On Self Destruct | `ejectPassengerOnSelfDestruct` | `bool` | – | 自爆時に搭乗者を吹き飛ばして放り出すトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && canUseSelfDestruct.boolValue` |
| Eject Passenger Force | `ejectPassengerForce` | `float` | 10 | 放出時に搭乗者へ加える力の大きさ。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && canUseSelfDestruct.boolValue` |
| Get Off Passengers On Self Destruct | `getOffPassengersOnSelfDestruct` | `bool` | – | 自爆時に搭乗者を通常の降車処理で降ろすトグル。 / 表示条件: `canUseSelfDestruct.boolValue && !ejectPassengerOnSelfDestruct.boolValue` |
| Eject Passenger Force | `ejectPassengerForce` | `float` | 10 | 放出時に搭乗者へ加える力の大きさ。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |

### Collision Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Objects On Collision | `damageObjectsOnCollision` | `bool` | true | 衝突した相手オブジェクトにダメージを与えるトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Damage Multiplier On Collision | `damageMultiplierOnCollision` | `float` | 1 | 衝突速度に掛けるダメージ倍率（1〜100）。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && damageObjectsOnCollision.boolValue` / Range (1, 100) |
| Min Vehicle Velocity To Damage | `minVehicleVelocityToDamage` | `float` | 20 | 相手にダメージを与えるのに必要な自車の最低速度。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && damageObjectsOnCollision.boolValue` |
| Min Collision Velocity To Damage | `minCollisionVelocityToDamage` | `float` | 20 | ダメージ判定に必要な衝突の相対速度の下限。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && damageObjectsOnCollision.boolValue` |
| Ignore Shield On Collision | `ignoreShieldOnCollision` | `bool` | true | 衝突ダメージで相手のシールドを無視するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && damageObjectsOnCollision.boolValue` |

### Remote Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | 衝突相手の`remoteEventSystem`へリモートイベントを送る。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && damageObjectsOnCollision.boolValue` |

### Launch Passengers On Collision Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Launch Driver On Collision | `launchDriverOnCollision` | `bool` | – | 強い衝突時に搭乗者を車外へ吹き飛ばすトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Min Collision Velocity To Launch | `minCollisionVelocityToLaunch` | `float` | – | 搭乗者が吹き飛ぶ衝突速度のしきい値。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && launchDriverOnCollision.boolValue` |
| Launch Direction Offset | `launchDirectionOffset` | `Vector3` | – | 吹き飛ばす方向へ加える位置オフセット。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && launchDriverOnCollision.boolValue` |
| Extra Collision Force | `extraCollisionForce` | `float` | 1.2f | 吹き飛ばす方向に掛ける追加の力の倍率。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && launchDriverOnCollision.boolValue` |
| Ignore Ragdoll Collider | `ignoreRagdollCollider` | `bool` | – | 放出時にラグドールのコライダーとの衝突を無視する。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && launchDriverOnCollision.boolValue` |

### Collision Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Apply Damage To Driver | `applyDamageToDriver` | `bool` | – | 放出時に搭乗者へもダメージを与えるトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && launchDriverOnCollision.boolValue` |
| Use Collision Velocity As Damage | `useCollisionVelocityAsDamage` | `bool` | – | オンなら衝突速度をそのままダメージ量として使う。 / 表示条件: `launchDriverOnCollision.boolValue && applyDamageToDriver.boolValue` |
| Collision Damage Amount | `collisionDamageAmount` | `float` | – | 衝突速度を使わない場合に与える固定ダメージ量。 / 表示条件: `applyDamageToDriver.boolValue && !useCollisionVelocityAsDamage.boolValue` |
| Ignore Shield On Launch | `ignoreShieldOnLaunch` | `bool` | true | 放出ダメージでシールドを無視するトグル。 / 表示条件: `launchDriverOnCollision.boolValue && applyDamageToDriver.boolValue` |

### Vehicle Explosion Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Explode Vehicle When Destroyed Enabled | `explodeVehicleWhenDestroyedEnabled` | `bool` | true | 破壊時に爆発エフェクトと破片処理を行うトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Vehicle Explosion Force | `vehicleExplosionForce` | `float` | 500 | 破片を吹き飛ばす爆発力の強さを設定。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Vehicle Explosion Radius | `vehicleExplosionRadius` | `float` | 50 | 破片が爆発の影響を受ける半径。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Vehicle Explosion Force Mode | `vehicleExplosionForceMode` | `ForceMode` | ForceMode.Impulse | 破片爆発の`ForceMode`（加速の与え方）。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |

### Damage On Collision Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Receive Damage From Collision | `receiveDamageFromCollision` | `bool` | – | 衝突時に車両自身がダメージを受けるトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Min Velocity To Damage Collision | `minVelocityToDamageCollision` | `float` | – | 自車がダメージを受ける衝突速度の下限。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && receiveDamageFromCollision.boolValue` |
| Use Current Velocity As Damage | `useCurrentVelocityAsDamage` | `bool` | – | オンなら衝突速度をそのままダメージ量にする。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && receiveDamageFromCollision.boolValue` |
| Default Damage Collision | `defaultDamageCollision` | `float` | – | 衝突速度を使わない場合の固定ダメージ量。 / 表示条件: `receiveDamageFromCollision.boolValue && !useCurrentVelocityAsDamage.boolValue` |
| Collision Damage Multiplier | `collisionDamageMultiplier` | `float` | – | 衝突ダメージ量に掛ける倍率を設定。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && receiveDamageFromCollision.boolValue` |
| Check Min Vertical Distance To Get Damage From Collision | `checkMinVerticalDistanceToGetDamageFromCollision` | `bool` | – | 一定の高さ以下の接触をダメージ対象から除外するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && receiveDamageFromCollision.boolValue` |
| Min Vertical Distance Transform To Get Damage From Collision | `minVerticalDistanceTransformToGetDamageFromCollision` | `Transform` | – | このTransformの高さ未満の接触はダメージ無効になる。 / 表示条件: `receiveDamageFromCollision.boolValue && checkMinVerticalDistanceToGetDamageFromCollision.boolValue` |
| Use Collider List To Ignore Damage From Collision | `useColliderListToIgnoreDamageFromCollision` | `bool` | – | 指定コライダーへの接触ではダメージを受けないトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue && receiveDamageFromCollision.boolValue` |

### Impact Surface Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Impact Surface | `useImpactSurface` | `bool` | – | 被弾時のデカールに専用のインパクト面を使うトグル。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |
| Main Decal Manager Name | `mainDecalManagerName` | `string` | "Decal Manager" | デカールマネージャーをシーン内で検索する時のオブジェクト名。 / 表示条件: `showAllSettings.boolValue \|\| showPhysicsSettings.boolValue` |

### Events On Vehicle State Changed

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Changed | `useEventsOnStateChanged` | `bool` | – | 乗降・破壊イベントを有効にするトグル。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event On Get On | `eventOnGetOn` | `UnityEvent` | – | プレイヤーが搭乗した時に実行されるイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventsOnStateChanged.boolValue` |
| Event On Get Off | `eventOnGetOff` | `UnityEvent` | – | プレイヤーが降車した時に実行されるイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventsOnStateChanged.boolValue` |
| Event On Destroyed | `eventOnDestroyed` | `UnityEvent` | – | 車両が破壊された時に実行されるイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventsOnStateChanged.boolValue` |
| Event On Fix Destroyed Vehicle | `eventOnFixDestroyedVehicle` | `UnityEvent` | – | 破壊された車両が修理された時に実行されるイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventsOnStateChanged.boolValue` |

### Jump Platforms Events

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Jump Platform Events | `useJumpPlatformEvents` | `bool` | true | ジャンプ台のイベント呼び出しを有効にするトグル。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Jump Platform Event | `jumpPlatformEvent` | `eventParameters.eventToCallWithVector3` | – | ジャンプ台から方向を受け取るイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useJumpPlatformEvents.boolValue` |
| Jump Platform Parable Event | `jumpPlatformParableEvent` | `eventParameters.eventToCallWithVector3` | – | 放物線ジャンプ台の方向を受け取るイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useJumpPlatformEvents.boolValue` |
| Set New Jump Power Event | `setNewJumpPowerEvent` | `eventParameters.eventToCallWithAmount` | – | ジャンプ力を新しい値へ変更するイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useJumpPlatformEvents.boolValue` |
| Set Original Jump Power Event | `setOriginalJumpPowerEvent` | `UnityEvent` | – | ジャンプ力を元の値へ戻すイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useJumpPlatformEvents.boolValue` |

### Vehicle Driving State Events

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Passenger Getting On Off Event | `passengerGettingOnOffEvent` | `UnityEvent` | – | 誰かが乗降するたびに呼ばれるイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Change Vehicle State Event | `changeVehicleStateEvent` | `UnityEvent` | – | 運転と停止の状態が変わるたびに呼ばれるイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |

### Vehicle AI Events

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events To Check If Vehicle Used By AI On Passenger Enter Exit | `useEventsToCheckIfVehicleUsedByAIOnPassengerEnterExit` | `bool` | – | AI使用車両の乗降時にイベントで判定するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event To Check If Vehicle Used By AI On Passenger Enter | `eventToCheckIfVehicleUsedByAIOnPassengerEnter` | `UnityEvent` | – | 乗車時にAI使用か確認するためのイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventsToCheckIfVehicleUsedByAIOnPassengerEnterExit.boolValue` |
| Event To Check If Vehicle Used By AI On Passenger Exit | `eventToCheckIfVehicleUsedByAIOnPassengerExit` | `UnityEvent` | – | 降車時にAI使用か確認するためのイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventsToCheckIfVehicleUsedByAIOnPassengerEnterExit.boolValue` |

### Events To Send Passengers Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event To Send Passenger | `useEventToSendPassenger` | `bool` | – | 乗降した搭乗者をイベントで送るトグル。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event To Send Passenger On Get On | `eventToSendPassengerOnGetOn` | `eventParameters.eventToCallWithGameObject` | – | 乗車したキャラクターを渡すイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventToSendPassenger.boolValue` |
| Event To Sent Passenger On Get Off | `eventToSentPassengerOnGetOff` | `eventParameters.eventToCallWithGameObject` | – | 降車したキャラクターを渡すイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue && useEventToSendPassenger.boolValue` |

### Events To Send Stats On Save

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Send Current Health Amount | `eventToSendCurrentHealthAmount` | `eventParameters.eventToCallWithAmount` | – | セーブ用に現在の体力値を送るイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event To Send Current Fuel Amount | `eventToSendCurrentFuelAmount` | `eventParameters.eventToCallWithAmount` | – | セーブ用に現在の燃料値を送るイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |
| Event To Send Current Boost Amount | `eventToSendCurrentBoostAmount` | `eventParameters.eventToCallWithAmount` | – | セーブ用に現在のブースト値を送るイベント。 / 表示条件: `showAllSettings.boolValue \|\| showEventSettings.boolValue` |

### Horn/Friends Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Horn To Call Friends | `useHornToCallFriends` | `bool` | – | クラクションで仲間を呼び寄せるトグル。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Call Only Found Friends | `callOnlyFoundFriends` | `bool` | – | 発見済みの仲間だけを呼ぶトグル（半径探索をしない）。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue && useHornToCallFriends.boolValue` |
| Radius To Call Friends | `radiusToCallFriends` | `float` | – | クラクションで仲間を探す時の半径。 / 表示条件: `useHornToCallFriends.boolValue && !callOnlyFoundFriends.boolValue` |
| Use Horn Event | `useHornEvent` | `bool` | – | クラクション入力時にイベントを実行するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Horn Event | `hornEvent` | `UnityEvent` | – | クラクション入力時に実行されるイベント。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue && useHornEvent.boolValue` |

### Eject Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Eject From Vehicle | `canEjectFromVehicle` | `bool` | – | 運転中に脱出（放出）入力を許可するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Eject Passenger Force | `ejectPassengerForce` | `float` | 10 | 放出時に搭乗者へ加える力の大きさ。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue && canEjectFromVehicle.boolValue` |

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | AIが運転する車両か。オンならAI制御を自動で開始する。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### Move Inside Vehicle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Main Update Rigidbody State Inside Rigidbody System | `useMainUpdateRigidbodyStateInsideRigidbodySystem` | `bool` | – | 指定システム内のオブジェクトとの衝突判定を無視するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |
| Main Update Rigidbody State Inside Rigidbody System | `mainUpdateRigidbodyStateInsideRigidbodySystem` | `updateRigidbodyStateInsideRigidbodySystem` | – | 衝突を無視する対象を管理するシステムへの参照。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue && useMainUpdateRigidbodyStateInsideRigidbodySystem.boolValue` |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Log Collisions | `showDebugLogCollisions` | `bool` | – | 衝突の接触情報をコンソールに出力するトグル。 / 表示条件: `showAllSettings.boolValue \|\| showOtherSettings.boolValue` |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Health Amount To Take On Editor | `healthAmountToTakeOnEditor` | `float` | – | エディタのデバッグで車両から減らす体力量。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |

### Debug Launch Driver

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Debug Launch Character Speed | `debugLaunchCharacterSpeed` | `float` | – | デバッグの放出テストで使う速度。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |
| Debug Launch Character Position | `debugLaunchCharacterPosition` | `Vector3` | – | デバッグの放出テストで使う方向の基準位置。 / 表示条件: `showAllSettings.boolValue \|\| showDebugSettings.boolValue` |

### Vehicle Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| IK Driving Manager | `IKDrivingManager` | `IKDrivingSystem` | – | 乗降や座席を管理する`IKDrivingSystem`への参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Weapons Manager | `weaponsManager` | `vehicleWeaponSystem` | – | 車両武器を管理する`vehicleWeaponSystem`への参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | 車両の移動に使うメインの`Rigidbody`。 / 表示条件: `showVehicleElements` がオンのとき |
| Damage In Screen Manager | `damageInScreenManager` | `damageInScreen` | – | 被弾時に画面演出を出す`damageInScreen`への参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Map Information Manager | `mapInformationManager` | `mapObjectInformation` | – | マップ表示用の`mapObjectInformation`への参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Vehicle Camera Manager | `vehicleCameraManager` | `vehicleCameraController` | – | 車両カメラを制御する`vehicleCameraController`への参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Gas Tank Manager | `gasTankManager` | `useInventoryObject` | – | 燃料補給タンクの`useInventoryObject`への参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Vehicle Gravitymanager | `vehicleGravitymanager` | `vehicleGravityControl` | – | 重力制御を行う`vehicleGravityControl`への参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Main Vehicle Controller | `mainVehicleController` | `vehicleController` | – | 車両の移動処理を行うメインコントローラーへの参照。 / 表示条件: `showVehicleElements` がオンのとき |
| Main Vehicle AI Nav Mesh | `mainVehicleAINavMesh` | `vehicleAINavMesh` | – | AI運転に使う`vehicleAINavMesh`への参照。 / 表示条件: `showVehicleElements` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `advancedSettings` | `advancedSettingsClass` | new advancedSettingsClass () | – |
| `damageTypeID` | `int` | -1 | – |
| `damageCanBeBlocked` | `bool` | – | – |
| `remoteEventNameList` | `List<string>` | new List<string> () | – |
| `vehicleHealth` | `Slider` | – | – |
| `vehicleBoost` | `Slider` | – | – |
| `vehicleAmmo` | `Slider` | – | – |
| `vehicleFuel` | `Slider` | – | – |
| `colliderListToIgnoreDamageFromCollision` | `List<Collider>` | new List<Collider> () | – |
| `audioSourceList` | `List<audioSourceInfo>` | new List<audioSourceInfo> () | – |
| `isBeingDriven` | `bool` | – | – |
| `passengersOnVehicle` | `bool` | – | – |
| `cursorUnlocked` | `bool` | – | – |
| `customVehiclePartsListToDestroy` | `List<vehiclePartInfo>` | new List<vehiclePartInfo> () | – |
| `fireParticles` | `List<ParticleSystem>` | new List<ParticleSystem> () | – |
| `colliderLayerIndexParts` | `List<int>` | new List<int> () | – |
| `colliderParts` | `List<Collider>` | new List<Collider> () | – |
| `colliderWithoutMeshesParts` | `List<Collider>` | new List<Collider> () | – |
| `colliderWithoutMeshesPartsToIgnore` | `List<Collider>` | new List<Collider> () | – |
| `colliderWithMeshesParts` | `List<Collider>` | new List<Collider> () | – |
| `vehicleDamageReceiverList` | `List<vehicleDamageReceiver>` | new List<vehicleDamageReceiver> () | – |
| `vehiclePartsToIgnore` | `List<GameObject>` | new List<GameObject> () | – |
| `vehicleRendererList` | `List<Renderer>` | new List<Renderer> () | – |
| `vehiclePartInfoList` | `List<vehiclePartInfo>` | new List<vehiclePartInfo> () | – |
| `impactDecalList` | `string []` | – | – |
| `impactDecalIndex` | `int` | – | – |
| `impactDecalName` | `string` | – | – |
| `currentHUDElements` | `playerHUDManager.vehicleHUDElements` | – | – |
| `showAllSettings` | `bool` | – | – |
| `showMainSettings` | `bool` | – | – |
| `showVehicleStats` | `bool` | – | – |
| `showAdvancedSettings` | `bool` | – | – |
| `showEventSettings` | `bool` | – | – |
| `showDebugSettings` | `bool` | – | – |
| `showOtherSettings` | `bool` | – | – |
| `showPhysicsSettings` | `bool` | – | – |
| `showVehicleElements` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setUnlockCursorState(bool state)` | カーソル解放が許可されている場合のみ`cursorUnlocked`を設定し、IK運転側へ反映する。 |
| `disableUnlockedCursor()` | カーソルをロック状態に戻し、IK運転システムにも解放解除を通知するだけ。 |
| `setVehicleInteractionTriggerState(bool state)` | 車両のメインコライダーの`enabled`を設定し、操作不可フラグを反転して保持する。 |
| `isInteractionDisabledOnVehicle()` | 操作トリガーが無効化されているか`interactionDisabledOnVehicle`を返すだけ。 |
| `setIgnoreCanUseSelfDestructActiveState(bool state)` | `ignoreCanUseSelfDestructActive`を設定するだけ。 |
| `setIgnoreCanEjectFromVehicleActiveState(bool state)` | `ignoreCanEjectFromVehicleActive`を設定するだけ。 |
| `activateSelfDestructionOnVehicleExternally(float newSelfDestructDelayTime)` | 自爆禁止・待ち時間・乗員降車なしを設定し、未起動なら自爆コルーチンを開始する。 |
| `activateSelfDestruction()` | 未起動なら自爆コルーチンを開始し、起動済みなら停止してフラグとビープを解除する。 |
| `callEventOnGetOff()` | `useEventsOnStateChanged`が有効で登録があれば`eventOnGetOff`を発火する。 |
| `callEventOnGetOn()` | `useEventsOnStateChanged`が有効で登録があれば`eventOnGetOn`を発火する。 |
| `callEventOnDestroyed()` | `useEventsOnStateChanged`が有効で登録があれば`eventOnDestroyed`を発火する。 |
| `ejectFromVehicle()` | 全乗員を降車させ、搭乗・運転状態をfalseにして状態変更イベントと`changeVehicleState`を呼ぶ。 |
| `ejectFromVehicleWithFreeFloatingMode()` | フリーフローティングモードを有効にしてから`ejectFromVehicle`を呼ぶだけ。 |
| `changeIgnorePassengerCollidersState(bool state)` | 前回乗員のコライダーと車体コライダー間の`Physics.IgnoreCollision`を一括で設定する。 |
| `ignoreCollisionWithVehicleColliderList(List<Collider> colliderList, bool state)` | メッシュ付きコライダー群と指定リストの全組み合わせで衝突判定を無視または復帰させる。 |
| `ignoreCollisionWithVehicleColliderList(Collider colliderToIgnore, bool state)` | メッシュ付きコライダー群と指定コライダー1個の衝突判定を無視または復帰させる。 |
| `ignoreCollisionWithSolidVehicleColliderList(Collider colliderToIgnore, bool state)` | 車体の`colliderParts`全てと指定コライダーの衝突判定を無視または復帰させる。 |
| `checkIgnorPassengersCollidersState()` | 既存コルーチンを停止し、1秒だけ乗員コライダーを無視して戻すコルーチンを開始する。 |
| `setVehiceColliderWithMeshListLayer(string newLayerName)` | `colliderWithMeshesParts`の各GameObjectのレイヤーを名前から解決して設定する。 |
| `setVehiceColliderListLayer(string newLayerName)` | `colliderParts`の各GameObjectのレイヤーを名前から解決して設定する。 |
| `setVehicleOriginalListLayer()` | `colliderParts`のレイヤーを保存済みの`colliderLayerIndexParts`へ戻す。 |
| `getVehicleCollider()` | `vehicleDamageReceiver`を持つ最初の`colliderParts`を返し、無ければnullを返す。 |
| `manualStartOrStopVehicle(bool state, GameObject passenger)` | 乗降イベントとカーソル処理後、`isBeingDriven`を設定し`changeVehicleState`を呼ぶ。 |
| `setCurrentPassenger(GameObject passenger)` | `currentPassenger`を設定するだけ。 |
| `activateDevice()` | 盗難判定を行い、必要ならAI運転者を降車させてから乗降処理を実行する。 |
| `setIgnoreSettingPassengerStateActiveState(bool state)` | `ignoreSettingPassengerStateActive`を設定するだけ。 |
| `setPassengerState(bool passengerOnDriverSeat)` | 乗員一覧を更新し、運転席なら`isBeingDriven`を反転、乗降イベントと自動ブレーキを処理する。 |
| `activateAutoBrakeOnGetOff()` | `mainVehicleController`の自動ブレーキ処理を呼ぶだけ。 |
| `updatePassengersInVehicleCheckState()` | 乗員リストの数から`passengersOnVehicle`をtrue/falseに更新するだけ。 |
| `activaAIVehicle()` | 乗員がいて運転中なら何もせず、そうでなければ運転状態を反転して状態変更イベントを呼ぶ。 |
| `setUsedByAIState(bool state)` | 値が変わった時だけ`usedByAI`を設定し、運転状態と食い違えば`activaAIVehicle`で反転させる。 |
| `setUsedByAIStateWithoutActivatingDrvingState(bool state)` | 値が変わった時だけ`usedByAI`を設定するだけ。 |
| `currentVehicleVelocity()` | `mainRigidbody`の`linearVelocity`を返し、未設定なら`Vector3.zero`を返す。 |
| `addObjectToIgnoreCollision(GameObject newObject)` | `objectsToIgnoreCollisions`に追加しnullを除去して無効化フラグを更新する。 |
| `removeObjectToIgnoreCollision(GameObject newObject)` | `objectsToIgnoreCollisions`から削除しnullを除去して無効化フラグを更新する。 |
| `checkOnCollisionEnterExternally(Collision collision)` | `checkOnCollisionEnterOnlyExternally`を無視して外部から衝突処理一式を実行させる。 |
| `setNewVehicleGravityForce(float newVehicleGravityForce)` | 重力制御がある場合のみ`vehicleGravitymanager`へ新しい重力値を渡す。 |
| `setOriginalGravityForce()` | 重力制御がある場合のみ`vehicleGravitymanager`の元の重力値へ戻す。 |
| `setReducedVehicleSpeed(float newValue)` | `mainRigidbody.linearVelocity`に引数の値を掛けて速度を変化させる。 |
| `launchCharacterOnVehicleCollision(Vector3 collisionDirection, float collisionVelocity)` | 搭乗者を降車させて`pushFullCharacter`で吹き飛ばし、設定時はダメージも与える。 |
| `checkIfDetectSurfaceBelongToVehicle(Collider surfaceFound)` | `colliderParts`に含まれるコライダーかどうかを返すだけ。 |
| `getHealth(float amount)` | 生存中に`healthAmount`を加算・上限clampし、HPバーとダメージ演出を更新する。 |
| `updateHealthSlider(float value)` | `vehicleHealth`が割り当て済みなら`value`を設定するだけ。 |
| `getEnergy(float amount)` | 生存中に`boostAmount`を加算・上限clampし、ブーストバーを更新する。 |
| `removeEnergy(float amount)` | `boostAmount`を減算して0未満をclampし、ブーストバーを更新する。 |
| `updateEnergySlider(float value)` | `vehicleBoost`が割り当て済みなら`value`を設定するだけ。 |
| `getFuel(float amount)` | 生存中に`fuelAmount`を加算し、上限到達でガソリンタンクを無効化して燃料バーを更新する。 |
| `updateFuelSlider(float value)` | `vehicleFuel`が割り当て済みなら`value`を設定するだけ。 |
| `setGasTankState(bool state)` | `gasTankManager`にトリガーの有効/無効を渡すだけ。 |
| `refillFuelTank()` | `gasTankManager`の使用量を取得し、0より大きければ`getFuel`で燃料を補充する。 |
| `refillFuelTankByInventoryObject()` | 運転中かつタンクがある時、インベントリ自動使用を運転者に設定して元の設定へ戻す。 |
| `getAmmo(string ammoName, int amount)` | 武器マネージャが有効なら`getAmmo`へ名前と数量をそのまま渡す。 |
| `getSpeed(float speed, float maxSpeed)` | `currentSpeed`テキストを「速度 / 最大速度」形式で更新する。 |
| `manageBarInfo(string sliderType, bool regenerate, bool constantRegenerate, float regenerateSpeed, float regenerateTime, float regenerateAmount, Slider bar, float barAmount, float maxAmount, float lastTime)` | 再生設定に応じ、待ち時間経過後に体力・エネルギー・燃料を速度または量で回復させる。 |
| `useBoost(bool moving)` | 移動中にブーストを消費し、無限なら最大値に保ち、使用可否をboolで返す。 |
| `setVehicleUseFuelState(bool state)` | `vehicleUseFuel`を設定するだけ。 |
| `setPauseVehicleUseFuelState(bool state)` | `pauseVehicleUseFuel`を設定するだけ。 |
| `useFuel()` | 燃料使用が無効/停止中や無限ならtrueを返し、通常は`fuelUseRate`で消費してバーを更新する。 |
| `removeFuel(float amount)` | 燃料使用が有効なら`amount`を減算し、0未満clampとタンク再有効化、バー更新を行う。 |
| `setRemainFuel(float newAmount)` | `fuelAmount`を設定するだけ。 |
| `activateEventToSendCurrentFuelAmount()` | 現在の`fuelAmount`を引数に`eventToSendCurrentFuelAmount`を発火する。 |
| `activateEventToSendCurrentHealthAmount()` | 現在の`healthAmount`を引数に`eventToSendCurrentHealthAmount`を発火する。 |
| `activateEventToSendCurrentBoostAmount()` | 現在の`boostAmount`を引数に`eventToSendCurrentBoostAmount`を発火する。 |
| `setRemainHealth(float newAmount)` | `healthAmount`を設定するだけ。 |
| `setRemainBoost(float newAmount)` | `boostAmount`を設定するだけ。 |
| `setHealthInfo()` | 割り当て済みなら`vehicleHealth`の`maxValue`と`value`を現在値に設定する。 |
| `setBoostInfo()` | 割り当て済みなら`vehicleBoost`の`maxValue`と`value`を現在値に設定する。 |
| `setFuelInfo()` | 割り当て済みなら`vehicleFuel`の`maxValue`と`value`を現在値に設定する。 |
| `setWeaponName(string name, int ammoPerClip, int clipSize)` | 武器名テキストと`vehicleAmmo`の最大値・現在値を設定する。 |
| `useAmmo(int clipSize, int remainAmmo)` | 弾薬テキストを「クリップ/残弾」または「/Inf」で表示し、`vehicleAmmo`値を更新する。 |
| `setDamage(float amount, Vector3 fromDirection, Vector3 damagePos, GameObject bulletOwner, GameObject projectile, bool damageConstant, bool searchClosestWeakSpot, bool damageCanBeBlocked)` | 飛翔体の重複と無敵・破壊済みを除外し、弱点判定後にHPを減らして被弾演出と破壊処理を行う。 |
| `setDamageTargetOverTimeState(float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, int damageTypeID)` | 既存の継続ダメージを停止し、間隔ごとに`setDamage`を呼ぶコルーチンを開始する。 |
| `stopDamageOverTime()` | `damageOverTimeCoroutine`が存在すれば停止するだけ。 |
| `setDamageOrHealthTargetWithDelay(float waitAmount, float valueAmount, int damageTypeID)` | 既存の遅延処理を停止し、待機後に正なら回復・負ならダメージを与えるコルーチンを開始する。 |
| `stopDamageOrHealthTargetWithDelay()` | `damageOrHealthTargetWithDelayCoroutine`が存在すれば停止するだけ。 |
| `getClosesWeakSpotIndex(Vector3 collisionPosition)` | `damageReceiverList`のうち指定位置に最も近い弱点の添字を返し、無ければ-1を返す。 |
| `fixDestroyedVehicle()` | 破壊済みなら`destroyed`を解除し、体力・燃料・ブーストを満タンにして各修復処理とイベントを呼ぶ。 |
| `destroyVehicleWithoutExplodeOrSeparateParts()` | 爆発設定を一時的にfalseにして破壊処理を実行し、終了後に設定を戻す。 |
| `destroyVehicleWithoutExplodeOrSeparatePartsAndDisableInteraction()` | 上記の非爆発破壊に加え、同乗者のデバイス登録を外しメインコライダーを無効化する。 |
| `destroyVehicle(Vector3 damagePosition)` | 被破壊イベントの後、爆発設定時はパーツ分離・爆風・音・フェードを行い、最後にIK運転を無効化する。 |
| `destroyVehicleAtOnce()` | `IKDrivingManager.destroyVehicle`を呼ぶだけ。 |
| `getHUDBars(playerHUDManager newVehicleHUDInfo, playerHUDManager.vehicleHUDElements hudElements, bool drivingState)` | HUD各要素の参照を保持してバー値を反映し、武器・体力・燃料・ブースト・速度の表示可否を切り替える。 |
| `getCurrentHUDElements()` | `currentHUDElements`を返すだけ。 |
| `getCurrentVehicleHUDInfo()` | `currentVehicleHUDInfo`を返すだけ。 |
| `setWeaponState(bool state)` | 武器有効かつ未破壊なら武器状態を変更し、弾薬表示とカーソルの表示を切り替える。 |
| `showVehicleHUDActive()` | `showVehicleHUD`を返すだけ。 |
| `isDisablePlayerHUDEnabled()` | `disablePlayerHUDEnabled`を返すだけ。 |
| `useJumpPlatform(Vector3 direction)` | `useJumpPlatformEvents`が有効なら`jumpPlatformEvent`へ方向を渡して発火する。 |
| `useJumpPlatformParable(Vector3 direction)` | イベント使用が有効なら`jumpPlatformParableEvent`へ方向を渡して発火する。 |
| `useJumpPlatformWithKeyButton(bool state, float newJumpPower)` | 状態に応じてジャンプ力設定イベントか元に戻すイベントを発火する。 |
| `debugLaunchCharacterOnVehicleCollision()` | デバッグ用の位置と速度から方向を計算し、`launchCharacterOnVehicleCollision`を呼ぶ。 |
| `setVehicleParts()` | 各種パーツ・コライダー・レンダラー・武器リストを再取得し、シーンをダーティにしてログを出す。 |
| `setVehicleDamageReceivers()` | `vehicleDamageReceiver`を全取得して親車両を設定し、リストへ登録してインスペクタを更新する。 |
| `updateVehicleDamageReceivers()` | `setVehicleDamageReceivers`を呼び、シーンをダーティに更新する。 |
| `setColliderList()` | 非トリガーコライダーとレイヤーを収集し、Renderer無しのコライダーを別リストに分けて更新する。 |
| `setColliderWithoutMeshesPartsToIgnore(List<Transform> newList)` | 渡されたTransform群のコライダーを無視リストへ入れ、インスペクタを更新する。 |
| `setVehicleRendererParts()` | `vehiclePartsToIgnore`以外の子Rendererを`vehicleRendererList`へ集める。 |
| `setVehicleParticleSystemList()` | `damageParticles`配下の`ParticleSystem`を`fireParticles`に集め直し、`updateComponent`を呼ぶ。 |
| `setVehiclePartsInfoList()` | `vehicleRendererList`の各要素から`vehiclePartInfo`を作り直して`vehiclePartInfoList`を更新する。 |
| `setCustomVehiclePartsListToDestroy()` | `useCustomVehiclePartsToDestroy`が有効な時、カスタム破壊パーツの`Rigidbody`と`Collider`を取得し直す。 |
| `setVehicleInput()` | `IKDrivingManager`の`inputActionManager`の`setInputManagerOnEditor`を呼び出す。 |
| `setVehicleWeaponsComponents()` | `weaponsManager`が設定されていれば、その`setVehicleWeaponsComponents`を呼ぶだけ。 |
| `getVehicleComponents()` | `vehicleController`を取得して車両コンポーネントを収集し、`vehicleGravitymanager`に設定して更新する。 |
| `getAllDamageReceivers()` | 子の`vehicleDamageReceiver`を列挙し、`damageReceiverList`を「Spot N」名で作り直す。 |
| `getMaxHealthAmount()` | `maxHealthAmount`を返すだけ。 |
| `getAuxHealthAmount()` | `auxHealthAmount`を返すだけ。 |
| `addAuxHealthAmount(float amount)` | `auxHealthAmount`に`amount`を加算するだけ。 |
| `getHealthAmountToLimit()` | `maxHealthAmount`から`auxHealthAmount`を引いた残量を返す。 |
| `getCurrentEnergyAmount()` | エネルギー量として`boostAmount`を返すだけ。 |
| `getMaxEnergyAmount()` | `maxBoostAmount`を返すだけ。 |
| `getAuxEnergyAmount()` | `auxPowerAmount`を返すだけ。 |
| `addAuxEnergyAmount(float amount)` | `auxPowerAmount`に`amount`を加算するだけ。 |
| `getEnergyAmountToLimit()` | `maxBoostAmount`から`auxPowerAmount`を引いた残量を返す。 |
| `checkIfMaxEnergy()` | 現在のエネルギーが最大以上かどうかを返すだけ。 |
| `getCurrentFuelAmount()` | `fuelAmount`を返すだけ。 |
| `getMaxFuelAmount()` | `maxFuelAmount`を返すだけ。 |
| `getAuxFuelAmount()` | `auxFuelAmount`を返すだけ。 |
| `addAuxFuelAmount(float amount)` | `auxFuelAmount`に`amount`を加算するだけ。 |
| `getFuelAmountToLimit()` | `maxFuelAmount`から`auxFuelAmount`を引いた残量を返す。 |
| `hasFuel()` | 燃料が残っているか、または`vehicleUseFuel`が無効ならtrueを返す。 |
| `killByButton()` | `destroyVehicle`を呼び出して車両を破壊するだけ。 |
| `destroyVehicle()` | 自車両に体力全量分のダメージを与える`setDamage`を、前方・上方位置を指定して呼ぶ。 |
| `takeHealth(float damageAmount)` | `damageVehicle`に`damageAmount`を渡すだけ。 |
| `damageVehicle(float damageAmount)` | `setDamage`で`damageAmount`分の被弾処理を自車両に対して実行する。 |
| `getVehicleRadius()` | `vehicleRadius`を返すだけ。 |
| `activateHorn()` | `useHornEvent`が有効なら`hornEvent`を発火し、続けて`callToFriends`を呼ぶ。 |
| `callToFriends()` | `useHornToCallFriends`が有効なら、現ドライバーの`friendListManager`で既知の仲間を呼ぶか`radiusToCallFriends`内を探索させる。 |
| `getPlaceToShoot()` | `placeToShoot`を返すだけ。 |
| `getCurrentDriver()` | `IKDrivingManager`の現在のドライバーを返し、未設定ならnullを返す。 |
| `getLastDriver()` | `IKDrivingManager`の最後のドライバーを返し、未設定ならnullを返す。 |
| `currentDriverIsAI()` | 現在のドライバーがAIかどうかを`IKDrivingManager`に問い合わせる。 |
| `getOffFromVehicleToDriverAI()` | `IKDrivingManager`の`getOffFromVehicleToDriverAI`を呼ぶだけ。 |
| `getVehicleName()` | `vehicleName`を返すだけ。 |
| `setVehicleName(string newName)` | `vehicleName`を設定し、`updateComponent`と`updateDirtyScene`でシーンを更新する。 |
| `getImpactListInfo()` | `impactDecalManager`が無ければ生成し、デカール名一覧を`impactDecalList`に複製する。 |
| `getDecalImpactIndex()` | `impactDecalIndex`を返すだけ。 |
| `isUseImpactSurfaceActive()` | `useImpactSurface`を返すだけ。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | 破壊済みなら何もせず、`layerForPassengers`のレイヤーなら`IKDrivingManager`にトリガー情報を渡す。 |
| `getVehicleCameraController()` | `vehicleCameraManager`を返すだけ。 |
| `getAudioSourceElement(string name)` | `audioSourceList`から名前が一致する`AudioSource`を返し、無ければnullを返す。 |
| `isVehicleBeingDriven()` | `isBeingDriven`を返すだけ。 |
| `isVehicleFull()` | `IKDrivingManager`の`isVehicleFull`に問い合わせて結果を返す。 |
| `getIKDrivingSystem()` | `IKDrivingManager`を返すだけ。 |
| `getVehicleGravityControl()` | `vehicleGravitymanager`を返すだけ。 |
| `isForcingPassengersToGetOffOnVehicleDestroyedActive()` | `IKDrivingManager`の同メソッドに問い合わせて結果を返す。 |
| `setPlayerCameraParentAndPosition(Transform mainCameraTransform, playerCamera playerCameraManager)` | カメラの親と位置を`IKDrivingManager`に設定し、武器有効時は`weaponsManager`へカメラ情報を渡す。 |
| `vehicleIsDestroyed()` | `destroyed`を返すだけ。 |
| `setInvencibleState(bool state)` | `invincible`を`state`に設定するだけ。 |
| `setInfiniteEnergyState(bool state)` | `infiniteBoost`を`state`に設定するだけ。 |
| `setInfiniteFuelState(bool state)` | `infiniteFuel`を`state`に設定するだけ。 |
| `setVehicleAndCameraParent(Transform newParent)` | カメラの親を`vehicleCameraManager`に設定し、親の有無に応じて子状態フラグを更新する。 |
| `setNewMainCameraTransform(Transform newTransform)` | `mainVehicleController`の`setNewMainCameraTransform`を呼ぶだけ。 |
| `setNewPlayerCameraTransform(Transform newTransform)` | `mainVehicleController`の`setNewPlayerCameraTransform`を呼ぶだけ。 |
| `setUseForwardDirectionForCameraDirectionState(bool state)` | `mainVehicleController`に前方方向をカメラ方向に使う状態を設定させる。 |
| `setUseRightDirectionForCameraDirectionState(bool state)` | `mainVehicleController`に右方向をカメラ方向に使う状態を設定させる。 |
| `setAddExtraRotationPausedState(bool state)` | `mainVehicleController`の追加回転を一時停止する状態を設定させる。 |
| `isVehicletAsChildOfParent()` | `vehicleSetAsChildOfParent`を返すだけ。 |
| `setVehicletAsChildOfParentState(bool state)` | `vehicleSetAsChildOfParent`を`state`に設定するだけ。 |
| `setExplodeVehicleWhenDestroyedEnabledState(bool state)` | `explodeVehicleWhenDestroyedEnabled`を`state`に設定するだけ。 |
| `setFadeVehiclePiecesOnDestroyedState(bool state)` | `fadeVehiclePiecesOnDestroyed`を`state`に設定するだけ。 |
| `checkIfMaxHealth()` | 現在の体力が最大以上かどうかを返すだけ。 |
| `getHealthAmountToPick(float amount)` | 限界までの残量と`amount`を比べ、加算した実量を返しつつ`auxHealthAmount`を増やす。 |
| `checkIfMaxFuel()` | 現在の燃料が最大以上かどうかを返すだけ。 |
| `setRegenerateFuelState(bool state)` | `regenerateFuel`を`state`に設定するだけ。 |
| `setOriginalRegenerateFuelState()` | `originalRegenerateFuelValue`で燃料自動回復の状態を戻す。 |
| `startBrakeVehicleToStopCompletely()` | `mainVehicleController`の停止ブレーキ開始処理を呼ぶだけ。 |
| `endBrakeVehicleToStopCompletely()` | `mainVehicleController`の停止ブレーキ終了処理を呼ぶだけ。 |
| `getCurrentSpeed()` | `mainVehicleController`から現在速度を取得して返す。 |
| `changeVehicleState()` | `mainVehicleController`の`changeVehicleState`を呼ぶだけ。 |
| `passengerGettingOnOff()` | `mainVehicleController`の`passengerGettingOnOff`を呼ぶだけ。 |
| `isVehicleOnGround()` | `mainVehicleController`に接地状態を問い合わせて返す。 |
| `getHorizontalAxis()` | `mainVehicleController`の横軸入力を返す。 |
| `getVerticalAxis()` | `mainVehicleController`の縦軸入力を返す。 |
| `getPassengerGameObjectList()` | `IKDrivingManager`から乗員の`GameObject`リストを取得して返す。 |
| `inputShowControlsMenu()` | 運転中なら操作メニューの開閉状態を反転させて切り替える。 |
| `inputSelfDestruct()` | 自爆禁止や球体モードでない等の条件を満たす時、`activateSelfDestruction`で自爆を開始/停止する。 |
| `inputEject()` | 射出禁止や球体モードでない等の条件を満たす時、`ejectFromVehicle`で乗員を射出する。 |
| `inputEjectWithFreeFloatingMode()` | 条件を満たす時、`ejectFromVehicleWithFreeFloatingMode`で自由浮遊モード付き射出を行う。 |
| `inputUnLockCursor()` | 運転中かつカーソル解除可能なら、カーソル解除状態を反転させる。 |
| `inputHoldOrReleaseSecondaryButton(bool holdingButton)` | カーソル解除中のみ、押下でカメラを停止し、離すと再開する。 |
| `inputGetOffFromVehicle()` | 運転中で球体モードでなければ、`IKDrivingManager`に降車を要求する。 |
| `inputJump()` | `mainVehicleController`の`inputJump`を呼ぶだけ。 |
| `inputHoldOrReleaseJump(bool holdingButton)` | `mainVehicleController`へジャンプの押下/離しをそのまま渡す。 |
| `inputHoldOrReleaseTurbo(bool holdingButton)` | `mainVehicleController`へターボの押下/離しをそのまま渡す。 |
| `inputSetTurnOnState()` | `mainVehicleController`の`inputSetTurnOnState`を呼ぶだけ。 |
| `inputHorn()` | `mainVehicleController`の`inputHorn`を呼ぶだけ。 |
| `inputHoldOrReleaseBrake(bool holdingButton)` | `mainVehicleController`へブレーキの押下/離しをそのまま渡す。 |
| `inputRefillFuelTankByInventoryObject()` | 運転中で燃料タンクがあれば、現ドライバーを在庫消費元として自動給油処理を実行する。 |
| `getAIVehicleNavmesh()` | `mainVehicleAINavMesh`を返すだけ。 |
| `setHealthAmount(float newValue)` | `healthAmount`を`newValue`に設定するだけ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`でこのコンポーネントのインスペクタ表示を更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `hornEvent` | `UnityEvent` | – |
| `eventOnGetOn` | `UnityEvent` | – |
| `eventOnGetOff` | `UnityEvent` | – |
| `eventOnDestroyed` | `UnityEvent` | – |
| `eventOnFixDestroyedVehicle` | `UnityEvent` | – |
| `setOriginalJumpPowerEvent` | `UnityEvent` | – |
| `passengerGettingOnOffEvent` | `UnityEvent` | – |
| `changeVehicleStateEvent` | `UnityEvent` | – |
| `eventToCheckIfVehicleUsedByAIOnPassengerEnter` | `UnityEvent` | – |
| `eventToCheckIfVehicleUsedByAIOnPassengerExit` | `UnityEvent` | – |
| `eventOnCustomVehicleParts` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnTriggerEnter(Collider col)`, `OnTriggerExit(Collider col)`, `addAuxHealthAmountWithHealthManagement(float amount)`, `checkIfDeadWithHealthManagement()`, `checkIfDetectSurfaceBelongToVehicleWithHealthManagement(Collider surfaceFound)`, `checkIfMaxEnergyWithHealthManagement()`, `checkIfMaxFuelWithHealthManagement()`, `checkIfMaxHealthWithHealthManagement()`, `getAuxHealthAmountWithHealthManagement()`, `getCharacterOrVehicleWithHealthManagement()`, `getCurrentEnergyAmountWithHealthManagement()`, `getCurrentFuelAmountWithHealthManagement()`, `getCurrentHealthAmount()`, `getCurrentHealthAmountWithHealthManagement()`, `getCurrentShieldAmount()`, `getDecalImpactIndexWithHealthManagement()`, `getHealthAmountToPickWithHealthManagement(float amount)`, `getMaxHealthAmountWithHealthManagement()`, `getPlaceToShootGameObjectWithHealthManagement()`, `getPlaceToShootWithHealthManagement()`, `getVehicleDriverWithHealthManagement()`, `getVehicleHUDManagerWithHealthManagement()`, `getVehicleWithHealthManagement()`, `isDead()`, `isUseImpactSurfaceActiveWithHealthManagement()`, `isUseShieldActive()`, `isVehicleBeingDrivenWithHealthManagement()`, `isVehicleWithHealthManagement()`, `killCharacterWithHealthManagement()`, `killCharacterWithHealthManagement(GameObject projectile, Vector3 direction, Vector3 position, GameObject attacker, bool damageConstant)`, `removeDamagetTargetOverTimeStateWithHealthManagement()`, `removeEnergyWithHealthManagement(float amount)`, `removeFuelWithHealthManagement(float fuelAmount)`, `setDamageOrHealthTargetWithDelayWithHealthManagement(float waitAmount, float valueAmount, int damageTypeID)`, `setDamageTargetOverTimeStateWithHealthManagement(float damageOverTimeDelay, float damageOverTimeDuration, float damageOverTimeAmount, float damageOverTimeRate, bool damageOverTimeToDeath, int damageTypeID)`, `setDamageWithHealthManagement(float damageAmount, Vector3 fromDirection, Vector3 damagePos, GameObject attacker, GameObject projectile, bool damageConstant, bool searchClosestWeakSpot, bool ignoreShield, bool ignoreDamageInScreen, bool damageCanBeBlocked, bool canActivateReactionSystemTemporally, int damageReactionID, int damageTypeID)`, `setEnergyWithHealthManagement(float amount)`, `setFuelWithHealthManagement(float fuelAmount)`, `setHealWithHealthManagement(float healAmount)`

</details>

## 内部型

- `advancedSettingsClass`（class）
- `damageReceiverInfo`（class）
- `vehiclePartInfo`（class）
