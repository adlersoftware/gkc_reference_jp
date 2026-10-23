# playerIdleSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/playerIdleSystem.cs:6`

**概要**: 待機（idle）アニメーションの開始/停止と、再生するidleのインデックスを管理するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Idle Enabled At Start | `idleEnabledAtStart` | `bool` | true | – |
| Idle Active | `idleActive` | `bool` | – | – |
| Current Idle Info Index | `currentIdleInfoIndex` | `int` | – | – |
| Play Random Idle | `playRandomIdle` | `bool` | – | – |

### Idle Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Idle Info List | `idleInfoList` | `List<idleInfo>` | new List<idleInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Start Idle | `eventOnStartIdle` | `UnityEvent` | – | – |
| Event On Stop Idle | `eventOnStopIdle` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateIdle()` | `playIdle()` を呼ぶだけ。 |
| `deactivateIdle()` | `stopIdle()` を呼ぶだけ。 |
| `setIdleIndex(int newValue)` | `currentIdleInfoIndex` を設定し、リスト末尾を超えたら 0 に戻す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartIdle` | `UnityEvent` | – |
| `eventOnStopIdle` | `UnityEvent` | – |

## 内部型

- `idleInfo`（class）
