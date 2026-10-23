# hiddenMeleeSurface

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/hiddenMeleeSurface.cs:5`

**概要**: 斬撃サーフェスを隠しサーフェスとして扱うためのフラグを保持する小型コンポーネント。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hidden Surface Enabled | `hiddenSurfaceEnabled` | `bool` | true | – |
| Main Melee Attack Surface Info | `mainMeleeAttackSurfaceInfo` | `meleeAttackSurfaceInfo` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isSurfaceEnabled()` | `hiddenSurfaceEnabled`の値をそのまま返すだけ。 |
| `setHiddenSurfaceEnabledState(bool state)` | `hiddenSurfaceEnabled`を設定するだけ。 |
