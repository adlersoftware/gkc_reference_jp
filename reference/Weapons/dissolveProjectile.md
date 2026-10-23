# dissolveProjectile

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `projectileSystem`
- **ソース**: `Weapons/Projectiles/dissolveProjectile.cs:6`

**概要**: 着弾した物体へ`dissolveObject`を付け、シェーダーや色を渡して溶かす投射物。溶解完了で自身を破棄する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer | `layer` | `LayerMask` | – | – |
| Use Layer Mask To Ignore | `useLayerMaskToIgnore` | `bool` | – | – |
| Layer Mask To Ignore | `layerMaskToIgnore` | `LayerMask` | – | – |
| Time To Destroy Object | `timeToDestroyObject` | `float` | 0.9f | – |
| Dissolve Speed | `dissolveSpeed` | `float` | 1 | – |

### Shader Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shader To Apply | `shaderToApply` | `Shader` | – | – |
| Dissolve Texture | `dissolveTexture` | `Texture` | – | – |
| Dissolve Color | `dissolveColor` | `Color` | – | – |
| Dissolve Color Alpha | `dissolveColorAlpha` | `float` | – | – |
| Dissolve Shader Field Name | `dissolveShaderFieldName` | `string` | "_Amount" | – |
| Dissolve Shader Texture Field Name | `dissolveShaderTextureFieldName` | `string` | "_DissolveTexture" | – |
| Dissolve Shader Color Field Name | `dissolveShaderColorFieldName` | `string` | "_DissolveColor" | – |
| Dissolve Shader Alpha Color Field Name | `dissolveShaderAlphaColorFieldName` | `string` | "_DissolveColorAlpha" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Dissolve Found | `objectToDissolveFound` | `bool` | – | – |
| Current Fade Value | `currentFadeValue` | `float` | 1 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `dissolveObject(GameObject objectToDissolve)` | 対象のColliderを取得して`checkObjectDetected`へ渡すだけ。 |
| `checkObjectDetected(Collider col)` | 着弾音と停止処理の後、対象やキャラ・乗物に`dissolveObject`を用意して設定し、溶解を開始する。 |
| `destroyObject()` | `destroyProjectile()`を呼んで自身を消すだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetProjectile()`

</details>
