# GKC_SimplePoolPreloadSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Pooling System/GKC_SimplePoolPreloadSystem.cs:5`

**概要**: `poolObjectPreloadInfoList`に登録したプレハブを、`Start`時に`GKC_PoolingSystem.Preload`で指定個数だけ事前生成するプリロード用コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Preload Objects Enabled | `preloadObjectsEnabled` | `bool` | true | – |

### Object List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pool Object Preload Info List | `poolObjectPreloadInfoList` | `List<poolObjectPreloadInfo>` | new List<poolObjectPreloadInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `preloadObjects()` | リスト内でプレハブが設定された各項目を、`objectAmount`個ずつ`GKC_PoolingSystem.Preload`で事前生成する。 |

## 内部型

- `poolObjectPreloadInfo`（class）
