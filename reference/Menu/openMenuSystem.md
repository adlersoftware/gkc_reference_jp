# openMenuSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Menu/openMenuSystem.cs:5`

**概要**: メニューの開閉を遅延付きコルーチンで実行し、対象プレイヤーの`menuPause`へポーズ画面や入力の状態を反映する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Open Menu Enabled | `openMenuEnabled` | `bool` | – | – |
| Menu To Open Name | `menuToOpenName` | `string` | – | – |
| Open Pause Menu | `openPauseMenu` | `bool` | – | – |
| Open Menu Delay | `openMenuDelay` | `float` | – | – |
| Close Menu Delay | `closeMenuDelay` | `float` | – | – |
| Pause Escape Menu Key | `pauseEscapeMenuKey` | `bool` | true | – |
| Allow To Exit Menu With Title Menu Text Button | `allowToExitMenuWithTitleMenuTextButton` | `bool` | – | – |
| Menu Opened With Action System | `menuOpenedWithActionSystem` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Action Open Menu System | `useCustomActionOpenMenuSystem` | `bool` | – | – |
| Main Custom Action Open Menu System | `mainCustomActionOpenMenuSystem` | `customActionOpenMenuSystem` | – | – |

### Blur Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Blur Menu | `ignoreBlurMenu` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Menu Opened | `menuOpened` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Menu Pause | `mainMenuPause` | `menuPause` | – | – |
| Current Player | `currentPlayer` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `toggleOpenOrCloseMenu()` | `menuOpened`の反転状態で`openOrCloseMenu`を呼ぶだけ。 |
| `openMenu()` | `openOrCloseMenu(true)`を呼ぶだけ。 |
| `closeMenu()` | `openOrCloseMenu(false)`を呼ぶだけ。 |
| `closeMenuIfOpened()` | `menuOpened`が真なら`closeMenu`を呼ぶだけ。 |
| `openOrCloseMenu(bool state)` | 無効時や`mainMenuPause`未取得時は中断し、既存コルーチンを止めて開閉コルーチンを開始する。 |
| `stopOpenOrCloseMenuCoroutine()` | `menuCoroutine`があれば停止するだけ。 |
| `setCurrentPlayer(GameObject newPlayer)` | プレイヤーが変わったときだけ保持し、`getPauseManager`で参照を更新する。 |
| `getPauseManager()` | `currentPlayer`の`playerComponentsManager`から`menuPause`を取得する。 |
