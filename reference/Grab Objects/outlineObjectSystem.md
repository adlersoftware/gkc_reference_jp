# outlineObjectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/outlineObjectSystem.cs:6`

**概要**: マテリアルのシェーダー差し替えでアウトラインと透過を制御するコンポーネントで、描画要素と元シェーダーを保存する。表示中のプレイヤーをリスト管理し、解除時に元へ戻す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Outline Enabled | `useOutlineEnabled` | `bool` | true | – |
| Shader Outline Width Name | `shaderOutlineWidthName` | `string` | "_Outline" | – |
| Shader Outline Color Name | `shaderOutlineColorName` | `string` | "_OutlineColor" | – |
| Ignore Shader Outline Change | `ignoreShaderOutlineChange` | `bool` | – | – |

### Custom Outline Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Outline Values | `useCustomOutlineValues` | `bool` | – | – |
| Custom Outline Width | `customOutlineWidth` | `float` | 0.05f | – |
| Custom Outline Color | `customOutlineColor` | `Color` | Color.yellow | – |
| Use Custom Shader | `useCustomShader` | `bool` | – | – |
| Custom Shader | `customShader` | `Shader` | – | – |
| Custom Active Duration | `customActiveDuration` | `float` | 2 | – |

### Transparency Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Transparency Active | `useTransparencyActive` | `bool` | true | – |
| Transparency Active | `transparencyActive` | `bool` | – | – |
| Use Custom Transparency Values | `useCustomTransparencyValues` | `bool` | – | – |
| Custom Alpha Transparency | `customAlphaTransparency` | `float` | – | – |
| Transparency Color Name | `transparencyColorName` | `string` | "_BaseColor" | – |

### Others Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Mesh Parent | `meshParent` | `GameObject` | – | – |
| Ignore Particles | `ignoreParticles` | `bool` | – | – |
| Ignore Line Renderer | `ignoreLineRenderer` | `bool` | – | – |
| Use Meshes To Ignore | `useMeshesToIgnore` | `bool` | – | – |
| Meshes To Ignore | `meshesToIgnore` | `List<Transform>` | new List<Transform> () | – |
| Use Custom Mesh List | `useCustomMeshList` | `bool` | – | – |
| Custom Mesh List | `customMeshList` | `List<Transform>` | new List<Transform> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Render Elements Stored | `renderElementsStored` | `bool` | – | – |
| Outline Active | `outlineActive` | `bool` | – | – |
| Outline Temporary Active | `outlineTemporaryActive` | `bool` | – | – |

### Render Parts Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Renderer Parts | `rendererParts` | `List<Renderer>` | new List<Renderer> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Outline State Change | `useEventOnOutlineStateChange` | `bool` | – | – |
| Event On Enable Outline | `eventOnEnableOutline` | `UnityEvent` | – | – |
| Event On Disable Outline | `eventOnDisableOutline` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableCustomOutlineStateTemporaly()` | 自身がアクティブなら一時表示コルーチンを開始し、`customActiveDuration` 経過後にアウトラインを自動で消す。 |
| `stopUpdateTemporalStateCoroutine()` | `temporalStateCoroutine` があれば `StopCoroutine` するだけ。 |
| `enableCustomOutlineState()` | カスタム設定値で `setOutlineState` を true として呼び、アウトラインを有効にする。 |
| `disableCustomOutlineState()` | カスタム設定値で `setOutlineState` を false として呼び、アウトラインを無効にする。 |
| `setOutlineState(bool state, Shader shaderToApply, float shaderOutlineWidth, Color shaderOutlineColor, playerController newPlayerToCheck)` | 状態が変わった時だけ各 `Renderer` にシェーダー・幅・色を適用または `originalShader` へ戻し、プレイヤー登録とイベントを行う。 |
| `isOutlineActive()` | `outlineActive` を返すだけ。 |
| `getMeshParent()` | `meshParent` が未設定なら自身を代入してから返す。 |
| `storeRenderElements()` | 初回のみ `meshParent` 配下の `Renderer` と元シェーダーを集め、除外設定を反映して保存する。 |
| `checkChildsObjectsToIgnore(Transform obj)` | `meshesToIgnore` か `objectsToIgnoreChildren` に含まれるかを返す。 |
| `disableOutlineAndRemoveUsers()` | プレイヤーリストを空にし、アウトラインと透過を解除して関連フラグを false にする。 |
| `setTransparencyState(bool state, Shader shaderToApply, float alphaTransparency)` | 状態が変わった時だけシェーダーを差し替え `transparencyColorName` のアルファを設定し、解除時は元シェーダーかアウトラインへ戻す。 |
| `isTransparencyActive()` | `transparencyActive` を返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnEnableOutline` | `UnityEvent` | – |
| `eventOnDisableOutline` | `UnityEvent` | – |
