# laser

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/laser.cs:4`

**概要**: レーザービームの見た目を制御する基底コンポーネント。UVスクロール・幅の脈動・ビーム長を毎フレーム更新する。

**公式ドキュメント抜粋**（[GKC Update 3.03-1](../../docs/annex/changelog/gkc-update-3.03-1.md)）

> UMA 2 Honor AI Added tutorial videos to configure URP and HDRP with GKC easily Added quick change direction, to make a turn of 180 degrees when moving from one direction to another quickly, to make the player to feel more dynamic and react better to the input New option to use pinch in and out on touch devices, allowing to trigger separate events in both directions, which can be used for different input actions. In this example, I have configured events to trigger the same functions used on the mouse wheel to move the camera closer or farther from the player. The option checks when enough distance has been applied (closer or farther from the initial) for both fingers and also, it checks that no other touch input is pressed, to avoid awkward situations and the minimum distance difference on the fingers to check events The pinch system has also an option to simulate two fingers in the unit…

## インスペクター設定

### Laser Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Scroll Speed | `scrollSpeed` | `float` | 0.09f | – |
| Pulse Speed | `pulseSpeed` | `float` | 0.28f | – |
| Noise Size | `noiseSize` | `float` | 0.19f | – |
| Max Width | `maxWidth` | `float` | 0.1f | – |
| Min Width | `minWidth` | `float` | 0.2f | – |
| Animate Laser Enabled | `animateLaserEnabled` | `bool` | true | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| L Renderer | `lRenderer` | `LineRenderer` | – | – |
| Main Renderer | `mainRenderer` | `Renderer` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `animateLaser()` | マテリアルのUVをスクロールし、幅を脈動させて`LineRenderer`の太さとテクスチャ長を更新する。 |
| `laserAnimation()` | 揺らぎ用の`aniDir`と`minWidth`をランダムに更新して待つだけのコルーチン。 |
| `disableLaser()` | 自身を無効化し、`LineRenderer`があれば合わせて無効化する。 |
