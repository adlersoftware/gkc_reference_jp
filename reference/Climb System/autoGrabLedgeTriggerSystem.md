# autoGrabLedgeTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Climb System/autoGrabLedgeTriggerSystem.cs:5`

**概要**: トリガーに入ったプレイヤーへ、指定した`ledgeTransform`への自動掴みを要求する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Ledge Zone Active | `ledgeZoneActive` | `bool` | true | – |
| Ledge Transform | `ledgeTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 対象タグならプレイヤーへ`ledgeTransform`付きの自動掴みを要求し、退出時は解除する。 |
