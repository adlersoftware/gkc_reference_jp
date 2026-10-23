# doubleJumpAnimationTrigger

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/doubleJumpAnimationTrigger.cs:5`

**概要**: 通常ジャンプと二段ジャンプの際に、Animator のトリガーを送って専用アニメーションを再生するコンポーネント。状態に応じて再生可否を判定する。

## インスペクター設定

### Ground Jump Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ground Jump Animation Enabled | `groundJumpAnimationEnabled` | `bool` | – | – |
| Delay To Enter On Air State On Ground Jump | `delayToEnterOnAirStateOnGroundJump` | `float` | 0.3f | – |
| Ground Jump In Place Animation Trigger Name | `groundJumpInPlaceAnimationTriggerName` | `string` | "Ground Jump In Place" | – |
| Ground Jump Moving Animation Trigger Name | `groundJumpMovingAnimationTriggerName` | `string` | "Ground Jump Moving" | – |

### Double Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Double Jump Animation Enabled | `doubleJumpAnimationEnabled` | `bool` | true | – |
| Double Jump Animation Trigger Name | `doubleJumpAnimationTriggerName` | `string` | "Double Jump" | – |
| Head Track Can Look Pause Duration | `headTrackCanLookPauseDuration` | `float` | 0.5f | – |
| Use Min Wait To Use Animation After Double Jump | `useMinWaitToUseAnimationAfterDoubleJump` | `bool` | – | – |
| Min Wait To Use Animation After Double Jump | `minWaitToUseAnimationAfterDoubleJump` | `float` | 0.5f | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Ground Jump Animation Active | `ignoreGroundJumpAnimationActive` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Head Track | `mainHeadTrack` | `headTrack` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateGroundJumpAnimation()` | 無視フラグや無効時は何もせず、カスタムキャラや外部ジャンプなら中止し、移動中かどうかで移動/停止用トリガーを送る。 |
| `activateDoubleJumpAnimation()` | FBA・武器・カスタム・移動不可・調整中・再使用待ちなら中止し、頭追従を止めてトリガーを送る。 |
| `setIgnoreGroundJumpAnimationActiveState(bool state)` | `ignoreGroundJumpAnimationActive` を設定するだけ。 |
| `setGroundJumpAnimationEnabledState(bool state)` | `groundJumpAnimationEnabled` を設定するだけ。 |
| `setDoubleJumpAnimationEnabledState(bool state)` | `doubleJumpAnimationEnabled` を設定するだけ。 |
| `setGroundJumpAnimationEnabledStateFromEditor(bool state)` | 値を設定してから `updateComponent` を呼ぶ。 |
| `setDoubleJumpAnimationEnabledStateFromEditor(bool state)` | 値を設定してから `updateComponent` を呼ぶ。 |
