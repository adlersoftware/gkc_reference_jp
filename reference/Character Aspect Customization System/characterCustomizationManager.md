# characterCustomizationManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Character Aspect Customization System/characterCustomizationManager.cs:6`

**概要**: キャラクターの外見を管理する中核コンポーネントで、`characterObjectTypeInfoList`の装備パーツ、`characterAccessoriesTypeInfoList`のアクセサリー、`characterBlendShapeTypeInfoList`のブレンドシェイプを切り替えます。現在装備中の`currentPiecesList`と`currentAccessoriesList`を保持し、テンプレート適用や一人称視点時のメッシュ非表示も扱います。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Customization Enabled | `characterCustomizationEnabled` | `bool` | true | – |
| Object Category Name | `objectCategoryName` | `string` | "Object" | – |
| Blend Shapes Category Name | `blendShapesCategoryName` | `string` | "BlendShapes" | – |
| Accessories Category Name | `accessoriesCategoryName` | `string` | "Accessories" | – |

### Main Character Base Model Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Character Base Info | `mainCharacterBaseInfo` | `characterObjectTypeInfo` | – | – |

### Character Sets Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Object Type Info List | `characterObjectTypeInfoList` | `List<characterObjectTypeInfo>` | new List<characterObjectTypeInfo> () | – |

### Character Accesories Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Accessories Type Info List | `characterAccessoriesTypeInfoList` | `List<characterObjectTypeInfo>` | new List<characterObjectTypeInfo> () | – |

### Character Blend Shapes Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Blend Shape Type Info List | `characterBlendShapeTypeInfoList` | `List<characterBlendShapeTypeInfo>` | new List<characterBlendShapeTypeInfo> () | – |

### Head Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Object Name | `headObjectName` | `string` | "Head" | – |
| Objects On Head List | `objectsOnHeadList` | `List<string>` | new List<string> () | – |

### Body Parts Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Multiple Body Parts Info List | `useMultipleBodyPartsInfoList` | `bool` | – | – |
| Multiple Body Parts Info List | `multipleBodyPartsInfoList` | `List<multipleBodyPartsInfo>` | new List<multipleBodyPartsInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Keep All Character Meshes Disabled Active | `keepAllCharacterMeshesDisabledActive` | `bool` | – | – |
| Head Active Temporaly | `headActiveTemporaly` | `bool` | – | – |

### Current Elements Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Pieces List | `currentPiecesList` | `List<string>` | new List<string> () | – |
| Current Accessories List | `currentAccessoriesList` | `List<string>` | new List<string> () | – |
| Temporal Blendshape Info List | `temporalBlendshapeInfoList` | `List<temporalBlendshapeInfo>` | new List<temporalBlendshapeInfo> () | – |

### Editor Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Armor Set To Create Piece Meshes Objects | `armorSetToCreatePieceMeshesObjects` | `string` | – | – |

