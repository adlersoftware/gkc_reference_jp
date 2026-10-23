# cameraEffect

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Camera Effect/cameraEffect.cs:5`

**概要**: カメラエフェクトの基底クラス。`renderEffect` を仮想メソッドとして持つだけで、実際の描画は派生クラスが実装する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Render Effect | `useRenderEffect` | `bool` | true | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `renderEffect(RenderTexture source, RenderTexture destination, Camera mainCamera)` | 本体が空で何もしない。 |
