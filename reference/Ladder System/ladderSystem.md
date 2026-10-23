# ladderSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Ladder System/ladderSystem.cs:6`

**概要**: はしご本体のコンポーネント。トリガーに入ったプレイヤーへ自身を登録して設定を渡し、退出時に解除する。

**公式ドキュメント抜粋**（[Ladder System](../../docs/player-controller-components/elements-used-by-other-components/ladder-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `string` | – | – |
| Ladder Active | `ladderActive` | `bool` | true | – |
| Use Ladder Horizontal Movement | `useLadderHorizontalMovement` | `bool` | true | – |
| Move In Ladder Center | `moveInLadderCenter` | `bool` | – | – |
| Use Local Movement Direction | `useLocalMovementDirection` | `bool` | – | – |
| Jump On Third Person Enabled | `jumpOnThirdPersonEnabled` | `bool` | true | – |
| Jump On First Person Enabled | `jumpOnFirstPersonEnabled` | `bool` | true | – |

### FBA Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Use Simple Ladders On FBA | `canUseSimpleLaddersOnFBA` | `bool` | – | – |
| Use Extra Follow Transform Position Offset Active FBA | `useExtraFollowTransformPositionOffsetActiveFBA` | `bool` | – | – |
| Extra Follow Transform Position Offset FBA | `extraFollowTransformPositionOffsetFBA` | `Vector3` | – | – |
| Change View To FBA During Ladder Usage | `changeViewToFBADuringLadderUsage` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events Enter Exit Ladder | `useEventsEnterExitLadder` | `bool` | – | – |
| Event To Send Current Player On Enter | `eventToSendCurrentPlayerOnEnter` | `eventParameters.eventToCallWithGameObject` | – | – |
| Event To Send Current Player On Exit | `eventToSendCurrentPlayerOnExit` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use Events On Jump | `useEventsOnJump` | `bool` | – | – |
| Event On Jump | `eventOnJump` | `UnityEvent` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | true | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.red | – |
| Gizmo Length | `gizmoLength` | `float` | 4 | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ladder Direction Transform | `ladderDirectionTransform` | `Transform` | – | – |
| Ladder Raycast Direction Transform | `ladderRaycastDirectionTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 対象タグのプレイヤーにはしご検出状態と方向・移動設定を渡し、退出時は解除してイベントを呼ぶ。 |
| `checkEventOnJump()` | `useEventsOnJump`が有効なら`eventOnJump`を発火するだけ。 |
| `isJumpOnThirdPersonEnabled()` | `jumpOnThirdPersonEnabled`を返すだけ。 |
| `isJumpOnFirstPersonEnabled()` | `jumpOnFirstPersonEnabled`を返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnJump` | `UnityEvent` | – |
