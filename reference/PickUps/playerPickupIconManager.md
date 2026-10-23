# playerPickupIconManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `PickUps/playerPickupIconManager.cs:6`

**概要**: プレイヤーごとに拾得物アイコンをHUDへ生成し、`pickUpIconList`で追跡する。表示/非表示、一時停止、画面サイズ更新、`pickUpManager`とのID同期を担う。

**公式ドキュメント抜粋**（[Player Pickup Icon Manager](../../docs/character-level-components/character/player-pickup-icon-manager.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Icons Active | `showIconsActive` | `bool` | true | – |
| Show Icons Paused | `showIconsPaused` | `bool` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Layer For First Person | `layerForFirstPerson` | `LayerMask` | – | – |
| Layer For FBA | `layerForFBA` | `LayerMask` | – | – |
| Check Icontype | `checkIcontype` | `checkIconType` | – | – |
| Max Distance Icon Enabled | `maxDistanceIconEnabled` | `float` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Manager Name | `mainManagerName` | `string` | "Pickup Manager" | – |
| Main Panel Name | `mainPanelName` | `string` | "Pickup Objects Icons" | – |
| Use Canvas Group On Icons | `useCanvasGroupOnIcons` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pick Up Icon List | `pickUpIconList` | `List<pickUpIconInfo>` | new List<pickUpIconInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pick Up Icon Object | `pickUpIconObject` | `GameObject` | – | – |
| Pickup Object Icon Parent | `pickupObjectIconParent` | `Transform` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Pickup Manager | `mainPickupManager` | `pickUpManager` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableIcon(bool state, int index)` | `useCanvasGroupOnIcons`なら`alpha`を1/0に、そうでなければ`iconObject`をアクティブ切替する。 |
| `setPickUpIcon(GameObject target, Texture targetTexture, int objectID, GameObject iconPrefab)` | HUDの親を確保してアイコンを生成し、`target`・ID・テクスチャを設定してリストに追加し、停止中なら非表示にする。 |
| `removeAtTarget(int index)` | `index`のアイコンを`Destroy`し、`pickUpManager`へID削除を通知してリストから外す。範囲外なら警告を表示する。 |
| `removeAtTargetByID(int objectID)` | `objectID`に一致するアイコンを`Destroy`してリストから削除する。 |
| `setPauseState(bool state, int index)` | `index`が範囲内ならその要素の`paused`を設定するだけ。 |
| `pauseOrResumeShowIcons(bool state)` | `showIconsPaused`を設定し、アイコン親オブジェクトのアクティブ状態を反転させる。 |
| `pauseOrResumeShowIconsFromEditor(bool state)` | `pauseOrResumeShowIcons`を呼んだ後に`updateComponent()`でシーンを更新する。 |
| `setShowIconsActiveState(bool state)` | `showIconsActive`を設定するだけ。 |
| `updateScreenValues()` | `screenWidth`と`screenHeight`を現在の`Screen`サイズで更新する。 |
| `setShowIconsActiveStateFromEditor(bool state)` | `showIconsActive`を設定した後に`updateComponent()`でシーンを更新する。 |

## 内部型

- `checkIconType`（enum）
