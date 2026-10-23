# headExplodeExample

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/headExplodeExample.cs:5`

**概要**: 頭部パーツを消すデモ用スクリプトで、任意でタイムバレット演出も併用する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Time Bullet | `useTimeBullet` | `bool` | true | – |
| Time Bullet Duration | `timeBulletDuration` | `float` | 3 | – |
| Time Scale | `timeScale` | `float` | 0.2f | – |
| Head Transform | `headTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `explode()` | `useTimeBullet`ならタイムバレットを発動し、`headTransform`の`localScale`を0にする。 |
| `explodeBodyPart(Transform objectToExplode)` | `objectToExplode`がnullでなければ`localScale`を0にするだけ。 |
