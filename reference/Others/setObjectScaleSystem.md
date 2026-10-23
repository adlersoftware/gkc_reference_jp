# setObjectScaleSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/setObjectScaleSystem.cs:6`

**概要**: 名前付きのスケール状態へコルーチンで補間しながら拡大縮小する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Scale Speed | `changeScaleSpeed` | `float` | – | – |
| Object To Scale | `objectToScale` | `Transform` | – | – |
| Scale State Info List | `scaleStateInfoList` | `List<scaleStateInfo>` | new List<scaleStateInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setScaleState(string scaleStateName)` | `scaleStateInfoList`から名前一致の項目を選び、その`objectScale`で`changeScale`を呼ぶ。 |
| `changeScale(Vector3 newScale)` | 既存コルーチンを止め、`newScale`へLerpで近づけるコルーチンを開始する。 |

## 内部型

- `scaleStateInfo`（class）
