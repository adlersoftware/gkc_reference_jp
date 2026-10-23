# manualDetonationMineObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/manualDetonationMineObject.cs:6`

**概要**: 手動起爆式の地雷オブジェクト。起爆用イベントを持ち、所有する `manualDetonationMineSystem` に自身の解除を依頼する。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Activate Mine | `eventToActivateMine` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateMine()` | `eventToActivateMine` を発火するだけ。 |
| `removeMine()` | `mainManualDetonationMineSystem` があれば `removeCurrentMine` を呼んで自身を解除させる。 |
| `setManualDetonationMineSystem(manualDetonationMineSystem newManualDetonationMineSystem)` | `mainManualDetonationMineSystem` を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToActivateMine` | `UnityEvent` | – |
