# GKCRiderSocketSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/GKCRiderSocketSystem.cs:5`

**概要**: ライダー系コンポーネントへの参照を保持するだけの小さなソケット。`mainRiderSystem` を外部から取得するために使う。

## インスペクター設定

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rider System | `riderSystem` | `mainRiderSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getMainRiderSystem()` | 保持している`mainRiderSystem`参照を返すだけ。 |
