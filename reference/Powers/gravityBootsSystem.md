# gravityBootsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/gravityBootsSystem.cs:6`

**概要**: 重力ブーツ。壁面など任意の表面に吸着して歩けるよう、法線方向へ重力と向きを回転させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Gravity Boots Enabled | `gravityBootsEnabled` | `bool` | – | – |
| Gravity Boots Rotation Speed | `gravityBootsRotationSpeed` | `float` | 10 | – |
| Use Extra Raycast Detection On Gravity Boots Enabled | `useExtraRaycastDetectionOnGravityBootsEnabled` | `bool` | true | – |
| Avoid Rigidbodies On Raycast Enabled | `avoidRigidbodiesOnRaycastEnabled` | `bool` | – | – |
| Rotate To Original Normal On Air Enabled | `rotateToOriginalNormalOnAirEnabled` | `bool` | true | – |
| Stop Gravity Adherence When Stop Run | `stopGravityAdherenceWhenStopRun` | `bool` | true | – |
| Allow Circumnavigation On All Surfaces With Ignoretag List | `allowCircumnavigationOnAllSurfacesWithIgnoretagList` | `bool` | – | – |
| Circumnavigation On All Surfaces With Ignoretag List | `circumnavigationOnAllSurfacesWithIgnoretagList` | `List<string>` | new List<string> () | – |

### Surface Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Raycast Distance | `raycastDistance` | `float` | 2 | – |
| Ground Raycast Distance | `groundRaycastDistance` | `float` | 5 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Gravity Boots Active | `gravityBootsActive` | `bool` | – | – |
| Main Coroutine Active | `mainCoroutineActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Gravity Boots Start | `useEventOnGravityBootsStart` | `bool` | – | – |
| Use Event On Gravity Boots End | `useEventOnGravityBootsEnd` | `bool` | – | – |
| Event On Gravity Boots Start | `eventOnGravityBootsStart` | `UnityEvent` | – | – |
| Event On Gravity Boots End | `eventOnGravityBootsEnd` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Gravity System | `mainGravitySystem` | `gravitySystem` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 監視コルーチンを停止し、稼働フラグを下ろす。 |
| `stopGravityBoots()` | 重力ブーツを終了し、元の法線へ戻して周回移動の設定を無効化する。 |
| `areGravityBootsActive()` | 重力ブーツが発動中かどうかを返すだけ。 |
| `setGravityBootsEnabledState(bool state)` | 有効化時は監視開始と周回設定の反映、無効化時は停止を行い、開始/終了イベントを発火する。 |
| `toggleGravityBootsEnabledState()` | 重力ブーツの有効フラグを反転させて設定し直す。 |
| `disableGravityBootsState()` | 発動中なら停止し、有効フラグも下ろす。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnGravityBootsStart` | `UnityEvent` | – |
| `eventOnGravityBootsEnd` | `UnityEvent` | – |
