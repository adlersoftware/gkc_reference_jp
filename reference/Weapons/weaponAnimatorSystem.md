# weaponAnimatorSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/weaponAnimatorSystem.cs:6`

**概要**: 武器の一人称アニメーターの状態を管理し、待機・歩き・走り・射撃・リロード・エイム・抜刀・納刀・近接の各アニメを`CrossFadeInFixedTime`で切り替えるコンポーネント。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Animator Enabled | `weaponAnimatorEnabled` | `bool` | true | – |
| Idle Animator Name | `idleAnimatorName` | `string` | "Idle" | – |
| Walk Animator Name | `walkAnimatorName` | `string` | "Walk" | – |
| Run Animator Name | `runAnimatorName` | `string` | "Run" | – |
| Shoot Animator Name | `shootAnimatorName` | `string` | "Shoot" | – |
| Shoot Aim Animator Name | `shootAimAnimatorName` | `string` | "Aim Shoot" | – |
| Reload With Ammo Animator Name | `reloadWithAmmoAnimatorName` | `string` | "Reload With Ammo" | – |
| Reload Without Ammo Animator Name | `reloadWithoutAmmoAnimatorName` | `string` | "Reload Without Ammo" | – |
| Reload Projectile Close Animator Name | `reloadProjectileCloseAnimatorName` | `string` | "Reload Close" | – |
| Draw Animatorname | `drawAnimatorname` | `string` | "Draw" | – |
| Holster Animator Name | `holsterAnimatorName` | `string` | "Holster" | – |
| Aim In Animator Name | `aimInAnimatorName` | `string` | "Aim In" | – |
| Aim Out Animator Name | `aimOutAnimatorName` | `string` | "Aim Out" | – |
| Melee Attack Animator Name | `meleeAttackAnimatorName` | `string` | "Melee Attack" | – |
| No Ammo Animator Name | `noAmmoAnimatorName` | `string` | "No Ammo" | – |
| Shoot Last Projectile Animator Name | `shootLastProjectileAnimatorName` | `string` | "Shoot Last Projectile" | – |

### Animation Duration Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shoot Duration | `shootDuration` | `float` | 0.1f | – |
| Reload With Ammo Duration | `reloadWithAmmoDuration` | `float` | 4.5f | – |
| Reload Without Ammo Duration | `reloadWithoutAmmoDuration` | `float` | 4.5f | – |
| Draw Duration | `drawDuration` | `float` | 0.8f | – |
| Holster Duration | `holsterDuration` | `float` | 0.8f | – |

### Melee Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Melee Attack Animation | `useMeleeAttackAnimation` | `bool` | – | – |
| Melee Attack Animation Duration | `meleeAttackAnimationDuration` | `float` | 1 | – |
| Melee Attack Start Duration | `meleeAttackStartDuration` | `float` | 0.4f | – |
| Melee Attack Middle Duration | `meleeAttackMiddleDuration` | `float` | 0.3f | – |
| Melee Attack End Duration | `meleeAttackEndDuration` | `float` | 0.3f | – |
| Use Multiple Melee Attacks | `useMultipleMeleeAttacks` | `bool` | – | – |
| Melee Attack Animator Name List | `meleeAttackAnimatorNameList` | `List<weaponMeleeAttackInfo>` | new List<weaponMeleeAttackInfo> () | – |

### Reload Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Reload Position | `useReloadPosition` | `bool` | – | – |
| Reload Position | `reloadPosition` | `Transform` | – | – |
| Reload Projectiles One By One | `reloadProjectilesOneByOne` | `bool` | – | – |
| Reload Projectile Open Duration | `reloadProjectileOpenDuration` | `float` | 0.5f | – |
| Reload Projectile Close Duration | `reloadProjectileCloseDuration` | `float` | 0.5f | – |
| Use Reload Projectile Close | `useReloadProjectileClose` | `bool` | – | – |
| Pause Regular Reload Sound | `pauseRegularReloadSound` | `bool` | – | – |

### Others Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Idle Animation | `useIdleAnimation` | `bool` | true | – |
| Use Walk Animation | `useWalkAnimation` | `bool` | true | – |
| Use Run Animation | `useRunAnimation` | `bool` | true | – |
| Use Aim In Animation | `useAimInAnimation` | `bool` | true | – |
| Use Aim Out Animation | `useAimOutAnimation` | `bool` | true | – |
| Use Aim Extra Movement | `useAimExtraMovement` | `bool` | true | – |
| Use Walk Run Extra Movement | `useWalkRunExtraMovement` | `bool` | – | – |
| Use Animation For Recoil Without Aim | `useAnimationForRecoilWithoutAim` | `bool` | – | – |
| Use Animation For Recoil With Aim | `useAnimationForRecoilWithAim` | `bool` | – | – |
| Check If No Ammo Remain | `checkIfNoAmmoRemain` | `bool` | – | – |

