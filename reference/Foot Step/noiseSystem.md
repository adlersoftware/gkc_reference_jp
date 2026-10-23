# noiseSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Foot Step/noiseSystem.cs:5`

**概要**: オブジェクトが発する騒音を周囲へ通知するコンポーネントで、表面のデカール設定から可否を判定し、ノイズ信号やノイズメッシュを発生させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Noise | `useNoise` | `bool` | – | – |
| Noise Radius | `noiseRadius` | `float` | – | – |
| Noise Expand Speed | `noiseExpandSpeed` | `float` | – | – |
| Use Noise Detection | `useNoiseDetection` | `bool` | – | – |
| Noise Detection Layer | `noiseDetectionLayer` | `LayerMask` | – | – |
| Noise Decibels | `noiseDecibels` | `float` | 1 | Range (0, 2) |
| Use Noise Position Offset | `useNoisePositionOffset` | `bool` | – | – |
| Noise Position Offset | `noisePositionOffset` | `Vector3` | – | – |
| Enable Only Used By Player | `enableOnlyUsedByPlayer` | `bool` | – | – |
| Force Noise Detection | `forceNoiseDetection` | `bool` | – | – |
| Noise ID | `noiseID` | `int` | -1 | – |
| Activate Noise At Start | `activateNoiseAtStart` | `bool` | – | – |

### Rigidbody Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used On Rigidbody | `usedOnRigidbody` | `bool` | – | – |
| Use Rigidbody Collision Speed | `useRigidbodyCollisionSpeed` | `bool` | – | – |
| Max Collision Speed Value | `maxCollisionSpeedValue` | `float` | – | – |
| Collision Noise Multiplier | `collisionNoiseMultiplier` | `float` | 1 | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Decal Manager Name | `mainDecalManagerName` | `string` | "Decal Manager" | – |
| Main Noise Mesh Manager Name | `mainNoiseMeshManagerName` | `string` | "Noise Mesh Manager" | – |
| Use Noise Mesh | `useNoiseMesh` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Show Noise Detection Gizmo | `showNoiseDetectionGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.green | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateNoise()` | 表面のデカール設定で可否を判定し、ノイズ信号とノイズメッシュを出して追加半径などをリセットする。 |
| `activateNoiseExternally()` | `useNoise`が有効な時だけ`activateNoise`を呼び出す。 |
| `setUseNoiseState(bool state)` | `useNoise`フラグを設定するだけ。 |
| `setimpactObject(GameObject newObject)` | `impactObject`を差し替えるだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnCollisionEnter(Collision col)`

</details>
