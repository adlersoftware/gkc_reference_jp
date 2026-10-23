# headTrackTarget

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Head Track/headTrackTarget.cs:5`

**概要**: トリガーに入った`headTrack`へ自身を注視対象として登録し、注視位置と可視判定を提供するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Target Enabled | `targetEnabled` | `bool` | true | – |
| Position Offset | `positionOffset` | `Vector3` | – | – |
| Min Distance To Look | `minDistanceToLook` | `float` | 4 | – |
| Visibility Types | `visibilityTypes` | `targetVisibilityTypes` | – | – |
| Tags To Locate | `tagsToLocate` | `List<string>` | new List<string> () | – |
| Use Custom Layer | `useCustomLayer` | `bool` | – | – |
| Custom Layer | `customLayer` | `LayerMask` | – | – |
| Store Head Track Found | `storeHeadTrackFound` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Track Found List | `headTrackFoundList` | `List<headTrack>` | new List<headTrack> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.yellow | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Target To Look | `targetToLook` | `Transform` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getLookPositon()` | `targetToLook`があればその位置＋オフセット、無ければ自身の変換位置にオフセットを足して返す。 |
| `lookTargetVisible(Vector3 headPosition, LayerMask layer)` | 無効時や距離超過ならfalseを返し、Raycast設定時は遮蔽物の有無で可視判定する。 |
| `drawLine(Vector3 startPosition, Vector3 endPosition, Color color)` | `showGizmo`が有効な時のみデバッグラインを描画する。 |
| `setEnableState(bool state)` | `targetEnabled`を設定するだけ。 |
| `disableState()` | `targetEnabled`をfalseにするだけ。 |
| `addTagToLocate(string tagToAdd)` | 未登録ならタグを追加し、コライダーを一度切替えてトリガー判定を再評価させる。 |
| `removeTagToLocate(string tagToAdd)` | そのタグの`headTrack`を注視リストから外してから、タグを削除する。 |
| `removeAllHeadTracksFoundAndDisableHeadTrack()` | 記録した全`headTrack`から自身を解除し、コライダーとターゲットを無効にする。 |
| `enableHeadTrack()` | `targetEnabled`をtrueにし、コライダーを有効化する。 |

## 内部型

- `targetVisibilityTypes`（enum）
