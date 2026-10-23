# IKWeaponSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `weaponObjectInfo`
- **ソース**: `Weapons/IKWeaponSystem.cs:6`

**概要**: 武器1丁ごとの設定コンポーネントで、一人称/三人称の武器メッシュ位置、手と肘のIK目標、スウェイ、射撃時のカメラ揺れ、アタッチメント、デュアルウェルト、耐久値、インベントリ用プレハブ生成を保持する。実際の処理は`playerWeaponSystem`(`weaponSystemManager`)や`playerWeaponsManager`へ委譲する部分が多い。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Game Object | `weaponGameObject` | `GameObject` | – | 武器オブジェクトのルート。各コンポーネントの取得元になる。 / 表示条件: `showSettings` がオンのとき |
| Extra Rotation | `extraRotation` | `float` | – | エイム時に上半身と武器へ加える追加の回転角。 / 表示条件: `showSettings` がオンのとき |
| Aim Fov Value | `aimFovValue` | `float` | – | エイム中に設定するカメラのFOV値。 / 表示条件: `showSettings` がオンのとき |
| Aim Fov Speed | `aimFovSpeed` | `float` | – | エイム時にFOVを変更する速さ。 / 表示条件: `showSettings` がオンのとき |
| Weapon Enabled | `weaponEnabled` | `bool` | – | 武器が有効かどうか。OFFなら武器メッシュを非表示にする。 / 表示条件: `showSettings` がオンのとき |
| Hide Weapon If Kept In Third Person | `hideWeaponIfKeptInThirdPerson` | `bool` | – | 三人称で武器をしまっている間、メッシュを隠すかどうか。 / 表示条件: `showSettings` がオンのとき |
| Can Be Dropped | `canBeDropped` | `bool` | true | この武器を地面に落とせるかどうか。 / 表示条件: `showSettings` がオンのとき |

### New Animator Weapon ID Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Animator Weapon ID | `setNewAnimatorWeaponID` | `bool` | – | 装備時に専用のアニメーター武器IDへ切り替えるかどうか。 / 表示条件: `showSettings` がオンのとき |
| New Animator Weapon ID | `newAnimatorWeaponID` | `int` | – | 装備時に設定するアニメーターの武器ID。 / 表示条件: `showSettings.boolValue && setNewAnimatorWeaponID.boolValue` |
| Set New Animator Dual Weapon ID | `setNewAnimatorDualWeaponID` | `bool` | true | 二丁持ち時に専用のアニメーターIDへ切り替えるかどうか。 / 表示条件: `showSettings` がオンのとき |
| New Animator Dual Weapon ID | `newAnimatorDualWeaponID` | `int` | 0 | 二丁持ち時に設定するアニメーターの武器ID。 / 表示条件: `showSettings.boolValue && setNewAnimatorDualWeaponID.boolValue` |
| Set Upper Body Bending Multiplier | `setUpperBodyBendingMultiplier` | `bool` | – | 上半身の曲げ倍率をこの武器専用の値にするかどうか。 / 表示条件: `showSettings` がオンのとき |
| Horizontal Bending Multiplier | `horizontalBendingMultiplier` | `float` | 1 | 上半身を横方向へ曲げる倍率。 / 表示条件: `showSettings.boolValue && setUpperBodyBendingMultiplier.boolValue` |
| Vertical Bending Multiplier | `verticalBendingMultiplier` | `float` | 1 | 上半身を縦方向へ曲げる倍率。 / 表示条件: `showSettings.boolValue && setUpperBodyBendingMultiplier.boolValue` |
| Follow Full Rotation Point Direction | `followFullRotationPointDirection` | `bool` | – | 上半身を武器の回転点の向きへ追従させるかどうか。 / 表示条件: `showSettings.boolValue && setUpperBodyBendingMultiplier.boolValue` |
| Follow Full Rotation Clamp X | `followFullRotationClampX` | `Vector2` | new Vector2 (80, 80) | X軸で追従できる角度の上限と下限。 / 表示条件: `setUpperBodyBendingMultiplier.boolValue && followFullRotationPointDirection.boolValue` |
| Follow Full Rotation Clamp Y | `followFullRotationClampY` | `Vector2` | new Vector2 (40, 1) | Y軸で追従できる角度の上限と下限。 / 表示条件: `setUpperBodyBendingMultiplier.boolValue && followFullRotationPointDirection.boolValue` |
| Follow Full Rotation Clamp Z | `followFullRotationClampZ` | `Vector2` | new Vector2 (80, 80) | Z軸で追従できる角度の上限と下限。 / 表示条件: `setUpperBodyBendingMultiplier.boolValue && followFullRotationPointDirection.boolValue` |
| Set New Animator Crouch ID | `setNewAnimatorCrouchID` | `bool` | – | しゃがみ時に専用のアニメーターIDへ切り替えるかどうか。 / 表示条件: `showSettings` がオンのとき |
| New Animator Crouch ID | `newAnimatorCrouchID` | `int` | – | しゃがみ時に設定するアニメーターID。 / 表示条件: `showSettings.boolValue && setNewAnimatorCrouchID.boolValue` |
| Ignore Crouch While Weapon Active | `ignoreCrouchWhileWeaponActive` | `bool` | true | 武器を構えている間、しゃがみ状態を無視するかどうか。 / 表示条件: `showSettings` がオンのとき |
| Pivot Point Rotation Active | `pivotPointRotationActive` | `bool` | true | 武器の回転支点（ピボット）を有効にするかどうか。 / 表示条件: `showSettings` がオンのとき |
| Use New Max Angle Difference | `useNewMaxAngleDifference` | `bool` | – | 上半身の最大回転角度をこの武器専用の値にするかどうか。 / 表示条件: `showSettings` がオンのとき |
| Horizontal Max Angle Difference | `horizontalMaxAngleDifference` | `float` | 90 | 上半身の横方向の最大回転角度。 / 表示条件: `showSettings.boolValue && useNewMaxAngleDifference.boolValue` |
| Vertical Max Angle Difference | `verticalMaxAngleDifference` | `float` | 90 | 上半身の縦方向の最大回転角度。 / 表示条件: `showSettings.boolValue && useNewMaxAngleDifference.boolValue` |

### Unlock Cursor Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Unlock Cursor On First Person | `canUnlockCursor` | `bool` | – | 一人称でカーソルをロック解除できるようにするかどうか。 / 表示条件: `showSettings` がオンのとき |
| Can Unlock Cursor On Third Person | `canUnlockCursorOnThirdPerson` | `bool` | – | 三人称でもカーソルをロック解除できるようにするかどうか。 / 表示条件: `showSettings` がオンのとき |
| Disable HUD When Cursor Unlocked | `disableHUDWhenCursorUnlocked` | `bool` | – | カーソル解放中にHUDを非表示にするかどうか。 / 表示条件: `showSettings` がオンのとき |

### Weapon Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon System Manager | `weaponSystemManager` | `playerWeaponSystem` | – | 武器本体の`playerWeaponSystem`への参照。 / 表示条件: `showSettings` がオンのとき |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | プレイヤーの`playerWeaponsManager`への参照。 / 表示条件: `showSettings` がオンのとき |
| Weapon Transform | `weaponTransform` | `Transform` | – | 武器メッシュのTransform。位置合わせの基準に使う。 / 表示条件: `showSettings` がオンのとき |
| Right Hand Mount Point | `rightHandMountPoint` | `Transform` | – | 右手に武器を親子付けるためのポイント。 / 表示条件: `showSettings` がオンのとき |
| Left Hand Mount Point | `leftHandMountPoint` | `Transform` | – | 左手に武器を親子付けるためのポイント。 / 表示条件: `showSettings` がオンのとき |

