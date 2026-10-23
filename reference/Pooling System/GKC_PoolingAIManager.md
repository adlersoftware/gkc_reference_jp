# GKC_PoolingAIManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Pooling System/GKC_PoolingAIManager.cs:5`

**概要**: シーン内の`GKC_PoolingElementAI`を収集してリスト管理し、全AIのプーリング管理を一括で有効/無効にするコンポーネント。収集や切り替えの後はシーン更新を通知する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Find Disabled Elements On Scene Game Objects | `findDisabledElementsOnSceneGameObjects` | `bool` | true | – |

### AI Pooling List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| GKC Pooling Element AI List | `GKC_PoolingElementAIList` | `List<GKC_PoolingElementAI>` | new List<GKC_PoolingElementAI> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getAllGKC_PoolingElementAIOnLevel()` | リストをクリアし、設定に応じて非アクティブも含む/含まない全`GKC_PoolingElementAI`を収集してシーンを更新する。 |
| `clearGKC_PoolingElementAIList()` | `GKC_PoolingElementAIList`をClearしてシーンを更新するだけ。 |
| `enableAllGKC_PoolingElementAIOnLevel()` | `enableOrDisableAllGKC_PoolingElementAIOnLevel(true)`を呼ぶだけ。 |
| `disableAllGKC_PoolingElementAIOnLevel()` | `enableOrDisableAllGKC_PoolingElementAIOnLevel(false)`を呼ぶだけ。 |
| `enableOrDisableAllGKC_PoolingElementAIOnLevel(bool state)` | リスト内の各AI要素へ`state`でのプーリング管理の有効/無効と対応イベントを適用し、シーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`でコンポーネントとシーンの更新を通知するだけ。 |
