# destroyGameObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/destroyGameObject.cs:5`

**概要**: オブジェクトを一定時間後や条件成立時に破棄、または非アクティブ化するコンポーネントで、プール返却や付随オブジェクトの同時処理にも対応する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Destroy Object Enabled | `destroyObjectEnabled` | `bool` | true | – |
| Destroy Object On Enable | `destroyObjectOnEnable` | `bool` | – | – |
| Timer | `timer` | `float` | 0.6f | – |
| Destroy Object At Start | `destroyObjectAtStart` | `bool` | true | – |
| Disable Instead Of Destroy Active | `disableInsteadOfDestroyActive` | `bool` | – | – |
| Destroy Just All Child Objects | `destroyJustAllChildObjects` | `bool` | – | – |

### Pooling Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Send Object To Pool System To Disable | `sendObjectToPoolSystemToDisable` | `bool` | – | – |
| Send Object By GKC Pooling Element To Disable | `sendObjectByGKC_PoolingElementToDisable` | `bool` | – | – |
| Main GKC Pooling Element | `mainGKC_PoolingElement` | `GKC_PoolingElement` | – | – |

### Objects To Destroy Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Destroy | `objectToDestroy` | `GameObject` | – | – |
| Use Game Object List | `useGameObjectList` | `bool` | – | – |
| Game Object List | `gameObjectList` | `List<GameObject>` | new List<GameObject> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Destroy Coroutine Active | `destroyCoroutineActive` | `bool` | – | – |
| Ignore Destroy Object Enabled | `ignoreDestroyObjectEnabled` | `bool` | – | – |
| Destroy Object Function Called | `destroyObjectFunctionCalled` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `destroyObjectInTime()` | 既存の破棄コルーチンを停止し、`timer` 秒後に破棄するコルーチンを開始する。 |
| `stopDestroyObjectCoroutine()` | 破棄コルーチンを停止し `destroyCoroutineActive` を false にする。 |
| `setTimer(float timeToDestroy)` | `timer` を設定するだけ。 |
| `destroy()` | 有効時に対象を破棄し、設定に応じて非アクティブ化・プール返却・子のみ破棄を選ぶ。 |
| `setDestroyObjectEnabledState(bool state)` | `destroyObjectEnabled` を設定するだけ。 |
| `setIgnoreDestroyObjectEnabledState(bool state)` | `ignoreDestroyObjectEnabled` を設定するだけ。 |
| `changeDestroyForSetActiveFunction(bool state)` | `disableInsteadOfDestroyActive` を設定するだけ。 |
| `setSendObjectToPoolSystemToDisableState(bool state)` | プール返却フラグを設定し、有効時は非アクティブ化設定も同時に有効にする。 |
| `checkToDestroyObjectInTime(bool callingFromStart)` | 未実行なら、起動時は `destroyObjectAtStart` を条件に、それ以外は無条件で破棄コルーチンを開始する。 |
| `cancelDestroy()` | `stopDestroyObjectCoroutine` を呼ぶだけ。 |
| `addObjectToGameObjectList(GameObject newObject)` | 未登録ならリストへ追加し、null 要素を取り除く。 |
| `setDestroyObjectEnabledStateFromEditor(bool state)` | 値を設定してから `updateComponent` でシーンを更新する。 |
| `addObjectToGameObjectListFromEditor(GameObject newObject)` | オブジェクトを追加してから `updateComponent` でシーンを更新する。 |
