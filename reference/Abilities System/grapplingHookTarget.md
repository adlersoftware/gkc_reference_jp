# grapplingHookTarget

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/Grappling Hook System/grapplingHookTarget.cs:6`

**概要**: グラップリングフックの対象地点コンポーネント。プレイヤーがトリガーに入ると対象リストへ登録し、フック・スイング受信時のイベントを持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grappling Hook Target Enabled | `grapplingHookTargetEnabled` | `bool` | true | – |
| Tags To Check | `tagsToCheck` | `List<string>` | new List<string> () | – |
| Layermask To Check | `layermaskToCheck` | `LayerMask` | – | – |

### Custom Hook Transform Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Transform Target | `useCustomTransformTarget` | `bool` | – | – |
| Custom Transform Target | `customTransformTarget` | `Transform` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Hook Received | `useEventOnHookReceived` | `bool` | – | – |
| Event On Hook Received | `eventOnHookReceived` | `UnityEvent` | – | – |
| Use Event On Swing Received | `useEventOnSwingReceived` | `bool` | – | – |
| Event On Swing Received | `eventOnSwingReceived` | `UnityEvent` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.green | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.white | – |
| Gizmo Radius | `gizmoRadius` | `float` | 0.3f | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Sphere Collider | `mainSphereCollider` | `SphereCollider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | 対象レイヤーとタグが合えば、`isEnter` に応じてプレイヤーの対象リストへ自身を登録・解除する。 |
| `checkEventOnHookReceived()` | `useEventOnHookReceived` が有効なら `eventOnHookReceived` を発火するだけ。 |
| `checkEventOnSwingReceived()` | `useEventOnSwingReceived` が有効なら `eventOnSwingReceived` を発火するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnHookReceived` | `UnityEvent` | – |
| `eventOnSwingReceived` | `UnityEvent` | – |
