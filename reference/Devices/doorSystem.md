# doorSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/doorSystem.cs:7`

**概要**: 扉パネルの移動/回転/アニメーションによる開閉、施錠、効果音、開閉イベント、マップアイコンを処理する。プレイヤーのトリガーや射撃、ボタンから開閉を呼び出せる。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Movement Type | `movementType` | `doorMovementType` | – | 開閉の方式（平行移動・回転・アニメーション）。 |
| Animation Name | `animationName` | `string` | – | 開閉に使うAnimationのクリップ名。 / 表示条件: `movementType.enumValueIndex == 2` |
| Animation Speed | `animationSpeed` | `int` | 1 | アニメーションの再生速度倍率。 / 表示条件: `movementType.enumValueIndex == 2` |
| Rotate In Both Directions | `rotateInBothDirections` | `bool` | – | プレイヤーの位置に応じて回転方向を反転する。 / 表示条件: `movementType.enumValueIndex == 1` |
| Open Sound | `openSound` | `AudioClip` | – | 開くときに鳴らすオーディオクリップ。 |
| Open Sound Audio Element | `openSoundAudioElement` | `AudioElement` | – | 開く音の再生設定（音量やピッチ）。 |
| Close Sound | `closeSound` | `AudioClip` | – | 閉じるときに鳴らすオーディオクリップ。 |
| Close Sound Audio Element | `closeSoundAudioElement` | `AudioElement` | – | 閉じる音の音量やピッチの再生設定。 |
| Door Type Info | `doorTypeInfo` | `doorType` | – | 開閉の操作方法（トリガー・ボタンなど）。 |
| Door State | `doorState` | `doorCurrentState` | – | 起動時の開閉状態を指定する。 |
| Open Speed | `openSpeed` | `float` | – | パネルが移動・回転する速さ。 |
| Hologram | `hologram` | `GameObject` | – | ホログラム式で使うオブジェクト参照。 |
| Close Door On Trigger Exit | `closeDoorOnTriggerExit` | `bool` | true | プレイヤーがトリガーから出たら閉じる。 |
| Close After Time | `closeAfterTime` | `bool` | – | 開いてから自動で閉じるかどうか。 |
| Time To Close | `timeToClose` | `float` | – | 開いてから自動で閉じるまでの秒数。 / 表示条件: `closeAfterTime` がオンのとき |
| Set Map Icons On Door | `setMapIconsOnDoor` | `bool` | true | マップに鍵状態のアイコンを登録する。 |

### Locked Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Locked | `locked` | `bool` | – | 初期状態を施錠にしておく。 |
| Open Door When Unlocked | `openDoorWhenUnlocked` | `bool` | true | 解錠した瞬間にドアを開く。 / 表示条件: `locked` がオンのとき |
| Use Sound On Unlock | `useSoundOnUnlock` | `bool` | – | 解錠時に効果音を鳴らす。 / 表示条件: `locked` がオンのとき |
| Unlock Sound | `unlockSound` | `AudioClip` | – | 解錠時に鳴らすオーディオクリップ。 / 表示条件: `locked.boolValue && useSoundOnUnlock.boolValue` |
| Unlock Sound Audio Element | `unlockSoundAudioElement` | `AudioElement` | – | 解錠音の音量やピッチの再生設定。 / 表示条件: `locked.boolValue && useSoundOnUnlock.boolValue` |
| Unlock Audio Source | `unlockAudioSource` | `AudioSource` | – | 解錠音を鳴らすAudioSource。 / 表示条件: `locked.boolValue && useSoundOnUnlock.boolValue` |

### Open/Close Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Open And Close | `useEventOnOpenAndClose` | `bool` | – | 開閉時にイベントを呼ぶ。 |
| Open Event | `openEvent` | `UnityEvent` | – | 開いたときに実行するイベント。 / 表示条件: `useEventOnOpenAndClose` がオンのとき |
| Close Event | `closeEvent` | `UnityEvent` | – | 閉じたときに実行するイベント。 / 表示条件: `useEventOnOpenAndClose` がオンのとき |

### Lock/Unlock Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Unlock Door | `useEventOnUnlockDoor` | `bool` | – | 解錠時にイベントを呼ぶ。 |
| Even On Unlock Door | `evenOnUnlockDoor` | `UnityEvent` | – | 解錠時に実行するイベント。 / 表示条件: `useEventOnUnlockDoor` がオンのとき |
| Use Event On Lock Door | `useEventOnLockDoor` | `bool` | – | 施錠時にイベントを呼ぶ。 |
| Event On Lock Door | `eventOnLockDoor` | `UnityEvent` | – | 施錠時に実行するイベント。 / 表示条件: `useEventOnLockDoor` がオンのとき |

