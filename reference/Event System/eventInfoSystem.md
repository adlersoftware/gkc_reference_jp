# eventInfoSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Event System/eventInfoSystem.cs:6`

**概要**: 複数の`UnityEvent`とリモートイベントを、要素ごとの遅延（累積待ち、または同時カウント）付きで順に実行する。実行はコルーチンで行い、途中停止もできる。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event Info Enabled | `eventInfoEnabled` | `bool` | true | オフにするとイベントリストの実行をすべて無効にする。 |
| Use Delay Enabled | `useDelayEnabled` | `bool` | true | オンにすると各イベントを`delayToActivate`の時間だけ待って実行する。 |
| Use Accumulative Delay | `useAccumulativeDelay` | `bool` | – | オンにすると各遅延を積み上げて順番にイベントを実行する。 / 表示条件: `useDelayEnabled` がオンのとき |
| Use Speed Multiplier | `useSpeedMultiplier` | `bool` | – | オンにすると各イベントの遅延を`speedMultiplier`で割って調整する。 |
| Speed Multiplier | `speedMultiplier` | `float` | – | 遅延時間を割る倍率。大きいほど待ち時間が短くなる。 / 表示条件: `useSpeedMultiplier` がオンのとき |
| Main Remote Event System | `mainRemoteEventSystem` | `remoteEventSystem` | – | `useRemoteEvent`指定のイベントを送る先のリモートイベントシステム。 |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Stop Coroutine If Active | `useEventOnStopCoroutineIfActive` | `bool` | – | オンにすると実行中のコルーチンを停止した時にイベントを実行する。 |
| Event On Stop Coroutine If Active | `eventOnStopCoroutineIfActive` | `UnityEvent` | – | コルーチン停止時に実行するイベント。 / 表示条件: `useEventOnStopCoroutineIfActive` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `eventInfoList` | `List<eventInfo>` | new List<eventInfo> () | – |
| `eventInProcess` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopCheckActionEventInfoList()` | 実行中のコルーチンを停止し、処理中だった場合は`eventOnStopCoroutineIfActive`を呼んでから`eventInProcess`を偽にする。 |
| `activateActionEventInfoList()` | 無効時は何もせず、遅延ありならコルーチンを開始、なしなら全要素の`eventToUse`とリモートイベントを即時実行する。 |
| `addNewEvent()` | `eventInfoList`に新しい`eventInfo`を追加し、`updateComponent`でシーン更新をかけるエディタ用関数。 |
| `setEventInfoEnabledState(bool state)` | `eventInfoEnabled`を設定するだけの薄いセッター。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`を呼んでシーン更新をマークするだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStopCoroutineIfActive` | `UnityEvent` | – |

## 内部型

- `eventInfo`（class）
