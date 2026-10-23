# healthBarManagementSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/healthBarManagementSystem.cs:6`

**概要**: シーン内の体力バーを管理するシングルトンで、`healthSliderInfoList`にスライダー情報を保持し、登録された各`playerHealthBarManagementSystem`へ値や表示状態を一括転送する。`showSlidersActive`が偽の場合は大半のメソッドが早期リターンする。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Sliders Active | `showSlidersActive` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Health Slider Info List | `healthSliderInfoList` | `List<healthSliderInfo>` | new List<healthSliderInfo> () | – |
| Player Health Bar Management System List | `playerHealthBarManagementSystemList` | `List<playerHealthBarManagementSystem>` | new List<playerHealthBarManagementSys… | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 既に初期化済みなら戻り、別インスタンスがあれば自身を`Destroy`、なければ`Instance`に自身を登録する。 |
| `addNewPlayer(playerHealthBarManagementSystem newPlayer)` | `showSlidersActive`なら一覧に追加し、保持している全スライダー情報を新しいプレイヤーへ登録し直す。 |
| `disableHealhtBars()` | `showSlidersActive`なら`enableOrDisableHealhtBars(false)`を呼ぶだけ。 |
| `enableHealhtBars()` | `showSlidersActive`なら`enableOrDisableHealhtBars(true)`を呼ぶだけ。 |
| `enableOrDisableHealhtBars(bool state)` | 全`playerHealthBarManagementSystem`に`state`を渡し、体力バーの表示を一括で切り替える。 |
| `addNewTargetSlider(GameObject sliderOwner, GameObject sliderPrefab, Vector3 sliderOffset, float healthAmount, float shieldAmount, string ownerName, Color textColor, Color sliderColor, bool healthBarSliderActiveOnStart, bool useHealthSlideInfoOnScreen, bool useCircleHealthSlider)` | `showSlidersActive`なら`healthSliderInfo`を作成して採番し、全プレイヤーへ登録してIDを返す。 |
| `removeTargetSlider(int objectID)` | 全プレイヤーから`objectID`のスライダーを削除し、`healthSliderInfoList`から該当IDの要素も除去する。 |
| `removeElementFromObjectiveListCalledByPlayer(int objectId, GameObject currentPlayer)` | 一覧から`objectId`の要素を消し、`currentPlayer`以外のプレイヤーからも同じスライダーを削除する。 |
| `udpateSliderInfo(int objectID, string newName, Color textColor, Color backgroundColor)` | 全プレイヤーの`setSliderInfo`を呼び、名前と文字色・背景色を一括更新する。 |
| `updateSliderAmount(int objectID, float value)` | 全プレイヤーの`setSliderAmount`を呼び、体力スライダーの値を更新する。 |
| `setSliderAmount(int objectID, float sliderValue)` | `updateSliderAmount`へそのまま転送するだけ。 |
| `updateShieldSliderAmount(int objectID, float value)` | 全プレイヤーの`setShieldSliderAmount`を呼び、シールドスライダーの値を更新する。 |
| `setShieldSliderAmount(int objectID, float sliderValue)` | `updateShieldSliderAmount`へそのまま転送するだけ。 |
| `updateSliderMaxValue(int objectID, float maxSliderValue)` | 全プレイヤーの体力スライダー最大値を`maxSliderValue`に更新する。 |
| `updateShieldSliderMaxValue(int objectID, float maxSliderValue)` | 全プレイヤーのシールドスライダー最大値を`maxSliderValue`に更新する。 |
| `updateSliderOffset(int objectID, float value)` | 全プレイヤーの`updateSliderOffset`を呼ぶだけで、`showSlidersActive`は確認しない。 |
| `setSliderInfo(int objectID, string newName, Color textColor, Color backgroundColor)` | `udpateSliderInfo`へそのまま転送するだけ。 |
| `setSliderVisibleStateForPlayer(int objectID, GameObject player, bool state)` | `player`が一致するプレイヤーに限り、`setSliderVisibleState`でスライダー表示を切り替える。 |
| `setSliderLocatedState(int objectID, bool state)` | 全プレイヤーのスライダー配置状態を`state`に設定する。 |
| `setSliderLocatedStateForPlayer(int objectID, GameObject player, bool state)` | `player`が一致するプレイヤーに限り、スライダー配置状態を`state`に設定する。 |
| `setSliderVisibleState(int objectID, bool state)` | 全プレイヤーのスライダー表示状態を`state`に設定する。 |
| `pauseOrResumeShowHealthSliders(bool state)` | 全プレイヤーの`pauseOrResumeShowHealthSliders`を呼び、体力バーの表示を一時停止／再開する。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |
