# quickPlayerModeChangeSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/quickPlayerModeChangeSystem.cs:6`

**概要**: 武器・能力・格闘などの「クイックモード」と、装備スロットに相当する「セレクション」の入力切替をまとめて扱うコンポーネント。モード名/セレクション名で現在の選択を切り替え、切替時イベントや射撃・ブロックの停止を行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Quick Change Enabled | `quickChangeEnabled` | `bool` | true | – |
| Min Wait Time To Change Mode | `minWaitTimeToChangeMode` | `float` | 0.3f | – |
| Use Inventory Quick Access Slots System | `useInventoryQuickAccessSlotsSystem` | `bool` | true | – |
| Check If Input Active Mode Press Up During Mode Complete Check | `checkIfInputActiveModePressUpDuringModeCompleteCheck` | `bool` | – | – |

### Mode Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Quick Mode Info List | `quickModeInfoList` | `List<quickModeInfo>` | new List<quickModeInfo> () | – |

### Selection List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Selection Info Enabled | `selectionInfoEnabled` | `bool` | – | – |
| Set Selection Info Enable State Enabled | `setSelectionInfoEnableStateEnabled` | `bool` | true | – |
| External Set Selection Info Enabled | `externalSetSelectionInfoEnabled` | `bool` | true | – |
| Check Current Selection Info On Start | `checkCurrentSelectionInfoOnStart` | `bool` | – | – |
| Set Selection Info When Enabled | `setSelectionInfoWhenEnabled` | `bool` | true | – |
| Min Wait Time To Change Selection | `minWaitTimeToChangeSelection` | `float` | 0.3f | – |
| Activate Selection On Start | `activateSelectionOnStart` | `bool` | – | – |
| Set Custom Selection Index On Start | `setCustomSelectionIndexOnStart` | `bool` | – | – |
| Custom Selection Index On Start | `customSelectionIndexOnStart` | `int` | – | – |
| Selection Info List | `selectionInfoList` | `List<selectionInfo>` | new List<selectionInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Current Mode Name | `currentModeName` | `string` | – | – |
| Change Of Mode In Process | `changeOfModeInProcess` | `bool` | – | – |
| Current Selection Info Index | `currentSelectionInfoIndex` | `int` | -1 | – |
| Current Selection Info Name | `currentSelectionInfoName` | `string` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Melee Weapons Grabbed Manager | `mainMeleeWeaponsGrabbedManager` | `meleeWeaponsGrabbedManager` | – | – |
| Main Bow System | `mainBowSystem` | `bowSystem` | – | – |
| Main Inventory Quick Access Slots System | `mainInventoryQuickAccessSlotsSystem` | `inventoryQuickAccessSlotsSystem` | – | – |
| Main Player States Manager | `mainPlayerStatesManager` | `playerStatesManager` | – | – |
| Main Other Powers | `mainOtherPowers` | `otherPowers` | – | – |
| Main Close Combat System | `mainCloseCombatSystem` | `closeCombatSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine` が null でなければ `StopCoroutine` で停止するだけ。 |
| `stopUpdateCheckChangeOfModeCoroutine()` | モード切替の監視コルーチンを停止し、切替中とセレクション有効のフラグを false に戻す。 |
| `setSelectionModeDisabled(string selectionName)` | `setSelectionModeEnabledOrDisabledState` を false で呼ぶだけ。 |
| `setSelectionModeEnabled(string selectionName)` | `setSelectionModeEnabledOrDisabledState` を true で呼ぶだけ。 |
| `setSelectionModeEnabledOrDisabledState(bool state, string selectionName)` | 名前でセレクションを探して `selectionEnabled` を設定し、現在の選択を無効化したら次へ切り替える。 |
| `checkToSelectNextSelectionOnWeaponAmmoEmpty()` | 武器モード中に現在の武器の残弾が0なら、次のセレクションへ切り替える。 |
| `setSelectionInfoEnabledState(bool state)` | `selectionInfoEnabled` を設定するだけ。 |
| `setSetSelectionInfoEnableStateEnabledState(bool state)` | `setSelectionInfoEnableStateEnabled` を設定するだけ。 |
| `setExternalSetSelectionInfoEnabledState(bool state)` | `externalSetSelectionInfoEnabled` を設定するだけ。 |
| `inputActiveModePressHold(string modeName)` | 長押し入力時、現在のモードが押下中でパワーなら `inputHoldShootPower` を呼ぶ。 |
| `checkIfModeActiveToReleaseIt()` | 押下中のモードがあれば `inputActiveModePressUp` を呼んで解放する。 |
| `inputActiveModePressUp(string modeName)` | 押下中モードの離上処理。武器・弓・パワー・格闘の射撃やブロックを止め `pressDownActive` を false にする。 |
| `inputActivateMode(string modeName)` | 名前からモードを検索して現在モードを切り替え、旧モードの射撃停止・選択解除イベント送出の後に `useMode` を呼ぶ。 |
| `inputActivateModeDownHoldUpExternally(string modeName)` | モード有効化・長押し・離上の3メソッドを順に呼ぶだけ。 |
| `inputSetNextOrPreviousSelectionInfo(bool state)` | 前/次の有効なセレクションを弾薬も見て探し、射撃を止めて現在の選択と表示を更新する。 |
| `setSelectionInfoEnabledStateFromEditor(bool state)` | `selectionInfoEnabled` を設定した後に `updateComponent` を実行する。 |
| `setSetSelectionInfoEnableStateEnabledStateFromEditor(bool state)` | `setSelectionInfoEnableStateEnabled` を設定し `updateComponent` を実行。 |
| `setExternalSetSelectionInfoEnabledStateFromEditor(bool state)` | `externalSetSelectionInfoEnabled` を設定し `updateComponent` を実行。 |

## 内部型

- `quickModeInfo`（class）
- `selectionInfo`（class）
