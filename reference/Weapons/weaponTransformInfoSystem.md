# weaponTransformInfoSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/weaponTransformInfoSystem.cs:5`

**概要**: 武器の保持・照準位置をTransformリストとして保存し、貼り付けや位置調整を行うエディタ補助システム。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Weapon Transform Data | `mainWeaponTransformData` | `weaponTransformData` | – | 武器の位置情報を保存する`weaponTransformData`アセット。 |
| Weapon ID | `weaponID` | `int` | – | 保存データと照合する武器ID。値が違うと貼り付けを拒否する。 |
| Number Of Elements | `numberOfElements` | `int` | – | 貼り付け処理で数えた要素数を保持するカウンタ。 |

### Add New List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| New List To Add Name | `newListToAddName` | `string` | – | 追加する位置リストの名前。空なら親の名前を使用。 |
| New List To Add Parent | `newListToAddParent` | `Transform` | – | 子の`Transform`を収集してリスト化する親オブジェクト。 |

### Weapon Position Reference Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Weapon Transform | `mainWeaponTransform` | `Transform` | – | 武器本体の`Transform`。オフセット移動の基準になる。 |

### Weapon Offset Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Offset Parent Third Person | `currentOffsetParentThirdPerson` | `Vector3` | – | 三人称の位置をまとめて動かす`Vector3`オフセット。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `weaponsTransformInfoList` | `List<weaponsTransformInfo>` | new List<weaponsTransformInfo> () | – |
| `currentListName` | `string` | – | – |
| `mainWeaponPositionsParentThirdPerson` | `List<Transform>` | new List<Transform> () | – |
| `mainWeaponPositionChildsThirdPerson` | `List<Transform>` | new List<Transform> () | – |
| `mainWeaponPositionsParentFirstPerson` | `List<Transform>` | new List<Transform> () | – |
| `mainWeaponPositionChildsFirstPerson` | `List<Transform>` | new List<Transform> () | – |
| `currentOffsetParentFirstPerson` | `Vector3` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getMainWeaponPositionChildsThirdPerson()` | 三人称用の親の子Transformを集めてリストを作り直し、コンポーネントを更新する。 |
| `setCurrentOffsetParentOnThirdPersonWithOffsetValue(Vector3 newOffset)` | 三人称の各子と`mainWeaponTransform`を`newOffset`分だけ移動してコンポーネントを更新する。 |
| `setCurrentOffsetParentOnThirdPerson()` | 三人称の各子と本体を`currentOffsetParentThirdPerson`分だけずらして更新する。 |
| `getMainWeaponPositionChildsFirstPerson()` | 一人称用の親の子Transformを集めてリストを作り直し、コンポーネントを更新する。 |
| `setCurrentOffsetParentOnFirstPerson()` | 一人称の各子を`currentOffsetParentFirstPerson`分だけ移動してコンポーネントを更新する。 |
| `adjustDrawKeepPositionToWeaponPosition()` | 武器の現在位置と回転を一人称と三人称の`keepPosition`へ複写し、シーンを更新する。 |
| `copyTransformValuesToBuffer()` | 武器IDが変わればバッファを初期化し、各リストの子のローカル位置と回転を保存側へ記録する。 |
| `getListIndex(string listName)` | 保存済みリストから同名の項目を探して添字を返し、無ければ`-1`を返す。 |
| `pasteTransformValuesToBuffer()` | 武器IDが一致する場合のみ、保存値の位置と回転を各子へ書き戻してシーンとコンポーネントを更新する。 |
| `cleanPositionsOnScriptable()` | 保存側の武器IDを`-1`にし、位置リストを空にして更新する。 |
| `addNewList()` | 指定親の子Transformを新しいリストとして追加し、名前が空なら親名を使い、重複時は警告して中断する。 |
| `addNewEmptyList()` | `New List`という名前の空リストを追加してコンポーネントを更新する。 |
| `removeElementFromWeaponsTransformInfoList(List<Transform> objectTransformInfoList, int index)` | 指定リストの`index`が範囲内なら削除し、シーンとコンポーネントを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent(this)`で自身の更新を通知するだけ。 |

## 内部型

- `weaponsTransformInfo`（class）
