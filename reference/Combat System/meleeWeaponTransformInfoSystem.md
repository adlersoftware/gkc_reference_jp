# meleeWeaponTransformInfoSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/meleeWeaponTransformInfoSystem.cs:5`

**概要**: 実行中に手に持った武器と武器メッシュのlocal位置・回転を調整し、その値をScriptableObjectへコピー/貼り付けする開発・調整用コンポーネント。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Edit Weapon Transform Values Ingame | `editWeaponTransformValuesIngame` | `bool` | – | – |
| Weapon Position | `weaponPosition` | `Vector3` | – | – |
| Weapon Rotation | `weaponRotation` | `Vector3` | – | – |
| Current Weapon Object Transform | `currentWeaponObjectTransform` | `Transform` | – | – |
| Current Weapon Mesh Game Object | `currentWeaponMeshGameObject` | `GameObject` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |

### Melee Object Data Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Grabbed Object Melee Attack System | `mainGrabbedObjectMeleeAttackSystem` | `grabbedObjectMeleeAttackSystem` | – | – |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | – |
| Main Melee Weapon Hand Transform Data | `mainMeleeWeaponHandTransformData` | `meleeWeaponTransformData` | – | – |
| Main Melee Weapon Mesh Transform Data | `mainMeleeWeaponMeshTransformData` | `meleeWeaponTransformData` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `toggleEditWeaponTransformValuesIngameStateState()` | 再生中のみ`editWeaponTransformValuesIngame`を反転する。 |
| `setEditWeaponTransformValuesIngameState(bool state)` | 実行中編集フラグを設定し、対象Transform/メッシュとギズモ表示をクリアする。 |
| `selectCurrentWeaponObjectInGame()` | 再生中、所持武器か現在武器メッシュをエディタ上で選択状態にする。 |
| `copyTransformValuesToBuffer()` | 現在の手/メッシュのlocal位置・回転をScriptableObjectへコピーする。 |
| `getMeleeWeaponTypeNameByRegularWeaponName(string weaponName)` | 武器名からプリファブの`weaponInfoName`を探して返し、無ければ空文字を返す。 |
| `pasteTransformValuesToBuffer()` | バッファの位置・回転を所持武器情報や参照Transformへ書き込み、シーンを更新する。 |
| `cleanPositionsOnScriptable()` | 手/メッシュ用ScriptableObjectの名前とTransform値を初期化する。 |
| `toggleShowHandleGizmo()` | 再生中にギズモ表示を反転し、表示時は対象の武器Transformを取得する。 |
| `updateGrabbedWeaponReferenceValuesOnAllWeaponInfoList()` | 攻撃システム側の全武器参照値更新処理をそのまま呼ぶ。 |