### Door Found Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Door Found | `useEventOnDoorFound` | `bool` | – | ドアを発見したときにイベントを呼ぶ。 |
| Event On Unlocked Door Found | `eventOnUnlockedDoorFound` | `UnityEvent` | – | 未施錠のドアを発見したときのイベント。 / 表示条件: `useEventOnDoorFound` がオンのとき |
| Event On Locked Door Found | `eventOnLockedDoorFound` | `UnityEvent` | – | 施錠済みのドアを発見したときのイベント。 / 表示条件: `useEventOnDoorFound` がオンのとき |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sound Source | `soundSource` | `AudioSource` | – | 開閉音を再生するAudioSource。 |
| Map Object Information Manager | `mapObjectInformationManager` | `mapObjectInformation` | – | マップ登録に使うコンポーネント。 |
| Main Animation | `mainAnimation` | `Animation` | – | 開閉に使うAnimationコンポーネント。 |
| Hologram Door Manager | `hologramDoorManager` | `hologramDoor` | – | ホログラム側の制御コンポーネント。 |
| Device String Action Manager | `deviceStringActionManager` | `deviceStringAction` | – | 開閉に合わせて操作名を切り替える部品。 |

### Gizmo Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューに移動先の目印を表示する。 / 表示条件: `!usesAnimation` |
| Gizmo Arrow Length | `gizmoArrowLength` | `float` | 1 | 回転方向を示す矢印の先端の長さ。 / 表示条件: `!usesAnimation && showGizmo.boolValue` |
| Gizmo Arrow Line Length | `gizmoArrowLineLength` | `float` | 2.5f | 回転方向を示す矢印の線の長さ。 / 表示条件: `!usesAnimation && showGizmo.boolValue` |
| Gizmo Arrow Angle | `gizmoArrowAngle` | `float` | 20 | 矢印の先端の開き角度（度）。 / 表示条件: `!usesAnimation && showGizmo.boolValue` |
| Gizmo Arrow Color | `gizmoArrowColor` | `Color` | Color.white | 回転方向を示す矢印の色。 / 表示条件: `!usesAnimation && showGizmo.boolValue` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `doorsInfo` | `List<singleDoorInfo>` | new List<singleDoorInfo> () | – |
| `tagListToOpen` | `List<string>` | new List<string> () | – |
| `currentPlayerTransform` | `Transform` | – | – |
| `moving` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setDoorState()` | 開閉完了時に `doorState` を確定し、`enter`/`exit` と `moving` をリセットする。 |
| `lockDoor()` | 既存コルーチンを止め、0.01 秒後に閉じて `locked` を立てるコルーチンを開始する。 |
| `unlockDoor()` | 0.01 秒後に `locked` を解除し、設定に応じ扉を開くかホログラムを解錠するコルーチンを開始する。 |
| `isDisableDoorOpenCloseActionActive()` | `disableDoorOpenCloseAction` の値を返すだけ。 |
| `setEnableDisableDoorOpenCloseActionValue(bool state)` | `disableDoorOpenCloseAction` を `state` に設定するだけ。 |
| `openOrCloseElevatorDoor()` | ホログラム扉ならその外部入力処理を、なければ `changeDoorsStateByButton` を呼ぶ。 |
| `changeDoorsStateByButton()` | 開閉禁止中や移動中は何もせず、開いていれば閉じ、閉じていれば開く。 |
| `openDoorsIfClosed()` | 移動中でなく閉じている場合のみ `openDoors` を呼ぶ。 |
| `closeDoorsIfOpened()` | 移動中でなく開いている場合のみ `closeDoors` を呼ぶ。 |
| `openDoors()` | 非ロック時に `enter` を立て、各扉を開位置/回転へ設定し、開く音と `openEvent` を実行する。 |
| `closeDoors()` | 非ロック時に `exit` を立て、各扉を元の位置/回転へ戻し、閉じる音と `closeEvent` を実行する。 |
| `playSound(AudioElement clipSound)` | `AudioPlayer.PlayOneShot` で `clipSound` を再生するだけ。 |
| `setDeviceStringActionState(bool state)` | `deviceStringAction` があれば `changeActionName(state)` を呼ぶだけ。 |
| `doorsShooted(GameObject projectile)` | 投射物なら射撃式扉の状態を見て、閉じていれば開き、開いていれば再開時刻を更新する。 |
| `checkIfTagCanOpen(string tagToCheck)` | `tagListToOpen` に `tagToCheck` が含まれるかを返すだけ。 |
| `doorIsMoving()` | `moving` を返すだけ。 |
| `playDoorAnimation(bool playForward)` | `mainAnimation` の `animationName` を `playForward` に応じ正/負の速度で再生する。 |
| `isDoorOpened()` | 開状態かつ移動中でないかを返すだけ。 |
| `isDoorClosed()` | 閉状態かつ移動中でないかを返すだけ。 |
| `isDoorOpening()` | 開状態で移動中かを返すだけ。 |
| `isDoorClosing()` | 閉状態で移動中かを返すだけ。 |
| `setReducedVelocity(float newValue)` | `openSpeed` を `newValue` に設定するだけ。 |
| `setNormalVelocity()` | `openSpeed` を保存済みの `originalOpenSpeed` に戻すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `openEvent` | `UnityEvent` | – |
| `closeEvent` | `UnityEvent` | – |
| `evenOnUnlockDoor` | `UnityEvent` | – |
| `eventOnLockDoor` | `UnityEvent` | – |
| `eventOnLockedDoorFound` | `UnityEvent` | – |
| `eventOnUnlockedDoorFound` | `UnityEvent` | – |

## 内部型

- `doorMovementType`（enum）
- `doorType`（enum）
- `doorCurrentState`（enum）
- `singleDoorInfo`（class）
