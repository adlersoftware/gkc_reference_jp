# damageInScreen

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/damageInScreen.cs:5`

**概要**: 自分の体力変化を画面数値で見せるためのコンポーネント。起動時に`damageOnScreenInfoSystem`へ対象登録し、以降はID経由で表示を委譲する。

**公式ドキュメント抜粋**（[Damage In Screen](../../docs/player-controller-components/elements-used-by-other-components/damage-in-screen.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Screen Info Enabled | `showScreenInfoEnabled` | `bool` | – | Show or hide the damage and healing numbers for the player and friends in the game window. |
| Damage On Screen Id | `damageOnScreenId` | `int` | – | – |
| Remove Damage In Screen On Death | `removeDamageInScreenOnDeath` | `bool` | true | – |
| Icon Offset | `iconOffset` | `Vector3` | – | – |
| Main Manager Name | `mainManagerName` | `string` | "Damage On Screen Info Manager" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Damage In Screen | `pauseDamageInScreen` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Target Transform | `targetTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `showScreenInfo(float amount, bool damage, Vector3 direction, float healthAmount, float criticalDamageProbability)` | 表示有効かつ非一時停止なら`damageOnScreenInfoManager.setDamageInfo`へIDと値を渡す。 |
| `pauseOrPlayDamageInScreen(bool state)` | `pauseDamageInScreen`を`state`にするだけ。 |
| `setShowScreenInfoEnabledState(bool state)` | `showScreenInfoEnabled`を`state`にするだけ。 |
| `setShowScreenInfoEnabledStateFromEditor(bool state)` | 設定後に`updateComponent`で更新するだけ。 |
| `initializeDamageInScreenComponent()` | `targetTransform`を補完し、マネージャを検索/生成して対象登録しIDを受け取る。 |
