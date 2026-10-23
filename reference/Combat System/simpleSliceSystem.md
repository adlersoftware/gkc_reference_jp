# simpleSliceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/Slice System/simpleSliceSystem.cs:6`

**概要**: キャラクタやオブジェクト単体のスライス処理を`sliceSystemUtils`へ委譲する簡易スライスコンポーネント。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slice Enabled | `sliceEnabled` | `bool` | true | – |
| Object To Slice | `objectToSlice` | `GameObject` | – | – |
| Alternate Prefab | `alternatePrefab` | `GameObject` | – | – |
| Infill Material | `infillMaterial` | `Material` | – | – |
| Main Surface To Slice | `mainSurfaceToSlice` | `surfaceToSlice` | – | – |
| Severables | `severables` | `Transform []` | new Transform [0] | – |

### Slice Ragdoll Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Prefabs Path | `prefabsPath` | `string` | "" | – |
| Slice Material | `sliceMaterial` | `Material` | – | – |
| Set Tag On Skeleton Rigidbodies | `setTagOnSkeletonRigidbodies` | `bool` | true | – |
| Tag On Skeleton Rigidbodies | `tagOnSkeletonRigidbodies` | `string` | "box" | – |

### Physics Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Update Last Object Speed | `ignoreUpdateLastObjectSpeed` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Destroy Original Object | `ignoreDestroyOriginalObject` | `bool` | – | – |
| Events On Ignore Destroy Original Object | `eventsOnIgnoreDestroyOriginalObject` | `UnityEvent` | – | – |
| Set Custom ID On Slice Spieces | `setCustomIDOnSliceSpieces` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Slice Initialized | `sliceInitialized` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getRandomString()` | 保持している`randomString`を返すだけ。 |
| `setRandomString(string newValue)` | `randomString`が空のときだけ指定文字列を設定する。 |
| `setRandomString()` | `setCustomIDOnSliceSpieces`が有効で空のとき、10〜20文字のランダムIDを生成する。 |
| `destroyAllSlicedPiecesByRandomString()` | ID設定が有効で`randomString`があるとき、同じIDの切断片をまとめて削除する。 |
| `initializeValuesOnHackableComponent()` | 未初期化なら`sliceSystemUtils`で初期化し、`sliceInitialized`をtrueにする。 |
| `setDestructionPending(bool state)` | `sliceSystemUtils.setDestructionPending`に破壊待ちフラグを渡すだけ。 |
| `activateSlice(Collider objectCollider, Vector3 newNormalInWorldSpaceValue, Vector3 positionInWorldSpace, Vector3 slicePosition, bool updateLastObjectSpeed, Vector3 lastSpeed)` | `useParticlesOnSlice`ならパーティクルを出し、当たり位置を求めて`sliceCharacter`で切断する。 |
| `searchBodyParts()` | 非トリガーのコライダー付き剛体を部位として集め、`severables`配列を作り直す。 |
| `setTagOnBodyParts(string newTag)` | `severables`内の全トランスフォームのタグを指定タグに変更する。 |
| `getMainAlternatePrefab()` | `alternatePrefab`を返すだけ。 |
| `getSeverables()` | `severables`配列を返すだけ。 |
| `setNewSeverablesList(GameObject newObject)` | 指定オブジェクトの`genericRagdollBuilder`のボーンから`severables`を作り直す。 |
| `createRagdollPrefab()` | `alternatePrefab`が未設定ならパスを取得してスライス用ラグドールプレハブを生成する。 |
| `setSliceEnabledState(bool state)` | `sliceEnabled`を設定し、有効化時は初期化を実行する。 |
| `setMainSurfaceToSlice(surfaceToSlice newSurface)` | `mainSurfaceToSlice`を差し替えるだけ。 |
| `setSliceEnabledStateFromEditor(bool state)` | `sliceEnabled`を設定して`GKC_Utils.updateComponent`とダーティ更新を行うエディタ用。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventsOnIgnoreDestroyOriginalObject` | `UnityEvent` | – |
