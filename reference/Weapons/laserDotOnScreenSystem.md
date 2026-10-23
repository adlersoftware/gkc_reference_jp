# laserDotOnScreenSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/Attachments/laserDotOnScreenSystem.cs:6`

**概要**: レーザーの着弾点を画面座標へ変換し、HUDのドットアイコンとして表示するシステム。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Laser Dot Enabled | `laserDotEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Laser Dot Active | `laserDotActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Laser Dot Icon | `laserDotIcon` | `GameObject` | – | – |
| Laser Dot Icon Rect Transform | `laserDotIconRectTransform` | `RectTransform` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Target On Screen | `targetOnScreen` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateLaserDotPosition(Vector3 hitPoint)` | `hitPoint`を画面座標へ変換し、画面内ならアイコンを配置して表示し、外なら隠す。 |
| `setLasetDotIconActiveState(bool state)` | 有効設定を確認して`laserDotActive`を設定し、必要ならカメラやキャンバス情報を取得してアイコン表示を反映する。 |
