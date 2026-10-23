# actionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/actionSystem.cs:10`

**概要**: シーン上のデバイスやNPC側に置かれ、アクション情報リスト・プレイヤーリスト・各種イベントを保持してプレイヤーの`playerActionSystem`へアクションを渡すコンポーネント。エディタ用のリスト編集補助も含む。

**公式ドキュメント抜粋**（[Action System](../../docs/major-systems/action-system.md)）

> A core system that let's you create any Action, be it grabbing something or more, easily! Player Action System Component Tutorial - Add Action System By Input Tutorial: Create Objects to Grab & Carry Physically

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Min Distance To Activate Action | `useMinDistanceToActivateAction` | `bool` | – | ONにすると、距離がしきい値以内の時だけアクションを開始できる。 |
| Min Distance To Activate Action | `minDistanceToActivateAction` | `float` | – | アクションを開始できる最大距離。これを超えると実行されない。 / 表示条件: `useMinDistanceToActivateAction` がオンのとき |
| Use Min Angle To Activate Action | `useMinAngleToActivateAction` | `bool` | – | ONにすると、向きの角度差がしきい値以内の時だけ開始できる。 |
| Min Angle To Activate Action | `minAngleToActivateAction` | `float` | – | 開始を許可するプレイヤーとアクションの向きの角度差の上限（度）。 / 表示条件: `useMinAngleToActivateAction` がオンのとき |
| Check Opposite Angle | `checkOppositeAngle` | `bool` | – | ONにすると、180度反対を向いた状態でも角度条件を満たすとみなす。 / 表示条件: `useMinAngleToActivateAction` がオンのとき |
| Can Stop Previous Action | `canStopPreviousAction` | `bool` | – | ONにすると、他のアクション実行中でもこれを停止して開始できる。 |
| Can Force To Play Custom Action | `canForceToPlayCustomAction` | `bool` | – | ONにすると、実行中のアクションを中断して強制再生できる。 |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Trigger | `mainTrigger` | `Collider` | – | アクションのトリガー用Collider。未設定なら自身のColliderを使用。 |
| Animation Used On Upper Body | `animationUsedOnUpperBody` | `bool` | – | ONにすると上半身用レイヤーで再生し、通常アクション状態を維持する。 |
| Disable Regular Action Active State | `disableRegularActionActiveState` | `bool` | – | 上半身再生時に通常アクション用の`actionActive`をOFFにする。 / 表示条件: `animationUsedOnUpperBody` がオンのとき |
| Disable Regular Action Active State On End | `disableRegularActionActiveStateOnEnd` | `bool` | – | アクション終了時に通常アクション用フラグもOFFにする。 / 表示条件: `animationUsedOnUpperBody` がオンのとき |
| Set Player Parent During Action Active | `setPlayerParentDuringActionActive` | `bool` | – | ONにするとアクション中プレイヤーとカメラを指定Transformの子にする。 |
| Player Parent During Action | `playerParentDuringAction` | `Transform` | – | アクション中にプレイヤーを親子付ける先のTransform。 / 表示条件: `setPlayerParentDuringActionActive` がオンのとき |
| Disable Ignore Player List Change | `disableIgnorePlayerListChange` | `bool` | – | ONにすると外部起動時にプレイヤーリストを無視せず、範囲内の相手のみ対象にする。 |
| Enable Animator Layer On Action | `enableAnimatorLayerOnAction` | `bool` | – | ONにすると開始時に指定Animatorレイヤーのウェイトを有効にする。 |
| Animator Layer To Enable Name | `animatorLayerToEnableName` | `string` | – | 開始時に有効化するAnimatorレイヤー名。 / 表示条件: `enableAnimatorLayerOnAction` がオンのとき |

### First Person/FBA Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Camera View To Third Person On Action | `changeCameraViewToThirdPersonOnAction` | `bool` | – | ONにすると一人称で開始した際に三人称視点へ切り替える。 |
| Change Camera View To Third Person On Action On Full Body Awareness | `changeCameraViewToThirdPersonOnActionOnFullBodyAwareness` | `bool` | – | ONにするとFBA中に開始した際に三人称視点へ切り替える。 |
| Keep Camera Rotation To Head On Full Body Awareness | `keepCameraRotationToHeadOnFullBodyAwareness` | `bool` | – | ONにするとFBA中にカメラを頭の向きに追従させる。 |
| Actions Can Be Used On First Person | `actionsCanBeUsedOnFirstPerson` | `bool` | – | ONにすると一人称視点のままアクションを実行できる。 |
| Ignore Change To Third Person | `ignoreChangeToThirdPerson` | `bool` | – | ONにすると一人称時でも三人称への切り替えを行わない。 / 表示条件: `actionsCanBeUsedOnFirstPerson` がオンのとき |

