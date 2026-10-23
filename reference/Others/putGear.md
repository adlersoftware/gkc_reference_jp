# putGear

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/putGear.cs:5`

**概要**: 歯車がレール上に落ちたかを判定し、持ち主から離して所定位置へはめる。

## インスペクター設定

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disposed | `disposed` | `bool` | false | – |
| Engaged | `engaged` | `bool` | false | – |

### Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Init Pos | `initPos` | `GameObject` | – | – |
| Final Pos | `finalPos` | `GameObject` | – | – |
| Parent | `parent` | `GameObject` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Gear Placed | `eventOnGearPlaced` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkToDropObjectOnRail()` | `gear`の`grabbedObjectState`を取得し、保持中なら`GKC_Utils.dropObject`で持ち主に落とさせる。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnGearPlaced` | `UnityEvent` | – |
