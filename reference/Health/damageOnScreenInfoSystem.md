# damageOnScreenInfoSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/damageOnScreenInfoSystem.cs:6`

**概要**: シーン共有のダメージ表示マネージャ（シングルトン）。`currentID`で対象を登録し、複数の`playerDamageOnScreenInfoSystem`へ表示要求を配信する。

**公式ドキュメント抜粋**（[Damage On Screen Info System](../../docs/player-controller-components/elements-used-by-other-components/damage-on-screen-info-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Damage Active | `showDamageActive` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Target Info List | `targetInfoList` | `List<targetInfo>` | new List<targetInfo> () | – |
| Player Damage On Screen Info System List | `playerDamageOnScreenInfoSystemList` | `List<playerDamageOnScreenInfoSystem>` | new List<playerDamageOnScreenInfoSyst… | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 未初期化なら自身を静的`Instance`に登録し、既存の別インスタンスがあれば自身を破棄する。 |
| `addNewPlayer(playerDamageOnScreenInfoSystem newPlayer)` | `newPlayer`に`damageOnScreenId`を割り当てて一覧へ追加し、既存の全対象を再登録させる。 |
| `addNewTarget(Transform newTarget, bool removeDamageInScreenOnDeathValue, Vector3 iconOffset)` | `newTarget`と`iconOffset`から対象を登録して全プレイヤーへ追加し、割り当てたIDを返す。 |
| `setDamageInfo(int objectId, float amount, bool isDamage, Vector3 direction, float healhtAmount, float criticalDamageProbability)` | `objectId`の対象インデックスを探し、全プレイヤーの`setDamageInfo`へ転送する。 |
| `removeElementFromList(int objectId)` | `objectId`の対象を全プレイヤーから削除し、共有リストからも取り除く。 |
| `removeElementFromTargetListCalledByPlayer(int objectId, GameObject currentPlayer)` | プレイヤー起点の削除として共有リストから消し、他のプレイヤーにも削除を通知する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |

## 内部型

- `targetInfo`（class）
- `damageNumberInfo`（class）
