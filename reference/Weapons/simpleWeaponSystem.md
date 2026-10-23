# simpleWeaponSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/simpleWeaponSystem.cs:10`

**概要**: 武器コンポーネントの簡易版。射撃入力、弾の生成と向き、弾薬、リロード、効果音を扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Settings | `weaponSettings` | `weaponInfo` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Out Of Ammo | `outOfAmmo` | `AudioClip` | – | – |
| Out Of Ammo Audio Element | `outOfAmmoAudioElement` | `AudioElement` | – | – |
| Weapon Projectile | `weaponProjectile` | `GameObject` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Target For Scorch Layer | `targetForScorchLayer` | `LayerMask` | – | – |
| Projectiles Pool Enabled | `projectilesPoolEnabled` | `bool` | true | – |
| Max Amount Of Pool Elements On Weapon | `maxAmountOfPoolElementsOnWeapon` | `int` | 30 | – |
| Target To Damage Layer | `targetToDamageLayer` | `LayerMask` | – | – |
| Use Custom Ignore Tags | `useCustomIgnoreTags` | `bool` | – | – |
| Custom Tags To Ignore List | `customTagsToIgnoreList` | `List<string>` | new List<string> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Projectile Event On Fire | `sendProjectileEventOnFire` | `bool` | – | – |
| Projectile Event On Fire | `projectileEventOnFire` | `eventParameters.eventToCallWithGameObject` | – | – |

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
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Hold Shoot Active | `holdShootActive` | `bool` | – | – |
| Reloading | `reloading` | `bool` | – | – |
| Using Weapon | `usingWeapon` | `bool` | – | – |
| External Projectile To Fire Assigned | `externalProjectileToFireAssigned` | `bool` | – | – |
| External Projectile To Fire | `externalProjectileToFire` | `GameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Weapons Effects Source | `weaponsEffectsSource` | `AudioSource` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Weapon Animation | `weaponAnimation` | `Animation` | – | – |
| Player Collider | `playerCollider` | `Collider` | – | – |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | – |
| Player Camera Game Object | `playerCameraGameObject` | `GameObject` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Decal Manager Name | `mainDecalManagerName` | `string` | "Decal Manager" | – |
| Main Noise Mesh Manager Name | `mainNoiseMeshManagerName` | `string` | "Noise Mesh Manager" | – |
| Impact Decal List | `impactDecalList` | `string []` | – | – |
| Impact Decal Index | `impactDecalIndex` | `int` | – | – |
| Impact Decal Name | `impactDecalName` | `string` | – | – |
| Get Impact List Every Frame | `getImpactListEveryFrame` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `shootWeaponExternally()` | 押下と離しの入力処理を続けて呼び、外部から 1 回分の発射を実行する。 |
| `stopUpdateHoldShootWeaponCoroutine()` | 連射コルーチンを止め、保持中なら `shootWeapon(false)` で射撃を終了させる。 |
| `inputHoldOrReleaseShootWeapon(bool holdingButton)` | ボタン保持状態に応じて `setHoldShootWeaponState` を true/false で呼ぶだけ。 |
| `inputShootWeaponOnPressDown()` | `shootWeapon(true)` を呼ぶだけ。 |
| `inputShootWeaponOnPressUp()` | `shootWeapon(false)` を呼ぶだけ。 |
| `inputShootWeaponOnPress()` | `automatic` のときだけ `shootWeapon(true)` を呼ぶ。 |
| `shootWeapon(bool state)` | 武器管理を取得できれば一人称判定付きの `shootWeapon(bool,bool)` に委譲する。 |
| `addExternalProjectileToFire(GameObject newProjectile)` | 外部発射用の弾オブジェクトを設定し、有無フラグを更新する。 |
| `removeExternalProjectileToFire(GameObject newProjectile)` | 指定オブジェクトが現在の外部弾と一致するときだけ設定を解除する。 |
| `sendRemoteEventToExternalProjectile(string remoteEventName)` | 外部弾の `projectileSystem` にリモートイベント名を送る。 |
| `shootWeapon(bool isThirdPersonView, bool shootAtKeyDown)` | 連射間隔・弾薬を確認し、弾を生成して向き・拡散・威力を設定し、音や薬莢・弾薬消費まで行う。 |
| `checkWeaponAbility(bool keyDown)` | `weaponWithAbility` のとき、押下/離しに応じた UnityEvent を実行する。 |
| `updateProjectileInfoValues()` | 割り当て済みフラグを下ろして `setProjectileInfo` で弾情報を作り直す。 |
| `setProjectileInfoAssignedValue(bool state)` | `projectileInfoAssigned` を設定するだけ。 |
| `setTargetToDamageLayer(LayerMask newLayer)` | 対象レイヤーを保持し、設定済みなら `newProjectileInfo` にも反映する。 |
| `setSeekerProjectileInfo(Vector3 shootPosition)` | `applyDamage` に索敵を依頼し、最も近い目標オブジェクトを返す。 |
| `setProjectileSpread()` | 三人称照準時の拡散量からランダムな回転量を作り、0 なら零ベクトルを返す。 |
| `checkDroppedShellsRemoval()` | 排莢後 3 秒経過で、保持している薬莢をプール返却または破棄して一覧を空にする。 |
| `playSound(AudioElement clipSound)` | 効果音源を設定してから、指定 `AudioElement` をワンショット再生する。 |
| `useAmmo()` | `clipSize` を 1 減らすだけ。 |
| `useAmmo(int amount)` | 残弾数を上限に `clipSize` から `amount` を減らすだけ。 |
| `reloadWeapon(float waitTimeAmount)` | 既存のリロードを止め、`waitTimeAmount` 秒待つ `waitToReload` を開始する。 |
| `manualReload()` | リロード中でなくクリップが満杯未満なら、三人称リロード時間で `reloadWeapon` を呼ぶ。 |
| `canIncreaseRemainAmmo()` | `auxRemainAmmo` が `ammoLimit` 未満かどうかを返す。 |
| `hasMaximumAmmoAmount()` | 弾数上限が有効で残弾が上限以上なら true を返す。 |
| `hasAmmoLimit()` | `useAmmoLimit` を返すだけ。 |
| `ammoAmountToMaximumLimit()` | 上限までの不足分（`ammoLimit - auxRemainAmmo`）を返す。 |
| `getAmmo(int amount)` | 残弾に加算し、空だった場合は自動リロードし、最後に補助残弾を更新する。 |
| `addAuxRemainAmmo(int amount)` | `auxRemainAmmo` に加算するだけ。 |
| `hasAnyAmmo()` | 残弾・クリップ・無限弾のいずれかがあれば true を返す。 |
| `getAndUpdateAmmo(int amount)` | `getAmmo` を呼ぶだけ。 |
| `remainAmmoInClip()` | `clipSize` が 0 より大きいかを返す。 |
| `checkSendProjectileOnEventFire()` | フラグが立っていれば、生成した弾を引数に発射イベントを呼ぶ。 |
| `launchCurrentProjectile(GameObject newProjectile, Rigidbody projectileRigidbody, Vector3 cameraDirection)` | kinematic を解除し、放物線速度か前方への力を加えて弾を発射する。 |
| `checkParableTrayectory(bool usingThirdPerson, bool usingFirstPerson)` | 条件を判定するだけで本体が空のため、実質何もしない。 |
| `getImpactListInfo()` | `decalManager` を探して着弾デカール名の一覧を構築する。 |
| `setReducedVelocity(float multiplierValue)` | `weaponSpeed` に倍率を掛けるだけ。 |
| `setNormalVelocity()` | `weaponSpeed` を初期値に戻すだけ。 |
| `getWeaponSystemName()` | 武器名 `Name` を返すだけ。 |
| `getWeaponClipSize()` | `clipSize` を返すだけ。 |
| `getCurrentAmmoText()` | クリップ数と残弾を表す文字列を返し、無限弾なら `Inf` を付ける。 |
| `enableMuzzleFlashLight()` | `useMuzzleFlash` なら一度止めてからマズルフラッシュのコルーチンを開始する。 |
| `checkWeaponShootNoise()` | 騒音設定に応じて騒音通知やノイズメッシュ生成を行う。 |
| `getCurrentProjectileSystem()` | `currentProjectileSystem` を返すだけ。 |
| `getLastProjectilesSystemListFired()` | 直近に発射した弾のリストを返すだけ。 |
| `setCustomprojectilePosition(List<Transform> customProjectilePosition)` | `weaponSettings.projectilePosition` を差し替えるだけ。 |
| `setCustomTagsToIgnore(List<string> newTagList)` | null なら除外タグを無効化し、指定時はリストを差し替えて有効化する。 |
| `setCustommainCameraTransform(Transform newTransform)` | カメラ参照を保持し、null でなければカスタムカメラ使用を有効にする。 |
