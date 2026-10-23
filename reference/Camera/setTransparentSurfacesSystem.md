# setTransparentSurfacesSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Others/setTransparentSurfacesSystem.cs:5`

**概要**: 透明化対象サーフェスを共有するシングルトン的なマネージャ。シェーダの差し替えとアルファ値のコルーチン補間で、透明/通常を切り替える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Surface Enabled | `checkSurfaceEnabled` | `bool` | true | – |
| Transparent Shader | `transparentShader` | `Shader` | – | – |
| Alpha Blend Speed | `alphaBlendSpeed` | `float` | 5 | – |
| Alpha Transparency | `alphaTransparency` | `float` | 0.2f | – |
| Use Alpha Color | `useAlphaColor` | `bool` | true | – |
| Transparent Amount Name | `transparentAmountName` | `string` | "_TransparentAmount" | – |
| Color Property Name | `colorPropertyName` | `string` | "_Color" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Surface Info List | `surfaceInfoList` | `List<surfaceInfo>` | new List<surfaceInfo> () | – |
| Surface Game Object List | `surfaceGameObjectList` | `List<GameObject>` | new List<GameObject> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 初期化済みなら何もせず、重複インスタンスなら自身を破棄し、そうでなければ静的インスタンスに登録する。 |
| `addNewSurface(GameObject newSurface, Shader customShader)` | 子レンダラーのマテリアルを収集して元シェーダとアルファを保存し、透明シェーダに差し替えて登録・透明化する。 |
| `listContainsSurface(GameObject surfaceToCheck)` | 有効時のみ、`surfaceGameObjectList` に対象が含まれるかどうかを返す。 |
| `setSurfaceToRegular(int surfaceIndex, bool removeSurfaceAtEnd)` | 対象を通常へ戻すフラグを立て、全マテリアルのアルファを元へ補間し、`removeSurfaceAtEnd` なら完了後にリストから外す。 |
| `checkSurfaceToSetTransparentAgain(GameObject surfaceToCheck)` | 通常へ戻す途中（一時的でない）なら、そのサーフェスを再度透明化する。 |
| `setSurfaceTransparent(surfaceInfo currentSurfaceToCheck)` | 透明化フラグを立て、全マテリアルのアルファを `alphaTransparency` へ補間する。 |
| `setAlphaValue(surfaceInfo currentSurfaceToCheck, int surfaceIndex, Material currentMaterial, bool changingToTransparent, Shader originalShader, float originalAlphaColor, bool removeSurfaceAtEnd)` | 既存の補間コルーチンを止め、指定マテリアルのアルファ（または `_TransparentAmount`）を補間するコルーチンを開始する。 |
| `checkSurfacesToRemove()` | プレイヤー数が0になったサーフェスを通常へ戻し、リストから削除する。 |
| `changeSurfacesToTransparentOrRegularTemporaly(int playerID, int surfaceIndex, bool setTransparentSurface)` | 指定プレイヤーIDが登録されていれば、そのサーフェスを一時的に透明化または通常化する。 |
| `addPlayerIDToSurface(int playerID, GameObject surfaceToCheck)` | 一致するサーフェスに未登録ならプレイヤーIDを追加し、検出人数を増やす。 |
| `removePlayerIDToSurface(int playerID, int surfaceIndex)` | 登録済みならプレイヤーIDを外し、検出人数を減らす。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |

## 内部型

- `surfaceInfo`（class）
- `materialInfo`（class）
