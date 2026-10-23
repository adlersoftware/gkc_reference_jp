# decalTypeInformation

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Decal/decalTypeInformation.cs:5`

**概要**: オブジェクト表面のデカール(弾痕)種類を扱うコンポーネント。デカールマネージャへの参照取得、種類インデックスの保持、表面の有効状態を管理する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Impact Surface Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Manager Name | `mainManagerName` | `string` | "Decal Manager" | 参照するデカールマネージャーの識別名（既定は`Decal Manager`）。 |
| Decal Surface Active | `decalSurfaceActive` | `bool` | true | オフにするとこのオブジェクトへのデカール付着を無効にする。 |
| Parent Scorch On This Object | `parentScorchOnThisObject` | `bool` | – | オンにすると焦げ跡をこのオブジェクトの子として付ける。 |

### Debug/Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューにデカール名のラベルを表示する。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | シーンビューに出すラベルの文字色。 / 表示条件: `showGizmo` がオンのとき |
| Show Debug Print | `showDebugPrint` | `bool` | – | デカールタイプ変更時にログを出すデバッグ用フラグ。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `impactDecalList` | `string []` | – | – |
| `impactDecalIndex` | `int` | – | – |
| `impactDecalName` | `string` | – | – |
| `impactDecalManager` | `decalManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getImpactListInfo()` | デカールマネージャの`impactListInfo`から名前配列`impactDecalList`を作り直し、コンポーネントを更新する。 |
| `checkGetDecalManager()` | `impactDecalManager`が未設定なら`Instance`・自動生成・`FindObjectOfType`の順に探して設定する。 |
| `getDecalImpactIndex()` | `decalSurfaceActive`なら`impactDecalIndex`を、falseなら-1を返す。 |
| `setNewDecalType(string decalName)` | 名前が`impactDecalList`にあれば`impactDecalName`と`impactDecalIndex`を更新し、無ければ何もしない。 |
| `isParentScorchOnThisObjectEnabled()` | `parentScorchOnThisObject`の値を返すだけ。 |
| `setDecalSurfaceActiveState(bool state)` | `decalSurfaceActive`を`state`に設定するだけ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`で自身のインスペクタ表示を更新するだけ。 |
