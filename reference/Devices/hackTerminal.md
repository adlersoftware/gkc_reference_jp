# hackTerminal

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/hackTerminal.cs:10`
- **属性**: `Serializable`

**概要**: 4方向アイコンの順番当てでデバイスをハッキングする端末。HUD表示、カメラ移動、制限時間、成功/失敗イベントを管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Reset After Incorrect Hack | `resetAfterIncorrectHack` | `bool` | – | – |
| Timer Speed | `timerSpeed` | `float` | 10 | – |
| Type Time | `typeTime` | `float` | – | – |
| Min Swipe Dist | `minSwipeDist` | `float` | 50 | – |
| Hacking Animation | `hackingAnimation` | `string` | – | – |
| Electronic Device Game Object | `electronicDeviceGameObject` | `GameObject` | – | – |
| Hack Terminal Movement Speed | `hackTerminalMovementSpeed` | `float` | 2 | – |
| Hack Terminal Target Transform | `hackTerminalTargetTransform` | `Transform` | – | – |
| Icons | `icons` | `Texture[]` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Correct Hackedly Function | `correctHackedlyFunction` | `UnityEvent` | new UnityEvent () | – |
| Incorrectly Hacked Function | `incorrectlyHackedFunction` | `UnityEvent` | new UnityEvent () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Panel | `usingPanel` | `bool` | – | – |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Components and UI Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hack Hud | `hackHud` | `GameObject` | – | – |
| Hack Text | `hackText` | `GameObject` | – | – |
| Content | `content` | `GameObject` | – | – |
| Object To Hack | `objectToHack` | `GameObject` | – | – |
| Back Ground | `backGround` | `Image` | – | – |
| Current Password Text | `currentPasswordText` | `Text` | – | – |
| Hacked Color | `hackedColor` | `Color` | – | – |
| Time Slider | `timeSlider` | `Slider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activeHack()` | 未使用かつ未ハック時にHUDとカメラを開き、ランダムな正解順を生成して入力受付を開始する。 |
| `disableHack(bool state)` | スライダーを戻して入力受付を止め、`state`なら1秒後にカメラを元位置へ戻す。 |
| `moveHackTerminal(bool state)` | 端末UIを、開時は`hackTerminalTargetTransform`、閉時は元位置へ補間移動するコルーチンを開始する。 |
| `incorretlyHacked()` | 失敗表示と失敗イベントを実行し、`resetAfterIncorrectHack`に応じてカメラ復帰を即時か遅延にする。 |
| `stopHacking()` | 失敗表示と失敗イベントの後、入力受付とカメラ移動を停止する。 |
| `hasMoveCameraToDevice()` | `moveCameraToDevice`を取得し、`hasSecondMoveCameraToDevice`を呼ぶ。 |
| `setCurrentPlayer()` | `electronicDevice`からプレイヤーを取得し、入力管理とカメラ管理へ設定する。 |
| `getCameraMovementManager()` | `moveCameraToDevice`が未取得なら`GetComponent`で取得して保持する。 |
| `setTextContent(string textContent)` | `currentPasswordText`へ`textContent`を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `correctHackedlyFunction` | `UnityEvent` | – |
| `incorrectlyHackedFunction` | `UnityEvent` | – |
