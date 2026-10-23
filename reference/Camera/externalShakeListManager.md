# externalShakeListManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Player Camera/externalShakeListManager.cs:5`

**概要**: シーン内で共有する外部シェイク定義リストを保持するシングルトン的なマネージャ。全 `headBob` へリストや現在のシェイク状態を配布する。

**公式ドキュメント抜粋**（[External Shake List Manager](../../docs/additional-managers/external-shake-list-manager.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `externalShakeInfoList` | `List<externalShakeInfoListElement>` | new List<externalShakeInfoListElement… | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 初期化済みなら何もせず、重複インスタンスなら自身を破棄し、そうでなければ静的インスタンスに登録する。 |
| `setShakeInManagerList(externalShakeInfoListElement element, int index)` | 指定インデックスの要素を差し替えるだけ。 |
| `udpateAllHeadbobShakeList()` | シーン内の全 `headBob` に現在のシェイクリストを反映させる。 |
| `setExternalShakeStateByIndex(int index, bool isFirstPerson)` | 指定シェイクの一人称/三人称用ダメージシェイクを、全 `headBob` に設定する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |
