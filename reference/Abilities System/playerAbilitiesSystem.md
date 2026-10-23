# playerAbilitiesSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/playerAbilitiesSystem.cs:6`

**概要**: プレイヤーのアビリティ一覧を保持し、選択・押下/押上入力、有効/無効化、クールダウンやエネルギー消費、UI連携をまとめて扱う中核コンポーネント。入力系は`input...`、実処理は`press...`と`confirm...`に分かれる。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Abilities System Enabled | `abilitiesSystemEnabled` | `bool` | true | – |
| Current Ability Index | `currentAbilityIndex` | `int` | – | – |
| Disable Ability System On First Person | `disableAbilitySystemOnFirstPerson` | `bool` | – | – |

### Energy Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Energy Stat Name | `energyStatName` | `string` | "Current Energy" | – |
| Ignore Use Of Energy | `ignoreUseOfEnergy` | `bool` | – | – |

### Abilities List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ability Info List | `abilityInfoList` | `List<abilityInfo>` | new List<abilityInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Abilities Mode Active | `abilitiesModeActive` | `bool` | – | – |
| Can Move | `canMove` | `bool` | – | – |
| Player Currently Busy | `playerCurrentlyBusy` | `bool` | – | – |
| Current Ability Info | `currentAbilityInfo` | `abilityInfo` | – | – |
| Cancelling Current Ability Press | `cancellingCurrentAbilityPress` | `bool` | – | – |
| Current Ability Name | `currentAbilityName` | `string` | – | – |
| Previous Ability Active Name | `previousAbilityActiveName` | `string` | – | – |
| Ability Input In Use | `abilityInputInUse` | `bool` | – | – |
| Pause Check Using Device On Ability Input | `pauseCheckUsingDeviceOnAbilityInput` | `bool` | – | – |
| Input Paused | `inputPaused` | `bool` | – | – |
| Selecting Ability | `selectingAbility` | `bool` | – | – |

