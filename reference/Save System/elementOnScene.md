# elementOnScene

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Save System/Elements On Scene/elementOnScene.cs:6`

**概要**: シーン上の1オブジェクトの位置・回転・アクティブ状態・統計値をセーブ対象として保持するコンポーネント。読込時はイベント発火とTransform復元を行い、`elementOnSceneManager`と連携する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save Element Enabled | `saveElementEnabled` | `bool` | true | – |
| Element Scene | `elementScene` | `int` | – | – |
| Element ID | `elementID` | `int` | – | – |
| Element Active State | `elementActiveState` | `bool` | true | – |

### Transform Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Save Position Values | `savePositionValues` | `bool` | – | – |
| Save Rotation Values | `saveRotationValues` | `bool` | – | – |
| Use Custom Transform | `useCustomTransform` | `bool` | – | – |
| Custom Transform | `customTransform` | `Transform` | – | – |

### Element Prefab Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Element Prefab ID | `elementPrefabID` | `int` | -1 | – |

### Element Stats Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Stats | `useStats` | `bool` | – | – |
| Load Stats Delay | `loadStatsDelay` | `float` | – | – |
| Stat Info List | `statInfoList` | `List<statInfo>` | new List<statInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Object Active | `useEventOnObjectActive` | `bool` | – | – |
| Event On Object Active | `eventOnObjectActive` | `UnityEvent` | – | – |
| Use Event On Object Inactive | `useEventOnObjectInactive` | `bool` | true | – |
| Event On Object Inactive | `eventOnObjectInactive` | `UnityEvent` | – | – |
| Use Delay For Event | `useDelayForEvent` | `bool` | – | – |
| Delay For Event | `delayForEvent` | `float` | – | – |
| Use Event Object Object Active Without Delay | `useEventObjectObjectActiveWithoutDelay` | `bool` | – | – |
| Event Object Object Active Without Delay | `eventObjectObjectActiveWithoutDelay` | `UnityEvent` | – | – |
| Use Event Object Object Inactive Without Delay | `useEventObjectObjectInactiveWithoutDelay` | `bool` | – | – |
| Event Object Object Inactive Without Delay | `eventObjectObjectInactiveWithoutDelay` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Use Element Prefab ID | `useElementPrefabID` | `bool` | – | – |
| Object Originally On Scene | `objectOriginallyOnScene` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setElementScene(int newValue)` | `elementScene`を設定するだけ。 |
| `setElementID(int newValue)` | `elementID`を設定するだけ。 |
| `setNewPositionValues(Vector3 newValue)` | 復元用の`newPosition`を設定するだけ。 |
| `setNewRotationValues(Vector3 newValue)` | 復元用の`newRotation`を設定するだけ。 |
| `setUseEventOnObjectActiveState(bool state)` | `useEventOnObjectActive`を設定するだけ。 |
| `setUseEventOnObjectInactive(bool state)` | `useEventOnObjectInactive`を設定するだけ。 |
| `setElementActiveState(bool state)` | `elementActiveState`を設定し、デバッグ時はオブジェクト名と状態を出力する。 |
| `setElementPrefabIDValue(int newValue)` | `elementPrefabID`を設定するだけ。 |
| `setNewInstantiatedElementOnSceneManagerIngame()` | 自身をアクティブにしてマネージャへ新規生成要素として登録する。無効なら何もしない。 |
| `setElementActiveStateToMainElementOnSceneManager(bool state)` | 状態を設定し、元からシーンにある要素なら一時状態を記録、生成物なら一覧から外して自身を破棄する。 |
| `setNewInstantiatedElementOnSceneManagerIngameWithInfo()` | マネージャを取得し、情報付きの新規生成要素として自身を登録する。 |
| `addNewElementOnSceneManager()` | マネージャへ自身を新規要素として追加する。`saveElementEnabled`がfalseなら何もしない。 |
| `checkStateOnLoad()` | 有効時、遅延設定に応じて状態復元を呼び、さらに遅延なしイベントを発火する。 |
| `activateStateOnLoadWithDelay()` | `delayForEvent`秒待ってから`activateStateOnLoad`を実行するコルーチンを開始する。 |
| `activateStateOnLoad()` | 状態に応じてアクティブ/非アクティブのイベントを発火し、位置と回転を保存値へ戻す。 |
| `getElementPosition()` | `useCustomTransform`ならそのTransform、なければ自身の位置を返す。 |
| `getElementRotation()` | `useCustomTransform`ならそのオイラー角、なければ自身のオイラー角を返す。 |
| `isSaveElementEnabled()` | `saveElementEnabled`を返すだけ。 |
| `setSaveElementEnabledState(bool state)` | `saveElementEnabled`を設定するだけ。 |
| `setObjectOriginallyOnSceneState(bool state)` | `objectOriginallyOnScene`を設定するだけ。 |
| `setStatsSearchingByInfo(int currentElementScene, int currentElementID)` | マネージャへシーン番号とIDを渡し、統計情報の検索を依頼する。 |
| `checkStatsStateOnLoad()` | 有効かつ`useStats`のとき、遅延値に応じて統計復元を即時または遅延で行う。 |
| `setStatsOnLoadWithDelay()` | `loadStatsDelay`秒待って`setStatsOnLoad`を呼ぶコルーチンを開始する。 |
| `setStatsOnLoad()` | アクティブかつ`useStats`のとき、各`statInfo`の初期化イベントへ保存値を渡す。 |
| `setCurrentStatNameToSave(string newValue)` | 保存対象の統計名`currentStatNameToCheck`を設定するだけ。 |
| `setCurrentFloatValueToSave(float newValue)` | 有効かつ`useStats`のとき、名前に一致する`statInfo`のfloat値を更新する。 |
| `setCurrentBoolValueToSave(bool newValue)` | 有効かつ`useStats`のとき、名前に一致する`statInfo`のbool値を更新する。 |
| `checkEventOnStatsSave()` | 各有効な`statInfo`名を設定し、種類に応じて値を取得するイベントを発火する。 |
| `setUseElementPrefabIDState(bool state)` | `useElementPrefabID`を設定するだけ。 |
| `addSingleElementOnSceneToManager()` | マネージャを取得し、`addSingleElementOnSceneToManager`へ自身を渡す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnObjectActive` | `UnityEvent` | – |
| `eventOnObjectInactive` | `UnityEvent` | – |
| `eventObjectObjectActiveWithoutDelay` | `UnityEvent` | – |
| `eventObjectObjectInactiveWithoutDelay` | `UnityEvent` | – |

## 内部型

- `statInfo`（class）
