# meleeAttackSurfaceInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/meleeAttackSurfaceInfo.cs:6`

**概要**: 攻撃面（サーフェス）の名前・有効状態、武器投擲時のオフセットや付着設定、耐久倍率、各種イベント/リモートイベントを保持するデータコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Surface Enabled | `surfaceEnabled` | `bool` | true | – |
| Surface Name | `surfaceName` | `string` | – | – |

### Weapon Throw Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Offset Transform On Weapon Throw | `useOffsetTransformOnWeaponThrow` | `bool` | – | – |
| Offset Transform On Weapon Throw | `offsetTransformOnWeaponThrow` | `Transform` | – | – |
| Use Offset Distance On Weapon Throw | `useOffsetDistanceOnWeaponThrow` | `bool` | – | – |
| Offset Distance On Weapon Throw | `offsetDistanceOnWeaponThrow` | `float` | – | – |
| Disable Insta Teleport On This Surface | `disableInstaTeleportOnThisSurface` | `bool` | – | – |

### Attach To Surface On Throw Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Attach Melee Weapon On Surface Value | `setAttachMeleeWeaponOnSurfaceValue` | `bool` | – | – |
| Attach Melee Weapon On Surface Value | `attachMeleeWeaponOnSurfaceValue` | `bool` | – | – |

### Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Durability | `ignoreDurability` | `bool` | – | – |
| Extra Durability Multiplier | `extraDurabilityMultiplier` | `float` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Surface Detected | `useEventOnSurfaceDetected` | `bool` | – | – |
| Event On Surface Deteceted | `eventOnSurfaceDeteceted` | `UnityEvent` | – | – |

### Events On Throw/Return Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Throw Weapon | `useEventOnThrowWeapon` | `bool` | – | – |
| Event On Throw Weapon | `eventOnThrowWeapon` | `UnityEvent` | – | – |
| Use Event On Return Weapon | `useEventOnReturnWeapon` | `bool` | – | – |
| Event On Return Weapon | `eventOnReturnWeapon` | `UnityEvent` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event | `useRemoteEvent` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | new List<string> () | – |
| Use Remote Event On Weapon | `useRemoteEventOnWeapon` | `bool` | – | – |
| Remote Event On Weapon Name List | `remoteEventOnWeaponNameList` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Ignore Surface Active | `ignoreSurfaceActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getSurfaceName()` | `surfaceName`を返すだけ。 |
| `isSurfaceEnabled()` | `surfaceEnabled`かつ`ignoreSurfaceActive`でない場合にtrueを返す。 |
| `setNewSurfaceName(string newSurfaceName)` | サーフェス名を変更し、デバッグ表示が有効ならログを出す。 |
| `setOriginalSurfaceName()` | `Start`で保存した元のサーフェス名に戻す。 |
| `setIgnoreSurfaceActiveState(bool state)` | サーフェスを無視するフラグを設定し、必要ならログを出す。 |
| `setUseRemoteEventState(bool state)` | リモートイベント使用フラグを設定するだけ。 |
| `setUseRemoteEventOnWeaponState(bool state)` | 武器側リモートイベント使用フラグを設定するだけ。 |
| `checkEventOnSurfaceDetected()` | 有効なら`eventOnSurfaceDeteceted`を発火する。 |
| `checkEventOnThrowWeapon()` | 有効なら`eventOnThrowWeapon`を発火し、必要ならログを出す。 |
| `checkEventOnReturnWeapon()` | 有効なら`eventOnReturnWeapon`を発火し、必要ならログを出す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnSurfaceDeteceted` | `UnityEvent` | – |
| `eventOnThrowWeapon` | `UnityEvent` | – |
| `eventOnReturnWeapon` | `UnityEvent` | – |
