# factionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Faction/factionSystem.cs:5`

**概要**: ゲーム全体のfaction定義と関係(味方/敵/中立)を保持するシングルトン。登録キャラクターのリストを使い、関係判定・変更、警告、対象解除を各キャラへ配信する。

**公式ドキュメント抜粋**（[Faction System](../../docs/major-systems/faction-system.md)）

> A system for making character factions. Faction System Manager

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `factionList` | `List<factionInfo>` | new List<factionInfo> () | – |
| `factionStringList` | `string []` | – | – |
| `characterFactionManagerList` | `List<characterFactionManager>` | new List<characterFactionManager> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 初期化済みなら戻り、別インスタンスが存在すれば自身を破棄し、そうでなければ静的`Instance`に自身を設定する。 |
| `addCharacterToList(characterFactionManager character)` | `characterFactionManagerList`へ追加するだけ。 |
| `removeCharacterToList(characterFactionManager character)` | `characterFactionManagerList`から削除するだけ。 |
| `isCharacterFriendly(int ownFactionIndex, string characterToCheckFactionName)` | 同名factionならtrue、関係がfriendならtrue、関係未定義ならfalseを返す。 |
| `isCharacterEnemy(int ownFactionIndex, string characterToCheckFacionName)` | 同名factionはfalse、関係がenemyならtrue、関係未定義ならtrueを返す。 |
| `isAttackerEnemy(int ownFactionIndex, string characterToCheckFacionName, bool checkForFriendlyFactionAttackers, bool changeFactionRelationWithFriendlyAttackers)` | 同名で同士討ち設定があれば敵、関係が敵ならtrue、味方でも攻撃時敵化設定なら関係を敵へ変えてtrueを返す。 |
| `isCharacterNeutral(int ownFactionIndex, string characterToCheckFacionName)` | 同名factionはfalse、関係がneutralならtrue、関係未定義ならtrueを返す。 |
| `changeFactionRelation(int ownFactionIndex, string otherFactionName, relationInfo.relationType relationType)` | 自分以外のfactionとの関係を書き換え、同factionの全キャラへ`checkCharactersAround`を送る。 |
| `removeEnemiesFromNewFriendFaction(int ownFactionIndex)` | 同factionの全キャラについて、新たに味方になった相手を敵リストから除去させる。 |
| `removeEnemiesFromCharacter(int ownFactionIndex, Transform characterTransform)` | 指定したTransformのキャラだけ、同様に敵リストから相手を除去させる。 |
| `removeCharacterAsTargetFromEnemies(int ownFactionIndex, GameObject characterToRemove)` | 対象を敵とみなす全AIへ`removeTargetFromAICharacter`で対象解除を依頼する。 |
| `checkIfCharacterBelongsToFaction(string factionName, GameObject character)` | キャラの`characterFactionManager.factionName`が指定名と一致するかを返す。 |
| `isCharacterDetectedAsEnemyByOtherFaction(GameObject characterToCheck)` | 全キャラの`currentDetectedEnemyList`を走査し、対象が検出済みかを返す。 |
| `alertFactionOnSpotted(int ownFactionIndex, float alertCloseFactionRadius, GameObject target, Vector3 alertPosition)` | 同factionかつ指定位置から半径内のキャラへ`alertFaction`を送り、目標を警告する。 |
| `removeCharacterAsTargetOnSameFaction(GameObject characterToCheck, int ownFactionIndex)` | 同factionまたは非敵の全キャラへ、対象解除シグナルを送る。 |
| `addFaction()` | 既定名「New Faction」のfactionを`factionList`へ追加し、コンポーネントを更新する。 |
| `removeFaction(int factionIndexToRemove)` | 指定インデックスのfactionを`factionList`から削除し、コンポーネントを更新する。 |
| `updateFactionsList()` | faction名を再取得し、消えた関係を削除、新規factionとの関係を追加してindexを更新する。 |
| `getFactionIndex(string factionName)` | 名前が一致するfactionのインデックスを返し、存在しなければ-1を返す。 |
| `checkIfFactionExists(string factionName)` | `factionList`に指定名のfactionがあるかを返す。 |
| `checkIfFactionExistsInStringList(string factionName)` | `factionStringList`に指定名があるかを返す。 |
| `factionContainsRelation(int factionIndex, string factionWithRelation)` | 自身または関係リストに指定faction名があるかを返す。 |
| `setAllRelationsAsFriendOrEnemyOnFaction(int factionIndex, int relationTypeIndex)` | 0=friend、1=enemy、2=neutralで指定factionの全関係を一括設定し更新する。 |
| `getFactionStringList()` | `factionList`から`factionStringList`を作り直すだけ。 |
| `updateFactionListNames()` | `factionStringList`を更新してコンポーネントを更新する。 |
| `updateComponent()` | コンポーネントとシーンをダーティにするだけ。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |

## 内部型

- `factionInfo`（class）
- `relationInfo`（class）
