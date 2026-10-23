# simpleAIAction

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Custom AI Behavior/simpleAIAction.cs:6`

**概要**: カスタムAI行動の基底クラス。有効時のみ開始/終了イベントとコルーチンを管理し、継続時間の経過か外部呼び出しで終了する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action Enabled | `actionEnabled` | `bool` | true | – |
| Action Used By Player | `actionUsedByPlayer` | `bool` | – | – |
| Action Duration | `actionDuration` | `float` | – | – |
| Use Update System Coroutine | `useUpdateSystemCoroutine` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Action Active | `actionActive` | `bool` | – | – |
| Current Target | `currentTarget` | `Transform` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Start Action | `useEventOnStartAction` | `bool` | – | – |
| Event On Start Action | `eventOnStartAction` | `UnityEvent` | – | – |
| Use Event On End Action | `useEventOnEndAction` | `bool` | – | – |
| Event On End Action | `eventOnEndAction` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `startAIAction()` | `actionEnabled`ならコルーチンを開始して`actionActive`を立て、開始イベントを発火する。 |
| `endAIAction()` | 実行中なら終了イベントを発火してフラグを下ろし、コルーチン停止と状態リセットを行う。 |
| `stopActionCoroutine()` | `actionCoroutine`があれば停止するだけ。 |
| `activateCoroutine()` | `useUpdateSystemCoroutine`なら毎フレーム更新、そうでなければ`actionDuration`後に終了するコルーチンを開始する。 |
| `updateSystem()` | 空の仮想メソッドで、派生クラスでの拡張用。 |
| `resetStatesOnActionEnd()` | 空の仮想メソッドで、派生クラスでの拡張用。 |
| `setCustomTarget(Transform newTarget)` | `currentTarget`を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartAction` | `UnityEvent` | – |
| `eventOnEndAction` | `UnityEvent` | – |
