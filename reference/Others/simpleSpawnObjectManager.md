# simpleSpawnObjectManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleSpawnObjectManager.cs:5`

**概要**: カテゴリ別のスポーン情報リストを持ち、名前指定でオブジェクトを出現させたり、有効状態やリモートイベントを切り替える管理コンポーネント。

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Spawn Manager Enabled | `spawnManagerEnabled` | `bool` | true | – |
| Default Spawn Category | `defaultSpawnCategory` | `string` | – | – |

### Spawn List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Simple Spawn Info Element List | `simpleSpawnInfoElementList` | `List<simpleSpawnInfoElement>` | new List<simpleSpawnInfoElement> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Spawn Info Element List Selected | `spawnInfoElementListSelected` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Spawn Object | `mainSpawnObject` | `spawnObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentSpawnCategoryByName(string elementListName)` | `elementListName`のカテゴリを選択し、無ければ`defaultSpawnCategory`で選び直す。 |
| `activateSpawnObjectByName(string objectName)` | 現在カテゴリ内で`objectName`を探し、有効ならその設定でオブジェクトをスポーンさせる。 |
| `setSpawnObjectEnabledStateByName(string objectName)` | `objectName`の`spawnObjectEnabled`をtrueにする。 |
| `setSpawnObjectDisabledStateByName(string objectName)` | `objectName`の`spawnObjectEnabled`をfalseにする。 |
| `setSpawnObjectEnabledStateByName(bool state, string objectName)` | カテゴリを確保した上で`objectName`の`spawnObjectEnabled`を`state`にする。 |
| `setSpawnManagerEnabledState(bool state)` | `spawnManagerEnabled`を`state`にするだけ。 |
| `enableRemoteEventState(string remoteEventName)` | `spawnName;eventName`形式の名前を分解し、該当オブジェクトのリモートイベントを有効にする。 |
| `disableRemoteEventState(string remoteEventName)` | `spawnName;eventName`形式の名前を分解し、該当オブジェクトのリモートイベントを無効にする。 |
| `enableAllRemoteEventStates(string spawnInfoNameToSearch)` | `spawnInfoNameToSearch`の`customSpawnObject`の全リモートイベントを有効にする。 |
| `disableAllRemoteEventStates(string spawnInfoNameToSearch)` | `spawnInfoNameToSearch`の`customSpawnObject`の全リモートイベントを無効にする。 |

## 内部型

- `simpleSpawnInfoElement`（class）
- `simpleSpawnInfo`（class）
