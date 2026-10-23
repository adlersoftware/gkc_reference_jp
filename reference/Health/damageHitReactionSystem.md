# damageHitReactionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/damageHitReactionSystem.cs:6`

**概要**: 被弾方向・カテゴリ・確率から`hitReactionInfoList`のリアクションを選んで再生するシステム。ブロック/パリィの猶予やダメージ量に応じた`damageStateInfo`イベントも扱う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hit Reactions Enabled | `hitReactionsEnabled` | `bool` | true | – |
| Default Category Reaction | `defaultCategoryReaction` | `string` | "Melee" | – |

### Reaction Probability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Probability To Activate Reaction Multiplier | `probabilityToActivateReactionMultiplier` | `float` | 1 | Range (0, 1) |
| Can Change Probability Multiplier Externally | `canChangeProbabilityMultiplierExternally` | `bool` | true | – |
| Ignore Min Wait Time To Play Hit Reaction Again | `ignoreMinWaitTimeToPlayHitReactionAgain` | `bool` | – | – |
| Ignore Min Amount To Receive Damage | `ignoreMinAmountToReceiveDamage` | `bool` | – | – |

### Hit Reaction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hit Reaction Info List | `hitReactionInfoList` | `List<hitReactionInfo>` | new List<hitReactionInfo> () | – |
| Damage State Info List | `damageStateInfoList` | `List<damageStateInfo>` | new List<damageStateInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Hit Reaction Active | `hitReactionActive` | `bool` | – | – |
| Current Block ID | `currentBlockID` | `int` | – | – |
| Current Reaction Category | `currentReactionCategory` | `string` | – | – |
| Damage Reaction Paused | `damageReactionPaused` | `bool` | – | – |
| Ignore Parry Active | `ignoreParryActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Main Event On Hit Reaction Found | `useMainEventOnHitReactionFound` | `bool` | – | – |
| Main Event On Hit Reaction Found | `mainEventOnHitReactionFound` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Transform | `playerControllerTransform` | `Transform` | – | – |
| Main Player Action System | `mainPlayerActionSystem` | `playerActionSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkDamageReceived(float damageReceived, Vector3 damagePosition, GameObject objectBlocked)` | 有効かつ非停止なら`checkHitReaction`を呼び、被弾方向と確率から通常のヒットリアクションを再生する。 |
| `checkDamageReceivedTemporally(float damageReceived, Vector3 damagePosition, GameObject objectBlocked)` | `hitReactionActive`を見ずに、有効かつ非停止なら一時的な被弾リアクション判定を行う。 |
| `checkDamageBlocked(float damageReceived, float originalDamageAmountReceived, Vector3 damagePosition, bool damageBlocked, GameObject objectBlocked)` | `damageBlocked`と元ダメージ量を渡し、ブロック専用のリアクション判定を行う。 |
| `checkDamageReceivedUnblockable(float damageReceived, Vector3 damagePosition, GameObject objectBlocked)` | `unblockableDamage`を真としてガード無視の被弾リアクションを判定する。 |
| `checkReactionToTriggerExternally(float damageReceived, Vector3 damagePosition, GameObject objectBlocked)` | 外部トリガー用に、有効かつ非停止なら通常の被弾リアクション判定を呼ぶ。 |
| `activateDamageReactionByID(float damageReceived, Vector3 damagePosition, GameObject objectBlocked, int damageReactionID)` | `damageReactionID`を指定して該当IDのリアクションを直接再生する。 |
| `checkDamageStateTemporally(float damageReceived, bool damageBlockedByShieldSystem)` | ダメージ量が範囲内の`damageStateInfo`イベントを1つ発火。シールド時は半減し、無ければ既定状態を使う。 |
| `setHitReactionActiveState(bool state)` | `hitReactionActive`フラグを`state`にするだけ。 |
| `getHitReactionActiveState()` | `hitReactionActive`の値を返すだけ。 |
| `setHitReactionBlockIDValue(int newBlockID)` | `currentBlockID`からカテゴリ一致のパーフェクトブロック反応を確率抽選し、成立時は猶予コルーチンを開始する。 |
| `setPerfectBlockDuration()` | 進行中のコルーチンを止めて`setPerfectBlockDurationCoroutine`を開始し直すだけ。 |
| `setCurrentReactionCategory(string newCategory)` | `currentReactionCategory`を`newCategory`に設定するだけ。 |
| `setNewProbabilityToActivateReactionMultiplierValue(float newValue)` | `canChangeProbabilityMultiplierExternally`が真の時のみ発動確率の倍率を`newValue`に更新する。 |
| `setHitReactionsEnabledState(bool state)` | `hitReactionsEnabled`を`state`にするだけ。 |
| `setDamageReactionPausedState(bool state)` | `damageReactionPaused`を`state`にするだけ。 |
| `isDamageReactionPaused()` | `damageReactionPaused`の値を返すだけ。 |
| `setIgnoreParryActiveState(bool state)` | `ignoreParryActive`を`state`にするだけ。 |
| `setHitReactionsEnabledStateFromEditor(bool state)` | 状態を設定した後`updateComponent`でシーンをダーティ更新するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `mainEventOnHitReactionFound` | `UnityEvent` | – |

## 内部型

- `hitReactionInfo`（class）
- `hitDamageDirection`（enum）
- `damageStateInfo`（class）
