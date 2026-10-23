# manualDetonationMineSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/manualDetonationMineSystem.cs:6`

**概要**: 手動起爆式の地雷の設置と起爆を管理するコンポーネント。設置イベント、現在の地雷、設置時刻を保持する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Delay To Activate Mine | `minDelayToActivateMine` | `float` | – | – |
| Event To Place New Mine | `eventToPlaceNewMine` | `UnityEvent` | – | – |
| Current Mine | `currentMine` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `placeNewMine()` | `currentMine` が空の時だけ設置イベント `eventToPlaceNewMine` を発火する。 |
| `setCurrentMine(GameObject newMineObject)` | 現在の地雷を登録し、その `manualDetonationMineObject` に自身を渡して設置時刻を記録する。 |
| `activateCurrentMine()` | `minDelayToActivateMine` を過ぎていれば現在の地雷を起爆し、`removeCurrentMine` で参照を消す。 |
| `removeCurrentMine()` | `currentMine` を null にするだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToPlaceNewMine` | `UnityEvent` | – |
