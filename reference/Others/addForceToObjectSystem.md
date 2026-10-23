# addForceToObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/addForceToObjectSystem.cs:5`

**概要**: 登録したRigidbodyへ毎フレーム風の力を加え、プレイヤー・乗り物・通常オブジェクトで強さを変えつつ風の状態も同期するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Affect To Player Only On A Ir | `affectToPlayerOnlyOnAIr` | `bool` | – | – |
| Affect Only On Paraglider Active | `affectOnlyOnParagliderActive` | `bool` | – | – |
| Force Amount On Paraglider | `forceAmountOnParaglider` | `float` | – | – |
| Force Amount Characters | `forceAmountCharacters` | `float` | – | – |
| Force Amount Regular Objects | `forceAmountRegularObjects` | `float` | – | – |
| Force Amount Vehicles | `forceAmountVehicles` | `float` | – | – |
| Force Mode Characters | `forceModeCharacters` | `ForceMode` | – | – |
| Force Mode Regular Objects | `forceModeRegularObjects` | `ForceMode` | – | – |
| Force Mode Vehicles | `forceModeVehicles` | `ForceMode` | – | – |
| Add Force In Update | `addForceInUpdate` | `bool` | – | – |

### Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Player Enabled | `checkPlayerEnabled` | `bool` | true | – |
| Player Tag | `playerTag` | `string` | "Player" | – |
| Check Vehicles Enabled | `checkVehiclesEnabled` | `bool` | – | – |
| Use Layer To Check | `useLayerToCheck` | `bool` | – | – |
| Layer To Check | `layerToCheck` | `LayerMask` | – | – |

### Wind/Air Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Wind Object State Enabled | `checkWindObjectStateEnabled` | `bool` | – | – |
| Ignore Forces On Vehicle If Wind Active | `ignoreForcesOnVehicleIfWindActive` | `bool` | – | – |
| Wind Direction Transform | `windDirectionTransform` | `Transform` | – | – |
| Wind Force | `windForce` | `float` | – | – |
| Update Wind Direction On Update | `updateWindDirectionOnUpdate` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Rigidbody Info List | `rigidbodyInfoList` | `List<rigidbodyInfo>` | new List<rigidbodyInfo> () | – |
| Objects Detected | `objectsDetected` | `bool` | – | – |
| Pause Update Forces | `pauseUpdateForces` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Force Direction | `forceDirection` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPauseUpdateForcesState(bool state)` | `pauseUpdateForces`を`state`にするだけ。 |
| `setWindDetectedStateOnAllObjects(bool state)` | 風方向の毎更新が有効なら、対象各オブジェクトの風検出状態を`state`にする。 |
| `addNewObject(GameObject newObject)` | レイヤーなどの条件を満たす剛体を、乗り物やプレイヤーの判定込みで`rigidbodyInfoList`に登録する。 |
| `removeObject(GameObject objectToRemove)` | 一致する登録を外し、プレイヤーや風の外部力状態を解除してリストから削除する。 |
| `removeAllObjects()` | null要素を除去しつつ全登録を`removeObject`で解除し、リストを空にする。 |
| `setWindForceValue(float newValue)` | `windForce`を`newValue`にするだけ。 |

## 内部型

- `rigidbodyInfo`（class）
