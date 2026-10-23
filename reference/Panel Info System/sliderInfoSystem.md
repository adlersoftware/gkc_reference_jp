# sliderInfoSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Panel Info System/sliderInfoSystem.cs:6`

**概要**: 名前付きのUIスライダーを時間経過で増減させる管理コンポーネント。アクティブ中はコルーチンで値を加算または減算し続ける。

**公式ドキュメント抜粋**（[Slider Info System](../../docs/player-controller-components/elements-used-by-other-components/slider-info-system.md)）

> 

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slider Info System Enabled | `sliderInfoSystemEnabled` | `bool` | true | – |
| Slider Info List | `sliderInfoList` | `List<sliderInfo>` | new List<sliderInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateSliderByName(string sliderName)` | 名前一致のスライダーを有効化し、最大値と初期値・増減方向を設定して更新コルーチンを開始する。 |
| `deactivateSliderByName(string sliderName)` | 名前一致のスライダーGameObjectを非表示にし、コルーチンを止めて`sliderActive`をfalseにする。 |

## 内部型

- `sliderInfo`（class）
