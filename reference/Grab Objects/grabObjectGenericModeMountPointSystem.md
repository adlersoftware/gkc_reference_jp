# grabObjectGenericModeMountPointSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/grabObjectGenericModeMountPointSystem.cs:5`

**概要**: ジェネリックモードの把持で使うマウントポイントと参照位置を名前で引くためのデータ保持コンポーネント。既定ポイントとスケール倍率の設定も持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grab Objects Enabled | `grabObjectsEnabled` | `bool` | true | – |
| Use Custom Grabbed Object Scale Multiplier | `useCustomGrabbedObjectScaleMultiplier` | `bool` | – | – |
| Custom Grabbed Object Scale Multiplier | `customGrabbedObjectScaleMultiplier` | `float` | – | – |

### Mount Point List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Point Info List | `objectPointInfoList` | `List<objectPointInfo>` | new List<objectPointInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isUseCustomGrabbedObjectScaleMultiplierActive()` | `useCustomGrabbedObjectScaleMultiplier` を返すだけ。 |
| `getCustomGrabbedObjectScaleMultiplier()` | `customGrabbedObjectScaleMultiplier` を返すだけ。 |
| `isGrabObjectsEnabled()` | `grabObjectsEnabled` を返すだけ。 |
| `getMountPointByName(string mountPointName)` | `objectPointInfoList` から同名の `objectTransform` を返し、見つからなければ null を返す。 |
| `getDefaultMountPoint()` | `usePointAsDefault` が true の最初の項目の `objectTransform` を返し、無ければ null を返す。 |
| `getReferencePositionByName(string mountPointName, string referencePositionName)` | 指定マウント内の同名 `referencePosition` を返し、見つからなければ null を返す。 |

## 内部型

- `objectPointInfo`（class）
- `referencePositionInfo`（class）
