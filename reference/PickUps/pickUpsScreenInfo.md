# pickUpsScreenInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `PickUps/pickUpsScreenInfo.cs:6`

**概要**: 拾得した物の名前と数を画面に積み上げ表示し、`durationTimerPerText`経過ごとに古い表示を`Destroy`して位置を詰める。アイコン付きの表示にも対応する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pick Up Screen Info Enabled | `pickUpScreenInfoEnabled` | `bool` | – | 拾ったアイテムの情報を画面に出すかの切替。 |
| Duration Timer Per Text | `durationTimerPerText` | `float` | – | 1件のテキストを表示し続ける秒数。 |
| Vertical Distance | `verticalDistance` | `float` | – | 新しい行を積むときの縦方向の間隔。 |
| Horizontal Offset | `horizontalOffset` | `float` | – | テキストの水平位置をずらす量。 |
| Adjust Text Size Delta | `adjustTextSizeDelta` | `bool` | true | 文字数に応じてテキスト幅を自動で広げる切替。 |
| Text Size Delta Offset Multiplier | `textSizeDeltaOffsetMultiplier` | `float` | -1 | 広げた幅に合わせて横位置を補正する倍率。 |

### Icon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Icons Enabled | `useIconsEnabled` | `bool` | – | アイテム名と一緒にアイコンも出すかの切替。 |
| Icon Height | `iconHeight` | `float` | – | アイコン付きの行でテキストをずらす高さ。 |
| Vertical Icon Offset | `verticalIconOffset` | `float` | – | アイコン付き行の次に積む縦オフセット。 |
| Horizontal Icon Offset | `horizontalIconOffset` | `float` | – | アイコンの水平位置をずらす量。 |

### Others Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Used By AI | `usedByAI` | `bool` | – | AI操作のキャラでは表示しないためのフラグ。 |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Text To Add From Editor | `textToAddFromEditor` | `string` | – | エディタから表示確認するためのダミー文字列。 |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pickups Info Parent | `pickupsInfoParent` | `Transform` | – | 生成したテキストを並べる親`Transform`。 |
| Original Icon | `originalIcon` | `GameObject` | – | 複製して使うアイコンの元プレハブ。 |
| Original Text | `originalText` | `GameObject` | – | 複製して使うテキストの元プレハブ。 |
| Original Text Rect Transform | `originalTextRectTransform` | `RectTransform` | – | 複製元テキストの`RectTransform`参照。 |
| Main Player Controller | `mainPlayerController` | `playerController` | – | メニュー表示中か問い合わせる`playerController`。 |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `recieveInfo(string info)` | `originalText`を複製して文字数に応じ幅と縦位置を調整し、`info`を表示して`textList`に積み、タイマーをリセットする。 |
| `recieveInfo(string info, Texture icon)` | `useIconsEnabled`でなければ1引数版へ委譲し、そうでなければテキストとアイコンを生成して`icon`を`RawImage`に貼る。 |
| `setPickUpScreenInfoEnabled(bool state)` | `pickUpScreenInfoEnabled`を設定するだけ。 |
| `setPickUpScreenInfoEnabledFromEditor(bool state)` | `pickUpScreenInfoEnabled`を設定した後、`GKC_Utils.updateComponent`で更新する。 |
| `setUsedByAIState(bool state)` | `usedByAI`を設定するだけ。 |
| `addTextFromEditor()` | エディタの`textToAddFromEditor`を引数に`recieveInfo`を呼ぶだけ。 |
| `addTextAndIconFromEditor()` | エディタの文字列と`null`アイコンで2引数の`recieveInfo`を呼ぶだけ。 |

## 内部型

- `pickupScreenInfo`（class）
