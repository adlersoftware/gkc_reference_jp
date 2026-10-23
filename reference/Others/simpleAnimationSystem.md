# simpleAnimationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleAnimationSystem.cs:5`

**概要**: レガシー`Animation`の指定クリップを前後どちらかへ再生し、開始・終了イベントを発火する簡易アニメーション制御コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Animation Name | `animationName` | `string` | – | – |
| Forward Speed | `forwardSpeed` | `float` | 1 | – |
| Backward Speed | `backwardSpeed` | `float` | 1 | – |
| Reset Animation On Enable | `resetAnimationOnEnable` | `bool` | – | – |
| Reset Animation On Disable | `resetAnimationOnDisable` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Play Animation | `playAnimation` | `bool` | – | – |
| Playing Animation | `playingAnimation` | `bool` | – | – |
| Main Animation Located | `mainAnimationLocated` | `bool` | – | – |
| Playing Animation Forward | `playingAnimationForward` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Animation | `mainAnimation` | `Animation` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Play Animation Forward | `useEventOnPlayAnimationForward` | `bool` | – | – |
| Event On Play Animation Forward | `eventOnPlayAnimationForward` | `UnityEvent` | – | – |
| Use Event On End Of Animation Forward | `useEventOnEndOfAnimationForward` | `bool` | – | – |
| Event On End Of Animation Forward | `eventOnEndOfAnimationForward` | `UnityEvent` | – | – |
| Use Event On Play Animation Backward | `useEventOnPlayAnimationBackward` | `bool` | – | – |
| Event On Play Animation Backward | `eventOnPlayAnimationBackward` | `UnityEvent` | – | – |
| Use Event On End Of Animation Backward | `useEventOnEndOfAnimationBackward` | `bool` | – | – |
| Event On End Of Animation Backward | `eventOnEndOfAnimationBackward` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `playForwardAnimation()` | `playAnimation`をtrueにし、速度を`forwardSpeed`にして前方向再生のイベントを呼ぶ。 |
| `playBackwardAnimation()` | 速度を`-backwardSpeed`にし、未再生なら終端から逆再生を始めてイベントを呼ぶ。 |
| `playForwardNewAnimation(string newName)` | `animationName`を`newName`に差し替えてから`playForwardAnimation`を呼ぶ。 |
| `playBackwardNewAnimation(string newName)` | `animationName`を`newName`に差し替えてから`playBackwardAnimation`を呼ぶ。 |
| `playAnimationForwardIfAlreadyInProcess()` | `playingAnimation`がtrueのときだけ`playForwardAnimation`を呼ぶ。 |
| `playAnimationBackwardIfAlreadyInProcess()` | `playingAnimation`がtrueのときだけ`playBackwardAnimation`を呼ぶ。 |
| `rewindAnimation()` | 逆再生を開始し、再生中フラグを戻して`playAnimation`をtrueにする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPlayAnimationForward` | `UnityEvent` | – |
| `eventOnEndOfAnimationForward` | `UnityEvent` | – |
| `eventOnPlayAnimationBackward` | `UnityEvent` | – |
| `eventOnEndOfAnimationBackward` | `UnityEvent` | – |
