# GKCConditionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Condition System/GKCConditionSystem.cs:5`

**概要**: プレイヤー側に置かれ、トリガーで登録された`GKCConditionInfo`の判定呼び出しを代行するコンポーネント。`conditionSystemEnabled`がfalseの間は登録も判定も行わない。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Condition System Enabled | `conditionSystemEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current GKC Condition Info | `currentGKCConditionInfo` | `GKCConditionInfo` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentGKCConditionInfo(GKCConditionInfo newGKCConditionInfo)` | `conditionSystemEnabled`がtrueの時のみ`currentGKCConditionInfo`に新しい条件を保持する。 |
| `checkIfConditionComplete()` | 有効かつ条件が設定されていれば、その`GKCConditionInfo.checkIfConditionComplete`を呼ぶ。 |
| `refreshConditionSystemCheckStatus()` | `checkIfConditionComplete`を呼ぶだけ。 |
