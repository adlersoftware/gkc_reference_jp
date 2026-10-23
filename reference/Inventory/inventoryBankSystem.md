# inventoryBankSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Inventory/inventoryBankSystem.cs:12`

**概要**: 銀行（ベンダー）在庫を保持し、開閉アニメ・効果音・メニュー表示を制御するコンポーネント。在庫リストの生成/追加/削除、ランダム排出、空イベント、外部のメインバンクへの委譲を担う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Open Bank Delay | `openBankDelay` | `float` | – | バンクを開いてからメニュー表示まで待つ秒数。 |
| Animation Name | `animationName` | `string` | – | 開閉時に再生する`Animation`のクリップ名。 |
| Open Sound | `openSound` | `AudioClip` | – | バンクを開く時に鳴らす`AudioClip`。 |
| Open Audio Element | `openAudioElement` | `AudioElement` | – | 開く音の再生設定（音量・ピッチ）を持つ要素。 |
| Close Sound | `closeSound` | `AudioClip` | – | バンクを閉じる時に鳴らす`AudioClip`。 |
| Close Audio Element | `closeAudioElement` | `AudioElement` | – | 閉じる音の再生設定（音量・ピッチ）を持つ要素。 |

### Attach To Transform Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attach To Transform Active | `attachToTransformActive` | `bool` | – | オンで起動時に指定の`Transform`へ親子付けする。 |
| Transform To Attach | `transformToAttach` | `Transform` | – | 親子付けする対象の`Transform`。 / 表示条件: `attachToTransformActive` がオンのとき |
| Local Offset | `localOffset` | `Vector3` | – | 親子付け時のローカル位置オフセット。 / 表示条件: `attachToTransformActive` がオンのとき |

### Vendor Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use As Vendor System | `useAsVendorSystem` | `bool` | – | オンでこのバンクを売買用ベンダーとして動かす。 |
| Use General Buy Price Multiplier | `useGeneralBuyPriceMultiplier` | `bool` | – | オンで全商品の買値を一律倍率で補正する。 / 表示条件: `useAsVendorSystem` がオンのとき |
| General Buy Price Multiplayer Percentage | `generalBuyPriceMultiplayerPercentage` | `float` | – | 購入価格に掛ける一律の倍率（1で等倍）。 / 表示条件: `useAsVendorSystem.boolValue && useGeneralBuyPriceMultiplier.boolValue` |
| Use General Sell Price Multiplier | `useGeneralSellPriceMultiplier` | `bool` | – | オンで全商品の売値を一律倍率で補正する。 / 表示条件: `useAsVendorSystem` がオンのとき |
| General Sell Price Multiplayer Percentage | `generalSellPriceMultiplayerPercentage` | `float` | – | 売却価格に掛ける一律の倍率（1で等倍）。 / 表示条件: `useAsVendorSystem.boolValue && useGeneralSellPriceMultiplier.boolValue` |
| Infinite Vendor Amount Available | `infiniteVendorAmountAvailable` | `bool` | – | オンでベンダー在庫を無限に購入可能にする。 / 表示条件: `useAsVendorSystem` がオンのとき |
| Position To Spawn Objects | `positionToSpawnObjects` | `Transform` | – | 購入品などを生成する位置の`Transform`。 / 表示条件: `useAsVendorSystem` がオンのとき |

### Custom Inventory Bank Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Inventory From This Bank | `useInventoryFromThisBank` | `bool` | – | オンでこのバンク専用の在庫リストを使う。 |

### Bank Inventory List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Max Inventory Bank Slots Amount | `useMaxInventoryBankSlotsAmount` | `bool` | – | オンでこのバンクの最大スロット数を制限する。 / 表示条件: `useInventoryFromThisBank` がオンのとき |
| Max Inventory Bank Slots Amount | `maxInventoryBankSlotsAmount` | `int` | – | このバンクに置ける最大スロット数。 / 表示条件: `useInventoryFromThisBank.boolValue && useMaxInventoryBankSlotsAmount.boolValue` |

