# headBob

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Player Camera/headBob.cs:6`

**概要**: 一人称/三人称の頭部ボブと、発砲・ダメージなどの外部シェイクを状態リストとコルーチンで制御するコンポーネント。`mainCameraTransform`のローカル位置と回転を直接補間する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Head Bob Enabled | `headBobEnabled` | `bool` | – | ヘッドボブの動作全体を有効にする。 |
| Static Idle Name | `staticIdleName` | `string` | – | 静止アイドル時に切り替えるボブ状態名。 |
| Current State | `currentState` | `string` | "" | 現在再生中のヘッドボブ状態の名前。 |
| Reset Speed | `resetSpeed` | `float` | – | カメラの位置と角度を初期値へ戻す速度。 |
| Shake Camera In Locked Mode | `shakeCameraInLockedMode` | `bool` | – | カメラ固定モードでも揺れを許可する。 |
| Main Manager Name | `mainManagerName` | `string` | "External Shake List Manager" | 外部シェイク管理マネージャを識別する名前。 |

### Dynamic Idle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Dynamic Idle | `useDynamicIdle` | `bool` | – | 一定時間操作がない時に動的アイドルへ切り替える。 |
| Dynamic Idle Name | `dynamicIdleName` | `string` | – | 動的アイドル時に使うボブ状態名。 / 表示条件: `useDynamicIdle` がオンのとき |
| Time To Active Dynamic Idle | `timeToActiveDynamicIdle` | `float` | – | 動的アイドルへ切り替えるまでの待ち時間。 / 表示条件: `useDynamicIdle` がオンのとき |

### External Shake Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| External Shake Enabled | `externalShakeEnabled` | `bool` | – | 外部からのカメラ揺れ要求を受け付ける。 |
| External Force State Name | `externalForceStateName` | `string` | – | 外部シェイク中に再生するボブ状態名。 / 表示条件: `externalShakeEnabled` がオンのとき |

### Jump Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Jump Start State Name | `jumpStartStateName` | `string` | "Jump Start" | ジャンプ開始時に切り替える状態名。 |
| Jump End State Name | `jumpEndStateName` | `string` | "Jump End" | ジャンプ着地時に切り替える状態名。 |
| Jump Start Max Increase | `jumpStartMaxIncrease` | `Vector3` | – | ジャンプ開始時に加えるカメラの回転量。 |
| Jump Start Speed | `jumpStartSpeed` | `float` | – | ジャンプ開始時の回転の補間速度。 |
| Jump End Max Decrease | `jumpEndMaxDecrease` | `Vector3` | – | 着地時に加えるカメラの回転量。 |
| Jump End Speed | `jumpEndSpeed` | `float` | – | 着地時のカメラ回転の補間速度。 |
| Jump Reset Speed | `jumpResetSpeed` | `float` | – | 着地後に初期角度へ戻す補間速度。 |

### Player Bob State Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | 状態遷移のデバッグログを出力する。 |

### Player Elements Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | プレイヤー制御コンポーネントの参照。 |
| External Shake Manager | `externalShakeManager` | `externalShakeListManager` | – | 外部シェイクの一覧を管理する参照。 |

### Current State Info

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Bob State | `playerBobState` | `bobStates` | – | 現在使用しているボブ状態のデータ。 / 表示条件: `list.isExpanded` |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `firstPersonMode` | `bool` | – | – |
| `externalShakingActive` | `bool` | – | – |
| `headBobCanBeUsed` | `bool` | true | – |
| `bobStatesList` | `List<bobStates>` | new List<bobStates> () | – |
| `externalShakeInfoList` | `List<externalShakeInfoListElement>` | new List<externalShakeInfoListElement… | – |
| `headBobPaused` | `bool` | false | – |
| `damageShakeActive` | `bool` | – | – |
| `firstPersonActive` | `bool` | – | – |
| `cameraTypeFree` | `bool` | – | – |
| `currentExternalShakeName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isExternalShakingActive()` | `externalShakingActive`の値を返す。 |
| `canBeUsed()` | ボブ状態の`enableBobIn`と一人称/三人称・ポーズ状態から、現在のボブを適用できるかを判定して返す。 |
| `setFirstPersonViewActiveState(bool state)` | `firstPersonActive`を設定するだけ。 |
| `setCameraTypeFreeState(bool state)` | `cameraTypeFree`を設定するだけ。 |
| `cameraLockedAllowsShake()` | 自由カメラか、ロック時のシェイク許可設定が有効ならtrueを返す。 |
| `stopBobTransform()` | 有効時のみ、実行中コルーチンを止めてカメラの位置と回転を初期値へ戻すコルーチンを開始する。 |
| `stopBobRotation()` | 有効時のみ、実行中コルーチンを止めてカメラ回転を初期値へ戻すコルーチンを開始する。 |
| `setState(string stateName)` | 外部シェイク中などを除き、名前一致のボブ状態を現在状態にして、一人称のジャンプ名なら開始/終了処理を呼ぶ。 |
| `setFirstOrThirdHeadBobView(bool state)` | 一人称モードを設定し、三人称へ戻す時はカメラ回転リセットのコルーチンを開始する。 |
| `setFirstOrThirdMode(bool state)` | `firstPersonMode`を設定するだけ。 |
| `setShotShakeState(IKWeaponSystem.weaponShotShakeInfo shotShakeInfo)` | 発砲の揺れ情報を外部フォース状態へ反映し、視点別に回転/位置量と継続時間を設定して開始する。 |
| `setExternalShakeState(externalShakeInfo shakeInfo)` | 外部シェイク情報を保存して外部フォース状態を適用し、量・速度・継続時間・リピート・減衰の設定を反映する。 |
| `setExternalShakeStateByIndex(int index, bool isFirstPerson)` | 外部シェイクリストの指定要素から、一人称か三人称かのシェイクを選んで適用する。 |
| `setExternalShakeStateByName(string shakeName, float multiplier)` | 運転中でなければ名前一致のシェイクを探し、`multiplier`を掛けた値で適用してダメージシェイク中にする。 |
| `setExternalShakeStateToRepeat(externalShakeInfo shakeInfo)` | リピート用に外部シェイク情報を再適用し、継続時間の管理と減衰処理を再開する。 |
| `setExternalShakeDuration()` | `externalShakingActive`を立て、既存コルーチンを止めて継続時間の管理コルーチンを開始する。 |
| `stopExternalShake()` | 外部シェイクを終了し、三人称なら回転リセットを行った後、頭部ボブ状態をリセットする。 |
| `setCurrentExternalCameraShakeSystemEvents(UnityEvent eventAtStart, UnityEvent eventAtEnd)` | 開始/終了イベントを保持し、イベント使用フラグを立てるだけ。 |
| `disableUseShakeEventState()` | `useShakeEvent`をfalseにするだけ。 |
| `checkDecreaseShake()` | 減衰設定が有効なら、既存コルーチンを止めてシェイク量を徐々に0へ近づけるコルーチンを開始する。 |
| `playerAliveOrDead(bool state)` | 死亡状態を設定し、死亡時は頭部ボブを止めて静止アイドル状態へ切り替える。 |
| `playOrPauseHeadBob(bool state)` | `headBobCanBeUsed`を設定するだけ。 |
| `stopAllHeadbobMovements()` | 関連コルーチンを全て止めてシェイク等のフラグを落とし、静止アイドル状態に設定する。 |
| `jumpStarted()` | 頭部移動の停止中でなければ着地コルーチンを止め、ジャンプ開始用の回転コルーチンを開始する。 |
| `jumpEnded()` | 一人称かつ生存時のみ、ジャンプ開始コルーチンを止めて着地用の回転コルーチンを開始する。 |
| `setDefaultState()` | 既定のボブ状態を設定し、`playerControllerManager`の頭部ボブ状態をリセットする。 |
| `setShakeInManagerList(int index)` | 指定インデックスの外部シェイク情報を`externalShakeManager`へ渡す。 |
| `pauseHeadBodWithDelay(float delayAmount)` | 全ボブ動作を止め、`delayAmount`秒だけ頭部移動を停止するコルーチンを開始する。 |
| `updateExternalShakeInfoList(List<externalShakeInfoListElement> newExternalShakeInfoList)` | 外部シェイク情報リストを差し替えて`updateComponent`を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーン更新を呼んでインスペクタ表示を更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `currentEventAtStart` | `UnityEvent` | – |
| `currentEventAtEnd` | `UnityEvent` | – |

## 内部型

- `bobTransformType`（enum）
- `viewTypes`（enum）
- `bobStates`（class）