### Abilities Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | – |
| Main Player Abilities UI System | `mainPlayerAbilitiesUISystem` | `playerAbilitiesUISystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getCanMove()` | 死亡状態と移動可否を確認して`canMove`を更新し返す。 |
| `setNextAbility()` | 有効な次アビリティを順に探して選択し、UIの選択表示も更新する。 |
| `setPreviousAbility()` | 有効な前アビリティを逆順に探して選択し、UIの選択表示も更新する。 |
| `setCurrentAbilityByName(string abilityName)` | 同名や時間制限中の禁止時は何もせず、指定名のアビリティへ切替える。 |
| `removeCurrentAbilityInfo()` | `currentAbilityInfo`を`null`にし`currentAbilityIndex`を-1にするだけ。 |
| `disableAbilityGroupByName(List<string> abilityNameList)` | 名前リストを無効化用の一括処理へ渡す薄いラッパー。 |
| `enableAbilityGroupByName(List<string> abilityNameList)` | 名前リストを有効化用の一括処理へ渡す薄いラッパー。 |
| `enableOrDisableAbilityGroupByName(List<string> abilityNameList, bool state)` | `state`に応じリストの各アビリティを名前指定で有効/無効化する。 |
| `enableAbilityByName(string abilityName)` | 指定名を有効化しホイール表示可にして`enableAbility`を呼ぶ。 |
| `disableAbilityByName(string abilityName)` | 指定名を無効化し現在アビリティなら別へ切替え、Dpadアイコンも更新する。 |
| `disableAllAbilites()` | 全アビリティを無効化しDpadアイコンを更新、退避名も空にする。 |
| `deactivateAllAbilites()` | 全アビリティを対象に`deactivateAllAbilities(false)`を呼ぶ。 |
| `deactivateAllCurrentlyActiveAbilities()` | 現在選択中か押下で有効なアビリティだけを非アクティブ化する。 |
| `deactivateAbilityByName(string abilityName)` | 指定名を非アクティブ化し、時間制限中ならCD起動か制限停止を行う。 |
| `setPauseCheckUsingDeviceOnAbilityInputState(bool state)` | `pauseCheckUsingDeviceOnAbilityInput`を設定するだけ。 |
| `togglePauseCheckUsingDeviceOnAbilityInputState()` | デバイス使用チェックの一時停止フラグを反転する。 |
| `activateCustomAction(string actionName)` | `mainPlayerController`のカスタムアクションを名前指定で起動する。 |
| `playerIsBusy()` | デバイス使用・アクション中・メニュー等を確認し多忙か返す。 |
| `isActionActive()` | `mainPlayerController`のアクション実行状態をそのまま返す。 |
| `isPlayerCurrentlyBusy()` | `playerIsBusy()`の結果を返すだけ。 |
| `checkIfAbilityCanBeActivated()` | 現在アビリティが地上限定でないか地上なら起動可能と返す。 |
| `getNumberOfAbilitiesAvailable()` | 有効なアビリティの個数を数えて返す。 |
| `getNumberOfAbilitiesCanBeShownOnWheelSelection()` | ホイール表示可フラグが立つアビリティの個数を返す。 |
| `getCurrentAbilityIndex()` | `isCurrentAbility`の要素番号を探し、無ければ-1を返す。 |
| `getCurrentAbilityIndexValue()` | `currentAbilityIndex`の値をそのまま返す。 |
| `getCurrentAbilityName()` | `currentAbilityName`をそのまま返す。 |
| `checkIfAbilitiesAvailable()` | 有効なアビリティが1つでもあるかを返す。 |
| `getAbilityByName(string abilityName)` | 名前一致の`abilityInfo`を返し、無ければ`null`を返す。 |
| `isAbilityInputInUse()` | `abilityInputInUse`をそのまま返す。 |
| `isAbilitiesModeActive()` | `abilitiesModeActive`をそのまま返す。 |
| `setAbilitesModeActiveState(bool state)` | `abilitiesModeActive`を設定するだけ。 |
| `usePowerBar(float powerAmount)` | エネルギー統計値を`powerAmount`だけ消費する。 |
| `isThereEnergyAvailable()` | エネルギー統計値が0より大きいかを返す。 |
| `checkIfAbilityNeedsEnergy()` | エネルギー無視や非使用時は真、必要量不足なら偽を返す。 |
| `checkAbilityUseEnergy()` | レート無しのエネルギー使用設定時に`usePowerBar`で消費する。 |
| `checkAbilityUseEnergyInUpdate(bool useEnergyOnAbility, bool useEnergyWithRate, float energyAmountUsed)` | レート消費設定時にエネルギーを消費し、不足時は偽を返す。 |
| `cancelPressAbility()` | `cancellingCurrentAbilityPress`を立てて押下処理を無効化する。 |
| `checkIfAbilitiesOnUseOrCooldown(string abilityName)` | 指定アビリティがクールダウン中か時間制限中かを返す。 |
| `setInputPausedState(bool state)` | `inputPaused`を設定するだけ。 |
| `inputSelectAndPressDownNewAbility(string abilityName)` | 入力を確認後、指定アビリティを選択して押下使用を実行する。 |
| `inputSelectAndPressDownNewAbilityTemporally(string abilityName, bool abilityIsTemporallyActivated, bool ignoreCheckMenusState)` | メニュー確認を一時無視し、分離/通常いずれかの押下使用を行う。 |
| `inputSelectAndPressDownNewSeparatedAbility(string abilityName)` | 現在名を`previousAbilityActiveName`へ退避してから指定を押下使用する。 |
| `inputSelectAndPressHoldNewSeparatedAbility()` | 入力を確認し、現在アビリティの押し続け使用を呼ぶ。 |
| `inputSelectAndPressUpNewSeparatedAbility()` | 押上使用を実行し、退避した前のアビリティへ戻す。 |
| `checkPreviousAbilityActive()` | 退避名があればチェック無しでそのアビリティへ戻し名前を空にする。 |
| `setSelectingAbilityActiveState(bool state)` | `selectingAbility`を設定するだけ。 |
| `inputPressDownUseCurrentAbility()` | 入力を確認後`abilityInputInUse`を立てて押下使用処理へ進む。 |
| `pressDownUseCurrentAbility()` | 多忙・無効・CD・エネルギー等を確認し、条件イベントか確定押下を呼ぶ。 |
| `confirmPressDownUseCurrentAbility()` | エネルギー消費、押下状態反転、イベント、更新とCD/制限起動を行う。 |
| `inputPressHoldUseCurrentAbility()` | 入力を確認し、現在アビリティの押し続け処理を呼ぶ。 |
| `pressHoldUseCurrentAbility()` | 各種チェック後、必要ならエネルギー消費して`useAbilityPressHold`を呼ぶ。 |
| `inputPressUpUseCurrentAbility()` | `abilityInputInUse`を下ろして押上使用処理を呼ぶ。 |
| `pressUpUseCurrentAbility()` | 各種チェック後、条件イベントか確定押上処理を呼ぶ。 |
| `confirmPressUpUseCurrentAbility()` | 押上状態を反転してイベント呼出し、更新停止とCD/制限起動を行う。 |
| `inputSetNextAbility()` | 入力を確認後`setNextAbility`を呼ぶ。 |
| `inputSetPreviousAbility()` | 入力を確認後`setPreviousAbility`を呼ぶ。 |
| `setAbilitiesSystemEnabledState(bool state)` | `abilitiesSystemEnabled`を設定するだけ。 |
| `isAbilitiesSystemEnabled()` | `abilitiesSystemEnabled`をそのまま返す。 |
| `enableOrDisableAllAbilities(bool state)` | `state`に応じ全アビリティを名前指定で有効/無効化する。 |
| `setAbilitiesSystemEnabledStateFromEditor(bool state)` | 有効状態を設定し`updateComponent`でシーンを更新する。 |
| `enableOrDisableAllAbilitiesFromEditor(bool state)` | 全アビリティをエディタ用に有効/無効化しシーンを更新する。 |
| `enableOrDisableAllAbilitiesCanBeShownOnWheelFromEditor(bool state)` | 全アビリティのホイール表示可否を設定しシーンを更新する。 |
| `setAbilitesModeActiveStateFromEditor(bool state)` | モード状態を設定し`updateComponent`でシーンを更新する。 |
