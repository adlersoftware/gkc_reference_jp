# characterFactionManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Faction/characterFactionManager.cs:6`

**概要**: キャラクターの所属factionを管理するコンポーネント。factionSystemへの登録、味方/敵/中立の判定、検出済み敵リストの保持を行い、判定処理はほぼfactionSystemへ委譲する。

**公式ドキュメント抜粋**（[Character Faction Manager](../../docs/player-controller-components/player-controller/character-faction-manager.md)）

> Used to configure the faction where that character belongs, so the AI is able to identify each character and attack them if they are identified as enemies or leave them alone if the other character is a friend or neutral.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Faction Manager | `factionManager` | `factionSystem` | – | シーン内の`factionSystem`参照。未設定なら自動で検索・生成する。 |
| Character Transform | `characterTransform` | `Transform` | – | 陣営判定に使うキャラクター本体のTransform。未設定なら自身。 |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Character Faction Enabled | `ignoreCharacterFactionEnabled` | `bool` | – | ONにするとこのキャラクターを陣営判定の対象外にする。 |
| Remove As Target If Ignore Character Faction Is Activated | `removeAsTargetIfIgnoreCharacterFactionIsActivated` | `bool` | – | 無視をONにした時、敵のターゲットからこのキャラを外す。 |
| Check For Friendly Faction Attackers | `checkForFriendlyFactionAttackers` | `bool` | true | ONにすると同陣営の攻撃者も敵として扱う。 |
| Change Faction Relation With Friendly Attackers | `changeFactionRelationWithFriendlyAttackers` | `bool` | true | 同陣営攻撃者を敵扱いする際、陣営関係も敵に変更する。 |
| Main Manager Name | `mainManagerName` | `string` | "Faction System" | `factionSystem`をシーンに生成する際のGameObject名。 |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Ignore Character Faction State Change | `useEventsOnIgnoreCharacterFactionStateChange` | `bool` | – | ONにすると無視状態の切り替え時にイベントを呼ぶ。 |
| Event On Ignore Character Faction Enabled | `eventOnIgnoreCharacterFactionEnabled` | `UnityEvent` | – | 無視状態がONになった時に呼ばれるイベント。 / 表示条件: `useEventsOnIgnoreCharacterFactionStateChange` がオンのとき |
| Event On Ignore Character Faction Disabled | `eventOnIgnoreCharacterFactionDisabled` | `UnityEvent` | – | 無視状態がOFFになった時に呼ばれるイベント。 / 表示条件: `useEventsOnIgnoreCharacterFactionStateChange` がオンのとき |

