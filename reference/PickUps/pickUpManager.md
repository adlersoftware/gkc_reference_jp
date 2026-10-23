# pickUpManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `PickUps/pickUpManager.cs:6`

**概要**: 拾得物のHUDアイコン登録を一元管理するシングルトン。種類名からテクスチャとプレハブを解決し、IDで全プレイヤーの表示を追加・削除・一時停止する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Icons Active | `showIconsActive` | `bool` | true | ONの間だけピックアップアイコンの管理を行う。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `mainPickUpList` | `List<pickUpElementInfo>` | new List<pickUpElementInfo> () | – |
| `pickUpIconList` | `List<pickUpIconInfo>` | new List<pickUpIconInfo> () | – |
| `playerPickupIconManagerList` | `List<playerPickupIconManager>` | new List<playerPickupIconManager> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 自身を`Instance`として登録するシングルトン初期化で、既に別インスタンスがあれば`Destroy`する。 |
| `addNewPlayer(playerPickupIconManager newPlayer)` | `showIconsActive`なら`newPlayer`をリストに追加し、既存の全アイコンをそのプレイヤーにも登録する。 |
| `setPickUpIcon(GameObject target, string pickupIconGeneralName, string pickupIconName)` | `mainPickUpList`から種類名と個別名でアイコンとプレハブを引き、ID付きで登録して全プレイヤーへ通知し`currentID`を進める。 |
| `removeTarget(GameObject target)` | `target`に一致する登録を探し、そのIDとインデックスで`removeAtTarget`を呼ぶ。 |
| `removeAtTarget(int objectID, int objectIndex)` | 各プレイヤーへ`objectID`のアイコン削除を指示し、`objectIndex`の登録をリストから外す。 |
| `removeElementFromPickupListCalledByPlayer(int objectID)` | `objectID`に一致する要素を`pickUpIconList`から削除する。 |
| `setPauseState(bool state, GameObject iconObject)` | `iconObject`の登録に`paused`を立て、同じインデックスで各プレイヤーのアイコンも一時停止/再開する。 |
| `setNamesConfigured(int currentIndex)` | 指定要素の各`pickUpTypeList`の`Name`を、対応する`pickUpObject`の名前で更新する。 |
| `addNewPickup()` | `mainPickUpList`に`New Pickup Type`という要素を追加し、`udpateComponent()`を呼ぶ。 |
| `addNewPickupToList(int index)` | 指定要素の`pickUpTypeList`に`New Pickup`を追加して`udpateComponent()`を呼ぶ。 |
| `udpateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`で更新するだけ。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |
