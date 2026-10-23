# characterModelElementInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Character Builder/characterModelElementInfo.cs:5`

**概要**: 差し替え用キャラクターモデルの付加情報を保持するコンポーネント。Animator、人型ボーン、装備データ、身長設定などをまとめ、ボーンを自動取得できる。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Height On Character | `setNewHeightOnCharacter` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Animator | `setNewAnimator` | `bool` | – | – |
| New Runtime Animator Controller | `newRuntimeAnimatorController` | `RuntimeAnimatorController` | – | – |
| Set New Chest Up Vector Value On Runtime | `setNewChestUpVectorValueOnRuntime` | `bool` | – | – |
| Chest Up Vector | `chestUpVector` | `Vector3` | – | – |

### Armor Cloth Data Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Armor Cloth Data | `setNewArmorClothData` | `bool` | – | – |
| Main Armor Cloth Piece Template Data | `mainArmorClothPieceTemplateData` | `armorClothPieceTemplateData` | – | – |
| Main Full Armor Cloth Template Data | `mainFullArmorClothTemplateData` | `fullArmorClothTemplateData` | – | – |
| Main Character Aspect Customization Template Data | `mainCharacterAspectCustomizationTemplateData` | `characterAspectCustomizationTemplateData` | – | – |
| Set New Armor Cloth Set | `setNewArmorClothSet` | `bool` | – | – |
| Initial Character Aspect Customization Template | `initialCharacterAspectCustomizationTemplate` | `characterAspectCustomizationTemplate` | – | – |
| Set Random Armor Cloth Set | `setRandomArmorClothSet` | `bool` | – | – |
| Character Aspect Customization Template List | `characterAspectCustomizationTemplateList` | `List<characterAspectCustomizationTemplate>` | new List<characterAspectCustomization… | – |

### Character Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head | `head` | `Transform` | – | – |
| Neck | `neck` | `Transform` | – | – |
| Chest | `chest` | `Transform` | – | – |
| Spine | `spine` | `Transform` | – | – |
| Hips | `hips` | `Transform` | – | – |
| Right Lower Arm | `rightLowerArm` | `Transform` | – | – |
| Left Lower Arm | `leftLowerArm` | `Transform` | – | – |
| Right Hand | `rightHand` | `Transform` | – | – |
| Left Hand | `leftHand` | `Transform` | – | – |
| Right Lower Leg | `rightLowerLeg` | `Transform` | – | – |
| Left Lower Leg | `leftLowerLeg` | `Transform` | – | – |
| Right Foot | `rightFoot` | `Transform` | – | – |
| Left Foot | `leftFoot` | `Transform` | – | – |
| Right Toes | `rightToes` | `Transform` | – | – |
| Left Toes | `leftToes` | `Transform` | – | – |

### Ragdoll Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Ragdoll Bones Manually | `setRagdollBonesManually` | `bool` | – | – |
| Right Upper Arm | `rightUpperArm` | `Transform` | – | – |
| Left Upper Arm | `leftUpperArm` | `Transform` | – | – |
| Right Upper Leg | `rightUpperLeg` | `Transform` | – | – |
| Left Upper Leg | `leftUpperLeg` | `Transform` | – | – |
| Middle Spine | `middleSpine` | `Transform` | – | – |
| Pelvis | `pelvis` | `Transform` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Game Object | `characterGameObject` | `GameObject` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getCharacterElements()` | `getCharacterBones` でボーンを取得した後に `updateComponent` を呼ぶ。 |
| `getCharacterBones()` | Animator が無ければ取得し、頭・首・胸・背骨・腰・手足の人型ボーンを各フィールドへ格納する（不足時は警告や親による補正）。 |
