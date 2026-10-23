# vehicleWeaponSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/vehicleWeaponSystem.cs:7`

**概要**: 車両に搭載する武器システム。武器リストの選択・弾倉と残弾の管理・リロード・発射体生成・レーザーや照準カーソル、HUDへの弾薬表示とカメラ揺れを一括して制御する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Basic Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapons Enabled | `weaponsEnabled` | `bool` | true | 武器システム全体の有効状態。OFFで射撃と照準を停止。 |
| Vehicle | `vehicle` | `GameObject` | – | 射撃の所有者として扱う車両。自車は照準対象から除外。 |
| Weapon Look Direction | `weaponLookDirection` | `Transform` | – | 照準方向を向く武器の基準Transform。旋回角の制限判定に使用。 |
| Weapons Slots Amount | `weaponsSlotsAmount` | `int` | – | 番号キーで選択できる武器スロット数。これを超える入力は無効。 |
| Weapon Index To Start | `weaponIndexToStart` | `int` | – | 開始時に選択する武器の`weapons`リスト内インデックス。 |
| Projectiles Pool Enabled | `projectilesPoolEnabled` | `bool` | true | 発射物をプールで再利用するか。OFFでは毎回生成して破棄。 |
| Max Amount Of Pool Elements On Weapon | `maxAmountOfPoolElementsOnWeapon` | `int` | 30 | 1つの武器でプールに確保しておく発射物の最大数。 |
| Ignore Disable Vehicle Weapons If Destroyed | `ignoreDisableVehicleWeaponsIfDestroyed` | `bool` | – | 車両が破壊された後も武器を使い続けられるようにするか。 |
| Weapons Effects Source | `weaponsEffectsSource` | `AudioSource` | – | 射撃・リロード・弾切れの効果音を再生するAudioSource。 |
| Out Of Ammo | `outOfAmmo` | `AudioClip` | – | 弾切れの時に鳴らすAudioClip。 |
| Out Of Ammo Audio Element | `outOfAmmoAudioElement` | `AudioElement` | – | 弾切れ音の再生設定をまとめたAudioElement。 |

### Target Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | 照準のレイキャストとダメージ対象の検出に使うマスク。 |
| Target For Scorch Layer | `targetForScorchLayer` | `LayerMask` | – | 焦げ跡デカールを付ける対象を決めるマスク。 |
| Use Custom Ignore Tags | `useCustomIgnoreTags` | `bool` | – | 指定したタグのオブジェクトへの着弾を無視するか。 |

