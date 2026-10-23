# flamethrowerWeapon

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/flamethrowerWeapon.cs:7`

**概要**: 火炎放射器の連続噴射を制御し、燃料消費・連続音・開始終了音・パーティクルを切り替える武器挙動。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Energy Enabled | `useEnergyEnabled` | `bool` | true | – |
| Use Energy Rate | `useEnergyRate` | `float` | – | – |
| Amount Energy Used | `amountEnergyUsed` | `int` | – | – |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Play Sound Rate | `playSoundRate` | `float` | – | – |
| Min Delay To Play Sound | `minDelayToPlaySound` | `float` | – | – |
| Sound Effect | `soundEffect` | `AudioClip` | – | – |
| Sound Effect Audio Element | `soundEffectAudioElement` | `AudioElement` | – | – |
| Start Sound Effect | `startSoundEffect` | `AudioClip` | – | – |
| Start Sound Effect Audio Element | `startSoundEffectAudioElement` | `AudioElement` | – | – |
| End Sound Effect | `endSoundEffect` | `AudioClip` | – | – |
| End Sound Effect Audio Element | `endSoundEffectAudioElement` | `AudioElement` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Enabled | `weaponEnabled` | `bool` | – | – |
| Reloading | `reloading` | `bool` | – | – |
| Update Coroutine Active | `updateCoroutineActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Weapon State Change | `useEventsOnWeaponStateChange` | `bool` | – | – |
| Event On Weapon Enabled | `eventOnWeaponEnabled` | `UnityEvent` | – | – |
| Event On Weapon Disabled | `eventOnWeaponDisabled` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Configured On Weapon | `configuredOnWeapon` | `bool` | true | – |
| Weapon Manager | `weaponManager` | `playerWeaponSystem` | – | – |
| Main Particle System | `mainParticleSystem` | `ParticleSystem` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Start Audio Source | `startAudioSource` | `AudioSource` | – | – |
| End Audio Source | `endAudioSource` | `AudioSource` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`を止め、`updateCoroutineActive`を偽にする。 |
| `enableWeapon()` | `setWeaponState(true)`を呼ぶだけ。 |
| `disableWeapon()` | `setWeaponState(false)`を呼び、`reloading`も偽にする。 |
| `setWeaponState(bool state)` | リロード中は遷移を抑えつつ、パーティクルと開始・終了音を切り替え、有効時のみ更新コルーチンを回す。 |
| `stopUpdateCoroutineIfActive()` | `updateCoroutineActive`が真のときだけ`stopUpdateCoroutine()`を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnWeaponEnabled` | `UnityEvent` | – |
| `eventOnWeaponDisabled` | `UnityEvent` | – |
