# GKCTeleportHelper

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/GKCTeleportHelper.cs:3`

**概要**: シーン上のメインプレイヤーを対象に、テレポート・ダイアログ起動・移動速度の制限をまとめて行う補助コンポーネント。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Teleport Target | `teleportTarget` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `TeleportPlayer(GameObject player)` | `teleportTarget`（未設定なら自身）の位置と向きへ`player`を移動し、`playerController`があればそれ経由で反映する。 |
| `TeleportMainPlayer()` | `GKC_Utils.findMainPlayerOnScene`でメインプレイヤーを探して`TeleportPlayer`を呼び、見つからなければ警告を出す。 |
| `ActivateDialogOnSystem(GameObject dialogSystemObj)` | `dialogSystemObj`にメインプレイヤーを渡してダイアログを起動し、`electronicDevice`があれば外部使用を優先する。 |
| `SetPlayerWalkingSpeedLimit()` | メインプレイヤーを歩き速度既定に切り替え、NavMesh側の移動速度を0.5に制限する。 |
| `RestorePlayerSpeed()` | 歩き速度既定を解除して元の速度へ戻し、NavMeshのカスタム速度も無効化する。 |
