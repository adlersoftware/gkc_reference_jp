# slowObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `characterStateAffectedInfo`
- **ソース**: `Powers/slowObject.cs:6`

**概要**: オブジェクトを一定時間スローモーションにする状態。色変更コンポーネントを付与し、開始/終了イベントを持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Slow Speed | `useCustomSlowSpeed` | `bool` | – | – |
| Custom Slow Speed | `customSlowSpeed` | `float` | – | – |
| Object To Call Function | `objectToCallFunction` | `GameObject` | – | – |
| Use Slow Object Color | `useSlowObjectColor` | `bool` | true | – |
| Custom Slow Objects Color | `customSlowObjectsColor` | `Color` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Meshes To Ignore | `useMeshesToIgnore` | `bool` | – | – |
| Meshes To Ignore | `meshesToIgnore` | `List<Transform>` | new List<Transform> () | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Reduced Speed | `eventOnReducedSpeed` | `UnityEvent` | – | – |
| Event On Regular Speed | `eventOnRegularSpeed` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getObjectToCallFunction()` | 速度低下を通知する対象オブジェクトを返す。 |
| `isUseCustomSlowSpeedEnabled()` | カスタム速度を使うかどうかを返すだけ。 |
| `getCustomSlowSpeed()` | カスタム速度値を返すだけ。 |
| `checkChildsObjectsToIgnore(Transform obj)` | 指定`Transform`が無視メッシュ一覧またはその子に含まれるかを返す。 |
| `useMeshesToIgnoreEnabled()` | メッシュ無視の設定が有効かどうかを返すだけ。 |
| `checkEventOnReducedSpeed()` | 速度低下時の`UnityEvent`を発火するだけ。 |
| `checkEventOnRegularSpeed()` | 通常速度へ戻った時の`UnityEvent`を発火するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnReducedSpeed` | `UnityEvent` | – |
| `eventOnRegularSpeed` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateStateAffected(float stateDuration, float stateAmount)`

</details>
