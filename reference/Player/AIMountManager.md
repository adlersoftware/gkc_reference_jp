# AIMountManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Generic Model Controller/AIMountManager.cs:6`

**概要**: AIの乗り物（マウント）を呼び出したりテレポートさせたりする管理コンポーネント。プレイヤーとの距離に応じてリモートイベントを送る。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Mount Manager Enabled | `mountManagerEnabled` | `bool` | true | – |
| Remote Event To Call AI Mount | `remoteEventToCallAIMount` | `string` | "Set Player As Target For Mount AI" | – |
| Remote Event To Assign AI Mount | `remoteEventToAssignAIMount` | `string` | "Assign Player To Mount AI" | – |
| Min Distance To Call AI Mount | `minDistanceToCallAIMount` | `float` | 20 | – |
| Min Distance To Teleport AI Mount | `minDistanceToTeleportAIMount` | `float` | 100 | – |
| Layer To Teleport Raycast | `layerToTeleportRaycast` | `LayerMask` | – | – |
| Raycast Distance | `raycastDistance` | `float` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Call AI Mount | `eventOnCallAIMount` | `UnityEvent` | – | – |
| Event On Teleport AI Mount Before | `eventOnTeleportAIMountBefore` | `UnityEvent` | – | – |
| Event On Teleport AI Mount After | `eventOnTeleportAIMountAfter` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Current Mount Assigned | `currentMountAssigned` | `bool` | – | – |
| Current Mount Game Object | `currentMountGameObject` | `GameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Teleport AI Mount Target Transform | `teleportAIMountTargetTransform` | `Transform` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `assignCurrentMountGameObject(GameObject newObject)` | 機能有効時のみ `assignCurrentMountGameObjectCoroutine(newObject)` を開始する。 |
| `removeCurrentMountGameObject()` | 割当済みならマウントとプレイヤーの参照を null にし、フラグと時刻をリセットする。 |
| `callCurrentMount()` | 距離に応じてリモートイベント送信かテレポートを行い、実行時に呼び出しイベントを送出する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCallAIMount` | `UnityEvent` | – |
| `eventOnTeleportAIMountBefore` | `UnityEvent` | – |
| `eventOnTeleportAIMountAfter` | `UnityEvent` | – |
