# showMessageOnHUDSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/showMessageOnHUDSystem.cs:8`

**概要**: HUD上のメッセージパネルを名前やインデックスで表示・非表示し、表示時間や入力アクション名の置換、ローカライズも扱うコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Message Info List | `messageInfoList` | `List<messageInfo>` | new List<messageInfo> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Action Name Field | `actionNameField` | `string` | "-ACTION NAME-" | – |
| Panel For Custom Message Name | `panelForCustomMessageName` | `string` | "Custom Message" | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Input | `playerInput` | `playerInputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMessagePanelNameManually(string messageName)` | `currentPanelNameManually`を`messageName`にするだけ。 |
| `showMessagePanelManually(string messageContent)` | 手動指定名のパネルを探し、表示中でなければ`messageContent`をカスタム文言として表示する。 |
| `showCustomMessagePanel(string messageContent)` | `panelForCustomMessageName`のパネルに`messageContent`をカスタム文言として表示する。 |
| `showMessagePanel(string messageName)` | `messageName`のパネルが未表示（または再表示可）なら`showObjectMessage`で表示する。 |
| `hideMessagePanel(string messageName)` | 該当パネルのコルーチンを止め、GameObjectを非表示にして`showingMessage`をfalseにする。 |
| `showObjectMessage(int messageIndex)` | 既存のコルーチンを止め、`messageIndex`番のパネル表示コルーチンを開始する。 |

## 内部型

- `messageInfo`（class）
