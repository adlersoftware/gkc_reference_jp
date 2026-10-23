# slowDownAllAIOnSceneSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/slowDownAllAIOnSceneSystem.cs:6`

**概要**: シーン内のAIを一時停止・再開させてスローダウンさせる能力。敵のみを対象にする設定も持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slow Down Enabled | `slowDownEnabled` | `bool` | true | – |
| Player Faction Name | `playerFactionName` | `string` | "Player" | – |
| Slow Down Only Enemies | `slowDownOnlyEnemies` | `bool` | – | – |
| Pause Character Priority | `pauseCharacterPriority` | `int` | 1 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slow Down Active | `slowDownActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Start | `eventOnStart` | `UnityEvent` | – | – |
| Event On End | `eventOnEnd` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `toggleSlowDownState()` | `slowDownActive` を反転して `setSlowDownState` を呼ぶだけ。 |
| `setSlowDownState(bool state)` | `slowDownEnabled` なら状態を更新し、開始・終了イベントと敵のみ・全AIの一時停止を切り替える。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStart` | `UnityEvent` | – |
| `eventOnEnd` | `UnityEvent` | – |
