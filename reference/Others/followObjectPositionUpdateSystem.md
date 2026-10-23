# followObjectPositionUpdateSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/followObjectPositionUpdateSystem.cs:5`

**概要**: 指定した`objectToFollow`へ毎フレーム位置と回転を追従させる単純な追従コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Follow Object Active | `followObjectActive` | `bool` | true | – |
| Follow Position | `followPosition` | `bool` | true | – |
| Follow Rotation | `followRotation` | `bool` | true | – |
| Object To Follow | `objectToFollow` | `Transform` | – | – |
| Main Transform | `mainTransform` | `Transform` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Follow Located | `objectToFollowLocated` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setFollowObjectActiveState(bool state)` | `followObjectActive`に`state`を代入するだけ。 |
| `setObjectToFollow(Transform newObject)` | `objectToFollow`に`newObject`を代入するだけ。 |
| `setEnabledState(bool state)` | コンポーネントの`enabled`に`state`を代入するだけ。 |
| `setObjectToFollowFromEditor(Transform newObject)` | `setObjectToFollow`を呼んだ後に`updateComponent`でエディタ上の変更をシーンへ反映する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`を呼び、シーンをダーティとして保存対象にする。 |
