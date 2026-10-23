# customCharacterControllerManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Generic Model Controller/customCharacterControllerManager.cs:6`

**概要**: 蜘蛛や狼などの「カスタムキャラクターコントローラ」への切替を管理するコンポーネント。名前で状態を選択し、プレハブの生成、開始/終了イベント、メッシュ表示、カプセル値の同期を行う。

**公式ドキュメント抜粋**（[Custom Character Controller Manager](../../docs/player-controller-components/essential-components/custom-character-controller-manager.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Game With Custom Character Controller | `startGameWithCustomCharacterController` | `bool` | – | – |
| Custom Character Controller To Start Name | `customCharacterControllerToStartName` | `string` | – | – |
| Enable New Custom Character If Active When Toggling To New One | `enableNewCustomCharacterIfActiveWhenTogglingToNewOne` | `bool` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ignore Set AI Values | `ignoreSetAIValues` | `bool` | – | – |
| Set Character Mode On Regular State | `setCharacterModeOnRegularState` | `bool` | – | – |
| Set New Character Mode On Regular State | `setNewCharacterModeOnRegularState` | `bool` | – | – |
| New Character Mode On Regular State | `newCharacterModeOnRegularState` | `string` | – | – |
| Disable Foot Steps On Generic Mode Enabled | `disableFootStepsOnGenericModeEnabled` | `bool` | true | – |

### Character Controller List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Controller State Info List | `characterControllerStateInfoList` | `List<characterControllerStateInfo>` | new List<characterControllerStateInfo… | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Custom Character Controller Active | `customCharacterControllerActive` | `bool` | – | – |
| Current Character Controller Name | `currentCharacterControllerName` | `string` | – | – |
| Toggle Custom Character Controller Paused | `toggleCustomCharacterControllerPaused` | `bool` | – | – |
| Generic Model Visible On Editor | `genericModelVisibleOnEditor` | `bool` | – | – |
| Original Avatar | `originalAvatar` | `Avatar` | – | – |
| Current Custom Character Controller Base | `currentCustomCharacterControllerBase` | `customCharacterControllerBase` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | – |
| Event On Custom Character Enter | `eventOnCustomCharacterEnter` | `UnityEvent` | – | – |
| Event On Custom Character Exit | `eventOnCustomCharacterExit` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Original Animator Controller | `originalAnimatorController` | `RuntimeAnimatorController` | – | – |
| Main Player Weapon Manager | `mainPlayerWeaponManager` | `playerWeaponsManager` | – | – |
| Main Player States Manager | `mainPlayerStatesManager` | `playerStatesManager` | – | – |
| Custom Character Controller Parent | `customCharacterControllerParent` | `Transform` | – | – |
| Main Capsule Collider | `mainCapsuleCollider` | `CapsuleCollider` | – | – |
| Main Ragdoll Activator | `mainRagdollActivator` | `ragdollActivator` | – | – |
| Main Close Combat System | `mainCloseCombatSystem` | `closeCombatSystem` | – | – |
| Main Other Powers System | `mainOtherPowersSystem` | `otherPowers` | – | – |
| Main Health | `mainHealth` | `healthManagement` | – | – |
| Main Grab Objects | `mainGrabObjects` | `grabObjects` | – | – |
| Main AI Abilities System Brain | `mainAIAbilitiesSystemBrain` | `AIAbilitiesSystemBrain` | – | – |

### AI Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main AI Close Combat System Brain | `mainAICloseCombatSystemBrain` | `AICloseCombatSystemBrain` | – | – |

### Custom Character Prefab Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Custom Character Prefab | `customCharacterPrefab` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `toggleCustomCharacterControllerExternally(string characterControllerName)` | 一時的に停止フラグを false にして `toggleCustomCharacterController` を呼び、元に戻す。 |
| `toggleCustomCharacterController(string characterControllerName)` | 停止中なら無視し、未使用なら状態を設定、使用中なら解除したうえで設定に応じて新しいコントローラを有効化する。 |
| `disableCustomCharacterControllerState()` | 使用中のみ、終了イベントを送出して `setCharacterState(false)` を呼び、参照と名前をクリアする。 |
| `setRandomCustomCharacterControllerState()` | リストからランダムに選び、その名前で `setCustomCharacterControllerState` を呼ぶ。 |
| `setCustomCharacterControllerState(string characterControllerStateName)` | 同名なら無視し、現在状態を終了させたうえで対象を有効化し、必要ならプレハブを生成する。 |
| `isCustomCharacterControllerActive()` | `customCharacterControllerActive` を返すだけ。 |
| `checkEventsOnStateChange(bool state)` | イベント使用時、開始なら Enter、終了なら Exit のイベントを送出する。 |
| `setToggleCustomCharacterControllerPausedState(bool state)` | `toggleCustomCharacterControllerPaused` を設定するだけ。 |
| `addNewCustomCharacterController(customCharacterControllerBase newCustomCharacterControllerBase, string newName)` | 名前とコントローラを持つ状態情報を新規作成してリストへ追加し、`updateComponent` を呼ぶ。 |
| `addNewCustomCharacterControllerToSpawn(GameObject newCustomCharacterControllerBaseObject, string newName)` | プレハブと生成フラグを持つ状態情報をリストへ追加し、`updateComponent` を呼ぶ。 |
| `toggleCharacterModelMeshOnEditor(bool state)` | エディタ上でカスタムモデルの表示を切り替え、メインキャラのメッシュと武器メッシュは逆の状態にして更新する。 |
| `setStartGameWithCustomCharacterControllerFromEditor(bool state)` | `startGameWithCustomCharacterController` を設定して更新する。 |
| `setCustomCharacterControllerToStartNameFromEditor(string newCharacterName)` | 開始時のコントローラ名を設定し `updateComponent` を呼ぶ。 |
| `setCapsuleValuesFromMainCharacter()` | 現在のカスタムコントローラへメインカプセルの方向・中心・半径・高さをコピーする。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCustomCharacterEnter` | `UnityEvent` | – |
| `eventOnCustomCharacterExit` | `UnityEvent` | – |

## 内部型

- `characterControllerStateInfo`（class）
