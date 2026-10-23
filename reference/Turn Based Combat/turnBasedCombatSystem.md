# turnBasedCombatSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Turn Based Combat/turnBasedCombatSystem.cs:6`

**概要**: ターン制戦闘のシングルトン管理コンポーネント。戦闘の開始・終了、カメラ状態、チーム位置データやリスポーン位置を管理し、詳細処理はUIシステムへ委譲する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Configure New Teams Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| New Character Team Leader | `newCharacterTeamLeader` | `GameObject` | – | 新チームのリーダーに設定するプレイヤー。 |
| Team Position Data Name | `teamPositionDataName` | `string` | – | チームの配置データ名で、陣形情報の検索に使う。 |
| New Team Always Select First | `newTeamAlwaysSelectFirst` | `bool` | – | ONにするとこのチームが常に先手で行動する。 |
| Use Custom Camera State On New Team | `useCustomCameraStateOnNewTeam` | `bool` | – | ONにすると新チーム用のカメラ状態へ切り替える。 |
| Custom Camera State On New Team | `customCameraStateOnNewTeam` | `string` | – | 新チームで切り替え先にするカメラ状態名。 / 表示条件: `useCustomCameraStateOnNewTeam` がオンのとき |
| Use Reward System | `useRewardSystem` | `bool` | – | ONにすると戦闘終了後に報酬システムを実行する。 |
| Main Reward System | `mainRewardSystem` | `objectExperienceSystem` | – | 報酬の付与に使う`objectExperienceSystem`。 / 表示条件: `useRewardSystem` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `turnBasedCombatEnabled` | `bool` | true | – |
| `minWaitTimeToActiveCombatOnSpotted` | `float` | 2 | – |
| `minExtraWaitToReactivateCombatAfterRun` | `float` | 3 | – |
| `layerToAdjustToGround` | `LayerMask` | 1 << 0 \| 1 << 23 | – |
| `minDistanceToPlayerToStartCombat` | `float` | 10 | – |
| `defaultCameraStateNameOnTurnBasedCombatActive` | `string` | "Default Turn Based Combat Camera" | – |
| `defaultCameraStateNameOnReturnCameraToPlayer` | `string` | "Return Camera To Player" | – |
| `turnBasedCombatCameraInfoList` | `List<turnBasedCombatCameraInfo>` | new List<turnBasedCombatCameraInfo> () | – |
| `turnBasedCombatTeamPositionsInfoDataList` | `List<turnBasedCombatTeamPositionsInfoData>` | new List<turnBasedCombatTeamPositions… | – |
| `defaultEffectName` | `string` | "Default Effect" | – |
| `turnBasedCombatEffectInfoList` | `List<turnBasedCombatEffectInfo>` | new List<turnBasedCombatEffectInfo> () | – |
| `positionToRespawnList` | `List<Transform>` | new List<Transform> () | – |
| `turnBasedCombatActive` | `bool` | – | – |
| `checkingMinWaitTimeToActiveCombatOnSpotted` | `bool` | – | – |
| `freeCombatActive` | `bool` | – | – |
| `mainPlayer` | `GameObject` | – | – |
| `mainCamera` | `Camera` | – | – |
| `playerCameraManager` | `playerCamera` | – | – |
| `mainTurnBasedCombatUISystem` | `turnBasedCombatUISystem` | – | – |
| `mainAIAroundManager` | `AIAroundManager` | – | – |
| `mainFriendListManager` | `friendListManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | シングルトン未設定なら自身を登録し、既に別インスタンスがあればこのGameObjectを破棄する。 |
| `adjustTurnBasedCombatPositionToPlayer()` | リスポーン位置を地面へ合わせ、プレイヤーの位置とカメラ回転に合わせてこのシステムの位置・向きを調整する。 |
| `enableWaitTimeToActivateTurnBasedCombat()` | 戦闘が有効かつフリー戦闘中でなければ、索敵タイマーを開始してフレンドリストを取得し、更新コルーチンを起動する。 |
| `disableWaitTimeToActivateTurnBasedCombat()` | 索敵待機中ならフラグを下ろして更新コルーチンを停止するだけ。 |
| `stopUpdateCoroutine()` | `updateCoroutine`が実行中なら停止するだけ。 |
| `updateLastTimeCombatRunActive(float value)` | `lastTimeCombatRunActive`に`value`を設定するだけ。 |
| `clearCharactersAround()` | `mainAIAroundManager`の周囲キャラクター情報をクリアするだけ。 |
| `activateTurnBasedCombat()` | `activateOrDeactivateTurnBasedCombat(true)`を呼び、UIに戦闘開始を依頼するだけ。 |
| `deactivateTurnBasedCombat()` | `activateOrDeactivateTurnBasedCombat(false)`を呼び、UIに戦闘終了を依頼するだけ。 |
| `setTurnBasedCombatActiveState(bool state)` | 戦闘有効時のみ状態を設定し、開始時はカメラ切替と索敵コルーチン起動、終了時はカメラを戻して停止する。 |
| `setMinTeamAmountToCheck(int newAmount)` | `minTeamAmountToCheck`に`newAmount`を設定するだけ。 |
| `stopMovement()` | カメラ移動コルーチンを停止するだけ。 |
| `setCurrentPlayer(GameObject player)` | メインプレイヤーを設定し、そのコンポーネントからカメラ・AI索敵・フレンドリスト管理を取得する。 |
| `getTurnBasedCombatTeamPositionsInfoData(int teamSize, string teamPositionInfoName, bool isPlayerTeam)` | 指定名、またはチーム人数とプレイヤー・敵区分に一致するチーム位置情報データを返し、なければnullを返す。 |
| `setUseCustomCameraState(bool state, string cameraStateName)` | カスタムカメラ状態の使用フラグと状態名を保存するだけ。 |
| `getPositionToRespawnList()` | `positionToRespawnList`を返すだけ。 |
| `getClosestRespawnPosition(Vector3 currentPosition)` | リスポーン位置の中から`currentPosition`に最も近い位置を返し、候補がなければ`Vector3.zero`を返す。 |
| `updateAllCharacterStatsUIValue()` | ターン制戦闘が有効なら、UIシステムに全キャラクターのステータス更新を依頼する。 |
| `setNextTurn()` | ターン制戦闘が有効なら、UIシステムに次ターンへの切り替えを依頼する。 |
| `setCurrentCommandNameUsed(string commandName)` | ターン制戦闘が有効なら、使用コマンド名をUIシステムへ通知する。 |
| `activateEffect(string effectName)` | ターン制戦闘が有効なら、空文字を既定名に置き換えて該当エフェクトを探し、有効ならイベントを発火する。 |
| `setFreeCombatActiveState(bool state)` | フリー戦闘状態を保存し、UIシステム経由で全キャラクターにも同じ状態を設定する。 |
| `checkTeamsDeadStateAfterCharacterDeath(Transform characterTransform)` | UIシステムにチーム全滅判定を依頼するだけ。 |
| `checkCharacterStateAfterResurrect(Transform characterTransform)` | UIシステムに復活後の状態処理を依頼するだけ。 |
| `checkPlayerStateOnDeathDuringCombat()` | UIシステムにプレイヤー死亡時の処理を依頼するだけ。 |
| `inputConfirmCommand()` | ターン制戦闘が有効なら、UIシステムへコマンド確定入力を転送する。 |
| `inputCancelCommand()` | ターン制戦闘が有効なら、UIシステムへコマンドキャンセル入力を転送する。 |
| `inputSelectNextTarget()` | ターン制戦闘が有効なら、UIシステムへ次ターゲット選択入力を転送する。 |
| `inputSelectPreviousTarget()` | ターン制戦闘が有効なら、UIシステムへ前ターゲット選択入力を転送する。 |
| `inputToggleCombatMode()` | ターン制戦闘またはフリー戦闘が有効なら、UIシステムへ戦闘モード切替入力を転送する。 |
| `configureNewTeamInfo()` | 新しいチームリーダーとメンバーから各キャラクターのチーム情報を再設定し、完了後に設定用フィールドを初期化してシーンを更新する。 |
| `showAllTeamsInScene()` | シーン内のチーム情報コンポーネントからリーダーのものだけをリストに集めて更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`とシーン更新を呼ぶだけ。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |

## 内部型

- `turnBasedCombatCameraInfo`（class）
- `turnBasedCombatEffectInfo`（class）
