# playerHealthBarManagementSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/playerHealthBarManagementSystem.cs:7`

**概要**: プレイヤー側の体力バー管理。`healthSliderInfoList`で敵NPCの頭上スライダーを生成・更新し、オンスクリーンのメイン体力表示や親パネルの表示状態と同期する。

**公式ドキュメント抜粋**（[Player Health Bar Management System](../../docs/character-level-components/character/player-health-bar-management-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Sliders Active | `showSlidersActive` | `bool` | true | – |
| Disable Health Bars On Locked Camera | `disableHealthBarsOnLockedCamera` | `bool` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Layer For First Person | `layerForFirstPerson` | `LayerMask` | – | – |
| Layer For FBA | `layerForFBA` | `LayerMask` | – | – |
| Distance To Show Slider | `distanceToShowSlider` | `float` | 200 | – |
| Check Bar Type | `checkBarType` | `checkBarTypes` | – | – |
| Show Slider First Time Mode | `showSliderFirstTimeMode` | `showSliderModeFirstTime` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Manager Name | `mainManagerName` | `string` | "Health Bar Manager" | – |
| Main Panel Name | `mainPanelName` | `string` | "Health Bar Info" | – |
| Use Canvas Group On Icons | `useCanvasGroupOnIcons` | `bool` | – | – |

### Health Slider Info On Screen Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Health Slide Info On Screen | `useHealthSlideInfoOnScreen` | `bool` | – | – |
| Keep Health Bar Always Active If Show Slide On Screen | `keepHealthBarAlwaysActiveIfShowSlideOnScreen` | `bool` | true | – |
| Main Healt Slider Info On Screen Game Object | `mainHealtSliderInfoOnScreenGameObject` | `GameObject` | – | – |
| Main Healt Slider Info On Screen | `mainHealtSliderInfoOnScreen` | `AIHealtSliderInfo` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Show Sliders Paused | `showSlidersPaused` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Health Slider Info List | `healthSliderInfoList` | `List<healthSliderInfo>` | new List<healthSliderInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Healt Sliders Parent | `healtSlidersParent` | `Transform` | – | – |
| Health Bar Manager | `healthBarManager` | `healthBarManagementSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentHealthSliderState(bool state)` | 現在のスライダーを`state`で表示切替し`iconCurrentlyEnabled`も更新。オンスクリーン共有時は常に非表示。 |
| `disableHealhtBars()` | `enableOrDisableHealhtBars(false)`を呼び、全体力バーを非表示にするだけ。 |
| `enableHealhtBars()` | `enableOrDisableHealhtBars(true)`を呼び、全体力バーを再表示するだけ。 |
| `enableOrDisableHealhtBars(bool state)` | 一覧の全スライダーを`state`で表示/非表示にし、各`iconCurrentlyEnabled`を更新する。 |
| `addNewTargetSlider(GameObject sliderOwner, GameObject sliderPrefab, Vector3 sliderOffset, float healthAmount, float shieldAmount, string ownerName, Color textColor, Color sliderColor, int objectID, bool healthBarSliderActiveOnStart, bool useHealthSlideInfoOnScreenValue, bool useCircleHealthSlider)` | `sliderPrefab`から体力バーを生成して`objectID`で一覧に登録し、体力・シールド値と表示色を設定する。 |
| `removeTargetSlider(int objectID)` | `objectID`のスライダーを破棄して一覧から削除し、オンスクリーン対象ならメイン表示も消す。 |
| `removeElementFromListByPlayer(int objectID)` | `objectID`のスライダーを破棄し、`healthBarManager`の対象リストからもプレイヤー経由で削除する。 |
| `udpateSliderInfo(int objectID, string newName, Color textColor, Color backgroundColor)` | 対象の`nameText`をローカライズした`newName`と`textColor`に、背景を`backgroundColor`に更新する。 |
| `updateSliderAmount(int objectID, float value)` | 対象の体力スライダー値を`value`に更新し、表示中のオンスクリーン値にも反映する。 |
| `setSliderAmount(int objectID, float sliderValue)` | `updateSliderAmount`へそのまま転送するだけ。 |
| `updateShieldSliderAmount(int objectID, float value)` | 対象のシールドスライダー値を`value`に更新し、オンスクリーン側の値にも反映する。 |
| `setShieldSliderAmount(int objectID, float sliderValue)` | `updateShieldSliderAmount`へそのまま転送するだけ。 |
| `updateSliderMaxValue(int objectID, float newMaxValue)` | 対象の最大体力を更新し、円形時は`healthAmount`から割合を再計算してオンスクリーンにも反映する。 |
| `updateShieldSliderMaxValue(int objectID, float newMaxValue)` | 対象のシールド最大値を`newMaxValue`に更新し、オンスクリーン側の最大値も揃える。 |
| `updateSliderOffset(int objectID, float value)` | 対象の`sliderOffset`のY値だけを`value`に置き換える。 |
| `setSliderInfo(int objectID, string newName, Color textColor, Color backgroundColor)` | `udpateSliderInfo`へそのまま転送するだけ。 |
| `setSliderVisibleState(int objectID, bool state)` | 対象の`sliderCanBeShown`フラグを`state`にするだけ。 |
| `setSliderLocatedState(int objectID, bool state)` | 対象の`sliderOwnerLocated`フラグを`state`にするだけ。 |
| `pauseOrResumeShowHealthSliders(bool state)` | `showSlidersPaused`を設定し、親パネルの有効状態を反転してバー表示を一時停止/再開する。 |
| `pauseOrResumeShowHealthSlidersFromEditor(bool state)` | `pauseOrResumeShowHealthSliders`を呼んだ後`updateComponent`でシーンをダーティ更新する。 |
| `getPlayerGameObject()` | 保持している`playerGameObject`を返すだけ。 |
| `setShowSlidersActiveState(bool state)` | `showSlidersActive`フラグを`state`にするだけ。 |
| `setShowSlidersActiveStateFromEditor(bool state)` | 状態を設定した後`updateComponent`でシーンをダーティ更新するだけ。 |

## 内部型

- `checkBarTypes`（enum）
- `showSliderModeFirstTime`（enum）
