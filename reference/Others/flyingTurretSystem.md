# flyingTurretSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/flyingTurretSystem.cs:5`

**概要**: 追従対象の周囲に飛行タレットを生成し、手動射撃の有効化やAI制御の切り替えを行う。

## インスペクター設定

### Turret Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Flying Turret Enabled | `flyingTurretEnabled` | `bool` | true | – |
| Set Manual Fire On Turret Enabled | `setManualFireOnTurretEnabled` | `bool` | – | – |
| Manual Fire Input Enabled | `manualFireInputEnabled` | `bool` | – | – |
| Reactivate Auto Shoot After Delay | `reactivateAutoShootAfterDelay` | `bool` | – | – |
| Delay To Reactivate Auto Shoot | `delayToReactivateAutoShoot` | `float` | – | – |
| Current Camera Transform Direction | `currentCameraTransformDirection` | `Transform` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Flying Turret Active | `flyingTurretActive` | `bool` | – | – |
| Manual Control Active | `manualControlActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Flying Turret Object Prefab | `flyingTurretObjectPrefab` | `GameObject` | – | – |
| Flying Turret Object | `flyingTurretObject` | `GameObject` | – | – |
| Object To Follow | `objectToFollow` | `Transform` | – | – |
| Current AI Turret | `currentAITurret` | `AITurret` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableFlyingTurret()` | `flyingTurretActive`を反転して`setFlyingTurretActiveState`を呼ぶ。 |
| `setFlyingTurretActiveState(bool state)` | `flyingTurretActive`を更新し、必要ならタレットを生成して追従設定・手動射撃設定・SetActiveまで行う。 |
| `enableOrDisableManualFireOnTurret(bool state)` | タレット稼働中かつ手動射撃入力有効時、制御の上書きと射撃入力を`state`に合わせる。 |
| `enableOrDisableManualStateOnTurret(bool state)` | `currentAITurret`の制御上書きを`state`にし、`manualControlActive`も更新する。 |
| `inputToggleManualFire()` | タレット稼働中に`manualControlActive`を反転して手動制御状態を切り替える。 |
