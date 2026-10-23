# dropPickUpSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `PickUps/dropPickUpSystem.cs:5`

**概要**: 敵などの位置に、抽選・確率・ランダム内容の設定に従ってピックアップを生成し、爆発力で周囲に散らすシステム。設計図の分解素材ドロップや生成イベントにも対応する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Drop Pickups Enabled | `dropPickupsEnabled` | `bool` | true | ドロップ処理全体を有効にする。 |
| Drop Delay | `dropDelay` | `float` | – | 生成を始めるまでの待ち時間（秒）。 |
| Destroy After Dropping | `destroyAfterDropping` | `bool` | – | 生成後にこのオブジェクトを破棄する。 |
| Set Pickup Scale | `setPickupScale` | `bool` | – | 生成物のスケールを上書きする。 |
| Pick Up Scale | `pickUpScale` | `float` | – | 生成物に設定するスケール倍率。 |
| Random Content | `randomContent` | `bool` | – | 個数と量を範囲内でランダムにする。 |
| Max Radius To Instantiate | `maxRadiusToInstantiate` | `float` | 1 | 生成位置をばらつかせる半径。 |
| Pick Up Offset | `pickUpOffset` | `Vector3` | – | 生成位置に加えるローカル方向のずれ。 |
| Main Pickup Manager Name | `mainPickupManagerName` | `string` | "Pickup Manager" | ピックアップ管理を探すときの名前。 |
| Use Custom Transform Position To Spawn | `useCustomTransformPositionToSpawn` | `bool` | – | 生成位置を別のトランスフォーム基準にする。 |
| Custom Transform Position To Spawn | `customTransformPositionToSpawn` | `Transform` | – | 生成位置と向きの基準トランスフォーム。 / 表示条件: `useCustomTransformPositionToSpawn` がオンのとき |

### Drop Object Probability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use General Probability Drop Objects | `useGeneralProbabilityDropObjects` | `bool` | – | 全体共通のドロップ確率判定を使う。 |
| General Probability Drop Objects | `generalProbabilityDropObjects` | `float` | – | この値未満の乱数ならドロップしない（0〜100）。 / Range (0, 100) |
| Drop Random Object | `dropRandomObject` | `bool` | – | 設定リストを無視し1種類をランダムに落とす。 |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューに生成範囲を表示する。 |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Create Drop Pickup Objects Active | `ignoreCreateDropPickupObjectsActive` | `bool` | – | デバッグ用に生成処理を止める。 |

### Force To Pickups Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Extra Force To Pickup | `extraForceToPickup` | `float` | 5 | 生成物に加える爆発力の強さ。 |
| Extra Force To Pickup Radius | `extraForceToPickupRadius` | `float` | 5 | 爆発力が及ぶ範囲の半径。 |
| Force Mode | `forceMode` | `ForceMode` | ForceMode.Impulse | 爆発力の適用方法を決める`ForceMode`。 |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event To Send Spawned Objects | `useEventToSendSpawnedObjects` | `bool` | – | 生成物を通知するイベントを使う。 |
| Event To Send Spawned Objects | `eventToSendSpawnedObjects` | `eventParameters.eventToCallWithGameObject` | – | 生成したオブジェクトを渡すイベント。 / 表示条件: `useEventToSendSpawnedObjects` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `dropPickUpList` | `List<dropPickUpElementInfo>` | new List<dropPickUpElementInfo> () | – |
| `managerPickUpList` | `List<pickUpElementInfo>` | new List<pickUpElementInfo> () | – |
| `mainInventoryManagerName` | `string` | "Main Inventory Manager" | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setIgnoreCreateDropPickupObjectsActiveState(bool state)` | `ignoreCreateDropPickupObjectsActive` を設定するだけ。 |
| `createDropPickUpObjects()` | ドロップ有効かつ自身がアクティブなときだけ、遅延付きの生成コルーチンを開始する。 |
| `setDropPickupsEnabledState(bool state)` | `dropPickupsEnabled` を設定するだけ。 |
| `getManagerPickUpList()` | `pickUpManager` を検索・生成して一覧をコピーし、更新とログ出力を行う。 |
| `updateComponent()` | `GKC_Utils.updateComponent` で値を反映し、シーンをダーティにして更新を通知する。 |
| `getOffset()` | `pickUpOffset` を、カスタム出現位置か自身のローカル軸に沿ったワールドオフセットへ変換して返す。 |
| `getMainInventoryManager()` | `inventoryListManager` を取得し、無ければ生成や検索を試みて、発見状態をフラグに保持する。 |
| `setDropPickupsEnabledStateFromEditor(bool state)` | エディタ用にドロップ有効状態を設定し、続けてコンポーネントを更新する。 |

## 内部型

- `dropPickUpElementInfo`（class）
- `dropPickUpTypeElementInfo`（class）
