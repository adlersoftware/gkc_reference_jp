# simpleLamp

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleLamp.cs:5`

**概要**: ランプの設置状態と点灯を管理し、切り替え時にスイッチ音を鳴らす。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Has Lamp | `hasLamp` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Lamp Light | `lampLight` | `GameObject` | – | – |
| Switch Sound | `switchSound` | `AudioClip` | – | – |
| Switch Audio Element | `switchAudioElement` | `AudioElement` | – | – |
| Audio Source | `audioSource` | `AudioSource` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `lampPlaced()` | `hasLamp`を`true`にするだけ。 |
| `activateDevice()` | `lampLight`の`activeSelf`を反転させて`setActivateDeviceState`を呼ぶ。 |
| `setActivateDeviceState(bool state)` | `hasLamp`が`true`の時だけスイッチ音を鳴らし、`lampLight`のSetActiveを`state`に合わせる。 |
