# meleeWeaponRangeAttacksManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/meleeWeaponRangeAttacksManager.cs:6`

**概要**: 近接武器に付属する遠距離攻撃（ボウ等）を、`simpleWeaponSystem`による射撃と`playerCamera`のレティクル、エイム/ストレイフ/しゃがみ状態の切り替えとして中継するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Range Attacks Active | `rangeAttacksActive` | `bool` | – | – |
| Aiming Active Body Weight | `aimingActiveBodyWeight` | `float` | 0.5f | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Current Range Weapon ID | `currentRangeWeaponID` | `int` | – | – |
| Current Range Weapon Info | `currentRangeWeaponInfo` | `int` | – | – |
| Aiming Active | `aimingActive` | `bool` | – | – |

### Range Weapon Types List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Range Weapon System Info List | `rangeWeaponSystemInfoList` | `List<rangeWeaponSystemInfo>` | new List<rangeWeaponSystemInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Aim | `useEventsOnAim` | `bool` | – | – |
| Event On Start Aiming | `eventOnStartAiming` | `UnityEvent` | – | – |
| Event On Stop Aiming | `eventOnStopAiming` | `UnityEvent` | – | – |
| Call Events On Disable Range Attacks State | `callEventsOnDisableRangeAttacksState` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Grabbed Object Melee Attack System | `mainGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMeleeWeaponRangeAttackManagerActiveState(bool state)` | 有効状態を切り替え、有効時は射撃システムを初期化、無効時は射撃を止めてイベントを呼ぶ。 |
| `setCurrentRangeWeaponSystemByID(int rangeWeaponID)` | ID一致の遠距離武器を現在武器にし、その`simpleWeaponSystem`だけ有効化する。 |
| `fireCurrentRangeWeapon()` | 有効時、イベント発火後に現在の`simpleWeaponSystem`へ射撃の押下と離しを送る。 |
| `fireCurrentRangeWeaponByAttackRangeID(int newRangeID)` | 指定IDの遠距離武器に切り替えて発射位置を設定し、`fireCurrentRangeWeapon`を呼ぶ。 |
| `startFireCurrentRangeWeapon()` | 射撃開始を送り、ストレイフ/しゃがみを退避して切り替え、エイムとヘッドトラックを有効にする。 |
| `stopFireCurrentRangeWeapon()` | 射撃中なら射撃を止め、ストレイフ/しゃがみ/エイムを元に戻す。 |
| `startFireCurrentRangeWeaponByAttackRangeID(int newRangeID)` | 指定IDに切り替えて発射位置を設定してから`startFireCurrentRangeWeapon`を呼ぶ。 |
| `enableCustomReticle(string reticleName)` | カメラに指定名のカスタムレティクルを有効化させる。 |
| `disableCustomReticle(string reticleName)` | カメラの指定名カスタムレティクルを無効化する。 |
| `disableAllCustomReticle()` | カメラのカスタムレティクルを全て無効化する。 |
| `inputSetAimState(bool state)` | 遠距離攻撃が有効な時だけ`setAimState`でエイム状態を設定する。 |
| `inputToggleAimState()` | 遠距離攻撃が有効な時だけ現在のエイム状態を反転する。 |
| `setAimState(bool state)` | 状態が変われば`aimingActive`を更新し、開始/停止イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartAiming` | `UnityEvent` | – |
| `eventOnStopAiming` | `UnityEvent` | – |

## 内部型

- `rangeWeaponSystemInfo`（class）
