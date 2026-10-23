# followObjectPositionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/followObjectPositionSystem.cs:5`

**概要**: `FixedUpdate`で`objectToFollow`の位置と回転を自身（または`mainTransform`）へ同期する追従コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Follow Object Active | `followObjectActive` | `bool` | true | – |
| Object To Follow | `objectToFollow` | `Transform` | – | – |
| Follow Position | `followPosition` | `bool` | true | – |
| Follow Rotation | `followRotation` | `bool` | true | – |
| Main Transform | `mainTransform` | `Transform` | – | – |
| Check If Object To Follow Null | `checkIfObjectToFollowNull` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Follow Located | `objectToFollowLocated` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setFollowObjectActiveState(bool state)` | `followObjectActive`を`state`にするだけ。 |
| `setEnabledState(bool state)` | コンポーネントの`enabled`を`state`にするだけ。 |
| `enabledStateAndUpdatePositionOnce()` | コンポーネントを有効化し、`updatePositionOnce`で一度だけ位置を合わせる。 |
| `updatePositionOnce()` | `objectToFollow`があれば、追従フラグに従って位置と回転を一度だけコピーする。 |
| `setObjectToFollow(Transform newObject)` | `objectToFollow`を`newObject`にするだけ。 |
| `setObjectToFollowFromEditor(Transform newObject)` | 追従対象を設定した上で`updateComponent`によりシーンを更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`でインスペクタとシーンを更新する。 |