### Action State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Action Info Index | `currentActionInfoIndex` | `int` | – | 使用するアクション情報（`actionInfoList`）の現在のインデックス。 |

### Activate New Action After Action Complete

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Custom Action After Action Complete | `activateCustomActionAfterActionComplete` | `bool` | – | ONにすると完了後に指定したカスタムアクションを自動で開始する。 |
| Custom Action To Active After Action Complete | `customActionToActiveAfterActionComplete` | `string` | – | 完了後に開始するカスタムアクションの名前。 / 表示条件: `activateCustomActionAfterActionComplete` がオンのとき |

### Store Action On List To Play

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Action To List Stored To Play | `addActionToListStoredToPlay` | `bool` | – | ONにするとこのアクションを後で再生するリストに追加する。 |
| Play Action Automatically If Stored At End | `playActionAutomaticallyIfStoredAtEnd` | `bool` | – | ONにすると終了時にリスト先頭のアクションを自動再生する。 / 表示条件: `addActionToListStoredToPlay` がオンのとき |
| Clear Add Action To List Stored To Play | `clearAddActionToListStoredToPlay` | `bool` | – | ONにすると開始時に保存済みアクションリストを空にする。 |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Player Inside Outside | `useEventsOnPlayerInsideOutside` | `bool` | – | ONにするとプレイヤーの範囲への出入りでイベントを呼ぶ。 |
| Event On Player Inside | `eventOnPlayerInside` | `UnityEvent` | – | 最初のプレイヤーが範囲内に入った時に呼ばれるイベント。 / 表示条件: `useEventsOnPlayerInsideOutside` がオンのとき |
| Event On Player Outside | `eventOnPlayerOutside` | `UnityEvent` | – | プレイヤーが全員範囲外に出た時に呼ばれるイベント。 / 表示条件: `useEventsOnPlayerInsideOutside` がオンのとき |
| Use Events On Start End Action | `useEventsOnStartEndAction` | `bool` | – | ONにするとアクション開始時と終了時にイベントを呼ぶ。 |
| Event On Start Action | `eventOnStartAction` | `UnityEvent` | – | アクション開始時に呼ばれるイベント。 / 表示条件: `useEventsOnStartEndAction` がオンのとき |
| Event On End Action | `eventOnEndAction` | `UnityEvent` | – | アクション終了時に呼ばれるイベント。 / 表示条件: `useEventsOnStartEndAction` がオンのとき |
| Use Event After Resume Player | `useEventAfterResumePlayer` | `bool` | – | ONにするとプレイヤー操作再開後にイベントを呼ぶ。 |
| Event After Resume Player | `eventAfterResumePlayer` | `UnityEvent` | – | プレイヤーの操作再開後に呼ばれるイベント。 / 表示条件: `useEventAfterResumePlayer` がオンのとき |
| Send Current Player On Event | `sendCurrentPlayerOnEvent` | `bool` | – | ONにすると各イベント呼び出し時に現在のプレイヤーを渡す。 |
| Event To Send Current Player | `eventToSendCurrentPlayer` | `eventParameters.eventToCallWithGameObject` | – | 現在のプレイヤーを引数で受け取るイベント。 / 表示条件: `sendCurrentPlayerOnEvent` がオンのとき |
| Use Event Before Start Action | `useEventBeforeStartAction` | `bool` | – | ONにするとアクション開始直前にイベントを呼ぶ。 |
| Event Before Start Action | `eventBeforeStartAction` | `UnityEvent` | – | アクション開始前に呼ばれるイベント。 / 表示条件: `useEventBeforeStartAction` がオンのとき |
| Use Events To Enable Disable Action Object | `useEventsToEnableDisableActionObject` | `bool` | – | ONにするとアクションオブジェクトの有効/無効時にイベントを呼ぶ。 |
| Event To Enable Action Object | `eventToEnableActionObject` | `UnityEvent` | – | アクションオブジェクトが有効になった時に呼ばれるイベント。 / 表示条件: `useEventsToEnableDisableActionObject` がオンのとき |
| Event To Disable Action Object | `eventToDisableActionObject` | `UnityEvent` | – | アクションオブジェクトが無効になった時に呼ばれるイベント。 / 表示条件: `useEventsToEnableDisableActionObject` がオンのとき |

