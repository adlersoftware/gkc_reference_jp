# touchButtonListener

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`, `IPointerDownHandler`, `IPointerUpHandler`
- **ソース**: `Mobile/touchButtonListener.cs:8`
- **属性**: `System.Serializable`

**概要**: モバイル用タッチボタンの入力リスナー。押下・離上のフラグを管理し、設定時はアイコン色を変化させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Color On Press | `changeColorOnPress` | `bool` | – | – |
| Release Color | `releaseColor` | `Color` | – | – |
| Press Color | `pressColor` | `Color` | – | – |
| Color Change Speed | `colorChangeSpeed` | `float` | – | – |
| Use Current Color For Release | `useCurrentColorForRelease` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pressed Down | `pressedDown` | `bool` | false | – |
| Pressed Up | `pressedUp` | `bool` | false | – |
| Pressed | `pressed` | `bool` | – | – |
| Button Color Visible | `buttonColorVisible` | `bool` | true | – |
| Current Finger Id | `currentFingerId` | `int` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Button Icon | `buttonIcon` | `RawImage` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `OnPointerDown(PointerEventData eventData)` | `pressedDown`と`pressed`を立て、色変更とフラグ解除コルーチンを開始する。 |
| `checkTouchID()` | 現在のタッチを走査し、開始された指のIDを`currentFingerId`に保存する。 |
| `getCurrentFingerId()` | `currentFingerId`を返すだけ。 |
| `OnPointerUp(PointerEventData eventData)` | `pressedUp`を立てて`pressed`を下ろし、色を戻してフラグ解除コルーチンを開始する。 |
| `setButtonColorVisibleState(bool state)` | `buttonColorVisible`を設定し、アイコン色のアルファを表示・非表示に合わせる。 |
| `resetButtonState()` | 押下系フラグが立っていれば全て下ろし、必要ならアイコン色を戻す。 |
| `setButtonIconComponent()` | `RawImage`を`buttonIcon`として取得し、コンポーネントを更新する。 |
