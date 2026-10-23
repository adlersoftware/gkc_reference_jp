# AITurret

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Turret/AITurret.cs:7`

**概要**: タレットの武器選択・発砲・旋回と、プレイヤーによる遠隔操作、死亡時の分解処理を担う。目標判定はmanageAITargetに委ね、選択武器の有効化と付随イベントを切り替える。

## インスペクター設定

### Turret Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Rotation Speed | `rotationSpeed` | `float` | 10 | – |
| Input Rotation Speed | `inputRotationSpeed` | `float` | 5 | – |
| Range Angle X | `rangeAngleX` | `Vector2` | – | – |
| Override Rotation Speed | `overrideRotationSpeed` | `float` | 10 | – |
| Raycast Position Rotation Speed | `raycastPositionRotationSpeed` | `float` | 10 | – |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Located Enemy | `locatedEnemy` | `AudioClip` | – | – |
| Located Enemy Audio Element | `locatedEnemyAudioElement` | `AudioElement` | – | – |

### Weapons Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Default Weapon Active Name | `defaultWeaponActiveName` | `string` | – | – |
| Random Weapon At Start | `randomWeaponAtStart` | `bool` | – | – |
| Use General Layer To Damage | `useGeneralLayerToDamage` | `bool` | – | – |
| Layer To Damage | `layerToDamage` | `LayerMask` | – | – |
| Turret Weapon Info List | `turretWeaponInfoList` | `List<turretWeaponInfo>` | new List<turretWeaponInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dead | `dead` | `bool` | – | – |
| Shooting Weapons | `shootingWeapons` | `bool` | – | – |
| Weapons Active | `weaponsActive` | `bool` | – | – |
| Current Camera Transform Direction | `currentCameraTransformDirection` | `Transform` | – | – |
| Current Weapon Name | `currentWeaponName` | `string` | – | – |
| Current Weapon Index | `currentWeaponIndex` | `int` | – | – |

### Override Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Control Overriden | `controlOverriden` | `bool` | – | – |
| Use Custom Input Camera Direction | `useCustomInputCameraDirection` | `bool` | – | – |
| Override Position To Look | `overridePositionToLook` | `Transform` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Transparent | `transparent` | `Shader` | – | – |
| Layer For Gravity | `layerForGravity` | `LayerMask` | – | – |
| Fade Pieces On Death | `fadePiecesOnDeath` | `bool` | true | – |
| Fade Pieces Speed | `fadePiecesSpeed` | `float` | 5 | – |
| Destroy Pieces Wait Time | `destroyPiecesWaitTime` | `float` | 10 | – |
| Add Force To Turret Pieces On Death | `addForceToTurretPiecesOnDeath` | `bool` | true | – |
| Force Amount To Pieces | `forceAmountToPieces` | `float` | 500 | – |
| Radius Amount To Pieces | `radiusAmountToPieces` | `float` | 50 | – |

### Turret Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ray Cast Position | `rayCastPosition` | `GameObject` | – | – |
| Rotating Base | `rotatingBase` | `GameObject` | – | – |
| Head | `head` | `GameObject` | – | – |
| Target Manager | `targetManager` | `manageAITarget` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Audio Source | `audioSource` | `AudioSource` | – | – |
| Override Input | `overrideInput` | `overrideInputManager` | – | – |
| Turret Attacker | `turretAttacker` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `chooseNextWeapon()` | 武器インデックスを進め(末尾付近で0に戻る)、その武器を選んで発砲可能状態にする。 |
| `choosePreviousWeapon()` | 武器インデックスを戻し(先頭では末尾へ)、その武器を選んで発砲可能状態にする。 |
| `enableOrDisableWeapons(bool state)` | `weaponsActive`を設定し、有効なら武器を起動、無効なら停止する。 |
| `setOnSpottedState(bool state)` | trueで武器を起動、falseで頭部を初期回転へ戻すコルーチンを開始して武器を停止する。 |
| `setDeathState()` | 武器を止めて`dead`を立て、描画パーツへRigidbodyとColliderを付け、設定時は爆発力を加える。 |
| `setRandomWeapon()` | ランダムな武器インデックスを選び`setWeapon`を呼ぶ。 |
| `setWeapon(int weaponNumber)` | 指定インデックスの武器名で`setCurrentTurretWeapon`を呼ぶ。 |
| `startOverride()` | `overrideTurretControlState(true)`を呼ぶだけ。 |
| `stopOverride()` | `overrideTurretControlState(false)`を呼ぶだけ。 |
| `overrideTurretControlState(bool state)` | 操作権を切り替え、`manageAITarget.pauseAI`を同期し、旋回速度・射撃状態・武器のカメラ参照を更新する。 |
| `disableOverrideAfterDelay(float delayDuration)` | 実行中ならコルーチンを開始し直し、指定秒数の実時間後に`stopOverride`で操作を戻す。 |
| `stopDisableOverrideAfterDelayCoroutine()` | 保持している遅延解除コルーチンを停止するだけ。 |
| `setNewCurrentCameraTransformDirection(Transform newTransform)` | `currentCameraTransformDirection`を設定するだけ。 |
| `setNewTurretAttacker(GameObject newAttacker)` | `turretAttacker`を設定するだけ。 |
| `inputSetShootState(bool state)` | 武器が有効で起動から0.6秒経過していれば`shootingWeapons`を設定する。 |
| `inputSetWeaponsState()` | 現在の武器有効状態を反転して`enableOrDisableWeapons`を呼ぶ。 |
| `inputSetNextOrPreviousWeapon(bool state)` | trueで次の武器、falseで前の武器を選ぶ。 |

## 内部型

- `turretWeaponInfo`（class）
