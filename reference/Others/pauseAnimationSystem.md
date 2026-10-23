# pauseAnimationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/pauseAnimationSystem.cs:5`

**概要**: 人型ボーンのTransformをスナップショットで固定し、アニメーションを止めたように見せる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Animation Enabled | `pauseAnimationEnabled` | `bool` | true | – |
| Pause Animator State Instead Of Reduce Frames | `pauseAnimatorStateInsteadOfReduceFrames` | `bool` | – | – |
| Number Of Frames | `numberOfFrames` | `int` | 1 | Range (1, 60) |
| Pause Animation Active | `pauseAnimationActive` | `bool` | – | – |

### Transform List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Store Transform List On Start | `storeTransformListOnStart` | `bool` | – | – |
| Transform List | `transformList` | `List<Transform>` | new List<Transform> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Transform List Stored | `transformListStored` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Animator | `animator` | `Animator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPauseAnimationActiveState(bool state)` | `pauseAnimationEnabled`が`false`の時の有効化は無視し、それ以外は`pauseAnimationActive`を`state`にする。 |
| `activatPauseAnimationXSeconds(float newDuration)` | 既存コルーチンを止めてから、`newDuration`秒だけ停止するコルーチンを開始する。 |
| `setNumberOfFrames(int newValue)` | `numberOfFrames`に`newValue`を代入するだけ。 |
| `storeCharacterBones()` | `animator`から主要ボーンを取得して`transformList`を作り直し、null要素を除去する。 |

## 内部型

- `Snapshot`（class）
