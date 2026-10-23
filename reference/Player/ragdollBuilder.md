# ragdollBuilder

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Character Builder/ragdollBuilder.cs:7`

**概要**: 人型モデルのボーンからラグドール用のジョイント・リジッドボディ・コライダーを構築/削除するビルダー。構築後は `ragdollActivator` の各リストを更新する。

**公式ドキュメント抜粋**（[Ragdoll Builder](../../docs/character-level-components/character/ragdoll-builder.md)）

> Used to add automatically a ragdoll to the character, it is used by default when a new character is created, but it can be used at any moment too.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Animator Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Animator | `animator` | `Animator` | – | – |
| Main Ragdoll Activator | `mainRagdollActivator` | `ragdollActivator` | – | – |

### Skeleton Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head | `head` | `Transform` | – | – |
| Right Elbow | `rightElbow` | `Transform` | – | – |
| Left Elbow | `leftElbow` | `Transform` | – | – |
| Right Arm | `rightArm` | `Transform` | – | – |
| Left Arm | `leftArm` | `Transform` | – | – |
| Middle Spine | `middleSpine` | `Transform` | – | – |
| Pelvis | `pelvis` | `Transform` | – | – |
| Right Hips | `rightHips` | `Transform` | – | – |
| Left Hips | `leftHips` | `Transform` | – | – |
| Right Knee | `rightKnee` | `Transform` | – | – |
| Left Knee | `leftKnee` | `Transform` | – | – |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Same Mass To Each Bone | `setSameMassToEachBone` | `bool` | – | – |
| Total Mass | `totalMass` | `float` | – | – |
| Assign Bones Manually | `assignBonesManually` | `bool` | – | – |

### Ragdoll Scale and Mass Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hips Scale | `hipsScale` | `float` | 1 | – |
| Upper Legs Scale | `upperLegsScale` | `float` | 0.2f | – |
| Lower Legs Scale | `lowerLegsScale` | `float` | 0.2f | – |
| Upper Arms Scale | `upperArmsScale` | `float` | 0.25f | – |
| Lower Arms Scale | `lowerArmsScale` | `float` | 0.2f | – |
| Spine Scale | `spineScale` | `float` | 1 | – |
| Head Scale | `headScale` | `float` | 1 | – |
| Hips Mass Percentage | `hipsMassPercentage` | `float` | 20 | – |
| Upper Legs Mass Percentage | `upperLegsMassPercentage` | `float` | 9 | – |
| Lower Legs Mass Percentage | `lowerLegsMassPercentage` | `float` | 8 | – |
| Upper Arms Mass Percentage | `upperArmsMassPercentage` | `float` | 7 | – |
| Lower Arms Mass Percentage | `lowerArmsMassPercentage` | `float` | 6 | – |
| Spine Mass Percentage | `spineMassPercentage` | `float` | 10 | – |
| Head Mass Percentage | `headMassPercentage` | `float` | 10 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ragdoll Added | `ragdollAdded` | `bool` | – | – |
| Bones | `bones` | `List<boneParts>` | new List<boneParts> () | – |
| Bones Transforms | `bonesTransforms` | `List<Transform>` | new List<Transform> () | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Create Ragdoll | `eventOnCreateRagdoll` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getCharacterBonesFromEditor()` | ボーンを取得し、不足があれば警告を出して `bonesTransforms` を空にする。 |
| `setCharacterBones(Transform newHead, Transform newRightElbow, Transform newLeftElbow, Transform newRightArm, Transform newLeftArm, Transform newMiddleSpine, Transform newPelvis, Transform newRightHips, Transform newLeftHips, Transform newRightKnee, Transform newLeftKnee)` | 引数の11個のボーンTransformを対応するフィールドへ代入するだけ。 |
| `getCharacterBones()` | `animator` から人型ボーンを取得して格納し、`addBonesTransforms` でリスト化する。 |
| `checkAllBonesFound()` | 頭・骨盤・脚・腕・背骨の全ボーンが null でないかを返す。 |
| `createRagdoll()` | ボーンを取得/検証して胴体・脚・腕・頭の部位を生成し、成功時はコンポーネント構築と作成イベント、 activator 更新を行う。 |
| `updateRagdollActivatorParts()` | `mainRagdollActivator` のコライダー/リジッドボディ/部位リストを再設定し、コンポーネントを更新する。 |
| `removeRagdoll()` | 各ボーンから Joint・Rigidbody・Collider を削除し、`ragdollAdded` を false にする。 |
| `removeRagdollFromEditor()` | `removeRagdoll` を実行し、ボーンリストを空にして activator を更新し true を返す。 |
| `enableRagdollColliders()` | `setRagdollCollidersState(true)` を呼ぶだけ。 |
| `disableRagdollColliders()` | `setRagdollCollidersState(false)` を呼ぶだけ。 |
| `setRagdollCollidersState(bool state)` | `bones` 内の各ボーンの Collider の enabled を state に設定する。 |
| `setCheckIfRagdollComponentsAlreadyAddedOnModelActiveState(bool state)` | `checkIfRagdollComponentsAlreadyAddedOnModelActive` を設定するだけ。 |
| `setIgnoreStoreBonesByGetBoneTransformActiveState(bool state)` | `ignoreStoreBonesByGetBoneTransformActive` を設定するだけ。 |
| `getAnimator(Animator anim)` | `animator` フィールドを引数の Animator にするだけ。 |
| `setRagdollActivator(ragdollActivator newRagdollActivator)` | `mainRagdollActivator` を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCreateRagdoll` | `UnityEvent` | – |

## 内部型

- `boneParts`（class）
