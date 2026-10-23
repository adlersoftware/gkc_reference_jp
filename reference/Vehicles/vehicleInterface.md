# vehicleInterface

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/vehicleInterface.cs:7`

**概要**: 車両のUIキャンバスとUI要素リストを管理し、押された要素に応じて値送信イベントを発火するインターフェース。パネルの移動・回転操作も扱う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Interface Can Be Enabled | `interfaceCanBeEnabled` | `bool` | true | インターフェース全体の有効フラグ。オフなら表示も操作も不可。 |
| Interface Enabled | `interfaceEnabled` | `bool` | – | インターフェースが現在表示中かどうかの実行時状態。 |
| Vehicle | `vehicle` | `GameObject` | – | このインターフェースが紐づく車両のGameObject参照。 |
| Interface Canvas | `interfaceCanvas` | `GameObject` | – | 表示を切り替えるインターフェースのCanvas。 |

### Interface Panel Info List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Interface Panel Info List | `useInterfacePanelInfoList` | `bool` | – | パネルの移動・回転操作を有効にするトグル。 |
| HUD Manager | `HUDManager` | `vehicleHUDManager` | – | 車両の`vehicleHUDManager`への参照。運転者の取得に使う。 / 表示条件: `useInterfacePanelInfoList` がオンのとき |
| Interface Panel Parent | `interfacePanelParent` | `RectTransform` | – | 移動・回転中のパネルを一時的に親子付けするRectTransform。 / 表示条件: `useInterfacePanelInfoList` がオンのとき |
| Move Panel Speed | `movePanelSpeed` | `float` | 2 | マウス入力に対するパネルの移動速度。 / 表示条件: `useInterfacePanelInfoList` がオンのとき |
| Rotate Panel Speed | `rotatePanelSpeed` | `float` | 2 | マウス入力に対するパネルの回転速度。 / 表示条件: `useInterfacePanelInfoList` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `interfaceElementList` | `List<interfaceElement>` | new List<interfaceElement> () | – |
| `interfacePanelInfoList` | `List<interfacePanelInfo>` | new List<interfacePanelInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setInterfaceCanBeEnabledState(bool state)` | `interfaceCanBeEnabled`を設定するだけ。 |
| `enableOrDisableInterface(bool state)` | 有効化可否が真なら状態を設定してキャンバスを切り替え、無効化時は車両オフ用要素を初期値に戻す。 |
| `checkPressedUIElememt(GameObject uiElement)` | 一致するUI要素の設定に従い、スライダー値やトグル/ボタンのboolを読んでテキストと対応イベントへ反映する。 |
| `setMoveInterfacePanelPressed(RectTransform panelToCheck)` | パネル情報の押下判定をしたうえで`movingPanel`を反転する。 |
| `setRotateInterfacePanelPressed(RectTransform panelToCheck)` | パネル情報の押下判定をしたうえで`rotatingPanel`を反転する。 |
| `checkInterfacePanelInfoPressed(RectTransform panelToCheck)` | 対象パネルなら選択状態を反転し、選択時は親に付け替えてドライバーの入力管理を取得、解除時は元の親へ戻す。 |
| `resetInterfacePanelInfoPressed(RectTransform panelToCheck)` | 対象パネルのローカル位置と回転を記録済みの初期値に戻す。 |
| `setInterfaceCanvasState(bool state)` | 状態が異なるときだけ`interfaceCanvas`のアクティブを切り替える。 |
| `addInterfaceElement()` | 名前「New Element」の要素を`interfaceElementList`に追加してシーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とダーティシーン更新を呼ぶだけ。 |

## 内部型

- `interfaceElement`（class）
- `interfacePanelInfo`（class）