### Empty Inventory Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Inventory Empty | `useEventOnInventoryEmpty` | `bool` | – | オンで在庫が空になった時にイベントを実行。 |
| Event On Inventory Empty | `eventOnInventoryEmpty` | `UnityEvent` | – | 在庫が空の時に呼ぶ`UnityEvent`。 / 表示条件: `useEventOnInventoryEmpty` がオンのとき |
| Repeat Event On Inventory Empty | `repeatEventOnInventoryEmpty` | `bool` | – | オンで空イベントを毎回繰り返し実行する。 / 表示条件: `useEventOnInventoryEmpty` がオンのとき |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Animation | `mainAnimation` | `Animation` | – | 開閉アニメを再生する`Animation`。 |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | 開閉音を鳴らす`AudioSource`。 |
| Main Inventory List Manager | `mainInventoryListManager` | `inventoryListManager` | – | アイテム定義を参照する`inventoryListManager`。 |
| Main Inventory Bank Manager | `mainInventoryBankManager` | `inventoryBankManager` | – | 在庫を共有する`inventoryBankManager`。 |
| Main Spawn Object | `mainSpawnObject` | `spawnObject` | – | 排出オブジェクトを生成する`spawnObject`。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `usingInventoryBank` | `bool` | – | – |
| `inventoryListManagerList` | `List<inventoryListElement>` | new List<inventoryListElement> () | – |
| `bankInventoryList` | `List<inventoryInfo>` | new List<inventoryInfo> () | – |
| `inventoryManagerListString` | `string[]` | – | – |
| `inventoryManagerStringInfoList` | `List<inventoryManagerStringInfo>` | new List<inventoryManagerStringInfo> () | – |
| `playerControllerManager` | `playerController` | – | – |
| `mainInventoryManagerName` | `string` | "Main Inventory Manager" | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `spawnRandomObjectFromInventoryBank()` | このバンクかメインバンクの在庫からランダムに1種選び、1個減らして`spawnObject`で生成する。 |
| `setUsingInventoryBankState(bool state)` | `usingInventoryBank`を設定し、閉じたときは在庫空イベントを確認する。 |
| `activateInventoryBank()` | 既存コルーチンを停止し、開閉アニメ・効果音・メニュー表示を行うコルーチンを開始する。 |
| `checkEventOnInventoryEmpty()` | 在庫が空で未発火（または繰り返し設定）なら`eventOnInventoryEmpty`を発火する。 |
| `playAnimation(bool playForward)` | 開閉方向に応じて再生速度と開始位置を設定し、初回は`Play`、以後は`CrossFade`する。 |
| `playSound(bool state)` | ピッチを補正し、開く/閉じる用の効果音を`AudioPlayer`で再生する。 |
| `setCurrentPlayer(GameObject player)` | プレイヤーの在庫・操作・デバイス・ベンダーUIの各コンポーネントを取得して保持する。 |
| `setInventoryFromInventoryListManager()` | `inventoryListManagerList`を元に`bankInventoryList`を複製生成し、ベンダー価格なども反映する。 |
| `getInventoryListManagerList()` | メインの`inventoryListManager`からカテゴリ/オブジェクト名の一覧を再構築して更新する。 |
| `setInventoryObjectListNames()` | `inventoryListManagerList`の各要素の`Name`を`inventoryObjectName`で上書きして更新する。 |
| `addNewInventoryObjectToInventoryListManagerList()` | `inventoryListManagerList`に空の新規要素を追加してエディタ更新する。 |
| `getPositionToSpawnObjects()` | `positionToSpawnObjects`を返すだけ。 |
| `getBankInventoryList()` | `bankInventoryList`を返すだけ。 |
| `getBankInventoryListFromFullBank()` | 設定に応じてこのバンクかメインの在庫リストを返し、取得できなければnullを返す。 |
| `addInventoryObjectByName(string objectName, int amountToAdd)` | 同名在庫があれば加算、無ければメインリストから複製して追加し、外部バンク時は委譲する。 |
| `getInventoryObjectAmountByName(string inventoryObjectName)` | 同名オブジェクトの合計数を返し、無ければ-1を返す（外部バンク時は委譲）。 |
| `removeObjectAmountFromInventory(string objectName, int amountToRemove)` | 同名在庫の数量を減らし、0以下ならリストから削除する（外部バンク時は委譲）。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーン更新でエディタ表示を更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnInventoryEmpty` | `UnityEvent` | – |

## 内部型

- `inventoryManagerStringInfo`（class）