### Durability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Durability Affected Enabled | `useEventOnDurabilityAffectedEnabled` | `bool` | – | – |
| Durability Part Info List | `durabilityPartInfoList` | `List<durabilityPartInfo>` | new List<durabilityPartInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Transform | `characterTransform` | `Transform` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `resetAllCharacterObjectstoMainBaseModel()` | アクセサリーと全キャラクターオブジェクトを無効化してリストを空にし、`mainCharacterBaseInfo`のベースメッシュをすべて表示する。 |
| `setCustomizationFromTemplate(characterAspectCustomizationTemplate newCharacterAspectCustomizationTemplate, bool isFullSet)` | `isFullSet`ならベースモデルに戻してから、テンプレート内の全オプションを順に適用する。 |
| `checkDisableAccessoryByNameAndCategory(string categoryName, string objectName)` | 指定カテゴリと名前のアクセサリーを探し、装備中パーツの`disableAccesoriesSameTypeName`が有効なら同`typeName`のアクセサリーを非表示にする。 |
| `setObjectState(bool boolValue, string objectName, bool disableOtherObjects, string categoryOfObjectsToDisable, bool equippingObject)` | 指定カテゴリの他の装備を外したうえで対象の表示と装備リストを更新し、対象が見つかったかを返す。 |
| `setBlendShapeValue(string blendShapeName, float blendShapeValue, bool useRandomFloatValue, float sliderMaxValue)` | 指定名の値を`blendShapeLimits`内にクランプし、`sliderMaxValue`で正規化してメッシュに設定する。 |
| `getBlendShapeValue(string blendShapeName, float sliderMaxValue)` | 指定名の現在のブレンドシェイプ値を取得し、`blendShapeLimits.y / sliderMaxValue`でスライダー比に変換して返す。無ければ-1。 |
| `getExtraTypeNameListObjectByName(string objectName)` | パーツまたはアクセサリーから`useExtraTypeNameList`が有効な同名項目を探し、その`extraTypeNameList`を返す。無ければnull。 |
| `setEditActiveState(bool state)` | 本体が空で何もしない。 |
| `getTemporalBlendshapeInfoList()` | `temporalBlendshapeInfoList`をクリアし、全ブレンドシェイプの現在値を`temporalBlendshapeInfo`として収集して返す。 |
| `enableOrDisableHeadTemporaly(bool state)` | 頭のベースメッシュを一時的に表示/非表示し、装備中の頭パーツも反転させて`headActiveTemporaly`を更新する。 |
| `checkCameraViewToFirstOrThirdPerson(bool state)` | 一人称時は装備パーツとアクセサリーを非表示、三人称復帰時は表示に戻し、`keepAllCharacterMeshesDisabledActive`を設定する。 |
| `checkEquippedStateOnObject(bool state, string objectName, string categoryName)` | 装備/解除に合わせて同`typeName`のアクセサリーとベースメッシュを反転し、`ignoreDisableSameTypeName`などで対象を絞り込む。 |
| `setBlendshapeList(List<temporalBlendshapeInfo> newTemporalBlendshapeInfoList)` | 各`temporalBlendshapeInfo`の名前と値を`setBlendShapeValue`で順に適用してブレンドシェイプを復元するだけ。 |
| `getCurrentPiecesList()` | `currentPiecesList`をそのまま返すだけ。 |
| `getCurrentAccessoriesList()` | `currentAccessoriesList`をそのまま返すだけ。 |
| `setCurrentAccessoriesList(List<string> newTemporalAccessoriesList)` | リストを差し替え、含まれるアクセサリーを表示して`checkDisableAccessoryByNameAndCategory`を呼ぶ。 |
| `getArmorClothPieceByName(string categoryName)` | `currentPiecesList`内で指定`typeName`に一致する最初のパーツ名を返し、無ければ空文字を返す。 |
| `getArmorClothCategoryByName(string objectName)` | パーツ名から`typeName`を検索して返し、見つからなければ空文字を返す。 |
| `checkIfArmorPartCanBeEquippedOnSameBodyPart(string objectName)` | 同`typeName`の装備中パーツを調べ、同時装備が許可されていればその名前、無ければ競合一覧を返す。 |
| `checkIfObjectAlreadyOnCurrentPiecesList(string pieceName)` | `currentPiecesList`に含まれるかどうかを返すだけ。 |
| `checkEventOnDurabilityAffected(string bodyPartName)` | `useEventOnDurabilityAffectedEnabled`が有効なら、同名の`durabilityPartInfo`の耐久イベントを呼び出す。 |
| `setCharacterTransform(Transform newTransform)` | `characterTransform`が未設定のときだけ代入し、`mainAnimator`も未設定なら`Animator`を取得する。 |
| `renamePiece(string currentObjectName, string newObjectName)` | 一致するパーツの`Name`を`newObjectName`に変更し、見つかった場合はコンポーネントを更新する。 |
| `createPieceMeshesObjectsFromSetByName()` | 指定セットの各パーツを生成し、`GKC_Utils.createPieceMeshesObjectsFromSetByName`でメッシュを作るエディタ用処理。 |
| `checkCameraViewToFirstOrThirdPersonOnEditor(bool state)` | `keepAllCharacterMeshesDisabledActive`を設定してエディタ上のコンポーネントを更新するだけ。 |

## 内部型

- `characterObjectInfo`（class）
- `characterObjectTypeInfo`（class）
- `characterBlendShapeInfo`（class）
- `characterBlendShapeTypeInfo`（class）
- `temporalBlendshapeInfo`（class）
- `durabilityPartInfo`（class）
- `multipleBodyPartsInfo`（class）
