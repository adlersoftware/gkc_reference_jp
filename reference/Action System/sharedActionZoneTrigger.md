# sharedActionZoneTrigger

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/Shared Action System/sharedActionZoneTrigger.cs:6`

**概要**: トリガーの進入と退出を検出して、プレイヤーの共有アクション起動状態を切り替えるコンポーネント。タグやレイヤで対象を絞り込める。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shared Action Zone Trigger Enabled | `sharedActionZoneTriggerEnabled` | `bool` | true | – |
| Shared Action Zone Name On Enter | `sharedActionZoneNameOnEnter` | `string` | – | – |
| Use Shared Action Timer On Enter | `useSharedActionTimerOnEnter` | `bool` | – | – |
| Shared Action Timer On Enter | `sharedActionTimerOnEnter` | `float` | – | – |
| Set Shared Action Zone On Exit | `setSharedActionZoneOnExit` | `bool` | – | – |
| Shared Action Zone Name On Exit | `sharedActionZoneNameOnExit` | `string` | – | – |
| Use Shared Action Timer On Exit | `useSharedActionTimerOnExit` | `bool` | – | – |
| Shared Action Timer On Exit | `sharedActionTimerOnExit` | `float` | – | – |
| Enable Shared Action Remote Activator On Trigger Enter | `enableSharedActionRemoteActivatorOnTriggerEnter` | `bool` | – | – |
| Disable Shared Action Remote Activator On Trigger Exit | `disableSharedActionRemoteActivatorOnTriggerExit` | `bool` | – | – |

### Custom Shared Action Name Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Custom Shared Action Name On Enter | `setCustomSharedActionNameOnEnter` | `bool` | – | – |
| Custom Shared Action Name On Enter | `customSharedActionNameOnEnter` | `string` | – | – |
| Remove Custom Shared Action Name On Exit | `removeCustomSharedActionNameOnExit` | `bool` | – | – |

### Check Targets Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Tag List | `useTagList` | `bool` | – | – |
| Tag List | `tagList` | `List<string>` | new List<string> () | – |
| Use Layer Mask | `useLayerMask` | `bool` | – | – |
| Layer Mask | `layerMask` | `LayerMask` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | タグやレイヤで対象を絞り、進入時はアクティベータ有効化と名前設定、退出時は無効化やカスタム名削除を行う。 |
