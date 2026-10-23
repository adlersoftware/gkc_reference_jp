# playerStatesManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/playerStatesManager.cs:7`

**概要**: プレイヤーのモード（`playersMode`）と操作モード（`playerControlList`）の切り替え、モードメニューの開閉、各コンポーネントの一括有効化/無効化を担う管理クラス。

**公式ドキュメント抜粋**（[Player States Manager](../../docs/player-controller-components/player-controller/player-states-manager.md)）

> It allows you to configure different modes for the character and change between them in-game through input or events, like having a weapons mode, powers mode, close combat mode, melee weapons mode, simple mode without nothing extra or special to activate, etc...Basically, a list of states with events to trigger for each one.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Player Modes Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Mode By Input Enabled | `changeModeByInputEnabled` | `bool` | true | ONにすると入力操作でプレイヤーモードを切り替えられる。 |
| Change Mode Enabled | `changeModeEnabled` | `bool` | true | OFFにするとモード変更を禁止し既定モードに固定する。 / If enabled players will be able to change mode, for example, they will be able to change between weapon and power mode. If disabled players will forever be in the default mode. |

### Player Control Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Open Player Mode Menu Enabled | `openPlayerModeMenuEnabled` | `bool` | true | ONにすると操作モード選択メニューを開ける。 |
| Change Player Control Enabled | `changePlayerControlEnabled` | `bool` | true | ONにすると操作モードを次のものへ切り替えられる。 |
| Can Set Regular Mode Active | `canSetRegularModeActive` | `bool` | true | ONなら運転中やデバイス使用中は操作モードを変えさせない。 |
| Close Menu When Mode Selected | `closeMenuWhenModeSelected` | `bool` | true | モードを選んだ時にメニューを自動で閉じる。 |
| Use Blur UI Panel | `useBlurUIPanel` | `bool` | true | ONにするとメニュー表示中に背景をブラー表示する。 |
| Switch Between Player Controls Enabled | `switchBetweenPlayerControlsEnabled` | `bool` | – | ONならメニューを開かず入力で次の操作モードへ送る。 |
| Menu Panel Name | `menuPanelName` | `string` | "Player States Manager" | `menuPause`でメニューを識別するためのパネル名。 |

### Player's Mode and Control Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Default Players Mode | `useDefaultPlayersMode` | `bool` | – | ONにすると開始時のモードを名前で指定できる。 |
| Default Players Mode Name | `defaultPlayersModeName` | `string` | "Weapons" | 開始時に選択するプレイヤーモードの名前。 / 表示条件: `useDefaultPlayersMode` がオンのとき |
| Default Control State Name | `defaultControlStateName` | `string` | "Regular Mode" | 開始時と復帰時に使う操作モードの名前。 |
| Use Random Player Mode On Start | `useRandomPlayerModeOnStart` | `bool` | – | ONにすると開始時のモードをランダムに選ぶ。 |
| Use Random Player Mode On Start From Custom List | `useRandomPlayerModeOnStartFromCustomList` | `bool` | – | ONならランダム候補をカスタムリストから選ぶ。 / 表示条件: `useRandomPlayerModeOnStart` がオンのとき |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Enable Components | `eventToEnableComponents` | `UnityEvent` | – | 全コンポーネントを有効化した時に呼ぶイベント。 / 表示条件: `showEventsSettings` がオンのとき |
| Event To Disable Components | `eventToDisableComponents` | `UnityEvent` | – | 全コンポーネントを無効化した時に呼ぶイベント。 / 表示条件: `showEventsSettings` がオンのとき |
| Use Event If System Disabled | `useEventIfSystemDisabled` | `bool` | – | ONにするとシステム無効開始時に専用イベントを呼ぶ。 / 表示条件: `showEventsSettings` がオンのとき |
| Event If System Disabled | `eventIfSystemDisabled` | `UnityEvent` | – | システムが無効のまま開始した時に呼ぶイベント。 / 表示条件: `showEventsSettings.boolValue && useEventIfSystemDisabled.boolValue` |