### Base Rotation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Has Base Rotation | `hasBaseRotation` | `bool` | true | 旋回土台をカメラに合わせて回すか。OFFではカーソル照準を使う。 |
| Minimum X | `minimumX` | `float` | 25 | X軸の旋回を許可する角度範囲の0度側の境界。 / 表示条件: `hasBaseRotation` がオンのとき |
| Maximum X | `maximumX` | `float` | 315 | X軸の旋回を許可する角度範囲の360度側の境界。 / 表示条件: `hasBaseRotation` がオンのとき |
| Minimum Y | `minimumY` | `float` | 360 | Y軸の旋回を許可する角度範囲の0度側の境界。 / 表示条件: `hasBaseRotation` がオンのとき |
| Maximum Y | `maximumY` | `float` | 360 | Y軸の旋回を許可する角度範囲の360度側の境界。 / 表示条件: `hasBaseRotation` がオンのとき |
| Main Vehicle Weapons Game Object | `mainVehicleWeaponsGameObject` | `GameObject` | – | 武器一式をまとめた親オブジェクト。無効化時に表示も切り替える。 / 表示条件: `hasBaseRotation` がオンのとき |
| Base X | `baseX` | `GameObject` | – | 旋回土台のうちX軸回転を担当するGameObject。 / 表示条件: `hasBaseRotation` がオンのとき |
| Base Y | `baseY` | `GameObject` | – | 旋回土台のうちY軸回転を担当するGameObject。 / 表示条件: `hasBaseRotation` がオンのとき |
| Base X Rotation Speed | `baseXRotationSpeed` | `float` | 10 | X軸側の土台が目標角度へ追従する速さ。 / 表示条件: `hasBaseRotation` がオンのとき |
| Base Y Rotation Speed | `baseYRotationSpeed` | `float` | 10 | Y軸側の土台が目標角度へ追従する速さ。 / 表示条件: `hasBaseRotation` がオンのとき |
| No Input Weapon Direction | `noInputWeaponDirection` | `Transform` | – | カメラ入力がない時に武器の向きの基準となるTransform。 / 表示条件: `hasBaseRotation` がオンのとき |
| Can Rotate Weapons With No Camera Input | `canRotateWeaponsWithNoCameraInput` | `bool` | – | カメラを動かさずにマウスで武器を旋回できるようにするか。 / 表示条件: `hasBaseRotation` がオンのとき |
| No Camera Input Weapon Rotation Speed | `noCameraInputWeaponRotationSpeed` | `float` | – | カメラ入力なしで旋回する時の補間の速さ。 / 表示条件: `hasBaseRotation.boolValue && canRotateWeaponsWithNoCameraInput.boolValue` |
| Weapon Cursor Movement Speed | `weaponCursorMovementSpeed` | `float` | – | マウス入力で照準カーソルを動かす速さ。 / 表示条件: `hasBaseRotation.boolValue && canRotateWeaponsWithNoCameraInput.boolValue` |
| Weapon Cursor Raycast Layer | `weaponCursorRaycastLayer` | `LayerMask` | – | 照準カーソルから撃つ対象を探すレイキャストのマスク。 / 表示条件: `hasBaseRotation.boolValue && canRotateWeaponsWithNoCameraInput.boolValue` |
| Use Weapon Cursor Screen Limit | `useWeaponCursorScreenLimit` | `bool` | – | カーソルの移動を画面端の範囲内に制限するか。 / 表示条件: `hasBaseRotation.boolValue && canRotateWeaponsWithNoCameraInput.boolValue` |
| Weapon Cursor Horizontal Limit | `weaponCursorHorizontalLimit` | `float` | – | カーソルの移動を左右に制限する幅。 / 表示条件: `canRotateWeaponsWithNoCameraInput.boolValue && useWeaponCursorScreenLimit.boolValue` |
| Weapon Cursor Vertical Limit | `weaponCursorVerticalLimit` | `float` | – | カーソルの移動を上下に制限する幅。 / 表示条件: `canRotateWeaponsWithNoCameraInput.boolValue && useWeaponCursorScreenLimit.boolValue` |
| Circle Camera Limit2 5d | `circleCameraLimit2_5d` | `float` | 7 | 2.5D時のカーソル可動域。値を大きくするほど狭くなる。 / 表示条件: `hasBaseRotation` がオンのとき |

### Vehicle Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Camera Manager | `vehicleCameraManager` | `vehicleCameraController` | – | 車両カメラの制御。カメラ位置と2.5D判定を取得する。 |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | 射撃時の反動を加える車両のRigidbody。 |
| Action Manager | `actionManager` | `inputActionManager` | – | マウス軸やポーズ、タッチ状態を取得する入力管理。 |
| Hud Manager | `hudManager` | `vehicleHUDManager` | – | 弾数や武器名を表示し、搭乗状態も扱う車両HUD。 |
| Parable | `parable` | `launchTrayectory` | – | 照準中に弾道の放物線を描くlaunchTrayectory。 |
| Gravity Control Manager | `gravityControlManager` | `vehicleGravityControl` | – | 独自重力下で照準の上方向を決める重力制御。 |
| Vehicle Camera Manager Transform | `vehicleCameraManagerTransform` | `Transform` | – | 弾道計算に使うカメラのTransform。未設定なら自動取得。 |

### Touch Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Swipe Dist | `minSwipeDist` | `float` | 20 | タッチで武器を切り替えるスワイプの最小移動距離。 |

