# accessTerminal

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/accessTerminal.cs:11`

**概要**: コード入力式の端末で、画面上のキーやキーボードから桁を入力して `code` と照合する。解錠時は `unlockObject` を呼び、表示色・テキスト・イベント・ハックパネルを切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Code | `code` | `string` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Unlocked Color | `unlockedColor` | `Color` | – | – |
| Locked Color | `lockedColor` | `Color` | – | – |
| Allow To Use Keyboard | `allowToUseKeyboard` | `bool` | – | – |
| Use Move Camera To Device | `useMoveCameraToDevice` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Unlock This Terminal | `unlockThisTerminal` | `bool` | – | – |
| Disable Code Screen After Unlock | `disableCodeScreenAfterUnlock` | `bool` | – | – |
| Wait Delay After Unlock | `waitDelayAfterUnlock` | `float` | – | – |
| Set Locked State Text Enabled | `setLockedStateTextEnabled` | `bool` | true | – |
| Allow To Toggle Locked State | `allowToToggleLockedState` | `bool` | – | – |

### Text Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Background Panel Name | `backgroundPanelName` | `string` | "terminal" | – |
| Unlocked State String | `unlockedStateString` | `string` | "Unlocked" | – |
| Locked State String | `lockedStateString` | `string` | "Locked" | – |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Wrong Pass Sound | `wrongPassSound` | `AudioClip` | – | – |
| Wrong Pass Audio Element | `wrongPassAudioElement` | `AudioElement` | – | – |
| Corret Pass Sound | `corretPassSound` | `AudioClip` | – | – |
| Corret Pass Audio Element | `corretPassAudioElement` | `AudioElement` | – | – |
| Key Press Sound | `keyPressSound` | `AudioClip` | – | – |
| Key Press Audio Element | `keyPressAudioElement` | `AudioElement` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Device Unlocked | `useEventOnDeviceUnlocked` | `bool` | – | – |
| Event On Device Unlocked | `eventOnDeviceUnlocked` | `UnityEvent` | – | – |
| Use Event On Device Locked | `useEventOnDeviceLocked` | `bool` | – | – |
| Event On Device Locked | `eventOnDeviceLocked` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Device | `usingDevice` | `bool` | – | – |
| Unlocked | `unlocked` | `bool` | – | – |
| Locked | `locked` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pointer | `pointer` | `RectTransform` | – | – |
| Keys | `keys` | `GameObject` | – | – |
| Currect Code | `currectCode` | `Text` | – | – |
| State Text | `stateText` | `Text` | – | – |
| Wall Paper | `wallPaper` | `Image` | – | – |
| Hack Panel | `hackPanel` | `GameObject` | – | – |
| Hack Active Button | `hackActiveButton` | `GameObject` | – | – |
| Code Screen | `codeScreen` | `GameObject` | – | – |
| Unlocked Screen | `unlockedScreen` | `GameObject` | – | – |
| Audio Source | `audioSource` | `AudioSource` | – | – |
| Device Manager | `deviceManager` | `electronicDevice` | – | – |
| Hack Terminal Manager | `hackTerminalManager` | `hackTerminal` | – | – |
| Main Game Manager | `mainGameManager` | `gameManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `mainCoroutine` を停止し、端末の入力監視を止める。 |
| `pressButtonOnScreen()` | `checkPressedButton` を true にし、次回更新で画面ボタン押下を処理させる。 |
| `activateTerminal()` | 使用状態を反転して入力監視を再起動し、開始時は操作プレイヤー取得、終了時はハッキングを止める。 |
| `enableTerminal()` | 強制的に使用中にして入力監視を開始し、キー初期化と操作プレイヤー取得を行う。 |
| `disableTerminal()` | 使用状態を解除して入力監視を止め、ハッキング中なら中止する。 |
| `getCurrentUser()` | 現在の操作プレイヤーを取得し、そのメインカメラを `mainCamera` に保持する。 |
| `checkNumber(string numberString)` | 入力桁を画面へ追加し、規定桁数で `code` と照合して解錠／施錠、不一致なら音とリセットを行う。 |
| `setLockedState(bool state)` | 解錠／施錠の状態・表示・色を切り替え、必要なら `unlockObject`、ハックパネル停止、画面切替、イベントを行う。 |
| `setLockState(Scrollbar info)` | スクロールバー値が 0 なら `lockObject`、1 なら `unlockObject` を呼ぶだけ。 |
| `showPasswordOnHackPanel()` | ハックパネルに `code` を表示するだけ。 |
| `unlockAccessTerminal()` | 入力欄を空にし桁数を 1 つ手前から `code` を一括入力して、照合による解錠を成立させる。 |
| `activateHackButton()` | `hackActiveButton` があればアクティブにするだけ。 |
| `setNewCode(string newCode)` | `code` を差し替え、表示桁数と 0 詰めの初期表示を更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnDeviceUnlocked` | `UnityEvent` | – |
| `eventOnDeviceLocked` | `UnityEvent` | – |
