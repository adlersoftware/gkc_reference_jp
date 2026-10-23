# footStep

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Foot Step/footStep.cs:6`

**概要**: 片足ごとの足音コンポーネントで、設定した音量範囲のランダム音量で足音を再生し、有効状態の切り替えや遅延切り替えを提供する。

**公式ドキュメント抜粋**（[Welcome](../../docs/index.md)）

> Welcome to the Game Kit Controller (GKC) Documentation. Changelog GKC is the most complete First/Third Person Controller solution on the Unity Asset Store with unique Gravity and Sci-Fi features!\ \ GKC is a powerful engine that allows you to create most types of games very easily. It comes with a third/first-person controller with seamless camera view switching. This can cover almost any genre: shooter, adventure, action, puzzles, fixed camera horror/thriller, storytelling, fast or slow-paced type, 2.5d, top-down, point & click, isometric... The list goes on!\ \ Save thousands of hours in development and focus on making your game. Designed with a large amount of mechanics seen in AAA games in mind, to be highly customizable with the ability to enable anything you need and disable anything you don't, and to be easily extendable with your own code.\ \ It is the perfect foundation for your…

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Foot Step Enabled | `footStepEnabled` | `bool` | true | – |
| Layer | `layer` | `LayerMask` | – | – |
| Foot Side | `footSide` | `footType` | – | – |
| Wait Time Between Walk Steps | `waitTimeBetweenWalkSteps` | `float` | 0.4f | – |
| Wait Time Betwenn Run Steps | `waitTimeBetwennRunSteps` | `float` | 0.1f | – |

### Component

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Foot Step Manager | `mainFootStepManager` | `footStepManager` | – | – |
| Audio Source | `audioSource` | `AudioSource` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setStepVolumeRange(Vector2 newVolumeRange)` | 再生音量の範囲`volumeRange`を設定するだけ。 |
| `setOriginalStepVolume()` | 音量範囲を`mainFootStepManager`の既定値`feetVolumeRangeClamps`に戻すだけ。 |
| `enableOrDisableFootStep(bool state)` | 足音の有効フラグ`footStepEnabled`を設定するだけ。 |
| `setFooStepStateWithDelay(bool state, float delayAmount)` | 既存の遅延コルーチンを止め、`delayAmount`秒後に`state`へ切り替えるコルーチンを開始する。 |

## 内部型

- `footType`（enum）