### First Person Animator Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Weapon Animator First Person | `useWeaponAnimatorFirstPerson` | `bool` | – | 一人称の腕をアニメーターで動かすかどうか。 / 表示条件: `showSettings` がオンのとき |
| Main Weapon Animator System | `mainWeaponAnimatorSystem` | `weaponAnimatorSystem` | – | 一人称武器アニメーターの参照。 / 表示条件: `showSettings.boolValue && useWeaponAnimatorFirstPerson.boolValue` |

### Weapon Surface Collision Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | 表面衝突や近接攻撃の判定に使うレイヤーマスク。 / 表示条件: `showSettings` がオンのとき |
| Extra Collider Center On Fire Weapon On FBA | `extraColliderCenterOnFireWeaponOnFBA` | `Vector3` | – | FBAで発砲時に追加するコライダーの中心位置。 / 表示条件: `showSettings` がオンのとき |
| Extra Collider Scale On Fire Weapon On FBA | `extraColliderScaleOnFireWeaponOnFBA` | `Vector3` | – | FBAで発砲時に追加するコライダーのサイズ。 / 表示条件: `showSettings` がオンのとき |

### Weapon Attachment Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Weapon Attachment System | `mainWeaponAttachmentSystem` | `weaponAttachmentSystem` | – | 武器アタッチメントを管理するコンポーネントへの参照。 / 表示条件: `showSettings` がオンのとき |
| Ignore Use Attachment System | `ignoreUseAttachmentSystem` | `bool` | – | アタッチメント設定があっても使用しないようにするかどうか。 / 表示条件: `showSettings` がオンのとき |

### First Person Weapon Idle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Weapon Idle | `useWeaponIdle` | `bool` | – | 待機中に武器を揺らすアイドルモーションを使うかどうか。 / 表示条件: `showFirstPersonSettings.boolValue && showIdleSettings.boolValue` |
| Time To Active Weapon Idle | `timeToActiveWeaponIdle` | `float` | 3 | 操作が止まってからアイドルが始まるまでの秒数。 / 表示条件: `showIdleSettings.boolValue && useWeaponIdle.boolValue` |
| Idle Position Amount | `idlePositionAmount` | `Vector3` | – | アイドル時に揺らす位置の幅。 / 表示条件: `showIdleSettings.boolValue && useWeaponIdle.boolValue` |
| Idle Rotation Amount | `idleRotationAmount` | `Vector3` | – | アイドル時に揺らす回転の幅。 / 表示条件: `showIdleSettings.boolValue && useWeaponIdle.boolValue` |
| Idle Speed | `idleSpeed` | `Vector3` | – | アイドルモーションの揺れの速さ。 / 表示条件: `showIdleSettings.boolValue && useWeaponIdle.boolValue` |

### Weapon State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Moving | `playerMoving` | `bool` | – | プレイヤーが移動入力中かを示す実行時フラグ。 / 表示条件: `showIdleSettings.boolValue && useWeaponIdle.boolValue` |
| Idle Active | `idleActive` | `bool` | – | アイドルモーションが再生中かを示す実行時フラグ。 / 表示条件: `showIdleSettings.boolValue && useWeaponIdle.boolValue` |

### Full Body Awareness Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show FBA Gizmo | `showFBAGizmo` | `bool` | – | FBA時の武器位置調整用ギズモを表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showFullBodyAwarernessSettings.boolValue` |
| Show FBA Walk Gizmo | `showFBAWalkGizmo` | `bool` | – | FBAの歩行時オフセット位置を表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showFullBodyAwarernessSettings.boolValue` |
| Show FBA Aim Gizmo | `showFBAAimGizmo` | `bool` | – | FBAのエイム時オフセット位置を表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showFullBodyAwarernessSettings.boolValue` |
| Show FBA Crouch Gizmo | `showFBACrouchGizmo` | `bool` | – | FBAのしゃがみ時オフセット位置を表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showFullBodyAwarernessSettings.boolValue` |
| Show FBA Jump Gizmo | `showFBAJumpGizmo` | `bool` | – | FBAのジャンプ時オフセット位置を表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showFullBodyAwarernessSettings.boolValue` |
| Show FBA Run Gizmo | `showFBARunGizmo` | `bool` | – | FBAの走り時オフセット位置を表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showFullBodyAwarernessSettings.boolValue` |
| Show FBA Obstacle Gizmo | `showFBAObstacleGizmo` | `bool` | – | FBAの障害物回避時オフセット位置を表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showFullBodyAwarernessSettings.boolValue` |

### Shot Shake Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Same Value Both Views | `sameValueBothViews` | `bool` | – | 一人称と三人称で同じ射撃シェイク設定を使うかどうか。 / 表示条件: `showElementSettings.boolValue && showShotShakeSettings.boolValue` |
| Use Shot Shake In Third Person | `useShotShakeInThirdPerson` | `bool` | – | 三人称で発砲時にカメラシェイクを行うかどうか。 / 表示条件: `showElementSettings.boolValue && showShotShakeSettings.boolValue` |
| Use Shot Shake In First Person | `useShotShakeInFirstPerson` | `bool` | – | 一人称で発砲時にカメラシェイクを行うかどうか。 / 表示条件: `showElementSettings.boolValue && showShotShakeSettings.boolValue` |

### Shot Camera Noise Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Shot Camera Noise | `useShotCameraNoise` | `bool` | – | 発砲時にカメラへランダムなノイズ揺れを加えるかどうか。 / 表示条件: `showElementSettings.boolValue && showShotCameraNoiseSettings.boolValue` |
| Use Shot Camera Noise Duration | `useShotCameraNoiseDuration` | `bool` | – | カメラノイズを指定時間かけて減衰させるかどうか。 / 表示条件: `showShotCameraNoiseSettings.boolValue && useShotCameraNoise.boolValue` |
| Shot Camera Noise Duration | `shotCameraNoiseDuration` | `float` | – | カメラノイズが収まるまでの秒数。 / 表示条件: `useShotCameraNoise.boolValue && useShotCameraNoiseDuration.boolValue` |

