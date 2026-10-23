# durabilityInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Crafting System/durabilityInfo.cs:6`

**概要**: オブジェクトの耐久度を保持し、増減・全快・破損判定とイベント発火、遅延回復コルーチン、在庫側耐久値の同期を行う。エディタ用setterはコンポーネント更新も伴う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Name | `objectName` | `string` | – | – |
| Max Durability Amount | `maxDurabilityAmount` | `float` | – | – |
| Durability Amount | `durabilityAmount` | `float` | – | – |
| Invulnerability Active | `invulnerabilityActive` | `bool` | – | – |

### Regeneration Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Regeneration Speed | `regenerationSpeed` | `float` | 4 | – |
| Activate Regeneration After Delay | `activateRegenerationAfterDelay` | `bool` | – | – |
| Delay To Activate Regeneration | `delayToActivateRegeneration` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Object Is Broken | `objectIsBroken` | `bool` | – | – |
| Regeneration Active | `regenerationActive` | `bool` | – | – |
| Regeneration After Delay Active | `regenerationAfterDelayActive` | `bool` | – | – |
| Character Located | `characterLocated` | `bool` | – | – |
| Inventory Object Index | `inventoryObjectIndex` | `int` | -1 | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Empty Durability | `useEventOnEmptyDurability` | `bool` | – | – |
| Event On Empty Durability | `eventOnEmptyDurability` | `UnityEvent` | – | – |
| Use Event On Refilled Durability | `useEventOnRefilledDurability` | `bool` | – | – |
| Event On Refilled Durability | `eventOnRefilledDurability` | `UnityEvent` | – | – |
| Use Event On Invulnerability Active | `useEventOnInvulnerabilityActive` | `bool` | – | – |
| Event On Invulnerability Active | `eventOnInvulnerabilityActive` | `UnityEvent` | – | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Empty Durability | `useRemoteEventOnEmptyDurability` | `bool` | – | – |
| Remote Event List On Empty Durability | `remoteEventListOnEmptyDurability` | `List<string>` | new List<string> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Character Game Object | `mainCharacterGameObject` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeDurabilityValue(float newAmount)` | 耐久度を`newAmount`に設定し、0以下なら破損フラグ`objectIsBroken`をtrueにする。 |
| `getDurabilityAmount()` | 現在の耐久度`durabilityAmount`を返すだけ。 |
| `repairObjectFully()` | 耐久度を最大値で上書きするよう加減算メソッドを呼び出すだけ。 |
| `breakFullDurability()` | 耐久度を0で上書きするよう加減算メソッドを呼び出すだけ。 |
| `addOrRemoveDurabilityAmountToObjectByName(float newAmount, bool setAmountAsCurrentValue)` | 無敵中は無視し、耐久度を加算/代入して0〜最大に丸め、0なら破損、満タンなら全快の処理を呼ぶ。 |
| `updateDurabilityAmountState()` | 主人公を確認し、耐久0で未破損なら破損イベント/リモートイベントを発火し、在庫側の耐久値も更新する。 |
| `setFullDurabilityState()` | 耐久度を最大にして破損フラグを解除し、在庫側へ最大値を反映して全快イベントを発火する。 |
| `setInvulnerabilityActiveState(bool state)` | `invulnerabilityActive`を設定し、trueなら無敵化イベントを発火するだけ。 |
| `setMainCharacterGameObject(GameObject newObject)` | `mainCharacterGameObject`を`newObject`に設定するだけ。 |
| `checkMainCharacterGameObject()` | 未発見なら主人公を取得し直し、見つかったかどうかを`characterLocated`に記録する。 |
| `getMainCharacterGameObject()` | 本体が空で何もしない（サブクラスで上書きされる`virtual`メソッド）。 |
| `activateDurabilityRegeneration()` | 既存の回復コルーチンを止めてから、耐久度を徐々に戻すコルーチンを開始する。 |
| `stopUpdateRegenerationCoroutine()` | 回復コルーチンを止め、回復中なら耐久値を同期し、遅延回復も止めて回復フラグをfalseにする。 |
| `stopUpdateRegenerationAfterDelayCoroutine()` | 遅延回復コルーチンを停止し、`regenerationAfterDelayActive`をfalseにするだけ。 |
| `isDurabilityEmpty()` | 耐久度が0以下かどうかを返すだけ。 |
| `setObjectName(string newName)` | `objectName`を`newName`に設定するだけ。 |
| `setMaxDurabilityAmount(float newValue)` | `maxDurabilityAmount`を`newValue`に設定するだけ。 |
| `setInventoryObjectIndex(int newValue)` | `inventoryObjectIndex`を`newValue`に設定するだけ。 |
| `setObjectNameFromEditor(string newName)` | エディタ用に`setObjectName`を呼んだ後、コンポーネントとシーンを更新する。 |
| `setMaxDurabilityAmountFromEditor(float newValue)` | エディタ用に`setMaxDurabilityAmount`を呼んだ後、コンポーネントとシーンを更新する。 |
| `setDurabilityAmountFromEditor(float newValue)` | エディタ用に現在耐久度`durabilityAmount`を設定し、コンポーネントとシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnEmptyDurability` | `UnityEvent` | – |
| `eventOnRefilledDurability` | `UnityEvent` | – |
| `eventOnInvulnerabilityActive` | `UnityEvent` | – |