### Weapon Parts Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Weapon Mesh Parent | `mainWeaponMeshParent` | `Transform` | – | – |
| Weapon Mesh Offset Animator First Person | `weaponMeshOffsetAnimatorFirstPerson` | `Vector3` | – | – |
| Weapon Mesh Part Info List | `weaponMeshPartInfoList` | `List<weaponMeshPartInfo>` | new List<weaponMeshPartInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Idle Currently Active | `idleCurrentlyActive` | `bool` | – | – |
| Walk Currently Active | `walkCurrentlyActive` | `bool` | – | – |
| Run Currently Active | `runCurrentlyActive` | `bool` | – | – |
| Idle Active | `idleActive` | `bool` | – | – |
| Walk Active | `walkActive` | `bool` | – | – |
| Run Active | `runActive` | `bool` | – | – |
| Shoot Active | `shootActive` | `bool` | – | – |
| Reload Active | `reloadActive` | `bool` | – | – |
| Draw Active | `drawActive` | `bool` | – | – |
| Holster Active | `holsterActive` | `bool` | – | – |
| Aim Active | `aimActive` | `bool` | – | – |
| Aim In Active | `aimInActive` | `bool` | – | – |
| Aim Out Active | `aimOutActive` | `bool` | – | – |
| Reload Without Ammo Active | `reloadWithoutAmmoActive` | `bool` | – | – |
| Aiming Previously | `aimingPreviously` | `bool` | – | – |
| Weapon In First Person State Active | `weaponInFirstPersonStateActive` | `bool` | – | – |
| Melee Attack Active | `meleeAttackActive` | `bool` | – | – |
| Melee Attack Currently Active | `meleeAttackCurrentlyActive` | `bool` | – | – |
| No Ammo Active | `noAmmoActive` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Reload Projectile Open | `eventOnReloadProjectileOpen` | `UnityEvent` | – | – |
| Event On Reload Projectile One Byone | `eventOnReloadProjectileOneByone` | `UnityEvent` | – | – |
| Event On Reload Projectile Close | `eventOnReloadProjectileClose` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main IK Weapon System | `mainIKWeaponSystem` | `IKWeaponSystem` | – | – |
| Weapon Animator | `weaponAnimator` | `Animator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setIdleState(bool state)` | 無効時や射撃・リロード・近接中は何もせず、待機状態を設定して他状態を解除しアニメを更新する。 |
| `setWalkState(bool state)` | 歩き状態を設定して他状態を解除し、`updateAnimatorValues`で歩きアニメへ切り替える。 |
| `setRunState(bool state)` | 走り状態を設定して他状態を解除し、`updateAnimatorValues`で走りアニメへ切り替える。 |
| `setShootState(bool state)` | 射撃状態にして他状態を解除し、残弾が尽きる場合はNoAmmoを立てて射撃コルーチンを開始する。 |
| `setReloadState(bool state)` | リロード状態にして他状態とエイムを解除し、マガジンが空かで分岐してリロードコルーチンを開始する。 |
| `setAimState(bool state)` | エイム状態とイン・アウトのフラグを設定し、他状態を解除してアニメを更新する。 |
| `setDrawState(bool state)` | 抜刀状態を設定し、有効時は一人称状態を有効にしてアニメを更新する。 |
| `setHolsterState(bool state)` | 納刀状態を設定してアニメを更新するだけ。 |
| `setMeleeAttackState(bool state)` | リロード中や同一状態ならfalseを返し、近接状態にして他状態を解除しコルーチンを開始してtrueを返す。 |
| `stopAnimatorCoroutine()` | 実行中の`animatorCoroutine`を停止するだけ。 |
| `updateAnimatorValues()` | 有効な状態フラグに応じて各アニメーションへクロスフェードし、処理したフラグをfalseへ戻す。 |
| `setWeaponInFirstPersonStateActiveState(bool state)` | 一人称状態を設定し、アニメーターの有効化と再バインド、メッシュ位置オフセットの適用や復元を行う。 |
| `resetActiveStates()` | 待機・歩き・射撃・リロード・エイム・近接など全状態フラグをfalseに戻すだけ。 |
| `getDrawDuration()` | 抜刀アニメの再生時間を返すだけ。 |
| `getHolsterDuration()` | 納刀アニメの再生時間を返すだけ。 |
| `setMeleeAttackInfo()` | 複数近接攻撃が有効ならリストからランダムに1つ選んで設定し、無効ならnullにする。 |
| `getMeleeAttackStartDuration()` | 複数近接時は選択中の情報から、そうでなければ既定値から開始時間を返す。 |
| `getMeleeAttackMiddleDuration()` | 同様に近接攻撃の中間時間を返すだけ。 |
| `getMeleeAttackEndDuration()` | 同様に近接攻撃の終了時間を返すだけ。 |
| `enableOrDisableWeaponAnimator(bool state)` | IK武器へアニメーター使用状態を伝えて参照を登録し、アニメーターを取得してコンポーネントを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnReloadProjectileOpen` | `UnityEvent` | – |
| `eventOnReloadProjectileOneByone` | `UnityEvent` | – |
| `eventOnReloadProjectileClose` | `UnityEvent` | – |

## 内部型

- `weaponMeshPartInfo`（class）
- `weaponMeleeAttackInfo`（class）
