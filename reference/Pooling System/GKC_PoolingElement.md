# GKC_PoolingElement

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Pooling System/GKC_PoolingElement.cs:6`

**概要**: プール対象オブジェクトに付ける基底コンポーネントで、生成位置/回転、生成・破棄時のイベント、プーリング管理の有効/無効切り替えを提供する。状態確認用メソッドは派生クラスでの上書きを前提とした空実装。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Pooling Enabled | `usePoolingEnabled` | `bool` | true | – |
| Main Pool Game Object | `mainPoolGameObject` | `GameObject` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Position To Spawn | `currentPositionToSpawn` | `Vector3` | – | – |
| Current Rotation To Spawn | `currentRotationToSpawn` | `Quaternion` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Spawn | `useEventOnSpawn` | `bool` | – | – |
| Event On Spawn | `eventOnSpawn` | `UnityEvent` | – | – |
| Use Event On Despawn | `useEventOnDespawn` | `bool` | – | – |
| Event On Despawn | `eventOnDespawn` | `UnityEvent` | – | – |
| Event To Enable Pool Management | `eventToEnablePoolManagement` | `UnityEvent` | – | – |
| Event To Disable Pool Management | `eventToDisablePoolManagement` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPositionToSpawn(Vector3 newValue)` | 生成位置`currentPositionToSpawn`に`newValue`を代入するだけ。 |
| `setRotationToSpawn(Quaternion newValue)` | 生成回転`currentRotationToSpawn`に`newValue`を代入するだけ。 |
| `spawnPoolObject()` | `usePoolingEnabled`がtrueの時だけ生成イベントと生成後フックを実行する(実際の`Spawn`呼び出しはコメントアウト)。 |
| `despawnPoolObject()` | `usePoolingEnabled`がtrueの時だけ、破棄前フックと破棄イベントを実行して`GKC_PoolingSystem.Despawn`で返却する。 |
| `checkObjectStateBeforeDespawn()` | 本体が空で何もしない(派生クラスでの上書き用)。 |
| `checkObjectStateAfterSpawn()` | 本体が空で何もしない(派生クラスでの上書き用)。 |
| `checkEventOnSpawn()` | `useEventOnSpawn`がtrueの時、`eventOnSpawn`をInvokeするだけ。 |
| `checkEventOnDespawn()` | `useEventOnDespawn`がtrueの時、`eventOnDespawn`をInvokeするだけ。 |
| `setUsePoolingEnabledState(bool state)` | `usePoolingEnabled`に`state`を代入するだけ。 |
| `checkEventsOnEnableOrDisablePoolingManagementOnObject(bool state)` | プーリング有効フラグを設定し、有効/無効それぞれのイベントを実行、非再生中は`updateComponent`でシーンを更新する。 |
| `setUsePoolingEnabledStateFromEditor(bool state)` | フラグを設定して`updateComponent`でコンポーネントとシーンを更新する(エディタ用)。 |
| `checkEventsOnEnableOrDisablePoolingManagementOnObjectFromEditor(bool state)` | イベント付きの有効/無効切り替えをそのまま呼ぶだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnSpawn` | `UnityEvent` | – |
| `eventOnDespawn` | `UnityEvent` | – |
| `eventToEnablePoolManagement` | `UnityEvent` | – |
| `eventToDisablePoolManagement` | `UnityEvent` | – |
