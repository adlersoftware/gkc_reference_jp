# mainManagerAdministrator

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Game Manager/mainManagerAdministrator.cs:11`

**概要**: インベントリやミッションなどの各メインマネージャーのプレハブを一覧保持し、シーンへの生成・親の整理・プレハブへの反映を担う。

**公式ドキュメント抜粋**（[Main Manager Administrator](../../docs/major-systems/main-manager-administrator.md)）

> GKC has many main managers, including the main inventory manager, which handles all the inventory info objects created on the asset, or the faction system to configure the relations between groups of AI and players and if they are enemies, friends, or neutral, and more main systems used to handle different parts of the asset. This main manager is located on the player prefab parent, on the component Main Manager Administrator, where you can see a list of prefabs assigned there which are the managers themselves. The system automatically drops them on the scene at the start of the game if they haven’t been dropped manually on the editor. So for this, you can just press the button Add Main Managers to Scene and they will be placed in a new parent object on the hierarchy: This parent is called Main Managers Prefabs: Some of these managers are linked to their original prefabs in the project,…

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Place Managers In Parent | `placeManagersInParent` | `bool` | – | – |
| Main Manager Info List | `mainManagerInfoList` | `List<mainManagerInfo>` | new List<mainManagerInfo> () | – |
| Explanation | `explanation` | `string` | "This component stores the a list of … | TextArea (3, 15) |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 自身を`Instance`に登録し、既に別インスタンスがあれば自身のGameObjectを破棄する。 |
| `getComponentInstanceOnApplicationPlaying()` | 再生中のみ`getComponentInstance`を呼び、インスタンスを登録する。 |
| `setSpawnManagerOnAwakeEnabledByName(string managerName)` | 指定名のマネージャーの起動時生成フラグをtrueにする。 |
| `setSpawnManagerOnAwakeDisableddByName(string managerName)` | 指定名のマネージャーの起動時生成フラグをfalseにする。 |
| `setSpawnManagerOnAwakeEnabledStateByName(string managerName, bool state)` | 名前一致のマネージャーの起動時生成フラグを`state`にしてエディタ状態を更新する。 |
| `updateMainManagersInfoToPrefabs()` | エディタ限定で、シーン上のマネージャーをプレハブへ名前基準で置き換えて反映する。 |
| `addAllMainManagersToScene()` | 全マネージャーをシーンに生成し、設定に応じて親オブジェクトへまとめる。 |
| `setMainManagersOnParent()` | 親設定が有効なら、シーン上の各マネージャーを`managersParent`の子へ移動する。 |
| `setMainManagersOnParentFromEditor()` | `placeManagersInParent`をtrueにしてから`setMainManagersOnParent`を呼ぶ。 |
| `selectMainManagersParent()` | 親が未設定なら作成し、最初の子（無ければ親自身）をエディタで選択する。 |
| `addMainManagerToScene(string managerName)` | 名前一致のマネージャーがシーンに無ければプレハブから生成し、`mainManagerOnScene`に登録する。 |
| `addMainManagerToSceneWithType(string managerName, Type typeToSearch, bool callGetComponentInstance)` | 型でシーン上のマネージャーを探し、無ければ生成し、必要なら`getComponentInstance`を送る。 |

## 内部型

- `mainManagerInfo`（class）
