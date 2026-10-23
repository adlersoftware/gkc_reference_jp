# simpleSwitch

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/simpleSwitch.cs:6`

**概要**: 単発/双方向のスイッチ。アニメと効果音を再生し、`UnityEvent`または`SendMessage`で対象オブジェクトを操作する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Button Enabled | `buttonEnabled` | `bool` | true | オンでこのスイッチを操作できる状態にする。 |
| Use Single Switch | `useSingleSwitch` | `bool` | true | オンで押すたび単発動作、オフでオンとオフを切り替える。 |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Button Uses Animation | `buttonUsesAnimation` | `bool` | true | オンで押下時に`buttonAnimation`を再生する。 |
| Switch Animation Name | `switchAnimationName` | `string` | "simpleSwitch" | 再生するスイッチアニメーションのクリップ名。 / 表示条件: `buttonUsesAnimation` がオンのとき |
| Animation Speed | `animationSpeed` | `float` | 1 | アニメーションの再生速度倍率。負値で逆再生になる。 / 表示条件: `buttonUsesAnimation` がオンのとき |
| Not Usable While Animation Is Playing | `notUsableWhileAnimationIsPlaying` | `bool` | true | オンでアニメーション再生中は再操作できなくする。 / 表示条件: `buttonUsesAnimation` がオンのとき |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Press Sound | `pressSound` | `AudioClip` | – | 押した時に再生する`AudioClip`。 |
| Press Audio Element | `pressAudioElement` | `AudioElement` | – | 効果音の音量や音源を設定する`AudioElement`。 |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Current User | `sendCurrentUser` | `bool` | – | オンで操作したプレイヤーを`setCurrentUser`で通知する。 |
| Use Unity Events | `useUnityEvents` | `bool` | true | オンでUnityEventを実行、オフでSendMessageを使う。 |
| Object To Call Functions | `objectToCallFunctions` | `UnityEvent` | new UnityEvent () | 単発スイッチ時に実行するUnityEvent。 / 表示条件: `useUnityEvents.boolValue && useSingleSwitch.boolValue` |
| Switch Turned On | `switchTurnedOn` | `bool` | – | スイッチがオン状態かどうかの現在値。初期状態も指定。 / 表示条件: `useUnityEvents` がオンのとき |
| Turn On Event | `turnOnEvent` | `UnityEvent` | new UnityEvent () | オンに切り替えた時に実行するUnityEvent。 / 表示条件: `useUnityEvents` がオンのとき |
| Turn Off Event | `turnOffEvent` | `UnityEvent` | new UnityEvent () | オフに切り替えた時に実行するUnityEvent。 / 表示条件: `useUnityEvents` がオンのとき |
| Object To Active | `objectToActive` | `GameObject` | – | UnityEventを使わずSendMessageを送る対象オブジェクト。 |
| Active Function Name | `activeFunctionName` | `string` | – | `objectToActive`へ送る関数の名前。 |
| Send This Button | `sendThisButton` | `bool` | – | オンで送信時にこのスイッチ自身を引数として渡す。 |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Audio Source | `audioSource` | `AudioSource` | – | 効果音を再生する`AudioSource`。未設定なら自動取得。 |
| Button Animation | `buttonAnimation` | `Animation` | – | スイッチ動作に使う`Animation`コンポーネント。 |
| Device String Action Manager | `deviceStringActionManager` | `deviceStringAction` | – | ボタンの表示名を切り替える`deviceStringAction`。 |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentPlayer(GameObject newPlayer)` | `currentPlayer`を保持するだけ。 |
| `setCurrentUser(GameObject newPlayer)` | `currentPlayer`を保持するだけ。 |
| `turnSwitchOff()` | `switchTurnedOn`が`true`のときだけ`activateDevice`を呼ぶ。 |
| `turnSwitchOn()` | `switchTurnedOn`が`false`のときだけ`activateDevice`を呼ぶ。 |
| `activateDevice()` | 有効/アニメ再生可否を判定し、単発/双方向のアニメと効果音、ユーザー通知、イベントまたは関数呼び出しを行う。 |
| `setButtonEnabledState(bool state)` | `buttonEnabled`を設定するだけ。 |
| `triggerButtonEventFromEditor()` | `activateDevice`を呼ぶだけ。 |
| `playSingleAnimation()` | `animationSpeed`でアニメを再生し、押下音を鳴らす。 |
| `playDualAnimation(bool playForward)` | `playForward`に応じアニメの速度と開始位置を変えて再生し、押下音を鳴らす。 |
| `setDeviceStringActionState(bool state)` | `deviceStringAction`があれば、`changeActionName`で表示アクション名を切り替える。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `objectToCallFunctions` | `UnityEvent` | – |
| `turnOnEvent` | `UnityEvent` | – |
| `turnOffEvent` | `UnityEvent` | – |
