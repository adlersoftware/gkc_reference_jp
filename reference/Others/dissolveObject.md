# dissolveObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/dissolveObject.cs:5`

**概要**: 対象オブジェクトのマテリアルを溶かしシェーダーで徐々に消し、時間経過後に破棄するまでの演出を管理するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dissolve Object Enabled | `dissolveObjectEnabled` | `bool` | true | – |
| Time To Destroy Object | `timeToDestroyObject` | `float` | 0.9f | – |
| Dissolve Delay | `dissolveDelay` | `float` | – | – |
| Dissolve Speed | `dissolveSpeed` | `float` | 0.2f | – |
| Current Fade Value | `currentFadeValue` | `float` | 0 | – |

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

### Object To Dissolve Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Dissolve | `objectToDissolve` | `GameObject` | – | – |
| Use Game Object List | `useGameObjectList` | `bool` | – | – |
| Game Object List | `gameObjectList` | `List<GameObject>` | new List<GameObject> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Dissolve Found | `objectToDissolveFound` | `bool` | – | – |
| Ignore Dissolve Object Enabled | `ignoreDissolveObjectEnabled` | `bool` | – | – |
| Current Type Object Found | `currentTypeObjectFound` | `typeObjectFound` | – | – |
| Renderer Parts | `rendererParts` | `List<Renderer>` | new List<Renderer> () | – |
| Original Shader | `originalShader` | `List<Shader>` | new List<Shader> () | – |
| Material List | `materialList` | `List<Material>` | new List<Material> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopDissolveCoroutine()` | `dissolveCoroutine`があれば停止するだけ。 |
| `activateDissolve(GameObject newOjectToDissolve)` | 対象の種別（キャラ/乗り物/通常）を判定し、アウトラインを解除して溶解コルーチンを開始する。 |
| `destroyObject()` | `gameObjectList`や対象種別に応じてオブジェクトを即時に破棄する。 |
| `storeRenderElements()` | 対象のRendererとマテリアルを集め、溶解用シェーダーとテクスチャ・色を適用して記録する。 |
| `setDissolveObjectEnabledState(bool state)` | `dissolveObjectEnabled`を`state`にするだけ。 |
| `setIgnoreDissolveObjectEnabledState(bool state)` | `ignoreDissolveObjectEnabled`を`state`にするだけ。 |
| `cancelDissolve()` | `objectToDissolveFound`をfalseにし、時間経過後なら元のシェーダーへ戻してコルーチンを止める。 |
| `setDissolveObjectEnabledStateFromEditor(bool state)` | 状態を設定した上で`updateComponent`によりインスペクタを更新する。 |

## 内部型

- `typeObjectFound`（enum）
