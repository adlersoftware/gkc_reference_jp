# playerCullingSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Others/playerCullingSystem.cs:5`

**概要**: プレイヤーのレンダラーを対象に、マテリアルの透明度を補間してカリング（フェード）するシステム。対象レンダラーと元シェーダをリストで保持する。

**公式ドキュメント抜粋**（[Player Culling System](../../docs/player-controller-components/player-camera/player-culling-system.md)）

> Used to fade the player’s materials smoothly when the camera is close enough to it, so the camera view is not blocked by its meshes, something made in a lot of games in third person.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Culling System Enabled | `cullingSystemEnabled` | `bool` | true | – |
| Min Distance To Apply Shader | `minDistanceToApplyShader` | `float` | 1 | – |
| Min Culling Shader Value | `minCullingShaderValue` | `float` | 0.2f | – |
| Slerp Culling Speed | `slerpCullingSpeed` | `float` | 1 | – |
| Stipple Size | `stippleSize` | `float` | – | – |
| Transparent Amount Name | `transparentAmountName` | `string` | "_TransparentAmount" | – |
| Set Stipple Size | `setStippleSize` | `bool` | – | – |
| Stipple Size Name | `stippleSizeName` | `string` | "_StippleSize" | – |

### Player GameObject List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Game Object List | `playerGameObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| Player Game Object With Child List | `playerGameObjectWithChildList` | `List<GameObject>` | new List<GameObject> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Pause Culling State | `pauseCullingState` | `bool` | – | – |
| Culling Amount To Apply | `cullingAmountToApply` | `float` | – | – |
| Culling Active | `cullingActive` | `bool` | – | – |
| Current Distance | `currentDistance` | `float` | – | – |
| Current Culling Value | `currentCullingValue` | `float` | – | – |
| Materials Changed Checked | `materialsChangedChecked` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Culling Shader | `cullingShader` | `Shader` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Camera Transform | `cameraTransform` | `Transform` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Renderer Parts | `rendererParts` | `List<Renderer>` | new List<Renderer> () | – |
| Original Shader | `originalShader` | `List<Shader>` | new List<Shader> () | – |
| Material List | `materialList` | `List<Material>` | new List<Material> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPauseCullingState(bool state)` | `pauseCullingState` を設定するだけ。 |
| `getMaterialList()` | マテリアルリストが空なら、保持しているレンダラーからマテリアルと元シェーダを収集する。 |
| `clearRendererList()` | レンダラーと元シェーダのリストを空にするだけ。 |
| `setNewPlayerGameObject(GameObject newObject)` | `playerGameObjectList` を空にして新しいオブジェクト1つだけを追加する。 |
| `storePlayerRenderer()` | レンダラーリストを消してから、対象オブジェクトと子オブジェクトの `Renderer` を収集する。 |
| `storePlayerRendererFromEditor()` | `storePlayerRenderer` を実行してからコンポーネントを更新する。 |
| `clearRendererListFromEditor()` | レンダラーリストを消してからコンポーネントを更新する。 |
| `setCullingSystemEnabledState(bool state)` | `cullingSystemEnabled` を設定するだけ。 |
| `setCullingSystemEnabledStateFromEditor(bool state)` | 有効状態を設定してからコンポーネントを更新する。 |
| `updateComponent()` | コンポーネントとダーティシーンを更新するだけ。 |
