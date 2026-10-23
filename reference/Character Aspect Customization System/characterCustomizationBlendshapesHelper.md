# characterCustomizationBlendshapesHelper

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Character Aspect Customization System/characterCustomizationBlendshapesHelper.cs:5`

**概要**: ブレンドシェイプ値とアクセサリー構成を一時的に退避し、別のキャラクターモデルへ復元するための補助コンポーネントです。`characterCustomizationManager`を自動検索し、キャラクターモデルIDの取得と切り替えも提供します。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |
| Main Character Customization Manager | `mainCharacterCustomizationManager` | `characterCustomizationManager` | – | – |
| Main Character Model List Manager | `mainCharacterModelListManager` | `characterModelListManager` | – | – |

### Debug Temporal BlendShapes

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Temporal Blendshape Info List | `temporalBlendshapeInfoList` | `List<characterCustomizationManager.temporalBlendshapeInfo>` | new List<characterCustomizationManage… | – |

### Debug Temporal Accessories

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Temporal Current Accessories List | `temporalCurrentAccessoriesList` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Component Located | `componentLocated` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `storeBlendshapesCustomization()` | 必要ならマネージャーを探し、`getTemporalBlendshapeInfoList`の値と`getCurrentAccessoriesList`の内容を退避する。 |
| `setBlendshapeList()` | 退避したブレンドシェイプ値とアクセサリーリストをマネージャーへ渡して復元する。 |
| `checkMainCHaracterCustomizatationManager()` | 未検出なら`playerGameObject`から`characterCustomizationManager`を取得し、`componentLocated`を更新する。 |
| `setPlayerGameObject(GameObject newObject)` | 別のオブジェクトなら`playerGameObject`に代入し、マネージャーを再取得する。 |
| `getCurrentCharacterModelID()` | `mainCharacterModelListManager`があれば現在のモデルIDを返し、無ければ-1を返す。 |
| `setCurrentCharacterModelID(int newID)` | `mainCharacterModelListManager`があれば`replaceCharacterModelByID`でモデルを差し替えるだけ。 |
