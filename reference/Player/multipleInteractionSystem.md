# multipleInteractionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/multipleInteractionSystem.cs:6`

**概要**: 1つのオブジェクトに複数種別のインタラクション（デバイス）を持たせ、プレイヤーごとの利用登録や入退場イベントを管理する。コライダーとタグの有効/無効も切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Interaction Enabled | `interactionEnabled` | `bool` | true | – |
| Player Tag | `playerTag` | `string` | "Player" | – |

### Interaction Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Interaction Info List | `interactionInfoList` | `List<interactionInfo>` | new List<interactionInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Interaction Pause Active | `interactionPauseActive` | `bool` | – | – |
| Player List | `playerList` | `List<GameObject>` | new List<GameObject> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Trigger Enter | `useEventOnTriggerEnter` | `bool` | – | – |
| Event On Trigger Enter | `eventOnTriggerEnter` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use Event On Trigger Exit | `useEventOnTriggerExit` | `bool` | – | – |
| Event On Trigger Exit | `eventOnTriggerExit` | `eventParameters.eventToCallWithGameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Interaction Object | `mainInteractionObject` | `GameObject` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateInteraction(List<string> typeNameList, GameObject character)` | 有効かつ停止中でなければ、種別名リストに一致する項目を探し、遅延設定ならコルーチン、なければ即座に実行する。 |
| `checkEventOnEnterExit(bool state, GameObject newPlayer)` | 入場なら Enter、退場なら Exit のイベントを、使用時のみ `newPlayer` 付きで送出する。 |
| `setInteractionPauseActiveState(bool state)` | `interactionPauseActive` を設定するだけ。 |
| `removeDeviceFromPlayerList()` | 各プレイヤーの `usingDevicesSystem` から `mainInteractionObject` を解除する。 |
| `setMainColliderEnabledState(bool state)` | `mainCollider` の enabled が異なる場合だけ state に設定する。 |
| `disableInteractionIfActive()` | 停止中なら何もせず、そうでなければ `enableOrDisableInteraction(false)` を呼ぶ。 |
| `enableOrDisableInteraction(bool state)` | 全体無効時は何もせず、停止フラグを反転し、無効化時はデバイス解除、最後にコライダーを切り替える。 |
| `removeDeviceFromListAndDisableInteraction()` | デバイスをプレイヤーから解除し、タグを `Untagged` に変更する。 |
| `disableEntireMultipleInteraction()` | 全体を無効化し、デバイス解除とタグ変更を行う。 |
| `stopActivateInteractionCoroutine()` | `delayCoroutine` が null でなければ停止するだけ。 |
| `disableEntireMultipleInteractionFromEditor()` | 全体を無効化して `updateComponent` を実行する。 |

## 内部型

- `interactionInfo`（class）
