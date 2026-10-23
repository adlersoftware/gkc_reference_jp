# bodyMountPointsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Character Builder/bodyMountPointsSystem.cs:5`

**概要**: 武器や装備をキャラクターの各部位へ取り付けるためのマウントポイントを管理する。名前から人型ボーンやカスタムボーンを解決し、子オブジェクトの親子付けとオフセットを適用する。

**公式ドキュメント抜粋**（[Body Mount Points System](../../docs/player-controller-components/elements-used-by-other-components/body-mount-points-system.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Bone Transform To Locate Bone | `useBoneTransformToLocateBone` | `bool` | true | – |
| Body Mount Point Info List | `bodyMountPointInfoList` | `List<bodyMountPointInfo>` | new List<bodyMountPointInfo> () | – |

### Editor Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Mount Point To Edit Name | `mountPointToEditName` | `string` | – | – |
| Mount Point Initial Position Offset | `mountPointInitialPositionOffset` | `Vector3` | new Vector3 (-0.008f, -0.1237f, -0.02… | – |
| Mount Point Initial Euler Offset | `mountPointInitialEulerOffset` | `Vector3` | new Vector3 (47.453f, 0, -15.026f) | – |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Editing Mount Point | `editingMountPoint` | `bool` | – | – |
| Temporal Mount Point Transform | `temporalMountPointTransform` | `Transform` | – | – |
| Temporal Mount Point Object Reference | `temporalMountPointObjectReference` | `GameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Mount Point Object Reference Prefab | `mountPointObjectReferencePrefab` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `removeCharacterBodyMountPointsToTemporalParent(Transform newParent)` | 全マウントポイントの `objectTransform` を `newParent` の子へ移動する。 |
| `resetCharacterBodyMountPointsLocalPositions()` | 全 `objectTransform` のローカル位置を零、ローカル回転を identity に戻す。 |
| `setCharacterBodyMountPointsInfoList()` | 全マウントポイントについて個別設定メソッドを順に呼ぶ。 |
| `setIndividualCharacterBodyMountPointInfoByName(string mountPointName)` | 名前から項目を探し、カスタム/人型ボーンを解決して各オブジェクトを親子付けし、位置・角度オフセットを適用する。 |
| `getMountPointTransformByName(string mountPointName)` | 名前が一致するマウントポイントの最初の `objectTransform` を返し、無ければ null を返す。 |
| `getHumanBoneMountPointTransformByName(string mountPointName)` | 名前からカスタムボーン、人型ボーン、代替ボーンの順に解決して返す。 |
| `setCustomBoneMountPointTransformByName(string mountPointName, Transform newCUstomBoneTransform, bool state)` | 名前一致の項目にカスタムボーンの使用フラグとTransformを設定する。 |
| `setCustomBoneMountPointTransformByNameFromEditor(string mountPointName, Transform newCUstomBoneTransform, bool state)` | カスタムボーンを設定した後に `updateComponent` を呼ぶ。 |
| `toggleShowHandleGizmo()` | `showGizmo` を反転するだけ。 |
| `toggleEditMountPoint()` | 編集モードを反転し、開始時は対象ポイントのプレハブを生成、終了時は削除する。 |
| `setNewAnimator(Animator newAnimator)` | `mainAnimator` を設定して `updateComponent` を呼ぶ。 |

## 内部型

- `bodyMountPointInfo`（class）
- `objectPointInfo`（class）
