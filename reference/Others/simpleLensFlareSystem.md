# simpleLensFlareSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleLensFlareSystem.cs:5`

**概要**: レンズフレア用オブジェクトを一定時間だけ表示する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Lens Flare | `mainLensFlare` | `LensFlare` | – | – |
| Fade Lens Flare Speed | `fadeLensFlareSpeed` | `float` | 4 | – |
| Lens Active Duration | `lensActiveDuration` | `float` | 2 | – |
| Lens Flare Game Object | `lensFlareGameObject` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableLesnFlare(bool state)` | 既存コルーチンを止め、`lensActiveDuration`秒だけ`lensFlareGameObject`を表示するコルーチンを開始する（`state`は未使用）。 |
