# flashlight

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/flashlight.cs:7`

**概要**: 武器に付く懐中電灯で、残弾を電池として消費し、ライト・メッシュ・HUD表示・効果音を切り替える。

**公式ドキュメント抜粋**（[Flashlight](../../docs/player-controller-components/non-essential-components/flashlight.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Flashlight Enabled | `flashlightEnabled` | `bool` | true | – |
| Infinite Energy | `infiniteEnergy` | `bool` | – | – |
| Use Energy Rate | `useEnergyRate` | `float` | – | – |
| Amount Energy Used | `amountEnergyUsed` | `int` | – | – |
| Light Rotation Speed | `lightRotationSpeed` | `float` | 10 | – |
| Used Through Weapon System | `usedThroughWeaponSystem` | `bool` | true | – |

### Intensity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use High Intentity | `useHighIntentity` | `bool` | – | – |
| High Intensity Amount | `highIntensityAmount` | `float` | – | – |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Sound | `useSound` | `bool` | – | – |
| Turn On Sound | `turnOnSound` | `AudioClip` | – | – |
| Turn On Audio Element | `turnOnAudioElement` | `AudioElement` | – | – |
| Turn Off Sound | `turnOffSound` | `AudioClip` | – | – |
| Turn Off Audio Element | `turnOffAudioElement` | `AudioElement` | – | – |

### UI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Flashlight Indicator Panel | `useFlashlightIndicatorPanel` | `bool` | – | – |
| Main Slider | `mainSlider` | `Slider` | – | – |
| Flahslight Indicator Panel | `flahslightIndicatorPanel` | `GameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Is Activated | `isActivated` | `bool` | – | – |
| Reloading | `reloading` | `bool` | – | – |
| Using Flashlight | `usingFlashlight` | `bool` | – | – |
| Flash Light Input Paused State | `flashLightInputPausedState` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | – |
| Weapon Manager | `weaponManager` | `playerWeaponSystem` | – | – |
| Main Light | `mainLight` | `GameObject` | – | – |
| Main Flashlight | `mainFlashlight` | `Light` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Flashlight Meshes | `flashlightMeshes` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkIfEnoughBattery()` | 無限でなく武器システム経由なら残弾の有無を確認し、その結果を返す。 |
| `changeFlashLightState()` | 入力停止中なら何もせず、そうでなければ`isActivated`を反転して`setFlashlightState`を呼ぶ。 |
| `setFlashlightState(bool state)` | 点灯時は電池と有効設定を確認し、`isActivated`・音・`mainLight`のアクティブ状態を反映する。 |
| `turnOn()` | 電池と有効設定を確認してから`isActivated`を真にし、点灯音を鳴らす。 |
| `turnOff()` | `isActivated`を偽にして消灯音を鳴らすだけ。 |
| `playSound(bool state)` | `useSound`が真なら音源ピッチを整え、点灯か消灯かに応じた音を鳴らす。 |
| `changeLightIntensity(bool state)` | `useHighIntentity`が真なら`highIntensityActivated`を設定し、強度を高い値か元の値へ切り替える。 |
| `setHighIntensity()` | 武器システム経由でFBA中かつ照準入力がなければ何もせず、条件を満たすと高輝度へ切り替える。 |
| `setOriginalIntensity()` | `changeLightIntensity(false)`で元の明るさへ戻すだけ。 |
| `enableOrDisableFlashlightMeshes(bool state)` | `flashlightMeshes`があれば、有効化時は設定を確認してから表示を`state`に合わせる。 |
| `setFlashLightInputPausedState(bool state)` | `flashLightInputPausedState`を`state`にするだけ。 |
| `enableOrDisableFlashlightIndicator(bool state)` | `usingFlashlight`を設定し、HUDパネル表示と残量スライダーの最大値を更新する。 |
