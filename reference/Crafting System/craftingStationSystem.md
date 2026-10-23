# craftingStationSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/craftingStationSystem.cs:6`

**概要**: 入出力`craftingSocket`・接続先ステーション一覧・エネルギー供給元を保持する基底クラス。状態変化フックは`virtual`の空実装で、派生クラスが上書きする。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Station Name | `stationName` | `string` | – | – |
| Input Socked Enabled | `inputSockedEnabled` | `bool` | true | – |
| Output Socket Enabled | `outputSocketEnabled` | `bool` | true | – |
| Input Socket | `inputSocket` | `craftingSocket` | – | – |
| Output Socket | `outputSocket` | `craftingSocket` | – | – |
| Chech Sockets On Start | `chechSocketsOnStart` | `bool` | – | – |

### Stations To Connect Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Station To Connect Name List | `stationToConnectNameList` | `List<string>` | new List<string> () | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Energy Station System | `currentEnergyStationSystem` | `energyStationSystem` | – | – |
| Remove Remain Energy On Remove Energy Station | `removeRemainEnergyOnRemoveEnergyStation` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Infinite Energy | `useInfiniteEnergy` | `bool` | – | – |
| Energy Station Assigned | `energyStationAssigned` | `bool` | – | – |
| Crafting Station System Connected List | `craftingStationSystemConnectedList` | `List<craftingStationSystem>` | new List<craftingStationSystem> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Input Connected | `useEventOnInputConnected` | `bool` | – | – |
| Event On Input Connected | `eventOnInputConnected` | `UnityEvent` | – | – |
| Use Event On Input Removed | `useEventOnInputRemoved` | `bool` | – | – |
| Event On Input Removed | `eventOnInputRemoved` | `UnityEvent` | – | – |
| Use Event On Output Connected | `useEventOnOutputConnected` | `bool` | – | – |
| Event On Output Connected | `eventOnOutputConnected` | `UnityEvent` | – | – |
| Use Event On Output Removed | `useEventOnOutputRemoved` | `bool` | – | – |
| Event On Output Removed | `eventOnOutputRemoved` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setInputSocket(craftingSocket newSocket)` | 入力ソケットが有効なら`inputSocket`を設定し、接続イベントと`checkStateOnSetInput`を実行する。 |
| `removeInputSocket()` | 入力有効時のみ`inputSocket`をnullにして状態チェックと削除イベントを実行する。 |
| `setOutputSocket(craftingSocket newSocket)` | `inputSockedEnabled`時のみ`outputSocket`を設定し、接続イベントと状態チェックを実行する。 |
| `removeOutputSocket()` | `inputSockedEnabled`時のみ出力をnullにし、状態チェックと削除イベントを実行する。 |
| `sendEnergyValue(float newAmount)` | 本体が空で何もしない。 |
| `setInfiniteEnergyState(bool state)` | `useInfiniteEnergy`を設定するだけ。 |
| `checkStateOnSetInput()` | 本体が空で何もしない。 |
| `checkStateOnSetOuput()` | 本体が空で何もしない。 |
| `checkStateOnRemoveInput()` | 本体が空で何もしない。 |
| `checkStateOnRemoveOuput()` | 本体が空で何もしない。 |
| `setCurrentEnergyStationSystem(energyStationSystem newEnergyStationSystem)` | エネルギー供給元を設定して`energyStationAssigned`を更新し、状態変化チェックを呼ぶ。 |
| `checkEnergyStationOnStateChange()` | 本体が空で何もしない。 |
| `checkStateOnTakeObjectBack()` | 出力・入力ソケットの接続先に解除チェックを伝播し、自身の入力・出力解除チェックも実行する。 |
| `getStationName()` | `stationName`を返すだけ。 |
| `addCraftingStationSystem(craftingStationSystem newCraftingStationSystem)` | `craftingStationSystemConnectedList`に未登録なら追加するだけ。 |
| `removeCraftingStationSystem(craftingStationSystem newCraftingStationSystem)` | `craftingStationSystemConnectedList`に含まれていれば取り除くだけ。 |
| `clearCraftingStationSystemList()` | `craftingStationSystemConnectedList`を空にするだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnInputConnected` | `UnityEvent` | – |
| `eventOnInputRemoved` | `UnityEvent` | – |
| `eventOnOutputConnected` | `UnityEvent` | – |
| `eventOnOutputRemoved` | `UnityEvent` | – |
