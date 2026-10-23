# genericRagdollBuilder

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/genericRagdollBuilder.cs:7`

**概要**: 人型に限らない汎用ラグドールを、ボーンTransformのリストから構築・削除するビルダー。構築後は `ragdollActivator` へボーン/リジッドボディ/コライダーを登録する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ragdoll Name | `ragdollName` | `string` | "New Ragdoll" | – |
| Set Mass On Ragdoll | `setMassOnRagdoll` | `bool` | – | – |
| Total Mass | `totalMass` | `float` | 20 | – |
| Strength | `strength` | `float` | 0.0F | – |
| Flip Forward | `flipForward` | `bool` | false | – |
| Rotation Y Offset | `rotationYOffset` | `float` | – | – |

### Bones List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pelvis | `pelvis` | `Transform` | – | – |
| Left Hips | `leftHips` | `Transform` | null | – |
| Left Knee | `leftKnee` | `Transform` | null | – |
| Right Hips | `rightHips` | `Transform` | null | – |
| Right Knee | `rightKnee` | `Transform` | null | – |
| Left Arm | `leftArm` | `Transform` | null | – |
| Left Elbow | `leftElbow` | `Transform` | null | – |
| Right Arm | `rightArm` | `Transform` | null | – |
| Right Elbow | `rightElbow` | `Transform` | null | – |
| Middle Spine | `middleSpine` | `Transform` | null | – |
| Head | `head` | `Transform` | null | – |
| Ignore Empty Limb Fields Enabled | `ignoreEmptyLimbFieldsEnabled` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use List To Ignore On Ragdoll Activated | `useListToIgnoreOnRagdollActivated` | `bool` | – | – |
| Collider List To Ignore On Ragdoll Activated | `colliderListToIgnoreOnRagdollActivated` | `List<Collider>` | new List<Collider> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Bones | `bones` | `List<BoneInfo>` | new List<BoneInfo> () | – |
| Ragdoll Activated | `ragdollActivated` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Sent Bones List | `eventToSentBonesList` | `eventParameters.eventToCallWithTransformList` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Ragdoll Activator | `mainRagdollActivator` | `ragdollActivator` | – | – |
| Character Body | `characterBody` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkAllBonesFound()` | 頭・骨盤・背骨に加え、`ignoreEmptyLimbFieldsEnabled` でなければ手足のボーンも揃っているかを返す。 |
| `buildRagdoll()` | ボーンを検証し、揃っていれば構築して activator の更新と `updateComponent` を行う。 |
| `removeRagdoll()` | `bones` と `characterBody` 配下からジョイント・リジッドボディ・コライダーを削除する。 |
| `updateRagdollActivatorParts(bool addingRagdollOnEditorTime)` | `bones` からボーン/リジッドボディ/コライダーのリストを作り、activator へ ragdoll 情報として追加する。 |
| `updateRagdollActivatorPatsIngame()` | `updateRagdollActivatorParts(false)` を呼ぶだけ。 |
| `enableRagdollElements()` | `setActiveRagdollElements(true)` を呼ぶだけ。 |
| `disableRagdollElements()` | `setActiveRagdollElements(false)` を呼ぶだけ。 |
| `setActiveRagdollElements(bool state)` | 各ボーンの Collider を state に、Rigidbody の `isKinematic` をその逆に設定する。 |
| `activateRagdollState()` | 動作中なら無視し、コライダー有効化・衝突無視・レイヤー変更・`isKinematic` 解除・親解除を行う。 |
| `activateEventToSendBonesList()` | `bones` の Transform リストを作り、`eventToSentBonesList` で送出する。 |
| `getRagdollElementsOnBoneListManually()` | `characterBody` 配下の Rigidbody からボーンリストを再構築して activator を更新する。 |

## 内部型

- `BoneInfo`（class）
