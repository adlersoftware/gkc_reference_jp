# quickTravelStationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Map/quickTravelStationSystem.cs:6`

**概要**: ファストトラベル拠点のコンポーネント。プレイヤーを拠点位置へ移動させ、建物の切り替えや重力方向の再設定、到達イベントを行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Quick Travel Transform | `quickTravelTransform` | `Transform` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Max Distance To Check | `maxDistanceToCheck` | `float` | 4 | – |
| Animation Name | `animationName` | `string` | – | – |
| Enter Audio Sound | `enterAudioSound` | `AudioClip` | – | – |
| Enter Audio Element | `enterAudioElement` | `AudioElement` | – | – |
| Activate At Start | `activateAtStart` | `bool` | – | – |
| Set Gravity Direction | `setGravityDirection` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Map Creator Manager Name | `mainMapCreatorManagerName` | `string` | "Map Creator" | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Call Event On Teleport | `callEventOnTeleport` | `bool` | – | – |
| Event On Teleport | `eventOnTeleport` | `UnityEvent` | – | – |
| Call Event On Every Teleport | `callEventOnEveryTeleport` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Station Activated | `stationActivated` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Gravity Manager | `setGravityManager` | `setGravity` | – | – |
| Audio Source | `audioSource` | `AudioSource` | – | – |
| Station Animation | `stationAnimation` | `Animation` | – | – |
| Map Object Information Manager | `mapObjectInformationManager` | `mapObjectInformation` | – | – |
| Map Creator Manager | `mapCreatorManager` | `mapCreator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `travelToThisStation(Transform currentPlayer)` | プレイヤーを`quickTravelTransform`の位置と向きへ移動し、建物変更・重力・イベントを処理する。 |
| `activateStation()` | アニメーションを再生し、`mapObjectInformation`でマップアイコンを生成して起動済みにする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTeleport` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnTriggerEnter(Collider col)`

</details>
