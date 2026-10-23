# remoteEventActivator

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Event System/remoteEventActivator.cs:5`

**概要**: 指定したオブジェクト（自分で指定、またはシーン内のプレイヤー）の`remoteEventSystem`に対し、名前と任意の引数（float/bool/GameObject/Transform）付きでリモートイベントを送る。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remote Event To Call | `remoteEventToCall` | `string` | – | – |
| Search For Remote Event Socked Enabled | `searchForRemoteEventSockedEnabled` | `bool` | – | – |

### Remote Event Info Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Amount | `useAmount` | `bool` | – | – |
| Amount Value | `amountValue` | `float` | – | – |
| Use Bool | `useBool` | `bool` | – | – |
| Bool Value | `boolValue` | `bool` | – | – |
| Use Game Object | `useGameObject` | `bool` | – | – |
| Game Object To Use | `gameObjectToUse` | `GameObject` | – | – |
| Use Transform | `useTransform` | `bool` | – | – |
| Transform To Use | `transformToUse` | `Transform` | – | – |

### Remote Event List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remove Event Info List | `useRemoveEventInfoList` | `bool` | – | – |
| Use Same Remote Even To Call | `useSameRemoteEvenToCall` | `bool` | true | – |
| Remove Event Info List | `removeEventInfoList` | `List<removeEventInfo>` | new List<removeEventInfo> () | – |

### Set Object Manually Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Assign Object Manually | `assignObjectManually` | `bool` | – | – |
| Object To Assign | `objectToAssign` | `GameObject` | – | – |
| Search Player On Scene If Not Assigned | `searchPlayerOnSceneIfNotAssigned` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `callRemoteEvent(GameObject objectToCall)` | `currentObjectToCall`に対象を入れてから`callEvent`を呼ぶ。 |
| `setObjectToCall(GameObject objectToCall)` | `currentObjectToCall`を設定するだけの薄いセッター。 |
| `callEvent()` | 手動指定時は対象（未指定ならプレイヤー検索）を決め、その`remoteEventSystem`へ引数種別に応じたリモートイベントを送る。 |
| `findPlayerOnScene()` | `searchPlayerOnSceneIfNotAssigned`が真なら、シーンのメインプレイヤーを`objectToAssign`に入れる。 |

## 内部型

- `removeEventInfo`（class）