### Gizmo Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Third Person Gizmo | `showThirdPersonGizmo` | `bool` | – | 三人称用の武器位置ギズモを表示するかどうか。 / 表示条件: `showElementSettings` がオンのとき |
| Show First Person Gizmo | `showFirstPersonGizmo` | `bool` | – | 一人称用の武器位置ギズモを表示するかどうか。 / 表示条件: `showElementSettings` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | ギズモのラベルや線に使う色。 / 表示条件: `showElementSettings.boolValue && showThirdPersonGizmo.boolValue \|\| showFirstPersonGizmo.boolValue` |
| Show Position Gizmo | `showPositionGizmo` | `bool` | true | 武器の位置系ギズモをまとめて表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showThirdPersonGizmo.boolValue \|\| showFirstPersonGizmo.boolValue` |
| Show Main Weapon Positions Gizmo | `showMainWeaponPositionsGizmo` | `bool` | – | エイム・ウォーク・キープ位置の球を表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showThirdPersonGizmo.boolValue \|\| showFirstPersonGizmo.boolValue` |
| Show Collision Detection Gizmo | `showCollisionDetectionGizmo` | `bool` | – | 表面衝突判定の位置とレイを表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showThirdPersonGizmo.boolValue \|\| showFirstPersonGizmo.boolValue` |
| Show Edit Attachment Gizmo | `showEditAttachmentGizmo` | `bool` | – | アタッチメント編集位置のギズモを表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showThirdPersonGizmo.boolValue \|\| showFirstPersonGizmo.boolValue` |
| Show Hands Waypoint Gizmo | `showHandsWaypointGizmo` | `bool` | true | 手のIKウェイポイントを表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showThirdPersonGizmo.boolValue \|\| showFirstPersonGizmo.boolValue` |
| Show Weapon Waypoint Gizmo | `showWeaponWaypointGizmo` | `bool` | true | 武器のキープ経路ウェイポイントを表示するかどうか。 / 表示条件: `showElementSettings.boolValue && showThirdPersonGizmo.boolValue \|\| showFirstPersonGizmo.boolValue` |

### Weapon Pickup Prefab (No Inventory) Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Relative Path Weapons Pickups | `relativePathWeaponsPickups` | `string` | "" | 武器ピックアップのプレハブを生成・保存するパス。 / 表示条件: `showPrefabSettings` がオンのとき |
| Emtpy Weapon Prefab | `emtpyWeaponPrefab` | `GameObject` | – | ピックアップ生成の複製元になる空のプレハブ。 / 表示条件: `showPrefabSettings` がオンのとき |
| Weapon Pickup (No Inventory) | `weaponPrefabModel` | `GameObject` | – | 生成された武器ピックアップのプレハブ。 / 表示条件: `showPrefabSettings` がオンのとき |

### Weapon Pickup Prefab (Inventory) Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Pickup (Inventory) | `inventoryWeaponPrefabObject` | `GameObject` | – | インベントリに登録する武器プレハブ。 / 表示条件: `showPrefabSettings` がオンのとき |

### Create Inventory Weapon And Ammo Prefabs Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Relative Path Weapons Mesh | `relativePathWeaponsMesh` | `string` | "" | インベントリ武器メッシュのプレハブ保存先パス。 / 表示条件: `showPrefabSettings` がオンのとき |
| Relative Path Weapons Ammo Mesh | `relativePathWeaponsAmmoMesh` | `string` | "" | インベントリ弾薬メッシュのプレハブ保存先パス。 / 表示条件: `showPrefabSettings` がオンのとき |
| Inventory Weapon Category Name | `inventoryWeaponCategoryName` | `string` | "Weapons" | 武器を登録するインベントリカテゴリ名。 / 表示条件: `showPrefabSettings` がオンのとき |
| Weapon Name | `weaponName` | `string` | "New Weapon Name" | インベントリやピックアップに登録する武器名。 / 表示条件: `showPrefabSettings` がオンのとき |
| Inventory Ammo Category Name | `inventoryAmmoCategoryName` | `string` | "Ammo" | 弾薬を登録するインベントリカテゴリ名。 / 表示条件: `showPrefabSettings` がオンのとき |
| Ammo Amount Per Pickup | `ammoAmountPerPickup` | `int` | 10 | 弾薬ピックアップ1個あたりの弾数。 / 表示条件: `showPrefabSettings` がオンのとき |
| Weapon Ammo Mesh | `weaponAmmoMesh` | `GameObject` | – | 弾薬ピックアップに使うメッシュ。 / 表示条件: `showPrefabSettings` がオンのとき |
| Weapon Ammo Icon Texture | `weaponAmmoIconTexture` | `Texture` | – | 弾薬のインベントリ表示用アイコン。 / 表示条件: `showPrefabSettings` がオンのとき |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Lower Rotation Speed Aimed Third Person | `useLowerRotationSpeedAimedThirdPerson` | `bool` | – | 三人称でエイム中にカメラの回転速度を下げるかどうか。 / 表示条件: `showSingleWeaponSettings && isThirdPerson` |
| Vertical Rotation Speed Aimed In Third Person | `verticalRotationSpeedAimedInThirdPerson` | `float` | 4 | 三人称エイム中の縦方向の回転速度。 / 表示条件: `isThirdPerson && useLowerRotationSpeedAimedThirdPerson.boolValue` |
| Horizontal Rotation Speed Aimed In Third Person | `horizontalRotationSpeedAimedInThirdPerson` | `float` | 4 | 三人称エイム中の横方向の回転速度。 / 表示条件: `isThirdPerson && useLowerRotationSpeedAimedThirdPerson.boolValue` |
| Can Aim In First Person | `canAimInFirstPerson` | `bool` | – | 一人称でもエイムできるようにするかどうか。 / 表示条件: `showSingleWeaponSettings` がオンのとき |
| Use Lower Rotation Speed Aimed | `useLowerRotationSpeedAimed` | `bool` | – | 一人称でエイム中にカメラの回転速度を下げるかどうか。 / 表示条件: `showSingleWeaponSettings` がオンのとき |
| Vertical Rotation Speed Aimed In First Person | `verticalRotationSpeedAimedInFirstPerson` | `float` | 4 | 一人称エイム中の縦方向の回転速度。 / 表示条件: `showSingleWeaponSettings && useLowerRotationSpeedAimed.boolValue` |
| Horizontal Rotation Speed Aimed In First Person | `horizontalRotationSpeedAimedInFirstPerson` | `float` | 4 | 一人称エイム中の横方向の回転速度。 / 表示条件: `showSingleWeaponSettings && useLowerRotationSpeedAimed.boolValue` |

### First Person Arms Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| First Person Arms | `firstPersonArms` | `GameObject` | – | 一人称時に表示する腕のオブジェクト。 / 表示条件: `showSingleWeaponSettings && !isThirdPerson` |
| Disable Only First Person Arms Mesh | `disableOnlyFirstPersonArmsMesh` | `bool` | – | 腕全体ではなくメッシュだけを無効化するかどうか。 / 表示条件: `showSingleWeaponSettings && !isThirdPerson` |
| First Person Arms Mesh | `firstPersonArmsMesh` | `SkinnedMeshRenderer` | – | 無効化の対象となる一人称腕のSkinnedMeshRenderer。 / 表示条件: `showSingleWeaponSettings && !isThirdPerson` |

### Head Look Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Look When Aiming | `headLookWhenAiming` | `bool` | – | エイム中に頭部をターゲット方向へ向けるかどうか。 / 表示条件: `showSingleWeaponSettings && isThirdPerson` |
| Head Look Speed | `headLookSpeed` | `float` | – | 頭部をターゲットへ向ける際の追従速度。 / 表示条件: `isThirdPerson && headLookWhenAiming.boolValue` |
| Head Look Target | `headLookTarget` | `Transform` | – | エイム中に頭部を向ける対象のTransform。 / 表示条件: `isThirdPerson && headLookWhenAiming.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `thirdPersonWeaponInfo` | `IKWeaponInfo` | – | – |
| `firstPersonWeaponInfo` | `IKWeaponInfo` | – | – |
| `firstPersonSwayInfo` | `weaponSwayInfo` | – | – |
| `runFirstPersonSwayInfo` | `weaponSwayInfo` | – | – |
| `thirdPersonSwayInfo` | `weaponSwayInfo` | – | – |
| `runThirdPersonSwayInfo` | `weaponSwayInfo` | – | – |
| `thirdPersonshotShakeInfo` | `weaponShotShakeInfo` | – | – |
| `firstPersonshotShakeInfo` | `weaponShotShakeInfo` | – | – |
| `thirdPersonMeleeAttackShakeInfo` | `weaponShotShakeInfo` | – | – |
| `firstPersonMeleeAttackShakeInfo` | `weaponShotShakeInfo` | – | – |
| `extraFirstPersonArmsMeshes` | `List<SkinnedMeshRenderer>` | new List<SkinnedMeshRenderer> () | – |
| `currentWeapon` | `bool` | – | – |
| `aiming` | `bool` | – | – |
| `carrying` | `bool` | – | – |
| `showIdleSettings` | `bool` | – | – |
| `player` | `GameObject` | – | – |
| `moving` | `bool` | – | – |
| `surfaceDetected` | `bool` | – | – |
| `verticalShotCameraNoiseAmountFirstPerson` | `Vector2` | – | – |
| `horizontalShotCameraNoiseAmountFirstPerson` | `Vector2` | – | – |
| `verticalShotCameraNoiseAmountThirdPerson` | `Vector2` | – | – |
| `horizontalShotCameraNoiseAmountThirdPerson` | `Vector2` | – | – |
| `weaponInRunPosition` | `bool` | – | – |
| `playerRunning` | `bool` | – | – |
| `weaponConfiguredAsDualWeapon` | `bool` | – | – |
| `linkedDualWeaponName` | `string` | – | – |
| `weaponUsesAttachment` | `bool` | – | – |
| `jumpingOnProcess` | `bool` | – | – |
| `usingWeaponRotationPoint` | `bool` | – | – |
| `currentHeadLookTarget` | `Transform` | – | – |
| `usingDualWeapon` | `bool` | – | – |
| `disablingDualWeapon` | `bool` | – | – |
| `usingRightHandDualWeapon` | `bool` | – | – |
| `playerOnJumpStart` | `bool` | – | – |
| `playerOnJumpEnd` | `bool` | – | – |
| `crouchingActive` | `bool` | – | – |
| `reloadingWeapon` | `bool` | – | – |
| `actionActive` | `bool` | – | – |
| `weaponObjectActive` | `bool` | true | – |
| `IKPausedOnHandsActive` | `bool` | – | – |
| `showThirdPersonSettings` | `bool` | – | – |
| `showFirstPersonSettings` | `bool` | – | – |
| `showShotShakeSettings` | `bool` | – | – |
| `showSettings` | `bool` | – | – |
| `showElementSettings` | `bool` | – | – |
| `showSwaySettings` | `bool` | – | – |
| `showWalkSwaySettings` | `bool` | – | – |
| `showRunSwaySettings` | `bool` | – | – |
| `showFullBodyAwarernessSettings` | `bool` | – | – |
| `showPrefabSettings` | `bool` | – | – |
| `showShotCameraNoiseSettings` | `bool` | – | – |
| `useDurability` | `bool` | – | – |
| `durabilityAmount` | `float` | – | – |
| `maxDurabilityAmount` | `float` | – | – |
| `weaponUpdateActive` | `bool` | – | – |
| `fullBodyAwarenessActive` | `bool` | – | – |
| `usingWeaponAsOneHandWield` | `bool` | – | – |
| `parentWeaponOutsidePlayerBodyWhenNotActive` | `bool` | true | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeComponents()` | `weaponTransform` などを取得し、スウェイ情報とオーディオを初期化してから更新を開始する。 |
| `isWeaponUpdateActive()` | `weaponUpdateActive` を返すだけ。 |
| `activateWeaponUpdate()` | 既存の更新を停止してから更新コルーチンを開始し、`weaponUpdateActive` を true にする。 |
| `stopActivateWeaponUpdate()` | 更新コルーチンを停止し `weaponUpdateActive` を false にする。 |
| `setInitialWeaponState()` | 武器が無効か未使用時にメッシュを隠す設定ならメッシュを非表示にし、アタッチメント使用時は初期化を呼ぶ。 |
| `checkIfWeaponUsesAttachment()` | アタッチメント使用フラグと無視フラグから、アタッチメントを使うかを返す。 |
| `setPlayerOnJumpStartState(bool state)` | `playerOnJumpStart` を設定するだけ。 |
| `setPlayerOnJumpEndState(bool state)` | `playerOnJumpEnd` を設定するだけ。 |
| `isWeaponMoving()` | `moving` を返すだけ。 |
| `isDrawingWeaponInProcess()` | `drawingWeaponInProcess` を返すだけ。 |
| `isHolsteringWeaponInProcess()` | `holsteringWeaponInProcess` を返すだけ。 |
| `isAimingWeaponInProcess()` | `aimingWeaponInProcess` を返すだけ。 |
| `weaponCanFire()` | FBA時は一人称、それ以外は三人称照準中の設定を使い、`surfaceDetected` 時に発砲を禁止するか判定して返す。 |
| `weaponCanAim()` | FBA時のみ `surfaceDetected` と一人称の照準禁止設定から、照準できるかを返す。 |
| `isWeaponSurfaceDetected()` | `surfaceDetected` を返すだけ。 |
| `setWeaponSystemManager()` | `weaponGameObject` から武器と武器マネージャの参照を取得し `updateComponent` を呼ぶ。 |
| `checkWeaponBuilder()` | 同じオブジェクトに `weaponBuilder` があれば、`weaponsManager` を渡して確認を実行する。 |
| `getWeaponSystemManager()` | `weaponSystemManager` を返すだけ。 |
| `getPlayerWeaponsManager()` | `weaponsManager` を返すだけ。 |
| `getWeaponSystemKeyNumber()` | `playerWeaponSystem` の武器キー番号を返すだけ。 |
| `isUseRemainAmmoFromInventoryActive()` | 在庫の残弾を使う設定かを `playerWeaponSystem` に問い合わせて返す。 |
| `isWeaponEnabled()` | `weaponEnabled` を返すだけ。 |
| `setWeaponEnabledState(bool state)` | `weaponEnabled` を設定し、有効/無効イベントを `playerWeaponSystem` 経由で通知する。 |
| `getWeaponSystemName()` | `playerWeaponSystem` から武器名を取得して返すだけ。 |
| `renameWeapon(string newWeaponName)` | 新しい武器名を `playerWeaponSystem` に設定するだけ。 |
| `renameWeaponAmmo(string currentAmmoName, string newAmmoName)` | 現在と新しい弾名を `playerWeaponSystem` に渡してリネームするだけ。 |
| `getWeaponSystemAmmoName()` | `playerWeaponSystem` から弾名を取得して返すだけ。 |
| `getWeaponOriginalClipSize()` | `playerWeaponSystem` から元のマガジンサイズを返すだけ。 |
| `setRemainAmmoAmount(int newRemainAmmoAmount)` | 残弾数を `playerWeaponSystem` に設定するだけ。 |
| `setInitialProjectilesInMagazine(int newProjectilesInMagazine)` | マガジン内の初期弾数を `playerWeaponSystem` に設定するだけ。 |
| `getProjectilesInMagazine()` | マガジン内の弾数を `playerWeaponSystem` から返すだけ。 |
| `isCurrentMagazineEmpty()` | 現在のマガジンが空かを `playerWeaponSystem` に問い合わせて返す。 |
| `isRemainAmmoEmpty()` | 残弾が空かを `playerWeaponSystem` に問い合わせて返す。 |
| `checkWeaponSidePosition()` | 二丁持ち設定で描画前に手の側へ置く設定なら、`weaponTransform` を対応するキープ位置へ直接移動する。 |
| `drawOrKeepWeaponThirdPerson(bool state)` | 三人称の `carrying` を切り替え、抜刀/納刀の移動コルーチンを開始し、他武器状態と移動値をリセットする。 |
| `isUseDrawKeepWeaponAnimationActive()` | この武器の設定とマネージャの無視・二丁持ち状態から、抜刀/納刀アニメを使うかを返す。 |
| `isUseDrawKeepWeaponAnimationActiveOnThisWeapon()` | FBA時は全体設定か一人称設定、それ以外は三人称設定のフラグを返す。 |
| `updateFBAValues(bool useRifleValues)` | ライフル/拳銃用のFBA各オフセットと追加コライダー値を一括設定し `updateComponent` を呼ぶ。 |
| `resetFBAValues()` | FBAの各オフセットをゼロに戻し `updateComponent` を呼ぶ。 |
| `setNewFBAAimInfo(string infoName)` | 名前が一致する `FBAAimInfo` を探し、現在の照準情報として有効化する。 |
| `setRegularFBAAimInfo()` | カスタム照準情報を無効に戻すだけ。 |
| `setNewExtraColliderOnFireWeaponOnFBAValues(Vector3 newScaleValues, Vector3 newCenterValues)` | FBA時の追加コライダーのスケールと中心を設定し `updateComponent` を呼ぶ。 |
| `isdrawKeepWeaponAnimationInProcess()` | `drawKeepWeaponAnimationInProcess` を返すだけ。 |
| `setHandDeactivateIKStateToDisable()` | `currentIKWeaponsPosition` の追従先を武器位置に合わせ、手のIK重みと目標値を1にする。 |
| `setHandTargetValue(IKWeaponsPosition handInfo, float newValue)` | 指定した手情報の `targetValue` を設定するだけ。 |
| `setElbowTargetValue(IKWeaponsPosition handInfo, float newValue)` | 指定した手情報の肘の `targetValue` を設定するだけ。 |
| `placeWeaponDirectlyOnDrawHand(bool state)` | 三人称で抜刀/納刀アニメを挟まず、武器を手の位置へ直接移動するコルーチンを開始する。 |
| `aimOrDrawWeaponThirdPerson(bool state)` | 三人称の `aiming` を切り替え、照準/通常位置を目標に移動コルーチンを開始し、カーソルやスウェイも更新する。 |
| `walkOrSurfaceCollision(bool state)` | `surfaceDetected` を設定し、衝突/通常位置を目標に移動コルーチンを開始、カーソルと三人称の追加回転も更新する。 |
| `setWeaponRegularCursorState(bool firstPersonActive)` | 視点ごとの衝突時カーソル非表示設定に応じてカーソルを切り替え、発砲不可カーソルとレティクルを更新する。 |
| `walkOrRunWeaponPosition(bool state)` | `weaponInRunPosition` を切り替え、走り/歩き位置を目標に移動し、カーソル・スウェイ・一人称アニメ状態も更新する。 |
| `checkCursorState(bool firstPersonActive)` | 走り中のカーソル非表示設定に応じてカーソルを切り替え、スウェイ情報を歩き/走り用に切り替える。 |
| `setJumpStatetWeaponPosition(bool isJumpStart, bool isJumpEnd)` | ジャンプ開始/終了位置を目標に設定し、開始は移動、終了はディレイ付きのコルーチンを開始する。 |
| `updateWeaponWalkPositionToFullBodyAwarenessState(bool state)` | 移動・照準・IK停止中は何もせず、FBAの歩き位置とオフセットを目標に移動コルーチンを開始する。 |
| `setCrouchStatetWeaponPosition(bool state)` | `crouchingActive` を設定し、しゃがみ/立ち位置を目標にして移動コルーチンを開始する。 |
| `isWeaponInRunPosition()` | `weaponInRunPosition` を返すだけ。 |
| `useRunPositionOnFirstPerson()` | `useRunPositionFirstPerson` を返すだけ。 |
| `useRunPositionOnThirdPerson()` | `useRunPositionThirdPerson` を返すだけ。 |
| `useRunPositionOnFBA()` | `useRunPositionFBA` を返すだけ。 |
| `isPlayerRunning()` | `playerRunning` を返すだけ。 |
| `setPlayerRunningState(bool state)` | `playerRunning` を設定するだけ。 |
| `isWeaponItJumpStart()` | `weaponInJumpStart` を返すだけ。 |
| `isWeaponItJumpEnd()` | `weaponInJumpEnd` を返すだけ。 |
| `isjumpingOnProcess()` | `jumpingOnProcess` を返すだけ。 |
| `weaponUseJumpPositions()` | 視点ごとのジャンプ位置使用設定かFBA中かで、ジャンプ位置を使うかを返す。 |
| `useNewFovOnRunOnThirdPerson()` | `useNewFovOnRunThirdPerson` を返すだけ。 |
| `useNewFovOnRunOnFirstPerson()` | `useNewFovOnRunFirstPerson` を返すだけ。 |
| `isCursorHidden()` | `cursorHidden` を返すだけ。 |
| `setCursorHiddenState(bool state)` | `cursorHidden` を設定するだけ。 |
| `setCurrentSwayInfo(bool state)` | 現在の視点と走り状態に応じて、通常用/走り用のスウェイ情報を `currentSwayInfo` に割り当てる。 |
| `isUseReticleOnAimingEnabled()` | 照準時レティクルの一人称/三人称設定と現在の視点から、有効かを返す。 |
| `isUseReticleEnabled()` | 通常レティクルの一人称/三人称設定と現在の視点から、有効かを返す。 |
| `walkOrMeleeAttackWeaponPosition()` | 近接攻撃位置を目標に設定して攻撃コルーチンを開始し、カーソルやIK・親を調整する。 |
| `checkWeaponCameraShake()` | カメラシェイクを `playerWeaponSystem` に委譲するだけ。 |
| `setUseShotShakeState(bool state)` | 一人称と三人称の射撃シェイク使用フラグを同じ値に設定するだけ。 |
| `checkMeleeAttackExternally()` | 近接攻撃のシェイクとダメージ判定を順に呼ぶだけ。 |
| `checkMeleeAttackShakeInfo()` | 近接攻撃のシェイクを `playerWeaponSystem` に委譲するだけ。 |
| `checkMeleeAttackDamage()` | 近接用のレイ/カプセル判定を行い、当たった対象へダメージ・力・リモートイベント・音・パーティクルを適用する。 |
| `isMeleeAtacking()` | `meleeAtacking` を返すだけ。 |
| `setHandsIKTargetValue(float leftValue, float rightValue)` | 二丁持ちでは使用中の手、通常は左右それぞれの手情報の `targetValue` を設定する。 |
| `setElbowsIKTargetValue(float leftValue, float rightValue)` | 二丁持ちでは使用中の手、通常は左右それぞれの肘の `targetValue` を設定する。 |
| `setIKWeight(float leftValue, float rightValue)` | 手情報の `HandIKWeight` を左右それぞれの値に設定する。 |
| `resetElbowIKPositions()` | 各手の肘を元の親へ戻し、ローカル位置と回転をリセットする。 |
| `quickDrawWeaponThirdPerson()` | アニメを挟まず三人称の抜刀状態にし、武器を歩き位置へ置いてIKや他武器状態をリセットする。 |
| `checkDeactivateIKIfNotAiming()` | IK停止設定が有効なら手と肘のIK重み/目標値を0にし、武器を手の親へ付け替えて所定位置に置く。 |
| `adjustWeaponPositionToDeactivateIKOnHands()` | IK停止時に描画用の手へ付けた武器の位置/回転を、設定値に合わせて直接適用する。 |
| `quickKeepWeaponThirdPerson()` | 即座に三人称の納刀状態にし、武器をキープ位置へ置いてIK目標値・リロード・他状態をリセットする。 |
| `quickDrawWeaponThirdPersonAction()` | `quickDrawWeaponThirdPerson` を呼ぶだけ。 |
| `quickKeepWeaponThirdPersonAction()` | 三人称の納刀を即時に行い、IK重みを0にしてキープ位置へ置き、リロードや他状態もリセットする。 |
| `isWeaponHandsOnPositionToAim()` | `handsInfo` のうち照準位置に就いている手が2つかを返す。 |
| `isRightWeaponHandOnPositionToAim()` | 右手用の手情報の `handInPositionToAim` を返すだけ。 |
| `isLeftWeaponHandOnPositionToAim()` | 左手用の手情報の `handInPositionToAim` を返すだけ。 |
| `aimOrDrawWeaponFirstPerson(bool state)` | 一人称の `aiming` を切り替え、サイト/照準/歩き位置を目標に移動コルーチンを開始し、スウェイもリセットする。 |
| `drawOrKeepWeaponFirstPerson(bool state)` | 一人称の `carrying` を切り替え、武器メッシュと腕を出し入れするコルーチンを開始し、他武器状態をリセットする。 |
| `setNewSightPosition(Transform newTransform)` | 一人称の `sightPosition` を差し替えるだけ。 |
| `setNewSightRecoilPosition(Transform newTransform)` | 一人称の `sightRecoilPosition` を差し替えるだけ。 |
| `reloadWeaponFirstPerson()` | 一人称のリロード移動設定が無効なら何もせず、照準を解除してリロード移動コルーチンを開始する。 |
| `isReloadingWeapon()` | 自身か `playerWeaponSystem` のリロードアニメ状態から、リロード中かを返す。 |
| `cancelReloadIfActive()` | リロード中ならフラグと移動状態を戻し、`playerWeaponSystem` のリロードとアクション状態を解除する。 |
| `quickKeepWeaponFirstPerson()` | 一人称を即座に納刀し、メッシュと腕を非表示にしてキープ位置へ戻し、アニメ状態も解除する。 |
| `resetWeaponPositionInFirstPerson()` | 一人称のキープ位置（二丁持ちは左右別）へ武器のローカル位置/回転を直接設定する。 |
| `resetWeaponPositionInAnyView()` | 現在の視点と二丁持ちに応じたキープ位置へ、武器のローカル位置/回転を直接設定する。 |
| `setWeaponHasRecoilState(bool state)` | 一人称/三人称の `weaponHasRecoil` を同じ値に設定するだけ。 |
| `startRecoilFromExternalFunction()` | 照準中かつ照準処理中でなければ、現在の視点に応じて `startRecoil` を呼ぶ。 |
| `startRecoil(bool isThirdPersonView)` | リコイル停止設定と対象視点のリコイル設定を確認し、射撃アニメを再生してリコイル移動コルーチンを開始する。 |
| `endRecoil(bool isThirdPersonView)` | 現在の移動を止め、照準位置へ戻るリコイル復帰コルーチンを開始する。 |
| `disableOtherWeaponsStates()` | 衝突・走り・カーソル・近接などの一時状態をまとめて解除し、スウェイ情報を通常に戻す。 |
| `resetOtherWeaponsStates()` | ジャンプ中や走り中の全体状態を `playerWeaponsManager` 経由で解除し、カーソルとレティクルを戻す。 |
| `stopWeaponMovement()` | 武器移動コルーチンを停止し、スウェイリセット中なら止め、リコイル状態を解除する。 |
| `setWeaponSway(float mouseX, float mouseY, float vertical, float horizontal, bool running, bool shooting, bool onGround, bool externalShakingActive, bool usingDevice, bool isThirdPersonView, bool canMove, bool isFullBodyAwarenessActive)` | 入力・走り・接地などからスウェイ/ボブ/アイドルを計算し、武器メッシュのローカル位置/回転へ補間適用する。 |
| `getSwayPosition(Vector3 speed, Vector3 amount, float multiplier)` | `Time.time` のサイン波で、速度・振幅・倍率からスウェイ位置を計算して返す。 |
| `resetSwayValue()` | スウェイリセットを止めてから、武器メッシュを原点姿勢へ戻すコルーチンを開始する。 |
| `stopResetSwayValue()` | スウェイリセットコルーチンを停止し `resetingWeaponSwayValue` を false にする。 |
| `checkIfResetWeaponSway()` | 三人称で照準中なら `resetSwayValue` を呼ぶ。 |
| `checkIfResetWeaponSway(bool ignoreIfAiming)` | 三人称かつ照準中（引数で照準を無視）なら `resetSwayValue` を呼ぶ。 |
| `setWeaponSwayPausedState(bool state)` | `weaponSwayPaused` を設定するだけ。 |
| `resetWeaponMeshPositionRotation()` | `setWeaponMeshPositionRotation(null)`を呼び、武器メッシュを基準位置・回転へ戻す。 |
| `setWeaponMeshPositionRotation(Transform referenceTransform)` | 既存コルーチンを止め、武器メッシュを`referenceTransform`のローカル位置・回転へ補間するコルーチンを開始する。 |
| `stopSetWeaponMeshPositionRotation()` | `swayValueCoroutine`を停止するだけ。 |
| `setLastTimeMoved()` | `lastTimeMoved`に`Time.time`を代入するだけ。 |
| `enableOrDisableFirstPersonArms(bool state)` | 一人称アームを`state`で表示切替し、`disableOnlyFirstPersonArmsMesh`時はメッシュのみ切り替える。 |
| `enableOrDisableFirstPersonArmsDualWeapons(bool state)` | デュアル武器の左右の手メッシュのうち、使用中の手だけを`state`で有効化する。 |
| `setNewFirstPersonArms(GameObject newArms)` | `firstPersonArms`を差し替えて`updateComponent`を呼ぶ。 |
| `enableOrDisableFirstPersonArmsFromEditor(bool state)` | エディタ用に`enableOrDisableFirstPersonArms`を呼ぶだけ。 |
| `destroyFirstPersonArmsFromEditor()` | プレハブを展開し、一人称アームとデュアル用手メッシュを`DestroyImmediate`で削除する。 |
| `enableOrDisableWeaponMesh(bool state)` | `weaponSystemManager`の同名メソッドへ委譲するだけ。 |
| `setWeaponMeshScale(float newValue)` | `weaponSystemManager`へメッシュのスケール変更を委譲するだけ。 |
| `adjustAllFireWeaponTransformReferencePosition(float newValue)` | 三人称の各基準Transformと手のウェイポイントのローカル位置に`newValue`を乗算する。 |
| `setHandTransform(Transform rightHand, Transform leftHand, Transform newRightHandMountPoint, Transform newLeftHandMountPoint)` | 右手・左手とデュアル用の手Transform、左右のマウントポイントを差し替えて`updateComponent`を呼ぶ。 |
| `isPlayerCarringWeapon()` | `carryingWeapon`を返すだけ。 |
| `setShotCameraNoise()` | `useShotCameraNoise`時、視点別の範囲でランダムな揺れを`weaponsManager`へ要求する。 |
| `setCameraPositionMouseWheelEnabledState(bool state)` | `weaponsManager`へカメラ位置のマウスホイール可否を委譲するだけ。 |
| `checkIfIKHandsIsActive()` | 一人称中か、IK無効化設定なし、またはアタッチメント編集中ならtrueを返す。 |
| `enableOrDisableEditAttachment(bool state)` | 武器移動を止めて編集用コルーチンを開始し、必要なら左手も編集位置へ動かす。 |
| `moveHandForAttachment()` | 左手メッシュが無ければ戻り、編集位置/通常位置へ動かすコルーチンを開始する。 |
| `quickEnableOrDisableEditAttachment(bool state)` | コルーチンを使わず武器と左手を編集位置または歩き/しゃがみ位置へ即時配置する。 |
| `setUsingSecondPositionHandState(bool state)` | 一人称と三人称の`usingSecondPositionForHand`を同じ値にするだけ。 |
| `setNewSecondPositionHandTransformFirstPerson(Transform newTransform)` | 一人称の第2手位置を差し替え、編集中でなければ`checkHandsPosition`を呼ぶ。 |
| `setNewSecondPositionHandTransformThirdPerson(Transform newTransform)` | 三人称の第2手位置を差し替え、編集中でなければ`checkHandsPosition`を呼ぶ。 |
| `checkHandsPosition()` | 左手メッシュを、第2手位置が有効ならその位置へ、無ければ原点へ移動する。 |
| `stopEditAttachment()` | 編集中ならコルーチンを止め、`editingAttachments`をfalseにして左手メッシュを原点へ戻す。 |
| `getThirdPersonAttachmentCameraPosition()` | デュアル/右手状態に応じた三人称アタッチメントカメラのTransformを返す。 |
| `isWeaponOnRecoil()` | `weaponOnRecoil`を返すだけ。 |
| `setCurrentWeaponState(bool state)` | `currentWeapon`を設定して`weaponSystemManager`へ伝え、解除時は最終使用時刻を更新しIK停止を解く。 |
| `isCurrentWeapon()` | `currentWeapon`を返すだけ。 |
| `isAimingWeapon()` | `aiming`を返すだけ。 |
| `updateProjectileInfoValues()` | `weaponSystemManager`へ発射物情報の更新を委譲するだけ。 |
| `isPlayerCameraFirstPersonActive()` | `weaponsManager`に一人称カメラ中かを問い合わせて返す。 |
| `isAimModeInputPressed()` | `weaponsManager`へエイム入力の押下有無を問い合わせて返す。 |
| `setFullBodyAwarenessActiveState(bool state)` | `fullBodyAwarenessActive`を設定し、`weaponSystemManager`へも伝える。 |
| `isFullBodyAwarenessActive()` | `fullBodyAwarenessActive`を返すだけ。 |
| `enableOrDisableIKOnHandsFromFBAStateChange(bool state)` | FBA切替中フラグを立ててから`enableOrDisableIKOnHands`を呼ぶ。 |
| `isPlayerCrouching()` | `weaponsManager`へしゃがみ状態を問い合わせて返す。 |
| `isHideWeaponIfKeptInThirdPersonActive()` | `hideWeaponIfKeptInThirdPerson`を返すだけ。 |
| `initializeAttachmentSystem()` | アタッチメント使用時のみ`mainWeaponAttachmentSystem`を初期化する。 |
| `pickupAttachment(string attachmentName)` | 既に有効ならfalseを返し、そうでなければアタッチメントシステムへ取得を委譲する。 |
| `isAttachmentAlreadyActiveOnWeapon(string attachmentName)` | アタッチメントシステムへ装着済みかを問い合わせて返す。 |
| `checkIfWeaponAttachmentAssigned()` | 子から`weaponAttachmentSystem`を探して割り当て、有無をログ出力して`updateComponent`を呼ぶ。 |
| `selectAttachmentSystemOnEditor()` | エディタでアタッチメントシステムのオブジェクトを選択するだけ。 |
| `setWeaponAttachmentSystem(weaponAttachmentSystem attachmentSystem)` | アタッチメントシステムを設定し、使用フラグ更新と`assignWeaponToAttachment`を行う。 |
| `removeAttachmentSystem()` | `setWeaponAttachmentSystem(null)`を呼ぶだけ。 |
| `getWeaponAttachmentSystem()` | `mainWeaponAttachmentSystem`を返すだけ。 |
| `checkAttachmentsHUD()` | アタッチメントHUDの更新を委譲し、システムがあればtrueを返す。 |
| `enableAllAttachments()` | `mainWeaponAttachmentSystem`へ全アタッチメント有効化を委譲する。 |
| `checkSniperSightUsedOnWeapon(bool state)` | `weaponsManager`へスナイパーサイト使用状態を伝えるだけ。 |
| `setPlayerControllerMovementValues()` | `aiming`/`carrying`に応じた移動速度と走行可否を適用し、どちらでもなければ元に戻す。 |
| `setPlayerControllerMovementOriginalValues()` | `weaponsManager`へ移動値の復元を委譲するだけ。 |
| `setPlayerControllerCurrentIdleIDValue(int newValue)` | `weaponsManager`へ現在のアイドルID値を委譲するだけ。 |
| `setUsingDualWeaponState(bool state)` | `usingDualWeapon`を設定し、`weaponSystemManager`へも伝える。 |
| `disableUsingDualWeaponState()` | `setDisablingDualWeaponState(true)`を呼ぶだけ。 |
| `setDisablingDualWeaponState(bool state)` | `disablingDualWeapon`を設定するだけ。 |
| `isUsingDualWeapon()` | `usingDualWeapon`か`disablingDualWeapon`がtrueならtrueを返す。 |
| `setUsingRightHandDualWeaponState(bool state)` | 右手デュアル状態を設定し、`weaponSystemManager`へも伝える。 |
| `resetWeaponMeshTransform()` | `weaponSystemManager`へ武器メッシュのTransform初期化を委譲する。 |
| `isQuickDrawKeepDualWeaponActive()` | 手の設定か`weaponsManager`の強制フラグからクイックドロー維持を判定して返す。 |
| `setWeaponConfiguredAsDualWeaponState(bool state, string newWeaponName)` | 値が変わる場合に以前の状態を保存し、フラグとリンク先武器名を設定する。 |
| `disableWeaponConfiguredAsDualWeaponPreviously()` | `weaponConfiguredAsDualWeaponPreviously`をfalseにするだけ。 |
| `isWeaponConfiguredAsDualWeapon()` | `weaponConfiguredAsDualWeapon`を返すだけ。 |
| `getLinkedDualWeaponName()` | `linkedDualWeaponName`を返すだけ。 |
| `setCurrentWeaponAsOneHandWield()` | 片手持ち用に手の設定を変え、使用する手の歩き位置へ動かすコルーチンを開始する。 |
| `setCurrentWeaponAsTwoHandsWield()` | 両手持ちへ戻し、歩き位置を経て両手のIKウェイトを1にするコルーチンを開始する。 |
| `getUsingWeaponAsOneHandWieldState()` | `usingWeaponAsOneHandWield`を返すだけ。 |
| `setPlayer(GameObject newPlayer)` | `player`を設定するだけ。 |
| `getPlayerGameObject()` | `player`を返すだけ。 |
| `checkIfDeactivateIKIfNotAimingActive()` | FBA中はfalse、しゃがみ中はtrue、それ以外は武器ごとのIK無効化設定を返す。 |
| `setDeactivateIKIfNotAimingState(bool state)` | デュアル両手と通常の`deactivateIKIfNotAiming`をまとめて設定する。 |
| `enableOrDisableIKOnWeaponsDuringAction(bool state)` | 前提条件を満たす時だけ、動作中のIK切替コルーチンを開始し位置・速度・IKを更新する。 |
| `stopEnableOrDisableIKOnWeaponsDuringActionCoroutine()` | `actionCoroutine`を停止し、IK切替処理中フラグをfalseにする。 |
| `checkIfDisableCurrentWeaponIfEnableOrDisableIKOnWeaponsInProcess()` | IK切替コルーチン実行中ならそれを停止するだけ。 |
| `enableOrDisableIKOnHands(bool state)` | 所持中かつIK無効化設定なしの時、IK一時停止フラグを更新して動作切替を呼ぶ。 |
| `setIKPausedOnHandsActiveState(bool state)` | `IKPausedOnHandsActive`を設定するだけ。 |
| `setActionActiveState(bool state)` | `actionActive`を設定し、解除時はリロード中フラグを下ろして最終移動時刻を更新する。 |
| `checkIfSetNewAnimatorWeaponID()` | 一人称や所持状態に応じ、武器/しゃがみIDや角度上限、ピボット設定を`weaponsManager`へ反映する。 |
| `setWeaponMovingState(bool state)` | `moving`を設定するだけ。 |
| `setReloadingWithAnimationActiveState(bool state)` | リロード中フラグを両マネージャへ伝え、開始時は武器メッシュ位置を戻す。 |
| `activateCustomAction(string actionName)` | `weaponsManager`へカスタムアクション開始を委譲するだけ。 |
| `placeMagazineInPlayerHand(Transform magazineTransform, Transform magazineInHandTransform)` | 描画に使わない手のマウントへマガジンを親子付けし、手の位置・回転をコピーする。 |
| `setWeaponParent(bool state)` | 非アクティブ時に体の外へ出す設定なら、武器の親変更コルーチンを開始する。 |
| `stopSetWeaponParentCoroutine()` | `setParentCoroutine`を停止するだけ。 |
| `checkShootAnimatorState(bool state)` | `useWeaponAnimatorFirstPerson`時のみ、反動フラグを立てて射撃アニメ状態を設定する。 |
| `shootAnimatorStateComplete()` | `useWeaponAnimatorFirstPerson`時のみ、反動と射撃アニメのフラグを下ろす。 |
| `checkIdleAnimatorState(bool state)` | `useWeaponAnimatorFirstPerson`時のみアイドルアニメ状態を設定する。 |
| `checkWalkAnimatorState(bool state)` | `useWeaponAnimatorFirstPerson`時のみ歩きアニメ状態を設定する。 |
| `checkRunAnimatorState(bool state)` | `useWeaponAnimatorFirstPerson`時のみ走りアニメ状態を設定する。 |
| `checkReloadAnimatorState(bool state)` | `useWeaponAnimatorFirstPerson`時のみ、リロードアニメのフラグと状態を設定する。 |
| `reloadAnimatorStateComplete()` | リロード完了としてフラグを戻し、リロード位置使用時は一人称の構えを解除する。 |
| `setNewReloadTimeFirstPerson(float newValue)` | `weaponSystemManager`へ一人称のリロード時間を委譲するだけ。 |
| `reloadSingleProjectile()` | `weaponSystemManager`へ単発リロードを委譲するだけ。 |
| `pauseOrResumePlaySoundOnWeapon(bool state)` | `weaponSystemManager`へ武器サウンドの一時停止/再開を委譲する。 |
| `updateDurabilityAmountState()` | `useObjectDurability`時のみ耐久値の更新を委譲する。 |
| `initializeDurabilityValue(float newAmount, int currentObjectIndex)` | `useObjectDurability`時のみ耐久値とオブジェクト番号の初期化を委譲する。 |
| `setInventoryObjectIndex(int currentObjectIndex)` | `useObjectDurability`時のみインベントリのオブジェクト番号を委譲する。 |
| `getDurabilityAmount()` | 耐久値対応なら値を、非対応なら-1を返す。 |
| `repairObjectFully()` | `useObjectDurability`時のみ耐久値の全回復を委譲する。 |
| `breakFullDurabilityOnCurrentWeapon()` | `useObjectDurability`時のみ耐久値を0にする処理を委譲する。 |
| `checkEventOnEmptyDurability()` | `weaponsManager`へ耐久切れイベント処理を委譲するだけ。 |
| `canWeaponMarkTargets()` | `weaponSystemManager.canMarkTargets`を返すだけ。 |
| `canWeaponAutoShootOnTag()` | 武器設定の`autoShootOnTag`を返すだけ。 |
| `canWeaponAvoidShootAtTag()` | 武器設定の`avoidShootAtTag`を返すだけ。 |
| `setUseLowerRotationSpeedAimed(bool state)` | `useLowerRotationSpeedAimed`を設定するだけ。 |
| `setUseLowerRotationSpeedAimedThirdPerson(bool state)` | `useLowerRotationSpeedAimedThirdPerson`を設定するだけ。 |
| `createWeaponPrefab()` | 空プレハブに武器メッシュと名前を設定し、ピックアップ用プレハブとして保存する。 |
| `removeWeaponRegularPickup()` | `weaponPrefabModel`をnullにして`updateComponent`を呼ぶ。 |
| `assignWeaponPrefab()` | 武器名からインベントリ用プレハブを探して設定し、結果をログ出力する。 |
| `createInventoryWeaponAmmo()` | 武器名や弾メッシュ等の設定値を使ってインベントリ用の弾薬を作成する。 |
| `createInventoryWeapon()` | 武器名・メッシュ・アイコン等を設定してインベントリ武器を作成し、プレハブを割り当てる。 |
| `createInventoryWeaponExternally(string newWeaponName, string weaponDescriptionValue, Texture newWeaponIconTexture, bool useDurabilityValue, float durabilityAmountValue, float maxDurabilityAmountValue, float durabilityUsedOnAttackValue, float objectWeightValue, bool canBeSoldValue, float sellPriceValue, float vendorPriceValue)` | 渡された名前・説明・アイコン・耐久値などの引数を設定してから、インベントリ武器を作成する。 |
| `createInventoryWeaponAmmoExternally(string newWeaponAmmoName, int ammoAmount, GameObject newCustomAmmoMesh, Texture newCustomAmmoIcon, string newCustomAmmoDescription)` | 弾名を設定し、メッシュがあれば差し替えてプレハブ化し、インベントリ弾薬を作成する。 |
| `copyTransformValuesToBuffer(Transform transformToCopyValues)` | 対象のローカル位置・回転を`weaponsManager`のバッファへ唯一の要素として保存する。 |
| `pasteTransformValuesToBuffer(Transform transformToPasteValues)` | バッファに値があれば対象へローカル位置・回転を適用し、無ければ警告を出す。 |
| `selectWeaponAnimator()` | `useWeaponAnimatorFirstPerson`時、武器アニメーターのオブジェクトをエディタで選択する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーンのダーティ更新を呼ぶだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`getAmmoText()`, `getProjectilesInWeaponMagazine()`, `getWeaponAmmoName()`, `getWeaponName()`, `isFireWeapon()`, `isWeaponUseRemainAmmoFromInventoryActive()`, `setWeaponRemainAmmoAmount(int newRemainAmmoAmount)`

</details>

## 内部型

- `weaponShotShakeInfo`（class）