### Weapons List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Decal Manager Name | `mainDecalManagerName` | `string` | "Decal Manager" | 着弾デカール一覧を取得するDecal Managerの名前。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `weaponsActivate` | `bool` | – | – |
| `customTagsToIgnoreList` | `List<string>` | new List<string> () | – |
| `reloading` | `bool` | – | – |
| `aimingCorrectly` | `bool` | – | – |
| `weapons` | `List<vehicleWeapons>` | new List<vehicleWeapons> () | – |
| `currentLockedCameraCursorSize` | `Vector2` | – | – |
| `impactDecalList` | `string []` | – | – |
| `choosedWeapon` | `int` | – | – |
| `currentWeaponName` | `string` | – | – |
| `aimingHomingProjectile` | `bool` | – | – |
| `shootingPreviously` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkIfEnableWeaponCursor()` | 非射撃時カーソル非表示の設定なら武器カーソルを再表示し、`lastTimeFired` を更新する。 |
| `checkIfDisableWeaponCursor()` | 非射撃時に遅延時間を過ぎた武器カーソルを非表示にし、`hasBaseRotation` の場合は表示へ戻す。 |
| `launchCurrentProjectile(Vector3 cameraDirection)` | `currentProjectile` を非キネマティックにし、放物線速度か前方への力を加えて発射する。 |
| `shootWeapon(bool shootAtKeyDown)` | 射撃入力を処理し、発射体の生成・弾薬消費・発射音・薬莢・反動・ホーミング照準の開始と解除を行う。 |
| `setVehicleWeaponCameraDirection()` | カメラ前方、または銃口からカメラへの向きで `projectileDirectionToLook` を更新する。 |
| `autoReload()` | レーザーを停止し、リロード中でなければ `waitToReload` コルーチンを開始する。 |
| `changeWeaponLaserState(bool state)` | 現在武器の `vehicleLaser` を探して発光状態を切り替え、`usingLaser` を更新する。 |
| `createShells()` | `ejectShellOnShot` 時に発射位置へ薬莢を生成し、保持が15個を超えると最古の薬莢を破棄する。 |
| `testWeaponShake(int weaponIndex)` | 指定インデックス武器の揺れ設定に従い、一人称/三人称別の値をカメラの外部シェイクとして適用する。 |
| `checkShotShake()` | 現在武器の `shootShakeInfo` に応じ、一人称/三人称それぞれの揺れ値をカメラに適用する。 |
| `getAmmo(string ammoName, int amount)` | 同名武器の残弾を増やし、空だった場合は自動リロードし、HUDと補助残弾を更新する。 |
| `addAuxRemainAmmo(vehicleWeapons weaponToCheck, int amount)` | `auxRemainAmmo` に指定量を加算するだけ。 |
| `chooseNextWeapon()` | 武器有効時、`numberKey` を次へ進めて有効な武器を探し、`weaponChanged` で切り替える。 |
| `choosePreviousWeapon()` | `numberKey` を前へ戻して有効な武器を探し、`weaponChanged` で切り替える。 |
| `checkCurrentWeaponCustomReticle()` | カスタムレティクル設定なら画像・色・サイズを適用し、未設定なら既定のカーソル値へ戻す。 |
| `checkParableTrayectory(bool parableState)` | 放物線表示の位置とカメラを設定し、`changeParableState` で線の表示を切り替える。 |
| `isWeaponsEnabled()` | `weaponsEnabled` の値を返すだけ。 |
| `setVehicleHUDInfoManager(playerHUDManager newPlayerHUDManager)` | `vehicleHUDInfoManager` を差し替えるだけ。 |
| `setCurrentDriver(GameObject newDriver)` | `currentDriver` を設定するだけ。 |
| `setGKCSimpleRiderSystem(GKCSimpleRiderSystem newGKCSimpleRiderSystem)` | `mainGKCSimpleRiderSystem` を設定し、参照の有無フラグを更新する。 |
| `checkIfDetectSurfaceBelongToVehicle(Collider colliderToCheck)` | HUDかライダーシステムに問い合わせ、指定コライダーが自車の部位かを返す。 |
| `changeWeaponState(bool state)` | 乗降に合わせ武器を有効化/無効化し、HUD・カメラ・カーソル・レーザー・照準の状態を更新する。 |
| `getCameraInfo(Transform camera, bool useRotationInput)` | カメラTransformと回転入力の使用可否を保持し、武器カーソル要素を取得する。 |
| `getWeaponCursorElements()` | HUDの車両カーソルからRectTransform等を取得し、位置を戻して画面端の制限値を計算する。 |
| `setSeekerProjectileInfo(Vector3 shootPosition)` | `applyDamage` に索敵条件を渡し、見つかった最も近い目標を返す。 |
| `setProjectileSpread()` | `spreadAmount` の範囲でXYZ各軸のランダムな拡散ベクトルを返す。 |
| `checkAutoShootOnTag()` | カメラからのレイでタグ/レイヤー一致の目標を検出し、自動射撃の開始または解除を行う。 |
| `checkIfWeaponIsAvailable(string weaponName)` | 有効かつ同名の武器がリストに存在するかを返す。 |
| `canIncreaseRemainAmmo(vehicleWeapons weaponToCheck)` | `auxRemainAmmo` が `ammoLimit` 未満かどうかを判定して返す。 |
| `hasMaximumAmmoAmount(vehicleWeapons weaponToCheck)` | `useAmmoLimit` 有効時、残弾が上限以上かをログ出力しつつ判定する。 |
| `hasAmmoLimit(string weaponName)` | 有効かつ同名で `useAmmoLimit` が有効な武器があるかを返す。 |
| `ammoAmountToMaximumLimit(vehicleWeapons weaponToCheck)` | `ammoLimit` から `auxRemainAmmo` を引いた残りの加算可能量を返す。 |
| `hasMaximumAmmoAmount(string weaponName)` | 同名の有効武器がいずれも残弾上限に達しているかを返す。 |
| `getCurrentWeaponName()` | 武器選択済みなら `currentWeaponName` を、未選択なら空文字を返す。 |
| `getCurrentWeaponClipSize()` | 武器選択済みなら現在の `clipSize` を、未選択なら0を返す。 |
| `getCurrentWeaponRemainAmmo()` | 武器選択済みなら現在の `remainAmmo` を、未選択なら0を返す。 |
| `enableMuzzleFlashLight()` | `useMuzzleFlash` 時に既存コルーチンを停止し、銃口ライトの点灯/消灯コルーチンを開始する。 |
| `setWeaponsPausedState(bool state)` | `weaponsPaused` を設定するだけ。 |
| `setWeaponsEnabedStateAndWeaponMeshes(bool state)` | 武器の有効状態を設定し、武器ルートGameObjectの表示も同じ状態に切り替える。 |
| `setWeaponsEnabledState(bool state)` | `weaponsEnabled` を設定し、有効化した場合はコンポーネントを初期化する。 |
| `setMainVehicleWeaponsGameObjectParent(Transform newParent)` | 武器ルートGameObjectの親を指定Transformへ付け替える。 |
| `inputShootWeapon()` | 武器有効かつ乗車中で、自動武器なら `shootWeapon(true)` を呼ぶ。 |
| `inputHoldOrReleaseShootWeapon(bool holdingButton)` | 押下で射撃、離すと射撃解除と `lastShoot` リセットを行い、使用中のレーザーを停止する。 |
| `inputNextOrPreviousWeapon(bool setNextWeapon)` | 武器有効かつ乗車中に、次または前の武器へ切り替える。 |
| `setVehicleWeaponsComponents()` | 各武器の弾倉数を初期値として保存し、Animation取得と空弾倉設定を行ってコンポーネントを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` でこのコンポーネントの更新を通知する。 |
| `getImpactListInfo()` | シーンから `decalManager` を取得し、インパクト用デカール名の一覧を配列に取り込んで更新する。 |

## 内部型

- `vehicleWeapons`（class）
