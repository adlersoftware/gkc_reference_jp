# weaponSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/weaponSystem.cs:8`

**概要**: IK 付きの一人称/三人称武器の中核。射撃、弾生成、弾薬、HUD、騒音などを管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Settings | `weaponSettings` | `weaponInfo` | – | – |
| Out Of Ammo | `outOfAmmo` | `AudioClip` | – | – |
| Out Of Ammo Audio Element | `outOfAmmoAudioElement` | `AudioElement` | – | – |
| Weapon Projectile | `weaponProjectile` | `GameObject` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Projectiles Pool Enabled | `projectilesPoolEnabled` | `bool` | true | – |
| Max Amount Of Pool Elements On Weapon | `maxAmountOfPoolElementsOnWeapon` | `int` | 30 | – |
| Main Decal Manager Name | `mainDecalManagerName` | `string` | "Decal Manager" | – |
| Main Noise Mesh Manager Name | `mainNoiseMeshManagerName` | `string` | "Noise Mesh Manager" | – |
| Impact Decal List | `impactDecalList` | `string[]` | – | – |
| Impact Decal Index | `impactDecalIndex` | `int` | – | – |
| Impact Decal Name | `impactDecalName` | `string` | – | – |
| Get Impact List Every Frame | `getImpactListEveryFrame` | `bool` | – | – |
| Can Mark Targets | `canMarkTargets` | `bool` | – | – |
| Tag List To Mark Targets | `tagListToMarkTargets` | `List<string>` | new List<string> () | – |
| Mark Targets Layer | `markTargetsLayer` | `LayerMask` | – | – |
| Mark Target Name | `markTargetName` | `string` | – | – |
| Max Distance To Mark Targets | `maxDistanceToMarkTargets` | `float` | – | – |
| Can Mark Targets On First Person | `canMarkTargetsOnFirstPerson` | `bool` | – | – |
| Can Mark Targets On Third Person | `canMarkTargetsOnThirdPerson` | `bool` | – | – |
| Aim On First Person To Mark Target | `aimOnFirstPersonToMarkTarget` | `bool` | – | – |
| Use Mark Target Sound | `useMarkTargetSound` | `bool` | – | – |
| Mark Target Sound | `markTargetSound` | `AudioClip` | – | – |
| Mark Target Audio Element | `markTargetAudioElement` | `AudioElement` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | new List<string> () | – |
| Use Remote Event On Objects Found On Explosion | `useRemoteEventOnObjectsFoundOnExplosion` | `bool` | – | – |
| Remote Event Name On Explosion | `remoteEventNameOnExplosion` | `string` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reloading | `reloading` | `bool` | – | – |
| Carrying Weapon In Third Person | `carryingWeaponInThirdPerson` | `bool` | – | – |
| Carrying Weapon In First Person | `carryingWeaponInFirstPerson` | `bool` | – | – |
| Aiming In Third Person | `aimingInThirdPerson` | `bool` | – | – |
| Aiming In First Person | `aimingInFirstPerson` | `bool` | – | – |
| Show Settings | `showSettings` | `bool` | – | – |
| Using Weapon | `usingWeapon` | `bool` | – | – |
| Use Ammo From Main Player Weapon System | `useAmmoFromMainPlayerWeaponSystem` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | – |
| Player Camera Game Object | `playerCameraGameObject` | `GameObject` | – | – |
| IK Weapon Manager | `IKWeaponManager` | `IKWeaponSystem` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | – |
| Weapons Effects Source | `weaponsEffectsSource` | `AudioSource` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Weapon Animation | `weaponAnimation` | `Animation` | – | – |
| Parable | `parable` | `launchTrayectory` | – | – |
| Player Collider | `playerCollider` | `Collider` | – | – |
| Main Player Weapon System | `mainPlayerWeaponSystem` | `playerWeaponSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setWeaponCarryState(bool thirdPersonCarry, bool firstPersonCarry)` | 三人称/一人称の所持状態を設定し、放物線表示と武器アビリティ、所持開始/終了イベントを実行する。 |
| `setWeaponAimState(bool thirdPersonAim, bool firstPersonAim)` | 三人称/一人称の照準状態を設定し、空なら自動リロード、照準イベントや敵アイコン消去を行う。 |
| `setUsingWeaponState(bool state)` | 使用中フラグを設定し、HUD の武器アイコン・弾数表示を更新する。 |
| `checkCarryAndAimStates()` | 管理側の所持・照準状態と差異があれば、対応する setter を呼んで同期する。 |
| `inputShootWeaponOnPressDown()` | 入力可能かつ照準/一人称所持中でカーソル固定時、条件に応じ `shootWeapon(true)` を呼ぶ。 |
| `inputShootWeaponOnPressUp()` | 入力可能かつ射撃可能な状態なら `shootWeapon(false)` を呼ぶ。 |
| `inputShootWeaponOnPress()` | 自動武器かつバースト以外のとき、`shootWeapon(true)` を呼ぶ。 |
| `shootWeapon(bool state)` | 多忙でなければカーソル・走行・射撃状態を整え、内部の射撃処理に委譲する。 |
| `shootWeapon(bool isThirdPersonView, bool shootAtKeyDown)` | 発射可否・連射間隔・弾薬を確認し、弾生成・拡散・照準・リコイル・弾薬消費まで行う。 |
| `checkWeaponAbility(bool keyDown)` | `weaponWithAbility` のとき、押下/離しに応じた UnityEvent を実行する。 |
| `removeLocatedEnemiesIcons()` | 捕捉中の敵アイコンを全て削除し、リストを空にする。 |
| `setProjectileInfoAssignedValue(bool state)` | `projectileInfoAssigned` を設定するだけ。 |
| `setSeekerProjectileInfo(Vector3 shootPosition)` | 必要ならカメラを取得し、`applyDamage` で索敵して目標オブジェクトを返す。 |
| `setProjectileSpread()` | 一人称/三人称と照準状態から拡散量を決め、ランダムな回転量を返す。 |
| `checkDroppedShellsRemoval()` | 排莢後 3 秒経過で、保持中の薬莢を返却または破棄して一覧を空にする。 |
| `playSound(AudioElement clipSound)` | 効果音源を設定してから、指定 `AudioElement` をワンショット再生する。 |
| `useAmmo()` | 共有弾薬設定なら管理側に委譲し、そうでなければクリップを 1 減らして HUD を更新する。 |
| `useAmmo(int amount)` | 共有設定なら委譲し、そうでなければ上限で丸めて `amount` 減らし HUD を更新する。 |
| `reloadWeapon(float waitTimeAmount)` | 既存のリロードを止め、`waitTimeAmount` 秒待つ `waitToReload` を開始する。 |
| `manualReload()` | リロード中でなくクリップが満杯未満なら、`reloadTime` で `reloadWeapon` を呼ぶ。 |
| `canIncreaseRemainAmmo()` | `auxRemainAmmo` が `ammoLimit` 未満かどうかを返す。 |
| `hasMaximumAmmoAmount()` | 弾数上限が有効で残弾が上限以上なら true を返す。 |
| `hasAmmoLimit()` | `useAmmoLimit` を返すだけ。 |
| `ammoAmountToMaximumLimit()` | `ammoLimit` までの不足分を返すだけ。 |
| `getAmmo(int amount)` | 残弾に加算し、空で所持/照準中なら自動リロードし、補助残弾を更新する。 |
| `addAuxRemainAmmo(int amount)` | `auxRemainAmmo` に加算するだけ。 |
| `hasAnyAmmo()` | 残弾・クリップ・無限弾のいずれかがあれば true を返す。 |
| `getAndUpdateAmmo(int amount)` | `getAmmo` を呼び、HUD の弾数表示を更新する。 |
| `remainAmmoInClip()` | クリップに弾が残っているかを返す。 |
| `launchCurrentProjectile(GameObject currentProjectile, Rigidbody projectileRigidbody, Vector3 cameraDirection)` | kinematic を解除し、放物線速度か前方への力を加えて弾を発射する。 |
| `checkParableTrayectory(bool usingThirdPerson, bool usingFirstPerson)` | 条件に応じて放物線表示 `parable` の有効/無効と発射位置を設定する。 |
| `getWeaponComponents(playerWeaponsManager newPlayerWeaponsManager)` | 管理側の参照・カメラ・音源・アニメーション・放物線表示・コライダーを取得して更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` でこのコンポーネントを更新するだけ。 |
| `getImpactListInfo()` | `decalManager` を探して着弾デカール名の一覧を構築し、更新する。 |
| `setReducedVelocity(float multiplierValue)` | `weaponSpeed` に倍率を掛けるだけ。 |
| `setNormalVelocity()` | `weaponSpeed` を初期値に戻すだけ。 |
| `getWeaponSystemName()` | 武器名 `Name` を返すだけ。 |
| `getWeaponClipSize()` | クリップ内の弾数を返すだけ。 |
| `getCurrentAmmoText()` | クリップ数と残弾を表す文字列を返し、無限弾なら `Inf` を付ける。 |
| `enableMuzzleFlashLight()` | `useMuzzleFlash` なら一度止めてからマズルフラッシュのコルーチンを開始する。 |
| `checkWeaponShootNoise()` | 騒音設定に応じて騒音通知やノイズメッシュ生成を行う。 |

## 内部型

- `weaponInfo`（class）