### Detected Enemy List (Debug)

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Faction Manager Assigned | `factionManagerAssigned` | `bool` | – | `factionSystem`の取得に成功したかを示すデバッグ用フラグ。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `factionName` | `string` | – | – |
| `factionIndex` | `int` | – | – |
| `currentDetectedEnemyList` | `List<GameObject>` | new List<GameObject> () | – |
| `factionStringList` | `string []` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `changeCharacterToFaction(string factionToChange)` | `factionSystem`を再取得し、一致するfactionのindexと`factionName`を設定する。 |
| `isCharacterFriendly(string characterToCheckFacionName)` | `factionSystem.isCharacterFriendly`へ委譲して関係を返すだけ。未接続時はfalse。 |
| `isCharacterEnemy(string characterToCheckFacionName)` | `factionSystem.isCharacterEnemy`へ委譲して敵かどうかを返すだけ。未接続時はfalse。 |
| `isAttackerEnemy(string characterToCheckFacionName)` | 味方の攻撃も敵とみなす設定を渡し、`factionSystem.isAttackerEnemy`へ委譲するだけ。 |
| `isCharacterNeutral(string characterToCheckFacionName)` | `factionSystem.isCharacterNeutral`へ委譲し、中立かを返すだけ。未接続時はfalse。 |
| `getFactionName()` | `factionName`を返すだけ。 |
| `checkIfCharacterBelongsToFaction(string factionName, GameObject character)` | 対象キャラのfaction名が一致するかを`factionSystem`経由で返すだけ。 |
| `removeCharacterAsTargetOnSameFaction(GameObject characterGameObject)` | 同factionのAIから対象を外すよう、`factionSystem`へ自身のindexとともに委譲する。 |
| `sendSignalToRemoveCharacterAsTargetOnSameFaction(GameObject targetToRemove)` | 対象解除の`sendSignalToRemoveCharacterAsTarget`をtransformへ送るだけ。 |
| `checkCharactersAround()` | `checkCharactersAroundAI`メッセージを送り、周囲のキャラを再検出させる。 |
| `alertFaction(GameObject target)` | `characterTransform`へ`enemyAlert`メッセージを送り、対象を敵として味方AIへ警告する。 |
| `getFactionStringList()` | `factionStringList`を返すだけ。 |
| `addDetectedEnemyFromFaction(GameObject enemy)` | 重複しない場合のみ`currentDetectedEnemyList`へ敵を追加するだけ。 |
| `removeDetectedEnemyFromFaction(GameObject enemy)` | `currentDetectedEnemyList`に含まれていれば削除するだけ。 |
| `clearDetectedEnemyFromFaction()` | `currentDetectedEnemyList`を空にするだけ。 |
| `isCharacterDetectedAsEnemyByOtherFaction(GameObject characterToCheck)` | 他factionの検出済み敵リストに対象が含まれるかを`factionSystem`へ問い合わせて返す。 |
| `addCharacterFromFaction()` | `factionSystem`へ自身を登録し、`characterTransform`未設定ならtransformを代入する。 |
| `removeCharacterDeadFromFaction()` | 検出済み敵リストを消去し、死亡キャラとして`factionSystem`の登録リストから外す。 |
| `alertFactionOnSpotted(float alertCloseFactionRadius, GameObject target, Vector3 alertPosition)` | 指定半径内にいる同factionのキャラへ目標を警告するよう`factionSystem`へ委譲する。 |
| `getCharacterTransform()` | `characterTransform`を返すだけ。 |
| `getFactionManager()` | 未接続時に`factionSystem`をInstance・自動生成・Findの順で探して接続フラグを更新する。 |
| `setNeutralRelationWithFactionByName(string otherFactionName)` | 関係を中立に変更し、新関係で味方になった相手をAIの敵リストから除去する。 |
| `setEnemyRelationWithFactionByName(string otherFactionName)` | 関係を敵に変更し、`removeEnemiesFromNewFriendFaction`で対象リストを整理する。 |
| `setFriendRelationWithFactionByName(string otherFactionName)` | 関係を味方に変更し、味方になった相手をAIの敵リストから除去する。 |
| `changeCharacterToFactionAndCleanTargetListIngame(string factionToChange)` | factionを変更して自身を登録し直し、敵AIの対象リストから自身を除去する。 |
| `changeFactionRelation(string otherFactionName, factionSystem.relationInfo.relationType relationType)` | `factionSystem.changeFactionRelation`へ自身のindexとともに関係変更を委譲するだけ。 |
| `isIgnoreCharacterFactionEnabled()` | `ignoreCharacterFactionEnabled`を返すだけ。 |
| `setIgnoreCharacterFactionEnabledState(bool state)` | faction無視フラグを設定し、有効化時は設定次第で敵の対象から外し、対応イベントを発火する。 |
| `isRemoveAsTargetIfIgnoreCharacterFactionIsActivated()` | `removeAsTargetIfIgnoreCharacterFactionIsActivated`の値を返すだけ。 |
| `toggleIngoreCharacterFactionEnabled()` | faction無視フラグを現在値の反転で設定関数へ渡す。 |
| `getFactionListFromEditor()` | エディタ用に`factionSystem`を補ってfaction名リストを再取得し、コンポーネントを更新する。 |
| `changeCharacterToFactionFromEditor(string factionToChange)` | エディタ用にfactionリストを取得したうえでfactionを変更し、コンポーネントを更新する。 |
| `getFactionList()` | `factionList`の名前を`factionStringList`へ詰め直し、コンポーネントを更新する。 |
| `updateComponent()` | コンポーネントとシーンをダーティにして保存対象にするだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnIgnoreCharacterFactionEnabled` | `UnityEvent` | – |
| `eventOnIgnoreCharacterFactionDisabled` | `UnityEvent` | – |
