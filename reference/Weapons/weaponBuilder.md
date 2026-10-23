# weaponBuilder

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/weaponBuilder.cs:6`

**概要**: 武器モデルのパーツを差し替えて新しい武器を組み立てるエディタ向けコンポーネント。名前・アイコン・耐久値などを`playerWeaponSystem`やインベントリへ反映し、使用可能武器プレハブの生成も行う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon Name | `weaponName` | `string` | – | 生成する武器の名前。オブジェクト名やプレハブ名に使う。 |

### Usable Weapon Prefab Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Relative Path Usable Weapon Prefab | `relativePathUsableWeaponPrefab` | `string` | "" | 使用可能武器プレハブの保存先フォルダパス。 |
| Usable Weapon Prefab | `usableWeaponPrefab` | `GameObject` | – | 生成された使用可能武器プレハブへの参照。 |
| Layer To Place Weapon Prefab | `layerToPlaceWeaponPrefab` | `LayerMask` | – | 生成した武器プレハブを配置するレイヤー。 |

### Arms Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Arms Parent | `armsParent` | `Transform` | – | 腕モデルの親トランスフォーム参照（現在は未使用）。 |
| Current Arms Model | `currentArmsModel` | `GameObject` | – | 現在の腕モデル。差し替え時に削除される。 |
| Replace Arms Model | `replaceArmsModel` | `bool` | – | オンでビルド時に`newArmsModel`へ腕を差し替える。 |
| New Arms Model | `newArmsModel` | `GameObject` | – | 差し替え先となる新しい腕モデルのプレハブ。 / 表示条件: `replaceArmsModel` がオンのとき |

### Explanation

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Build Weapon Explanation | `buildWeaponExplanation` | `string` | "Make sure to drop the prefab of the … | ビルド手順を説明するエディタ表示用のテキスト。 / TextArea (3, 10) |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | 常時使用パーツの位置にギズモ球を表示する。 |
| Show Gizmo Label | `showGizmoLabel` | `bool` | – | パーツ名のラベルをシーンビューに表示する。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.black | シーンビューに出すラベル文字の色。 |
| Gizmo Radius | `gizmoRadius` | `float` | – | パーツ位置に描くギズモ球の半径。 |
| Use Handle | `useHandle` | `bool` | – | シーンビューのハンドルで位置と回転を編集できる。 |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | `playerWeaponsManager`参照。武器リストの更新に使う。 |
| Weapon Parent | `weaponParent` | `Transform` | – | ビルドした武器を置く親`Transform`。 |
| Main IK Weapon System | `mainIKWeaponSystem` | `IKWeaponSystem` | – | `IKWeaponSystem`参照。インベントリ登録などに使う。 |
| Main Player Weapon System | `mainPlayerWeaponSystem` | `playerWeaponSystem` | – | `playerWeaponSystem`参照。武器名の設定やレイヤー更新に使う。 |
| Weapon Mesh Parent | `weaponMeshParent` | `GameObject` | – | 武器メッシュの親`GameObject`。パーツの配置先。 |
| New Weapon Mesh Parent | `newWeaponMeshParent` | `Transform` | – | 移動対象パーツの新しい親となる`Transform`。 |
| Weapon View Transform | `weaponViewTransform` | `Transform` | – | ビルド後にエディタ視点を合わせる`Transform`。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `weaponPartInfoList` | `List<partInfo>` | new List<partInfo> () | – |
| `weaponSettingsInfoList` | `List<settingsInfo>` | new List<settingsInfo> () | – |
| `weaponPartsNotUsedOnAIList` | `List<GameObject>` | new List<GameObject> () | – |
| `weaponPartsToMoveToNewParentList` | `List<Transform>` | new List<Transform> () | – |
| `createWeaponInventoryActive` | `bool` | – | – |
| `createWeaponAmmoInventoryActive` | `bool` | – | – |
| `createUsableWeaponPrefabActive` | `bool` | – | – |
| `weaponAmmoAmountValue` | `int` | 10 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `buildWeapon()` | パーツ移動から調整・腕差し替え・インベントリ登録・プレハブ生成までを順に実行し、最後に`weaponViewTransform`へエディタ視点を合わせる。 |
| `adjustWeaponParts()` | 各パーツのIK位置を新メッシュへ付け替え、旧メッシュを破棄して`newWeaponMesh`を生成し、使用可否イベントを発火する。 |
| `checkArmsToReplace()` | `replaceArmsModel`が有効なら`newArmsModel`を複製して`mainIKWeaponSystem`の一人称腕に登録し、カメラ用レイヤーを適用する。 |
| `toogleArmsMeshActiveState()` | `currentArmsModel`のアクティブ状態を反転するだけ。 |
| `adjustWeaponSettings()` | `weaponSettingsInfoList`の各項目で有効なbool・float設定イベントを、保持している値を引数に呼び出す。 |
| `checkIfCreateInventoryWeapon()` | `createWeaponInventoryActive`なら名前・説明・アイコン・耐久値・重量・価格を渡して武器をインベントリに登録する。 |
| `setCustomAmmoMeshInfo(GameObject newCustomAmmoMesh, Texture newCustomAmmoIcon, string newCustomAmmoDescription)` | カスタム弾薬のメッシュ・アイコン・説明文を保持するだけ。 |
| `checkIfCreateInventoryWeaponAmmo()` | `createWeaponAmmoInventoryActive`なら武器名由来の弾薬名・数量・カスタム弾薬情報を渡してインベントリに登録する。 |
| `checkCreateUsableWeaponPrefab()` | `createUsableWeaponPrefabActive`なら使用可能武器プレハブを生成し、無効なら参照をnullにするだけ。 |
| `checkRemoteRegularWeaponPickupPrefab()` | `mainIKWeaponSystem`から通常武器のピックアップを削除するだけ。 |
| `adjustWeaponSettingsFromEditor()` | `adjustWeaponSettings`を呼んだうえでシーンをダーティにし、変更を保存対象にする。 |
| `completeWeaponBuild()` | 武器名を`mainPlayerWeaponSystem`とオブジェクト名へ反映し、武器リスト・ポケット登録・カメラ用レイヤーを更新する。 |
| `resetTemporalWeaponParts()` | 各パーツの一時メッシュ参照と位置・回転オフセットをクリアするだけ。 |
| `removeTemporalWeaponParts()` | 一時生成メッシュを破棄し、元メッシュと追加メッシュを再表示してパーツ設定を初期化する。 |
| `setCreateWeaponInventoryActiveState(bool state)` | `createWeaponInventoryActive`を設定してコンポーネントを更新するだけ。 |
| `setCreateWeaponAmmoInventoryActiveState(bool state)` | `createWeaponAmmoInventoryActive`を設定してコンポーネントを更新するだけ。 |
| `setWeaponAmmoAmountValue(float ammoAmount)` | 弾薬数をintへ丸めて`weaponAmmoAmountValue`に設定し、コンポーネントを更新するだけ。 |
| `setCreateUsableWeaponPrefabActiveState(bool state)` | `createUsableWeaponPrefabActive`を設定してコンポーネントを更新するだけ。 |
| `alignViewWithWeaponCameraPosition()` | エディタ視点を`weaponViewTransform`に合わせるだけ。 |
| `setEditorCameraPosition(Transform transformToUse)` | エディタのシーンビューを指定トランスフォームへ向けるだけ。 |
| `setNewWeaponName(string newWeaponName)` | 旧名を`previousWeaponName`に退避してから`weaponName`を更新し、コンポーネントを更新する。 |
| `setNewWeaponIconTexture(Texture newWeaponIconTexture)` | 武器アイコンのテクスチャを設定するだけ。 |
| `setNewWeaponDescription(string newValue)` | 武器の説明文を設定するだけ。 |
| `setObjectWeight(float newValue)` | 武器の重量を設定するだけ。 |
| `setCanBeSold(bool newValue)` | 売却可能かどうかのフラグを設定するだけ。 |
| `setvendorPrice(float newValue)` | 販売価格を設定するだけ。 |
| `setSellPrice(float newValue)` | 売却価格を設定するだけ。 |
| `setWeaponInventorySlotIconInEditor(Texture newTexture)` | インベントリスロット用アイコンを`mainPlayerWeaponSystem`へ設定するだけ。 |
| `setWeaponIconHUDInEditor(Texture newTexture)` | HUD用アイコンを`mainPlayerWeaponSystem`へ設定するだけ。 |
| `setWeaponIconInEditor(Texture newTexture)` | 武器アイコンを`mainPlayerWeaponSystem`へ設定するだけ。 |
| `setWeaponDurabilityInfo(bool useDurabilityValue, float durabilityAmountValue, float maxDurabilityAmountValue, float durabilityUsedOnAttackValue)` | 耐久機能の有無・現在値・最大値・攻撃毎の消費量をまとめて設定するだけ。 |
| `checkWeaponBuilder(playerWeaponsManager newPlayerWeaponsManager)` | `playerWeaponsManager`がnullでなければ自身へ登録し、その武器親を取得してコンポーネントを更新する。 |
| `checkWeaponsPartsToRemoveOnAI()` | AIで不要なパーツを破棄してリストを空にし、コンポーネントを更新する。 |
| `createUsableWeaponPrefab()` | 使用可能武器の保存先パスに`weaponName`でプレハブを作成し、シーンをダーティにする。 |
| `instantiateUsableWeaponPrefabInScene()` | 同じパスのプレハブを`layerToPlaceWeaponPrefab`レイヤーでシーンに配置する。 |

## 内部型

- `settingsInfo`（class）
- `partInfo`（class）
