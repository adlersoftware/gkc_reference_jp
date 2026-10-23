# enemyHackPanel

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/enemyHackPanel.cs:5`

**概要**: 敵デバイス用のハッキングパネル。ハックの開始・停止を`hackTerminal`へ渡し、成功/失敗のイベントを発火する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hack Panel | `hackPanel` | `GameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Device | `usingDevice` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hack Terinal Manager | `hackTerinalManager` | `hackTerminal` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Hack Function | `startHackFunction` | `UnityEvent` | new UnityEvent () | – |
| Correct Hackedly Function | `correctHackedlyFunction` | `UnityEvent` | new UnityEvent () | – |
| Incorrectly Hacked Function | `incorrectlyHackedFunction` | `UnityEvent` | new UnityEvent () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateHackPanel(bool state)` | `usingDevice`を設定し、開始時は`startHackFunction`と`activeHack`、停止時は`stopHacking`を実行する。 |
| `setCorrectlyHackedState()` | `setHackResult(true)`を呼ぶだけ。 |
| `setIncorrectlyHackedState()` | `setHackResult(false)`を呼ぶだけ。 |
| `setHackResult(bool state)` | `state`に応じて成功または失敗の`UnityEvent`を発火するだけ。 |
| `disablePanelHack()` | 1秒待ってから`moveHackTerminal(false)`でパネルを閉じるコルーチンを開始する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `startHackFunction` | `UnityEvent` | – |
| `correctHackedlyFunction` | `UnityEvent` | – |
| `incorrectlyHackedFunction` | `UnityEvent` | – |
