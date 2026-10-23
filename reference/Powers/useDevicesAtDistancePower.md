# useDevicesAtDistancePower

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/New Powers Behaviors/useDevicesAtDistancePower.cs:5`

**概要**: 離れた場所からデバイスやスイッチ、拾得物を使用するパワー。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Power Enabled | `powerEnabled` | `bool` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Tag To Check | `tagToCheck` | `List<string>` | new List<string> () | – |
| Use Infinite Raycast Distance | `useInfiniteRaycastDistance` | `bool` | true | – |
| Raycast Distance | `raycastDistance` | `float` | 100 | – |
| Ignore Device To Control At Distance Component | `ignoreDeviceToControlAtDistanceComponent` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |
| Player Collider | `playerCollider` | `Collider` | – | – |
| Player | `player` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activatePower()` | 前方のトリガーが対象タグなら、`electronicDevice`等として遠隔使用を開始する。 |