### Player Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Player Mode Text | `currentPlayerModeText` | `Text` | – | 現在のプレイヤーモード名を表示するUIテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Pause Manager | `pauseManager` | `menuPause` | – | メニューやブラーを制御する`menuPause`の参照。 / 表示条件: `showElementSettings` がオンのとき |
| Player Control Mode Menu | `playerControlModeMenu` | `GameObject` | – | 開閉する操作モード選択メニューのGameObject。 / 表示条件: `showElementSettings` がオンのとき |
| Current Player Control Mode Image | `currentPlayerControlModeImage` | `RawImage` | – | 現在の操作モードの画像を表示する`RawImage`。 / 表示条件: `showElementSettings` がオンのとき |
| Powers Manager | `powersManager` | `otherPowers` | – | パワー照準の解除に使う`otherPowers`の参照。 / 表示条件: `showElementSettings` がオンのとき |
| Grab Manager | `grabManager` | `grabObjects` | – | モード変更時に掴んだ物を落とす`grabObjects`。 / 表示条件: `showElementSettings` がオンのとき |
| Scanner Manager | `scannerManager` | `scannerSystem` | – | モード変更時にスキャンを止める`scannerSystem`。 / 表示条件: `showElementSettings` がオンのとき |
| Player Manager | `playerManager` | `playerController` | – | モード変更可否の判定に使う`playerController`。 / 表示条件: `showElementSettings` がオンのとき |
| Player Camera Manager | `playerCameraManager` | `playerCamera` | – | 一人称切替などに使う`playerCamera`の参照。 / 表示条件: `showElementSettings` がオンのとき |
| Gravity Manager | `gravityManager` | `gravitySystem` | – | 一人称時の重力演出を切り替える`gravitySystem`。 / 表示条件: `showElementSettings` がオンのとき |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | 武器の所持状態からモード変更可否を判定する。 / 表示条件: `showElementSettings` がオンのとき |
| Combat Manager | `combatManager` | `closeCombatSystem` | – | 有効/無効を連動して切り替える`closeCombatSystem`。 / 表示条件: `showElementSettings` がオンのとき |
| IK System Manager | `IKSystemManager` | `IKSystem` | – | IK状態のリセットと有効化を行う`IKSystem`。 / 表示条件: `showElementSettings` がオンのとき |
| Using Devices Manager | `usingDevicesManager` | `usingDevicesSystem` | – | デバイス使用状態を扱う`usingDevicesSystem`。 / 表示条件: `showElementSettings` がオンのとき |
| Override Element Manager | `overrideElementManager` | `overrideElementControlSystem` | – | 操作上書きを止める`overrideElementControlSystem`。 / 表示条件: `showElementSettings` がオンのとき |
| Head Bob Manager | `headBobManager` | `headBob` | – | 一人称/三人称で揺れ設定を切り替える`headBob`。 / 表示条件: `showElementSettings` がオンのとき |
| Damage In Screen Manager | `damageInScreenManager` | `damageInScreen` | – | 被ダメージ表示を一時停止する`damageInScreen`。 / 表示条件: `showElementSettings` がオンのとき |
| Main Upper Body Rotation System | `mainUpperBodyRotationSystem` | `upperBodyRotationSystem` | – | 有効状態を連動させる`upperBodyRotationSystem`。 / 表示条件: `showElementSettings` がオンのとき |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | 有効状態を連動させる`findObjectivesSystem`。 / 表示条件: `showElementSettings` がオンのとき |
| Main AI Nav Mesh | `mainAINavMesh` | `AINavMesh` | – | AIナビ移動の有効状態を連動させる`AINavMesh`。 / 表示条件: `showElementSettings` がオンのとき |
| Main Oxygen System | `mainOxygenSystem` | `oxygenSystem` | – | 一人称切替時に通知する`oxygenSystem`の参照。 / 表示条件: `showElementSettings` がオンのとき |
| Main Player Abilities System | `mainPlayerAbilitiesSystem` | `playerAbilitiesSystem` | – | モード変更時に停止する`playerAbilitiesSystem`。 / 表示条件: `showElementSettings` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `playersMode` | `List<playerMode>` | new List<playerMode> () | – |
| `currentPlayersModeName` | `string` | – | – |
| `playerControlList` | `List<playerControl>` | new List<playerControl> () | – |
| `currentControlStateName` | `string` | – | – |
| `audioSourceList` | `List<audioSourceInfo>` | new List<audioSourceInfo> () | – |
| `menuOpened` | `bool` | – | – |
| `playerStateInfoList` | `List<playerStateInfo>` | new List<playerStateInfo> () | – |
| `randomPlayerModeOnStartCustomList` | `List<string>` | new List<string> () | – |
| `mainRagdollActivator` | `ragdollActivator` | – | – |
| `mainFootStepManager` | `footStepManager` | – | – |
| `showElementSettings` | `bool` | – | – |
| `showEventsSettings` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkUseRandomPlayerModeOnStart()` | 有効ならランダムなモード名を選び `defaultPlayersModeName` に設定する。 |
| `isUseRandomPlayerModeOnStartActive()` | `useRandomPlayerModeOnStart` の値を返すだけ。 |
| `setDefaultPlayersModeAsCurrentOne()` | `defaultPlayersModeName` が空でなければ `setPlayerModeByName` でそのモードへ切り替える。 |
| `checkEventOnSystemDisabled()` | `useEventIfSystemDisabled` が有効なら `eventIfSystemDisabled` を発火するだけ。 |
| `setInitialPlayerModeByNameFromEditor(string modeName)` | 指定名の有効なモードを現在のモードとして反映し、コンポーネントを更新する。 |
| `enableOrDisablePlayerModeByNameFromEditor(string modeName, bool state)` | 指定名のモードの `modeEnabled` を設定してコンポーネントを更新する。 |
| `enablePlayerModeByNameFromEditor(string modeName)` | `enableOrDisablePlayerModeByNameFromEditor` をtrueで呼ぶだけ。 |
| `disablePlayerModeByNameFromEditor(string modeName)` | `enableOrDisablePlayerModeByNameFromEditor` をfalseで呼ぶだけ。 |
| `openOrCloseControlMode(bool state)` | ポーズメニューや武器状態を確認し、可能なら操作モードメニューの表示とポーズ・車両カメラを `state` に合わせて開閉する。 |
| `openOrCLoseControlModeMenuFromTouch()` | `menuOpened` を反転して `openOrCloseControlMode` を呼ぶ。 |
| `toogleCurrentControlMode(string controlModeNameToCheck)` | 指定名が現在と違えばそのモードへ、同じなら `defaultControlStateName` に戻す。 |
| `setCurrentControlMode(string controlModeNameToCheck)` | 名前が変わる場合に現在モードとアイコンを更新し、各モードの有効/無効イベントを発火、必要ならメニューを閉じる。 |
| `setNextPlayerControl()` | 切替が有効なとき、次の有効な操作モードを探して `setCurrentControlMode` を呼ぶ。 |
| `setNextPlayerMode()` | 武器やパワーの状態を確認した上で、現在indexのモードを有効化して他を無効化し、UIテキストとイベントを更新する。 |
| `setModeIndex()` | `changeModeEnabled` なら次の有効なモードindexを探して `setNextPlayerMode` を呼ぶ。 |
| `setIgnoreSetPlayerModeByNameActiveState(bool state)` | `ignoreSetPlayerModeByNameActive` フラグを設定するだけ。 |
| `setPlayerModeByNameCheckingCharacterIsNotBusy(string modeName)` | `canUseInput` が真のときだけ `setPlayerModeByName` を呼ぶ。 |
| `setPlayerModeByName(string modeName)` | 無視フラグが立っていなければ、有効な同名モードのindexを現在値に入れて `setNextPlayerMode` を呼ぶ。 |
| `updateCurrentPlayerMode()` | `setNextPlayerMode` を呼ぶだけ。 |
| `updateCurrentPlayerModeByName(string playerModeToCheck)` | 現在のモード名と一致する場合のみ `setNextPlayerMode` を呼ぶ。 |
| `getCurrentPlayersModeName()` | `currentPlayersModeName` を返すだけ。 |
| `checkPlayerStates(bool disableWeaponsValue, bool disableAimModeValue, bool disableGrabModeValue, bool disableScannerModeValue, bool resetAnimatorStateValue, bool disableGravityPowerValue, bool disablePowersValue, bool disablePlayerModesValue)` | 各引数がtrueの項目だけ武器・エイム・グラブ・スキャナ・Animator・重力・パワー・モードの無効化を順に実行する。 |
| `checkPlayerStates()` | 引数なし版で、武器・エイム・グラブ・スキャナ・Animator・重力・パワー・モードの無効化をすべて実行する。 |
| `disableWeapons()` | 武器マネージャに現在武器の無効化、射撃/エイムのリセット、リロード中断を行わせる。 |
| `disableAimMode()` | 三人称でエイム中なら `powersManager.deactivateAimMode` を呼んで解除する。 |
| `disableGrabMode()` | オブジェクトを掴んでいる場合にドロップさせ、グラブ入力の一時停止を解除する。 |
| `disableScannerMode()` | スキャナが起動中なら `disableScanner` を呼ぶ。 |
| `resetAnimatorState()` | `playerManager.resetAnimatorState` を呼び、外部コントローラビヘイビアが有効ならそれを無効化する。 |
| `disableGravityPower()` | 重力パワーが有効なら `stopGravityPower` を呼ぶ。 |
| `disablePowers()` | 走っていれば停止し、`mainPlayerAbilitiesSystem` があれば発動中の全アビリティを停止する。 |
| `disablePlayerModes()` | `canSetRegularModeActive` なら `defaultControlStateName` の操作モードに戻す。 |
| `setDefaultControlState()` | 現在の操作モードが既定と違えば既定モードへ切り替える。 |
| `setAllControllerComponentsState(bool state)` | コライダーや各マネージャ、IK、AI系などの `enabled` をまとめて設定し、有効/無効イベントを発火する。 |
| `getAudioSourceElement(string name)` | `audioSourceList` から名前一致の `AudioSource` を返し、見つからなければnullを返す。 |
| `disableVehicleDrivenRemotely()` | 遠隔操作中なら `useDevice` を、オーバーライド中なら `stopOverride` を呼んで解除する。 |
| `setPlayerStateByName(string stateName)` | `playerStateInfoList` 内で同名かつ有効な状態だけをアクティブにしてイベントを発火し、他は非アクティブにする。 |
| `inputChangeMode()` | `changeModeByInputEnabled` と入力可否を確認し、入力用フラグを立てて `setModeIndex` を呼ぶ。 |
| `inputChangePlayerControlMode()` | メニューが有効なら、切替設定に応じて次の操作モードへ送るか操作モードメニューを開閉する。 |
| `inputSetNextPlayerControl()` | `changePlayerControlEnabled` と入力可否を確認して `setNextPlayerControl` を呼ぶ。 |
| `setOpenPlayerModeMenuEnabledState(bool state)` | `openPlayerModeMenuEnabled` を設定するだけ。 |
| `setChangeModeByInputEnabledState(bool state)` | `changeModeByInputEnabled` を設定するだけ。 |
| `setOriginalChangeModeByInputEnabledState()` | 保存しておいた `originalChangeModeByInputEnabledValue` に戻すだけ。 |
| `setInitialPlayersModeOnStart(string newModeName)` | `useDefaultPlayersMode` をtrueにし、`defaultPlayersModeName` を指定名に設定する。 |
| `setFirstPersonEditor()` | 非再生時のみ、FBAか通常の一人称向けにカメラ・重力・武器・酸素などの設定を切り替える。 |
| `setThirdPersonEditor()` | 非再生時のみ、FBAか通常の三人称に戻すようカメラなどの設定を切り替える。 |
| `setInitialPlayersMode(string newModeName)` | 既定モード名を設定し、コンポーネントを更新する。 |
| `setOpenPlayerModeMenuEnabledStateFromEditor(bool state)` | `openPlayerModeMenuEnabled` を設定してコンポーネントを更新する。 |
| `setChangeModeByInputEnabledStateFromEditor(bool state)` | `changeModeByInputEnabled` を設定してコンポーネントを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToEnableComponents` | `UnityEvent` | – |
| `eventToDisableComponents` | `UnityEvent` | – |
| `eventIfSystemDisabled` | `UnityEvent` | – |

## 内部型

- `playerMode`（class）
- `playerControl`（class）
- `playerStateInfo`（class）
