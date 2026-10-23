# playerInfoPanelOnScreenSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Panel Info System/playerInfoPanelOnScreenSystem.cs:7`

**概要**: プレイヤーごとに画面上の情報パネルを管理し、対象オブジェクトに追従させてテキストや画像を表示する。画面座標変換・フェード・距離による自動解除も行う。

**公式ドキュメント抜粋**（[Player Info Panel On Screen System](../../docs/player-controller-components/essential-components/player-info-panel-on-screen-system.md)）

> Used to show panels in the screen for text, allowing to configure any type of text panel, with different size, font, design, etc… and be activated by the prefabs called Info Panel, showing info in-game on certain parts of the scene without pausing the game, in an easy way.

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Panel On Screen Enabled | `panelOnScreenEnabled` | `bool` | true | – |
| Use Fade Panel | `useFadePanel` | `bool` | – | – |
| Fade On Panel Speed | `fadeOnPanelSpeed` | `float` | – | – |
| Fade Off Panel Speed | `fadeOffPanelSpeed` | `float` | – | – |
| Action Name Field | `actionNameField` | `string` | "-ACTION NAME-" | – |

### Panel GameObject List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Panel Game Object List | `panelGameObjectList` | `List<infoPanel>` | new List<infoPanel> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Panel Transform Found List | `panelTransformFoundList` | `List<Transform>` | new List<Transform> () | – |
| Info Panel On Screen System List | `infoPanelOnScreenSystemList` | `List<infoPanelOnScreenSystem>` | new List<infoPanelOnScreenSystem> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Player Input | `playerInput` | `playerInputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`があれば停止するだけで、表示状態は変えない。 |
| `calculatePanelPosition()` | 追従対象の位置に`panelOffset`を加えて画面座標へ変換し、`targetOnScreen`判定と距離超過時の解除を行う。 |
| `getNewPanelInfo(infoPanelOnScreenSystem newInfoPanelOnScreenSystem)` | パネル設定を受け取り、テキスト・画像・位置を更新して表示し、更新コルーチンを開始する。 |
| `disablePanelInfo(Transform newObjectToFollow)` | 指定対象を追従リストから外し、残りが無ければフェードアウトか非表示にして更新を止める。 |
| `enableOrDisablePanel(bool state)` | パネルのGameObjectのactive状態を`state`に合わせるだけ。 |
| `fadePanel(infoPanel newInfoPanel, bool fadingPanel)` | 既存のフェードを停止し、`fadingPanel`がtrueならフェードアウト、falseならフェードインを開始する。 |

## 内部型

- `infoPanel`（class）
