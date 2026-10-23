# runtimeShatterRecursive

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/Slice System/runtimeShatterRecursive.cs:6`

**概要**: 対象オブジェクトを指定回数だけ再帰的に粉砕し、生成した破片にコライダーと剛体を付ける。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shatter Enabled | `shatterEnabled` | `bool` | true | – |
| Cross Section Material | `crossSectionMaterial` | `Material` | – | – |
| Number Of Shatters | `numberOfShatters` | `int` | – | – |
| Add Slice Component To Pieces | `addSliceComponentToPieces` | `bool` | – | – |

### Objects To Shatter List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objects To Shatter | `objectsToShatter` | `List<GameObject>` | – | – |
| Use Custom Shatter Position | `useCustomShatterPosition` | `bool` | – | – |
| Custom Shatter Position | `customShatterPosition` | `Transform` | – | – |
| Use Random Radius On Shatter Position | `useRandomRadiusOnShatterPosition` | `bool` | – | – |
| Random Radius On Shatter | `randomRadiusOnShatter` | `float` | – | – |

### Tag and Layer Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Tag On Cut | `setNewTagOnCut` | `bool` | – | – |
| New Tag On Cut | `newTagOnCut` | `string` | – | – |
| Set New Layer On Cut | `setNewLayerOnCut` | `bool` | – | – |
| New Layer On Cut | `newLayerOnCut` | `string` | – | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Apply Force On Shatter | `applyForceOnShatter` | `bool` | – | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |
| Force To Apply To Cut Part | `forceToApplyToCutPart` | `float` | – | – |

### Others Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Shatter At Start | `activateShatterAtStart` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Shatter | `useEventOnShatter` | `bool` | – | – |
| Event On Shatter | `eventOnShatter` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateShatterOnObject()` | 対象を親から外し、`numberOfShatters`回`randomShatter`を実行してから破砕イベントを発火する。 |
| `randomShatter()` | 現在の破片リストを1回ずつ粉砕し、元オブジェクトを除去して生成された破片をリストへ追加する。 |
| `addObjectsToShatter(GameObject newObject)` | 未登録の場合のみ`objectsToShatter`へ追加するだけ。 |
| `randomShatterSingle(GameObject objectToShatter)` | カスタム/ランダム半径の位置で`shatterObject`を呼び、破片にコライダー・剛体・爆発力・タグ/レイヤーを設定して返す。 |
| `checkEventOnShatter()` | `useEventOnShatter`が有効なときだけ`eventOnShatter`を発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnShatter` | `UnityEvent` | – |
