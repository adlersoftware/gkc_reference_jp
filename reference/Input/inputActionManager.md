# inputActionManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Input/inputActionManager.cs:6`

**概要**: `multiAxesList` の各アクションを毎フレーム判定してイベントを発火し、移動軸とマウス軸の値を公開する。手動制御・入力の上書き・タッチ操作との切替も扱う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Axis As Horizontal Movement Input | `useAxisAsHorizontalMovementInput` | `bool` | true | オンで横移動に入力軸をそのまま使い、オフでボタン値を補間。 |
| Use Axis As Vertical Movement Input | `useAxisAsVerticalMovementInput` | `bool` | true | オンで縦移動に入力軸をそのまま使い、オフでボタン値を補間。 |
| Horizontal Movement Input Lerp Speed | `horizontalMovementInputLerpSpeed` | `float` | 10 | 横移動値をボタン入力へ寄せる補間速度（毎秒の変化量）。 |
| Vertical Movement Input Lerp Speed | `verticalMovementInputLerpSpeed` | `float` | 5 | 縦移動値をボタン入力へ寄せる補間速度（毎秒の変化量）。 |

### Input State Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Actions | `showDebugActions` | `bool` | – | オンでアクション実行時に名前を`print`で出力。 |

### Manual Control Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Manual Control Active | `manualControlActive` | `bool` | – | オンで下の手動入力値を移動・カメラ軸として使用。 |
| Manual Horizontal Input | `manualHorizontalInput` | `float` | – | 手動制御時に使う横移動値（-1〜1）。 / 表示条件: `manualControlActive` がオンのとき / Range (-1, 1) |
| Manual Vertical Input | `manualVerticalInput` | `float` | – | 手動制御時に使う縦移動値（-1〜1）。 / 表示条件: `manualControlActive` がオンのとき / Range (-1, 1) |
| Manual Mouse Horizontal Input | `manualMouseHorizontalInput` | `float` | – | 手動制御時に使うマウス横軸の値（-1〜1）。 / 表示条件: `manualControlActive` がオンのとき / Range (-1, 1) |
| Manual Mouse Vertical Input | `manualMouseVerticalInput` | `float` | – | 手動制御時に使うマウス縦軸の値（-1〜1）。 / 表示条件: `manualControlActive` がオンのとき / Range (-1, 1) |
| Set Automatic Values On Horizontal Input | `setAutomaticValuesOnHorizontalInput` | `bool` | true | オンで横移動を手動値、オフで実際の入力値から取得。 / 表示条件: `manualControlActive` がオンのとき |
| Set Automatic Values On Vertical Input | `setAutomaticValuesOnVerticalInput` | `bool` | true | オンで縦移動を手動値、オフで実際の入力値から取得。 / 表示条件: `manualControlActive` がオンのとき |
| Set Automatic Values On Mouse Horizontal Input | `setAutomaticValuesOnMouseHorizontalInput` | `bool` | true | オンでマウス横軸を手動値、オフで実入力から取得。 / 表示条件: `manualControlActive` がオンのとき |
| Set Automatic Values On Vertical Vertical Input | `setAutomaticValuesOnVerticalVerticalInput` | `bool` | true | オンでマウス縦軸を手動値、オフで実入力から取得。 / 表示条件: `manualControlActive` がオンのとき |

### Touch Controls Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Touch Movement Joystick | `usingTouchMovementJoystick` | `bool` | true | タッチ端末でキーより仮想ジョイスティックを優先する。 / Use the touch joystick for control in preference to keys. |
| Enable Touch Joysticks | `enableTouchJoysticks` | `bool` | true | オンでタッチ移動ジョイスティックを有効にする。 |