### Gizmo And Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | ONにするとシーンビューにアクション位置のギズモを表示する。 |
| Show All Gizmo | `showAllGizmo` | `bool` | – | ONにすると各アクションの設定に関係なく全ギズモを表示する。 |
| Show Debug Print | `showDebugPrint` | `bool` | – | ONにするとアクション処理のデバッグログをコンソールに出力する。 |

### Replace Action Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Animation Replace | `activateAnimationReplace` | `bool` | – | ONにすると下記設定でAnimatorのアクションステートを差し替える。 |
| Main Animator | `mainAnimator` | `Animator` | – | 差し替え対象ステートを持つAnimator。未設定ならPlayerから取得。 / 表示条件: `activateAnimationReplace` がオンのとき |
| Animation Layer Name | `animationLayerName` | `string` | "Base Layer" | 差し替え対象ステートが含まれるAnimatorレイヤー名。 / 表示条件: `activateAnimationReplace` がオンのとき |
| Action Name To Replace | `actionNameToReplace` | `string` | – | 差し替えるアクション名（アクション名またはステート名）。 / 表示条件: `activateAnimationReplace` がオンのとき |
| New Animation Clip | `newAnimationClip` | `AnimationClip` | – | 差し替え後の新しいアニメーションクリップ。 / 表示条件: `activateAnimationReplace` がオンのとき |
| New Animation Speed | `newAnimationSpeed` | `float` | 1 | 差し替え後のステートに設定する再生速度。 / 表示条件: `activateAnimationReplace` がオンのとき |
| New Animation Is Mirror | `newAnimationIsMirror` | `bool` | – | ONにすると差し替え後のステートをミラー再生にする。 / 表示条件: `activateAnimationReplace` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `actionInfoList` | `List<actionInfo>` | new List<actionInfo> () | – |
| `playerList` | `List<GameObject>` | new List<GameObject> () | – |
| `actionTransform` | `Transform` | – | – |
| `categoryName` | `string` | – | – |
| `canInterruptOtherActionActive` | `bool` | – | – |
| `actionListToInterrupt` | `List<string>` | new List<string> () | – |
| `useCategoryToCheckInterrupt` | `bool` | – | – |
| `actionCategoryListToInterrupt` | `List<string>` | – | – |
| `eventOnInterrupOtherActionActive` | `UnityEvent` | – | – |
| `useEventOnInterruptedAction` | `bool` | – | – |
| `eventOnInterruptedAction` | `UnityEvent` | – | – |
| `useProbabilityToActivateAction` | `bool` | – | – |
| `probablityToActivateAction` | `float` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPlayerParentDuringActionActiveValues(bool state, Transform newParent)` | アクション中の親子付け設定`setPlayerParentDuringActionActive`と`playerParentDuringAction`を設定するだけ。 |
| `setUseMovingPlayerToPositionTargetValues(bool state, float newSpeed, float newDelay)` | 先頭の`actionInfo`の移動先指定を有効化し、true時は速度と遅延を設定する。 |
| `activateCustomAction(GameObject playerDetected)` | `disableIgnorePlayerListChange`がfalseなら`ignorePlayerList`をtrueにしてから`setPlayerActionActive`を呼ぶ。 |
| `setIgnorePlayerListValue(bool state)` | `ignorePlayerList`を設定するだけ。 |
| `setPlayerActionActive(GameObject playerDetected)` | 未登録なら入室イベントと`playerList`追加を行い、プレイヤーの`playerActionSystem`へ自身を現在アクションとして渡す。 |
| `setPlayerActionDeactivate(GameObject playerDetected)` | `playerList`から削除してプレイヤー側の現在アクションを解除し、リストが空なら退室イベントを送る。 |
| `checkSendCurrentPlayerOnEvent(GameObject currentPlayer)` | `sendCurrentPlayerOnEvent`が有効なら対象プレイヤーを引数にイベントを発火する。 |
| `checkEventBeforeStartAction()` | `useEventBeforeStartAction`が有効なら`eventBeforeStartAction`を発火する。 |
| `setCustomActionTransform(Transform newTransform)` | `actionTransform`を`newTransform`へ設定するだけ。 |
| `getCurrentactionInfo()` | `actionInfoList`から`currentActionInfoIndex`番目の要素を返す。 |
| `increaseCurrentActionInfoIndex()` | `currentActionInfoIndex`を1増やし、末尾を超えないよう上限で止める。 |
| `decreaseCurrentActionInfoIndex()` | `currentActionInfoIndex`を1減らし、0未満にならないよう下限で止める。 |
| `setCurrentActionInfoIndex(int newIndex)` | `currentActionInfoIndex`を設定し、リスト範囲内にクランプする。 |
| `resetCurrentActionInfoIndex()` | `currentActionInfoIndex`を0に戻すだけ。 |
| `getCurrentActionInfoIndex()` | `currentActionInfoIndex`を返すだけ。 |
| `destroyAction()` | `setObjectParent`が有効な`objectToSetParent`を破棄したうえで、自身のGameObjectも破棄する。 |
| `checkEventOnStartAction()` | `useEventsOnStartEndAction`が有効なら`eventOnStartAction`を発火する。 |
| `checkEventOnEndAction()` | `useEventsOnStartEndAction`が有効なら`eventOnEndAction`を発火する。 |
| `checkEventAfterResumePlayer()` | `useEventAfterResumePlayer`が有効なら`eventAfterResumePlayer`を発火する。 |
| `checkEventOnEnableActionObject()` | `useEventsToEnableDisableActionObject`が有効なら`eventToEnableActionObject`を発火する。 |
| `checkEventOnDisableActionObject()` | `useEventsToEnableDisableActionObject`が有効なら`eventToDisableActionObject`を発火する。 |
| `clearPlayerList()` | `playerList`を空にするだけ。 |
| `removePlayerFromList(GameObject playerToRemove)` | `playerList`に対象がいれば削除するだけ。 |
| `disableAction()` | 各プレイヤーのデバイスリストから自身を外してアクションを解除し、`mainTrigger`を無効化する。 |
| `setObjectToSetParentInfo(Transform currentObject, Vector3 position, Vector3 rotation, Transform originalParent)` | 親子付け対象のオブジェクトと元の位置・回転・親を記録するだけ。 |
| `checkResetObjectPositionAndParentAfterAction()` | 記録した対象を元の親・ローカル位置・回転へ戻す。 |
| `inputPlayCurrentAnimation()` | `inputPlayCurrentAnimation(true)`を呼び、デバイスリスト確認ありで再生要求を出す。 |
| `inputPlayCurrentAnimationWithoutCheckingIfExistsOnaDeviceList()` | `inputPlayCurrentAnimation(false)`を呼び、デバイスリスト確認なしで再生要求を出す。 |
| `addNewAction()` | `actionInfoList`へ空の`actionInfo`を追加しコンポーネントを更新する。 |
| `addNewActionFromEditor(string actionSystemName, float actionSystemDuration, float actionSystemSpeed, bool useActionSystemID, int actionSystemID, string actionSystemAnimationName)` | 先頭`actionInfo`とGameObject名を、指定名・再生時間・速度・IDまたはアニメーション名で初期化して更新する。 |
| `addNewEvent(int actionInfoIndex)` | 指定`actionInfo`の`eventInfoList`へ空の`eventInfo`を追加して更新する。 |
| `addNewEventFirstPerson(int actionInfoIndex)` | 指定`actionInfo`の`firstPersonEventInfoList`へ空の`eventInfo`を追加する。 |
| `duplicateThirdPersonEventsOnFirstPerson(int actionInfoIndex)` | 一人称イベントリストを空にしてから、三人称イベントの複製を追加する。 |
| `replaceAnimationAction()` | エディタ専用で、指定レイヤーのAnimatorStateを新しいクリップ・速度・ミラー設定へ差し替え、`actionInfo`も更新する。 |
| `getChildAnimatorState(string stateName, UnityEditor.Animations.AnimatorStateMachine stateMachine)` | ステートマシンを再帰的に辿って同名ステートを探し、ループ上限付きで`animatorStateToReplace`に保持する。 |
| `enableOrDisableAutoUseActionOnTriggerByAI(bool state)` | 非再生時のみ先頭`actionInfo`のAI停止と距離/角度チェックを設定し、`eventTriggerSystem`のタグリストも更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`でコンポーネントとシーンの更新を通知する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPlayerInside` | `UnityEvent` | – |
| `eventOnPlayerOutside` | `UnityEvent` | – |
| `eventOnStartAction` | `UnityEvent` | – |
| `eventOnEndAction` | `UnityEvent` | – |
| `eventAfterResumePlayer` | `UnityEvent` | – |
| `eventBeforeStartAction` | `UnityEvent` | – |
| `eventToEnableActionObject` | `UnityEvent` | – |
| `eventToDisableActionObject` | `UnityEvent` | – |
| `eventOnInterrupOtherActionActive` | `UnityEvent` | – |
| `eventOnInterruptedAction` | `UnityEvent` | – |

## 内部型

- `actionInfo`（class）
- `eventInfo`（class）
