# simpleRandomTextManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleRandomTextManager.cs:7`

**概要**: 登録したテキストからランダムまたはID指定で1つ選び、`Text`に表示する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Random Text Manager Enabled | `randomTextManagerEnabled` | `bool` | true | – |
| Random Text Info List | `randomTextInfoList` | `List<randomTextInfo>` | new List<randomTextInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Text Index Selected | `currentTextIndexSelected` | `int` | -1 | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Text | `mainText` | `Text` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setRandomText(int randomTextID)` | `randomTextID`が0以上ならID一致、-1以下ならランダムに項目を選び、前回と同じものを避けて`mainText`に表示する。 |

## 内部型

- `randomTextInfo`（class）
