# infoPanelOnScreenSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Panel Info System/infoPanelOnScreenSystem.cs:5`

**概要**: トリガーに入ったプレイヤーへ表示する情報パネルの設定を持つコンポーネント。パネル名・テキスト・画像・位置を定義し、プレイヤー側の表示システムへ渡す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Info Panel Enabled | `infoPanelEnabled` | `bool` | true | – |
| Show Panel Info Only First Time | `showPanelInfoOnlyFirstTime` | `bool` | – | – |

### Panel Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tags To Check | `tagsToCheck` | `List<string>` | new List<string> () | – |
| Layermask To Check | `layermaskToCheck` | `LayerMask` | – | – |
| Object To Follow | `objectToFollow` | `Transform` | – | – |

### Name Text Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Panel Name Text | `usePanelNameText` | `bool` | – | – |
| Panel Name Text | `panelNameText` | `string` | – | – |

### Image Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Image On Panel | `setImageOnPanel` | `bool` | – | – |
| Image On Panel | `imageOnPanel` | `Texture` | – | – |

### Panel Type Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Panel Name | `panelName` | `string` | "Default" | – |
| Panel Name Explanation | `panelNameExplanation` | `string` | "There are 4 types so far, but you ca… | TextArea (3, 10) |

### Panel Text Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Panel On Screen Text | `panelOnScreenText` | `string` | – | TextArea (8, 15) |
| Included Action Name On Text | `includedActionNameOnText` | `string` | – | – |
| Explanation | `explanation` | `string` | "Write -ACTION NAME- in the field Pan… | TextArea (3, 10) |

### Panel Position Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Panel Offset | `panelOffset` | `Vector3` | – | – |
| Use Fixed Panel Position | `useFixedPanelPosition` | `bool` | – | – |
| Use Separated Transform For Every View | `useSeparatedTransformForEveryView` | `bool` | – | – |
| Transform For Third Person | `transformForThirdPerson` | `Transform` | – | – |
| Transform For First Person | `transformForFirstPerson` | `Transform` | – | – |
| Remove Device From Player List On Max Distance | `removeDeviceFromPlayerListOnMaxDistance` | `bool` | – | – |
| Max Distance To Remove Device From Player List | `maxDistanceToRemoveDeviceFromPlayerList` | `float` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.green | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.white | – |
| Gizmo Radius | `gizmoRadius` | `float` | 0.3f | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | トリガーの出入りでタグとレイヤーが一致すればプレイヤーリストを更新し、パネル表示を有効/無効にする。 |
| `disablePanelText()` | 見つかっている全プレイヤーのパネルを閉じ、`infoPanelEnabled`をfalseにしてGameObjectを無効化する。 |
| `enableOrdisablePanelInfoFromPlayer(GameObject playerToCheck, bool enablePanel)` | プレイヤーの`playerComponentsManager`からパネル管理を取得し、`enablePanel`に応じて表示か追従解除を呼ぶ。 |
| `disablePanelInfoFromAllPlayersRemotely()` | リスト内の全プレイヤーにパネル非表示を要求する(遠隔操作用)。 |
