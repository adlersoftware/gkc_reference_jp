# laserVisionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/laserVisionSystem.cs:6`

**概要**: レーザーでオブジェクトを切断するビジョン能力。レーザー位置の移動量から切断方向を決め、`sliceSystem` でスライスする。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Laser Vision Enabled | `laserVisionEnabled` | `bool` | true | – |
| Slice With Laser Enabled | `sliceWithLaserEnabled` | `bool` | true | – |
| Slice Objects Active Rate | `sliceObjectsActiveRate` | `float` | 0.5f | – |
| Main Layermask | `mainLayermask` | `LayerMask` | – | – |
| Laser Raycast Distance | `laserRaycastDistance` | `float` | – | – |
| Min Laser Movement To Activate Slice | `minLaserMovementToActivateSlice` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Laser Vision Active | `laserVisionActive` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Laser Vision Enabled | `eventOnLaserVisionEnabled` | `UnityEvent` | – | – |
| Event On Laser Vision Disabled | `eventOnLaserVisionDisabled` | `UnityEvent` | – | – |
| Cut Parent Refence | `cutParentRefence` | `Transform` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Slice System | `mainSliceSystem` | `sliceSystem` | – | – |
| Laser Position Transform | `laserPositionTransform` | `Transform` | – | – |
| Laser Direction Transform | `laserDirectionTransform` | `Transform` | – | – |
| Laser Game Object | `laserGameObject` | `GameObject` | – | – |
| Cut Overlap Box Size | `cutOverlapBoxSize` | `Vector3` | – | – |
| Cut Position Transform | `cutPositionTransform` | `Transform` | – | – |
| Cut Direction Transform | `cutDirectionTransform` | `Transform` | – | – |
| Plane Definer1 | `planeDefiner1` | `Transform` | – | – |
| Plane Definer2 | `planeDefiner2` | `Transform` | – | – |
| Plane Definer3 | `planeDefiner3` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setLaserVisionActiveState(bool state)` | `laserVisionEnabled` を確認してから状態とレーザー表示を切り替え、対応するイベントを発火する。 |
| `toggleLaserVisionActiveState()` | 現在の `laserVisionActive` を反転して `setLaserVisionActiveState` を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnLaserVisionEnabled` | `UnityEvent` | – |
| `eventOnLaserVisionDisabled` | `UnityEvent` | – |
