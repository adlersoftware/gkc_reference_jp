# sharedActionSystemRemoteActivator

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/Shared Action System/sharedActionSystemRemoteActivator.cs:8`

**概要**: AIなどが対象を検出して相手キャラの共有アクションシステムを遠隔起動するコンポーネント。レイキャストや照準、目標システムで相手を探してアクション名を送る。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remote Activator Enabled | `remoteActivatorEnabled` | `bool` | true | – |
| Character Game Object | `characterGameObject` | `GameObject` | – | – |
| Set All Shared Actions Activator Result As Not Activated | `setAllSharedActionsActivatorResultAsNotActivated` | `bool` | – | – |

### Target Raycast Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Raycast Detection | `useRaycastDetection` | `bool` | – | – |
| Raycast Distance | `raycastDistance` | `float` | – | – |
| Raycast Layermask | `raycastLayermask` | `LayerMask` | – | – |
| Raycast Position Transform | `raycastPositionTransform` | `Transform` | – | – |
| Raycast Offset | `raycastOffset` | `Vector3` | – | – |

### Shared Action Activated Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remote Shared Action System Info List | `remoteSharedActionSystemInfoList` | `List<remoteSharedActionSystemInfo>` | new List<remoteSharedActionSystemInfo… | – |

### Actions To Ignore Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Actions To Ignore List | `useActionsToIgnoreList` | `bool` | – | – |
| Actions To Ignore List | `actionsToIgnoreList` | `List<string>` | new List<string> () | – |

### Target Match Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Match Target System To Get Target | `useMatchTargetSystemToGetTarget` | `bool` | – | – |
| Main Match Player To Target System | `mainMatchPlayerToTargetSystem` | `matchPlayerToTargetSystem` | – | – |
| Check On Friend List Manager To Get Target | `checkOnFriendListManagerToGetTarget` | `bool` | – | – |
| Main Friend List Manager | `mainFriendListManager` | `friendListManager` | – | – |
| Use Find Objectives System To Get Target | `useFindObjectivesSystemToGetTarget` | `bool` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Get Partner If Not Target Detected | `getPartnerIfNotTargetDetected` | `bool` | – | – |

### Editor Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shared Action Name | `sharedActionName` | `string` | – | – |
| Current External Character | `currentExternalCharacter` | `GameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Custom Shared Action Name | `customSharedActionName` | `string` | – | – |
| Custom Shared Action Name Active | `customSharedActionNameActive` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events It Target Detected | `useEventsItTargetDetected` | `bool` | – | – |
| Events It Target Detected | `eventsItTargetDetected` | `UnityEvent` | – | – |
| Use Events It Target Not Detected | `useEventsItTargetNotDetected` | `bool` | – | – |
| Events It Target Not Detected | `eventsItTargetNotDetected` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Shared Action System | `mainSharedActionSystem` | `sharedActionSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCustomSharedActionNameToUse(string newName)` | `customSharedActionName`を設定し、空文字でなければ有効フラグを立てる。 |
| `removeCustomSharedActionName()` | 空文字を設定してカスタム名を無効化するだけ。 |
| `checkSharedActionSystemByExternalDetection(string actionName)` | 検出方法で相手キャラを探し、見つかればその共有アクションシステムで`actionName`を起動、失敗時はイベントを発火する。 |
| `activateSharedActionByName()` | `remoteActivatorEnabled`と有効状態を確認し、外部キャラを渡して起動、結果でイベントを発火する。 |
| `setSetAllSharedActionsActivatorResultAsNotActivatedState(bool state)` | `setAllSharedActionsActivatorResultAsNotActivated`に`state`を設定するだけ。 |
| `setRemoteActivatorEnabledState(bool state)` | `remoteActivatorEnabled`に`state`を設定するだけ。 |
| `checkSharedActionSystemByExternalDetectionFromEditor()` | `sharedActionName`を引数に`checkSharedActionSystemByExternalDetection`を呼ぶだけ。 |
| `setSetAllSharedActionsActivatorResultAsNotActivatedStateFromEditor(bool state)` | 状態を設定した後、`updateComponent`でシーンを更新するエディタ用関数。 |
| `activateSharedActionByNameFromEditor()` | `activateSharedActionByName`を呼ぶだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventsItTargetDetected` | `UnityEvent` | – |
| `eventsItTargetNotDetected` | `UnityEvent` | – |

## 内部型

- `remoteSharedActionSystemInfo`（class）
