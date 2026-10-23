# meleeShieldObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/meleeShieldObjectSystem.cs:5`

**概要**: 盾オブジェクトの所持者と耐久値を管理し、ブロック時の耐久減少や修理・破壊を`durabilityInfo`へ委譲する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Block Damage Protection Amount | `blockDamageProtectionAmount` | `float` | 1 | – |
| Reduced Block Damage Protection Amount | `reducedBlockDamageProtectionAmount` | `float` | 0.1f | – |
| Use Max Block Range Angle | `useMaxBlockRangeAngle` | `bool` | true | – |
| Max Block Range Angle | `maxBlockRangeAngle` | `float` | 180 | – |
| Shield Carried On Right Arm | `shieldCarriedOnRightArm` | `bool` | – | – |
| Hide Weapon Mesh When Not Used | `hideWeaponMeshWhenNotUsed` | `bool` | – | – |

### Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Object Durability On Block | `useObjectDurabilityOnBlock` | `bool` | – | – |
| Durability Used On Block | `durabilityUsedOnBlock` | `float` | 1 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Character | `currentCharacter` | `GameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Durability Info | `mainDurabilityInfo` | `durabilityInfo` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentCharacter(GameObject newObject)` | 盾を所持するキャラクタ参照`currentCharacter`を設定するだけ。 |
| `getCurrentCharacter()` | `currentCharacter`をそのまま返すだけ。 |
| `checkDurabilityOnBlockWithShield(float extraMultiplier)` | 耐久使用が有効なら`durabilityUsedOnBlock`×`extraMultiplier`を減らし、0以下になったらtrueを返す。 |
| `updateDurabilityAmountState()` | 耐久使用が有効なときだけ`mainDurabilityInfo`の耐久値状態を更新する。 |
| `getDurabilityAmount()` | 耐久使用が有効なら現在の耐久値を返し、無効なら-1を返す。 |
| `initializeDurabilityValue(float newAmount, int currentObjectIndex)` | 耐久使用が有効なら耐久値を`newAmount`で初期化し、インベントリ番号`currentObjectIndex`も設定する。 |
| `setInventoryObjectIndex(int currentObjectIndex)` | 耐久使用が有効なら`mainDurabilityInfo`のインベントリ番号を設定するだけ。 |
| `repairObjectFully()` | 耐久使用が有効なら`mainDurabilityInfo`で耐久値を全回復する。 |
| `breakFullDurabilityOnCurrentWeapon()` | 耐久使用が有効なら`mainDurabilityInfo`で耐久値を0まで削る。 |
| `setUseObjectDurabilityOnBlockValue(bool newValue)` | ブロックで耐久値を消費するか`useObjectDurabilityOnBlock`を設定するだけ。 |
| `setDurabilityUsedOnBlockValue(float newValue)` | ブロック1回あたりの耐久消費`durabilityUsedOnBlock`を設定するだけ。 |
| `setUseObjectDurabilityOnBlockValueFromEditor(bool newValue)` | 値を設定したうえで`GKC_Utils.updateComponent`とシーンのダーティ更新を行うエディタ用。 |
| `setDurabilityUsedOnBlockValueFromEditor(float newValue)` | 耐久消費値を設定したうえで`GKC_Utils.updateComponent`とシーンのダーティ更新を行うエディタ用。 |
| `setObjectNameFromEditor(string newName)` | 耐久使用が有効なら`mainDurabilityInfo`へオブジェクト名をエディタから設定する。 |
| `setDurabilityAmountFromEditor(float newValue)` | 耐久使用が有効なら`mainDurabilityInfo`の現在耐久値をエディタから設定する。 |
| `setMaxDurabilityAmountFromEditor(float newValue)` | 耐久使用が有効なら`mainDurabilityInfo`の最大耐久値をエディタから設定する。 |
