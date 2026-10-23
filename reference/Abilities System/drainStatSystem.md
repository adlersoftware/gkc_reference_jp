# drainStatSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/drainStatSystem.cs:6`

**概要**: カメラ前方の対象を検出し、時間経過で相手のステータスを吸い取って自分を強化するドレイン能力。対象検出、吸収コルーチン、対象を引き寄せる処理をまとめて持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Drain Enabled | `drainEnabled` | `bool` | – | – |
| Layer To Check | `layerToCheck` | `LayerMask` | – | – |
| Use Sphere Cast All | `useSphereCastAll` | `bool` | – | – |
| Sphere Cast All Radius | `sphereCastAllRadius` | `float` | – | – |

### Drain Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Drain Stats Enabled | `drainStatsEnabled` | `bool` | true | – |
| Activate Drain Coroutine Directly | `activateDrainCoroutineDirectly` | `bool` | – | – |
| Drain Stat Rate | `drainStatRate` | `float` | 0.3f | – |
| Max Drain Distance | `maxDrainDistance` | `float` | 20 | – |
| Move Object Closer To Player | `moveObjectCloserToPlayer` | `bool` | – | – |
| Move Object Speed | `moveObjectSpeed` | `float` | 5 | – |
| Look Object Speed | `lookObjectSpeed` | `float` | 5 | – |
| Min Distance To Move | `minDistanceToMove` | `float` | 3 | – |
| Start Drain Delay | `startDrainDelay` | `float` | – | – |
| Stop Drain Directly | `stopDrainDirectly` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Drain Active | `drainActive` | `bool` | – | – |
| Drain Action Paused | `drainActionPaused` | `bool` | – | – |
| Move Object Active | `moveObjectActive` | `bool` | – | – |
| Detected Game Object List | `detectedGameObjectList` | `List<GameObject>` | new List<GameObject> () | – |

### Stats Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stats Info List | `statsInfoList` | `List<statsInfo>` | new List<statsInfo> () | – |

### Remote Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List On Start | `remoteEventNameListOnStart` | `List<string>` | new List<string> () | – |
| Remote Event Name List On End | `remoteEventNameListOnEnd` | `List<string>` | new List<string> () | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Start Drain | `eventOnStartDrain` | `UnityEvent` | – | – |
| Envet On End Drain | `envetOnEndDrain` | `UnityEvent` | – | – |
| Event To Stop Drain Manually | `eventToStopDrainManually` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopDrainManually()` | `drainActive` の時だけ手動停止用イベント `eventToStopDrainManually` を発火する。 |
| `stopDrainIfActive()` | `drainActive` なら `stopDrain` を呼び、必要に応じて終了イベントも発火する。 |
| `checkTargetToDrain()` | カメラ前方のレイキャストで対象を検出し、`drainActive` と対象リストを設定して開始イベントを発火する。 |
| `startDrainCoroutine()` | 既存のドレインコルーチンを止め、`activateDrainStatCoroutine` を開始する。 |
| `stopActivateDrainStatCoroutine()` | `drainCoroutine` が動いていれば停止する。 |
| `stopDrain()` | ドレインと引き寄せのコルーチンを止め、`drainActive` を下げて終了イベントと終了リモートイベントを実行する。 |
| `checkRemoteEventOnStart()` | `useRemoteEventOnObjectsFound` が有効なら検出済みオブジェクトへ開始用リモートイベントを送る。 |
| `checkRemoteEventOnEnd()` | `useRemoteEventOnObjectsFound` が有効なら検出済みオブジェクトへ終了用リモートイベントを送る。 |
| `startMoveObjectCoroutine()` | 既存の引き寄せコルーチンを止め、`moveObjectCoroutine` を開始する。 |
| `stopMoveObjectCoroutine()` | `moveCoroutine` が動いていれば停止する。 |
| `setDrainActionPausedState(bool state)` | `drainActionPaused` を設定するだけ。 |
| `setMoveObjectActiveState(bool state)` | `moveObjectActive` を設定し、有効になった時は引き寄せコルーチンを開始する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartDrain` | `UnityEvent` | – |
| `envetOnEndDrain` | `UnityEvent` | – |
| `eventToStopDrainManually` | `UnityEvent` | – |

## 内部型

- `statsInfo`（class）
