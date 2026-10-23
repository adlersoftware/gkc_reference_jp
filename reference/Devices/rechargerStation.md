# rechargerStation

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/rechargerStation.cs:5`

**概要**: プレイヤーが入ると体力とエネルギーを`healSpeed`で回復する充填ステーション。満タンで停止し、アニメと効果音を制御する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Heal Speed | `healSpeed` | `float` | – | – |
| Animation Name | `animationName` | `string` | – | – |
| Sound | `sound` | `AudioClip` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Healing | `healing` | `bool` | – | – |
| Fully Healed | `fullyHealed` | `bool` | – | – |
| Inside | `inside` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sound Audio Element | `soundAudioElement` | `AudioElement` | – | – |
| Button | `button` | `GameObject` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Button Collider | `buttonCollider` | `Collider` | – | – |
| Main Animation | `mainAnimation` | `Animation` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `healPlayer()` | プレイヤーが内部にいて未回復なら、回復を開始してアニメ再生・効果音ループ・ボタン無効化を行う。 |
| `stopHealing()` | 回復を止めて`fullyHealed`を`true`にし、効果音のループを解除する。 |
