# railMechanism

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/railMechanism.cs:6`

**概要**: レール上のオブジェクトを最終位置や停止位置へ補間移動させ、接続イベントやレール使用状態を管理するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check If Final Position Reached | `checkIfFinalPositionReached` | `bool` | true | – |
| Use Position To Move On Final | `usePositionToMoveOnFinal` | `bool` | – | – |
| Reset To Initial Position Ondrop | `resetToInitialPositionOndrop` | `bool` | – | – |
| Reset To Initial Position Speed | `resetToInitialPositionSpeed` | `float` | – | – |
| Displace Rail Speed | `displaceRailSpeed` | `float` | 1 | – |
| Movement Speed | `movementSpeed` | `float` | 2 | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Multiplier Value | `multiplierValue` | `float` | 1 | – |
| Speed Reduced | `speedReduced` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activated | `activated` | `bool` | – | – |
| Using Rail | `usingRail` | `bool` | – | – |
| Mechanism Can Be Engaged | `mechanismCanBeEngaged` | `bool` | true | – |

### Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object On Rail | `objectOnRail` | `Transform` | – | – |
| Stop Position | `stopPosition` | `Transform` | – | – |
| Final Position | `finalPosition` | `Transform` | – | – |
| Position To Move On Final | `positionToMoveOnFinal` | `Transform` | – | – |
| Initial Position Transform | `initialPositionTransform` | `Transform` | – | – |
| Position To Move On Stop | `positionToMoveOnStop` | `Transform` | – | – |
| Move Objects While Rail Is Moving | `moveObjectsWhileRailIsMoving` | `bool` | – | – |
| Objects To Move List | `objectsToMoveList` | `List<Transform>` | new List<Transform> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Mechanism Connected | `eventOnMechanismConnected` | `UnityEvent` | – | – |
| Event On Mechanism Stopped | `eventOnMechanismStopped` | `UnityEvent` | – | – |
| Use Event On Using Rail | `useEventOnUsingRail` | `bool` | – | – |
| Event On Using Rail | `eventOnUsingRail` | `UnityEvent` | – | – |
| Use Event On Drop Rail | `useEventOnDropRail` | `bool` | – | – |
| Event On Drop Rail | `eventOnDropRail` | `UnityEvent` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Radius | `gizmoRadius` | `float` | 0.2f | – |
| Gizmo Scale | `gizmoScale` | `float` | 0.2f | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkToDropObjectOnRail()` | `objectOnRail`の`grabbedObjectState`があれば、保持者からオブジェクトをドロップさせる。 |
| `engaged()` | 接続イベントを発火し、`activated`をtrueにしてタグを`Untagged`にする。 |
| `resetPosition(Transform targetTransform, float resetMovementSpeed, bool enganeAfterCoroutine)` | リセットを止め、`targetTransform`まで`resetMovementSpeed`で移動するコルーチンを開始する。 |
| `stopResetCoroutine()` | 実行中の`resetCoroutine`があれば停止するだけ。 |
| `setUsingRailState(bool state)` | `usingRail`を更新し、離脱時は初期位置へ戻し、状態に応じて使用/ドロップイベントを発火する。 |
| `getDisplaceRailSpeed()` | `displaceRailSpeed`を返すだけ。 |
| `engageRailAutomatically()` | オブジェクトをドロップさせ、最終位置へ移動した後に自動で`engaged`にする。 |
| `setReducedVelocity(float newMultiplierValue)` | `multiplierValue`を`newMultiplierValue`にし、初期位置へ戻すリセットを開始する。 |
| `setNormalVelocity()` | `multiplierValue`を初期値`originalMultiplierValue`に戻すだけ。 |
| `setMechanismCanBeEngagedState(bool state)` | `mechanismCanBeEngaged`を`state`にするだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnMechanismConnected` | `UnityEvent` | – |
| `eventOnMechanismStopped` | `UnityEvent` | – |
| `eventOnUsingRail` | `UnityEvent` | – |
| `eventOnDropRail` | `UnityEvent` | – |
