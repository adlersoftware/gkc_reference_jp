# playerHUDManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/playerHUDManager.cs:6`

**概要**: 車両乗車中に使うHUD管理コンポーネント。プレイヤーHUD・車両HUDの表示制御と、現在車両への体力/エネルギー/燃料/弾薬操作の橋渡し、HUD要素の有効/無効切り替えを担当する。

**公式ドキュメント抜粋**（[Player HUD Manager](../../docs/character-level-components/character/player-hud-manager.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player HUD Name | `playerHUDName` | `string` | "Player Info" | – |
| Player Bars Name | `playerBarsName` | `string` | "Player Bars" | – |
| Player Mode Name | `playerModeName` | `string` | "Player Mode" | – |
| Free Interaction Device Cursor | `freeInteractionDeviceCursor` | `GameObject` | – | – |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | true | – |

### HUD Element List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| HUD Element Info List | `HUDElementInfoList` | `List<HUDElementInfo>` | new List<HUDElementInfo> () | – |

### HUD Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player HUD | `playerHUD` | `GameObject` | – | – |
| Vehicle HUD | `vehicleHUD` | `GameObject` | – | – |
| Vehicle Health | `vehicleHealth` | `Slider` | – | – |
| Vehicle Boost | `vehicleBoost` | `Slider` | – | – |
| Vehicle Fuel | `vehicleFuel` | `Slider` | – | – |
| Vehicle Ammo | `vehicleAmmo` | `Slider` | – | – |
| Weapon Name | `weaponName` | `Text` | – | – |
| Ammo Info | `ammoInfo` | `Text` | – | – |
| Health Content | `healthContent` | `GameObject` | – | – |
| Energy Content | `energyContent` | `GameObject` | – | – |
| Ammo Content | `ammoContent` | `GameObject` | – | – |
| Fuel Content | `fuelContent` | `GameObject` | – | – |
| Vehicle Cursor | `vehicleCursor` | `GameObject` | – | – |
| Default Vehicle Cursor | `defaultVehicleCursor` | `Texture` | – | – |
| Default Vehicle Cursor Color | `defaultVehicleCursorColor` | `Color` | – | – |
| Default Vehicle Cursor Size | `defaultVehicleCursorSize` | `Vector2` | – | – |
| Speed Content | `speedContent` | `GameObject` | – | – |
| Current Speed | `currentSpeed` | `Text` | – | – |
| Vehicle Controls Menu | `vehicleControlsMenu` | `GameObject` | – | – |
| Vehicle Controls Menu Element | `vehicleControlsMenuElement` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setControlList(inputActionManager manager)` | 既存ボタンを破棄し、`showInControlsMenu` な入力軸ごとに操作表示を複製してメニューを閉じる。 |
| `setTouchingMenuPanelState(bool state)` | `fingerPressingTouchPanel` を設定するだけ。 |
| `isFingerPressingTouchPanel()` | `fingerPressingTouchPanel` の値を返すだけ。 |
| `openOrCloseControlsMenu(bool state)` | 状態が異なる場合のみ操作メニューの表示を切り替える。 |
| `setCurrentVehicleHUD(GameObject vehicle)` | 対象車両を保持し、その `vehicleHUDManager` を取得する。 |
| `closeControlsMenu()` | 現在車両があれば `IKDrivingManager` 経由で操作メニューを閉じる。 |
| `destroyCurrentVehicle()` | 搭乗中で未破壊なら、現在車両を破壊する。 |
| `damageCurrentVehicle(float damageAmount)` | 搭乗中で未破壊なら、現在車両にダメージを与える。 |
| `takeEnergyCurrentVehicle(float energyAmount)` | 搭乗中で未破壊なら、現在車両のエネルギーを減らす。 |
| `takeFuelCurrentVehicle(float fuelAmount)` | 搭乗中で未破壊なら、現在車両の燃料を減らす。 |
| `giveHealthCurrentVehicle(float healthAmount)` | 搭乗中で未破壊なら、現在車両の体力を回復する。 |
| `giveEnergyCurrentVehicle(float energyAmount)` | 搭乗中で未破壊なら、現在車両のエネルギーを回復する。 |
| `giveFuelCurrentVehicle(float fuelAmount)` | 搭乗中で未破壊なら、現在車両の燃料を回復する。 |
| `setInfiniteHealthCurrentVehicleState(bool state)` | 搭乗中で未破壊なら、現在車両の無敵状態を設定する。 |
| `setInfiniteEnergyCurrentVehicleState(bool state)` | 搭乗中で未破壊なら、現在車両の無限エネルギー状態を設定する。 |
| `setInfiniteFuelCurrentVehicleState(bool state)` | 搭乗中で未破壊なら、現在車両の無限燃料状態を設定する。 |
| `setInfiniteStatCurrentVehicleState(bool state)` | 体力・エネルギー・燃料の無限状態をまとめて設定する。 |
| `getHudElements()` | `hudElements` を返すだけ。 |
| `getVehicleCursor()` | `hudElements.vehicleCursor` を返すだけ。 |
| `setFreeInteractionDeviceCursorActiveState(bool state)` | 自由操作デバイス用カーソルの表示を、状態に合わせて切り替える。 |
| `enableOrDisableHUD(bool state)` | `playerHUDName` のHUD要素を、操作由来として切り替える。 |
| `enableOrDisablePlayerBars(bool state)` | `playerBarsName` のバー要素を、操作由来として切り替える。 |
| `enableOrDisablePlayerMode(bool state)` | `playerModeName` の要素を、操作由来として切り替える。 |
| `enableOrDisableHUDFromEditor(bool state)` | エディタ由来として `playerHUDName` の要素を切り替える。 |
| `enableOrDisablePlayerBarsFromEditor(bool state)` | エディタ由来として `playerBarsName` の要素を切り替える。 |
| `enableOrDisablePlayerModeFromEditor(bool state)` | エディタ由来として `playerModeName` の要素を切り替える。 |
| `enableOrDisableVehicleHUD(bool state)` | `vehicleHUD` の表示を状態に合わせて切り替える。 |
| `enableHUDElement(string elementName)` | 指定名のHUD要素を、操作由来で有効化する。 |
| `disableHUDElement(string elementName)` | 指定名のHUD要素を、操作由来で無効化する。 |
| `enableHUDElementFromEditor(string elementName)` | 指定名のHUD要素をエディタ由来で有効化し、有効フラグも立てる。 |
| `disableHUDElementFromEditor(string elementName)` | 指定名のHUD要素をエディタ由来で無効化し、有効フラグも下ろす。 |
| `enableOrDisableHUDElement(string elementName, bool state, bool usedFromEditor)` | 名前一致の要素の表示を切り替え、エディタ由来なら有効フラグも更新する。 |
| `isHUDElementEnabled(string elementName)` | 指定名の要素が有効として登録されているかを返す。 |

## 内部型

- `vehicleHUDElements`（class）
- `HUDElementInfo`（class）