### External Vehicle Touch Controls Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use External Vehicle Touch Controls Enabled | `useExternalVehicleTouchControlsEnabled` | `bool` | – | オンで乗り物乗降時にタッチ操作の切替イベントを実行。 |
| Disable Touch Joysticks On External Vehicle Enabled | `disableTouchJoysticksOnExternalVehicleEnabled` | `bool` | – | 乗り物操縦中はタッチの移動・カメラ操作を無効化する。 / 表示条件: `useExternalVehicleTouchControlsEnabled` がオンのとき |
| Event To Activate Touch Controls On External Vehicle | `eventToActivateTouchControlsOnExternalVehicle` | `UnityEvent` | – | 乗り物乗車時に呼び出す`UnityEvent`。 / 表示条件: `useExternalVehicleTouchControlsEnabled` がオンのとき |
| Event To Deactivate Touch Controls On External Vehicle | `eventToDeactivateTouchControlsOnExternalVehicle` | `UnityEvent` | – | 乗り物降車時に呼び出す`UnityEvent`。 / 表示条件: `useExternalVehicleTouchControlsEnabled` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `multiAxesList` | `List<multiAxes>` | new List<multiAxes> () | – |
| `inputActivated` | `bool` | – | – |
| `input` | `inputManager` | – | – |
| `inputCurrentlyActive` | `bool` | true | – |
| `inputPaused` | `bool` | – | – |
| `overrideInputValuesActive` | `bool` | – | – |
| `overrideInputAxisValue` | `Vector2` | – | – |
| `movementAxis` | `Vector2` | – | – |
| `mouseAxis` | `Vector2` | – | – |
| `rawMovementAxis` | `Vector2` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine` があれば停止するだけ。 |
| `setPositiveVerticalMovementAxisValue(int newValue)` | 上方向キーの押下フラグと垂直軸値を更新し、離した時に下方向が押されていれば-1を維持する。 |
| `setNegativeVerticalMovementAxisValue(int newValue)` | 下方向キーの押下フラグと垂直軸値を更新し、離した時に上方向が押されていれば1を維持する。 |
| `setPositiveHorizontalMovementAxisValue(int newValue)` | 右方向キーの押下フラグと水平軸値を更新し、離した時に左方向が押されていれば-1を維持する。 |
| `setNegativeHorizontalMovementAxisValue(int newValue)` | 左方向キーの押下フラグと水平軸値を更新し、離した時に右方向が押されていれば1を維持する。 |
| `getPlayerMovementAxis()` | 停止中や無効時はゼロを返し、手動制御や上書き中はその値、それ以外は`movementAxis` を返す。 |
| `getPlayerMouseAxis()` | 停止中や無効時はゼロを返し、手動制御中は手動マウス値と`mouseAxis` を設定に応じて混ぜて返す。 |
| `getPlayerRawMovementAxis()` | 生の移動軸を返し、手動制御時は-1/0/1に丸めた値、上書き時は上書き値の軸を返す。 |
| `resetMovementValues()` | `rawMovementAxis`、`movementAxis`、`mouseAxis` をゼロにするだけ。 |
| `enableOrDisableInput(bool state, GameObject driver)` | `inputActivated` を設定して更新コルーチンを再開始し、タッチ操作の設定を切替え、無効時は移動値とタッチ押下をリセットする。 |
| `pauseOrResumeInput(bool state)` | `inputPaused` を`state`にするだけ。 |
| `setInputCurrentlyActiveState(bool state)` | `inputCurrentlyActive` を`state`にするだけ。 |
| `overrideInputValues(Vector2 newInputValues, float newFootBrakeValue, float newHandBrakeValue, bool overrideState)` | 上書き用の軸値と`overrideInputValuesActive`、フット/ハンドブレーキ値をまとめて設定する。 |
| `getFootBrakeValue()` | `footBrake` を返すだけ。 |
| `getHandBrakeValue()` | `handBrake` を返すだけ。 |
| `setInputManager()` | `input` を自身・Instance・シーン検索の順で取得し、`multiAxesList` の件数を更新する。 |
| `isGameManagerPaused()` | `inputManager` が見つかっていればその`isGameManagerPaused` を返し、無ければfalseを返す。 |
| `getIsUsingTouchControlsValue()` | `inputManager` があればタッチ操作中かを返し、無ければfalseを返す。 |
| `setInputManagerOnEditor()` | `input` が未設定ならシーンから`inputManager` を探し、`updateComponent` を呼ぶ。 |
| `addNewAxes()` | `input` のマルチ軸名一覧を複製した新しい`multiAxes` をリストに追加し、シーンを更新する。 |
| `addNewAction(int multiAxesIndex)` | 指定マルチ軸に、対応するアクション名一覧を持つ空の`Axes` を追加してシーンを更新する。 |
| `updateMultiAxesList()` | 各`multiAxes` の名前から`input` 内のインデックスを引き直し、見つからなければ-1にして警告を出す。 |
| `updateAxesList(int multiAxesListIndex)` | 指定マルチ軸内の各アクションのインデックスと`keyButton` を`input` の定義から引き直す。 |
| `setAllAxesList(int multiAxesListIndex)` | 指定マルチ軸の`axes` を空にして、`input` のアクション定義から全件を作り直す。 |
| `setMultiAxesEnabledState(bool state)` | 全`multiAxes` の`currentlyActive` を`state`にし、シーンを更新する。 |
| `setAllActionsEnabledState(int multiAxesListIndex, bool state)` | 指定マルチ軸内の全アクションの`actionEnabled` を`state`にし、シーンを更新する。 |
| `setAxesActionName(int multiAxesIndex, int axesIndex)` | 指定アクションの`actionName` を`axesStringList` から設定し、インデックスが無効なら警告を出す。 |
| `updateComponent()` | `GKC_Utils.updateComponent` と`updateDirtyScene` でシーン更新を通知するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToActivateTouchControlsOnExternalVehicle` | `UnityEvent` | – |
| `eventToDeactivateTouchControlsOnExternalVehicle` | `UnityEvent` | – |

## 内部型

- `multiAxes`（class）
- `Axes`（class）
