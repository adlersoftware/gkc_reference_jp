# overrideInputManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Override System/overrideInputManager.cs:6`

**概要**: オーバーライド中の入力を管理するコンポーネント。マルチアクシスとアクションの定義・有効状態、入力の委譲、アクション画面の切替を行う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Input Enabled | `inputEnabled` | `bool` | – | ONの間だけ登録したアクション入力を処理する。 |
| Is Player Controller | `isPlayerController` | `bool` | – | ONならプレイヤー本体の入力として扱う。 |
| Player Input | `playerInput` | `playerInputManager` | – | 入力の読み取りに使う`playerInputManager`。 |
| Show Debug Actions | `showDebugActions` | `bool` | – | ONにすると押されたアクション名をログ出力する。 |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Destroy Object On Stop Override | `destroyObjectOnStopOverride` | `bool` | – | ONにするとオーバーライド終了時にイベントを呼ぶ。 |
| Event To Destroy | `eventToDestroy` | `UnityEvent` | – | オーバーライド終了時に呼ぶ後片付け用イベント。 / 表示条件: `destroyObjectOnStopOverride` がオンのとき |

### Main Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Override Function | `startOverrideFunction` | `UnityEvent` | – | オーバーライド開始時に実行するイベント。 |
| Stop Override Function | `stopOverrideFunction` | `UnityEvent` | – | オーバーライド終了時に実行するイベント。 |

### Pre Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Pre Override Functions | `usePreOverrideFunctions` | `bool` | – | ONにすると開始前の事前イベントを使う。 |
| Pre Start Override Function | `preStartOverrideFunction` | `UnityEvent` | – | オーバーライド開始直前に実行するイベント。 |
| Pre Stop Override Function | `preStopOverrideFunction` | `UnityEvent` | – | オーバーライド終了直前に実行するイベント。 |

### Action Screen Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Action Screen | `activateActionScreen` | `bool` | true | ONにすると操作中にアクション画面を表示する。 |
| Action Screen Name | `actionScreenName` | `string` | – | 表示するアクション画面の名前を指定する。 / 表示条件: `activateActionScreen` がオンのとき |

### Override Camera Controller

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Override Camera Controller Manager | `overrideCameraControllerManager` | `overrideCameraController` | – | オーバーライド中に使うカメラ制御の参照。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `multiAxesList` | `List<multiAxes>` | new List<multiAxes> () | – |
| `input` | `inputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`を停止するだけ。 |
| `getCustomRawMovementAxis()` | 入力が有効なら生の移動軸を、無効なら`Vector2.zero`を返す。 |
| `getCustomMovementAxis()` | 入力が有効なら移動軸を、無効なら`Vector2.zero`を返す。 |
| `getCustomMouseAxis()` | 入力が有効ならマウス軸を、無効なら`Vector2.zero`を返す。 |
| `setCustomInputEnabledState(bool state)` | カスタム入力の有効状態を設定し、コルーチンを止めたうえで有効時のみ入力監視コルーチンを開始する。 |
| `setPlayerInfo(GameObject player)` | 操作対象プレイヤーを設定し、入力管理・プレイヤー制御・オーバーライド制御系の参照を取得する。 |
| `overrideControlState(bool state, GameObject currentPlayer)` | 開始時は対象プレイヤーを設定して開始イベントを、終了時は終了イベントを実行し、入力状態とアクション画面を切り替える。 |
| `checkActivateActionScreen(bool state)` | `activateActionScreen`が有効なら、指定名のアクション画面を`state`に合わせて切り替える。 |
| `setPreOverrideControlState(bool state)` | `usePreOverrideFunctions`が有効なら、開始・終了に応じて事前オーバーライドイベントを発火する。 |
| `stopOverride()` | カスタム入力が有効なら、オーバーライド制御システムに現在の制御停止を依頼するだけ。 |
| `removeNewTemporalObjectFromOverrideControlSystem(GameObject newObject)` | 制御システムが設定されていれば、`newObject`を一時オブジェクトリストから削除する。 |
| `setPlayerInputActionState(bool playerInputActionState, string multiAxesInputName, string axesInputName)` | 指定マルチアクシス内の指定アクションの有効状態を`playerInputActionState`に設定する。 |
| `setPlayerInputMultiAxesState(bool playerInputMultiAxesState, string multiAxesInputName)` | 指定名のマルチアクシスの有効状態を`playerInputMultiAxesState`に設定するだけ。 |
| `enablePlayerInputMultiAxes(string multiAxesInputName)` | 指定名のマルチアクシスを有効にするだけ。 |
| `disablePlayerInputMultiAxes(string multiAxesInputName)` | 指定名のマルチアクシスを無効にするだけ。 |
| `isGamePaused()` | プレイヤー入力が割り当て済みならゲームポーズ状態を返し、未割り当てならfalseを返す。 |
| `addNewAxes()` | 入力マネージャーのマルチアクシス名を元に新しいマルチアクシスを追加し、コンポーネントを更新する。 |
| `addNewAction(int multiAxesIndex)` | 指定インデックスのマルチアクシスに、対応するアクション名を設定した新規アクションを追加して更新する。 |
| `updateMultiAxesList()` | 入力マネージャーの定義に合わせて各マルチアクシスの名前リストと名前を更新し、コンポーネントを更新する。 |
| `updateAxesList(int multiAxesListIndex)` | 指定マルチアクシス内の各アクションの名前リストを入力マネージャーの定義から再構築して更新する。 |
| `setAllAxesList(int multiAxesListIndex)` | 指定マルチアクシスのアクションを全削除し、入力マネージャーの全アクション定義から再作成して更新する。 |
| `setMultiAxesEnabledState(bool state)` | 全マルチアクシスの有効状態を`state`に設定してコンポーネントを更新する。 |
| `setAllActionsEnabledState(int multiAxesListIndex, bool state)` | 指定マルチアクシス内の全アクションの有効状態を`state`に設定して更新する。 |
| `getOverrideCameraControllerManager()` | `overrideCameraControllerManager`を返すだけ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`を呼ぶだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `startOverrideFunction` | `UnityEvent` | – |
| `stopOverrideFunction` | `UnityEvent` | – |
| `preStartOverrideFunction` | `UnityEvent` | – |
| `preStopOverrideFunction` | `UnityEvent` | – |
| `eventToDestroy` | `UnityEvent` | – |

## 内部型

- `multiAxes`（class）
- `Axes`（class）
