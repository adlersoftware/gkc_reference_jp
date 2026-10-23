# enableOrDisableObjectsOnDistanceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/enableOrDisableObjectsOnDistanceSystem.cs:6`

**概要**: カメラからの距離と画面内判定に応じて、登録オブジェクトの有効状態をまとめて切り替える管理コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Objects Active | `checkObjectsActive` | `bool` | true | – |
| Check For Null Objects | `checkForNullObjects` | `bool` | true | – |
| Max Distance Object Enabled On Screen | `maxDistanceObjectEnabledOnScreen` | `float` | – | – |
| Max Distance Object Enable Out Of Screen | `maxDistanceObjectEnableOutOfScreen` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Objects Paused | `showObjectsPaused` | `bool` | – | – |
| Is Manager Initialized | `isManagerInitialized` | `bool` | – | – |
| Object Info List | `objectInfoList` | `List<objectInfo>` | new List<objectInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 静的インスタンスを自身に設定する初期化で、既に別インスタンスがあれば自身の`GameObject`を破棄する。 |
| `enableOrDisableObject(bool state, int index)` | `objectInfoList[index]`を`state`でSetActiveし、対応する管理コンポーネントにも状態を通知する。 |
| `addObject(enableOrDisableObjectOnDistanceManager newEnableOrDisableObjectOnDistanceManager)` | 受け取った管理側から`objectInfo`を組み立てて`objectInfoList`に追加し、監視無効時は対象を非アクティブにする。 |
| `removeObject(Transform newTransform)` | `objectInfoList`から`objectTransform`が`newTransform`と一致する要素を探して削除する。 |
| `updateScreenValues()` | `screenWidth`と`screenHeight`を現在の`Screen`サイズで更新する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |

## 内部型

- `objectInfo`（class）
