# checkpointElement

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Checkpoint/checkpointElement.cs:6`

**概要**: 個々のチェックポイント。プレイヤーが触れるとセーブを実行し、自身を現在のチェックポイントとして管理者へ登録する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Checkpoint ID | `checkpointID` | `int` | – | – |
| Overwrite This Checkpoint | `overwriteThisCheckpoint` | `bool` | – | – |
| Save First Time Checkpoint Element Found | `saveFirstTimeCheckpointElementFound` | `bool` | true | – |
| Save In Every Trigger Enter | `saveInEveryTriggerEnter` | `bool` | – | – |

### Transform Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Save Transform | `useCustomSaveTransform` | `bool` | – | – |
| Custom Save Transform | `customSaveTransform` | `Transform` | – | – |
| Use Custom Camera Transform | `useCustomCameraTransform` | `bool` | – | – |
| Custom Camera Transform | `customCameraTransform` | `Transform` | – | – |
| Custom Camera Pivot Transform | `customCameraPivotTransform` | `Transform` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Save | `tagToSave` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Checkpoint Already Found | `checkpointAlreadyFound` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Checkpoint Activated | `useEventOnCheckpointActivated` | `bool` | – | – |
| Event On Checkpoint Activated | `eventOnCheckpointActivated` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Checkpoint Manager | `checkpointManager` | `checkpointSystem` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCheckPointManager(checkpointSystem manager)` | `checkpointManager`を設定し、コンポーネントを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`を呼び、シーンをダーティとして更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCheckpointActivated` | `UnityEvent` | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnTriggerEnter(Collider col)`

</details>
