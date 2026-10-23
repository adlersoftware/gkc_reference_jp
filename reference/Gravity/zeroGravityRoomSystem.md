# zeroGravityRoomSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Gravity/zeroGravityRoomSystem.cs:6`

**概要**: 範囲内のオブジェクトとキャラクターの重力を通常/無重力/カスタム方向へ切り替える重力ルーム。頂点ポリゴンで室内判定を行い、入退室時に重力設定や音、力を適用する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Room Has Regular Gravity | `roomHasRegularGravity` | `bool` | – | 室内を通常重力にする。カスタム重力方向は使われない。 |
| Room Has Zero Gravity | `roomHasZeroGravity` | `bool` | – | 室内のオブジェクトとキャラクターを無重力にする。 |
| Gravity Direction Transform | `gravityDirectionTransform` | `Transform` | – | カスタム重力の向き。このオブジェクトのUp方向を使用。 |
| Explanation | `explanation` | `string` | "The Gravity Direction will use the U… | 設定内容を説明するエディタ表示専用のテキスト。 / TextArea (2, 5) |

### New Gravity Outside Of Room Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use New Gravity Outside | `useNewGravityOutside` | `bool` | – | オンで退室時に室外用の重力設定を適用する。 |
| Outside Has Zero Gravity | `outsideHasZeroGravity` | `bool` | – | 室外を無重力にする。オフなら室外の向きを適用。 / 表示条件: `useNewGravityOutside` がオンのとき |
| Outside Gravity Direction Transform | `outsideGravityDirectionTransform` | `Transform` | – | 室外の重力方向。このオブジェクトのUp方向を使用。 / 表示条件: `useNewGravityOutside` がオンのとき |

### Objects Affected Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Objects Affected By Gravity | `objectsAffectedByGravity` | `bool` | true | 室内のオブジェクトに重力変化を適用する。 |
| Change Gravity Force For Objects | `changeGravityForceForObjects` | `bool` | – | オンで室内オブジェクトの重力加速度を変更する。 / 表示条件: `objectsAffectedByGravity` がオンのとき |
| New Gravity Force For Objects | `newGravityForceForObjects` | `float` | – | 室内オブジェクトに設定する重力加速度の値。 / 表示条件: `objectsAffectedByGravity.boolValue && changeGravityForceForObjects.boolValue` |

### Characters Affected Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Characters Affected By Gravity | `charactersAffectedByGravity` | `bool` | true | 室内のキャラクターに重力変化を適用する。 |
| Change Gravity Force For Characters | `changeGravityForceForCharacters` | `bool` | – | オンで室内キャラクターの重力加速度を変更する。 / 表示条件: `charactersAffectedByGravity` がオンのとき |
| New Gravity Force For Characters | `newGravityForceForCharacters` | `float` | – | 室内キャラクターに設定する重力加速度の値。 / 表示条件: `charactersAffectedByGravity.boolValue && changeGravityForceForCharacters.boolValue` |

### Zero Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Force To Objects On Zero Gravity State | `addForceToObjectsOnZeroGravityState` | `bool` | – | 無重力化した瞬間に室内オブジェクトへ力を加える。 |
| Force Amount To Object On Zero Gravity | `forceAmountToObjectOnZeroGravity` | `float` | – | 無重力化時に加える力の大きさ。 |
| Force Direction To Objects On Zero Gravity | `forceDirectionToObjectsOnZeroGravity` | `Transform` | – | 加える力の向き。このオブジェクトのUp方向。 |
| Force Mode To Objects On Zero Gravity | `forceModeToObjectsOnZeroGravity` | `ForceMode` | – | 力を加える方式を決める`ForceMode`。 |
| Add Initial Force To Objects On Zero Gravity State | `addInitialForceToObjectsOnZeroGravityState` | `bool` | – | 開始時に`AddExplosionForce`で弾き飛ばす。 |
| Initial Force To Objects On Zero Gravity | `initialForceToObjectsOnZeroGravity` | `float` | – | 開始時に加える爆発力の強さを指定する。 |
| Initial Force Radius To Objects On Zero Gravity | `initialForceRadiusToObjectsOnZeroGravity` | `float` | – | 開始時の爆発力が影響する半径を指定する。 |
| Initial Force Position To Objects On Zero Gravity | `initialForcePositionToObjectsOnZeroGravity` | `Transform` | – | 爆発力の中心となる位置のトランスフォーム。 |

### Tags To Affect

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Tag | `playerTag` | `string` | – | プレイヤー判定に使うタグ。部屋の登録に使用。 |

### Room Points List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Highest Point Poisition | `highestPointPoisition` | `Transform` | – | 室内判定の上限となる高さのトランスフォーム。 |
| Lowest Point Position | `lowestPointPosition` | `Transform` | – | 室内判定の下限となる高さのトランスフォーム。 |
| Room Points Parent | `roomPointsParent` | `Transform` | – | 部屋の輪郭点を追加するときの親トランスフォーム。 |

### Objects Inside Room List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Objects Inside Parent | `addObjectsInsideParent` | `bool` | – | 開始時に指定した親の子の剛体を室内登録する。 |
| Objects Inside Parent | `objectsInsideParent` | `Transform` | – | 室内として登録するオブジェクトの親トランスフォーム。 / 表示条件: `addObjectsInsideParent` がオンのとき |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Sounds | `useSounds` | `bool` | – | 重力状態が変わったときの効果音再生を有効にする。 |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | 各`AudioElement`に割り当てる`AudioSource`。 / 表示条件: `useSounds` がオンのとき |
| Regular Gravity Sound | `regularGravitySound` | `AudioClip` | – | 通常重力に戻したときに鳴らす効果音クリップ。 / 表示条件: `useSounds` がオンのとき |
| Regular Gravity Audio Element | `regularGravityAudioElement` | `AudioElement` | – | 通常重力音の再生設定を持つ`AudioElement`。 / 表示条件: `useSounds` がオンのとき |
| Zero Gravity Sound | `zeroGravitySound` | `AudioClip` | – | 無重力に切り替えたときに鳴らす効果音クリップ。 / 表示条件: `useSounds` がオンのとき |
| Zero Gravity Audio Element | `zeroGravityAudioElement` | `AudioElement` | – | 無重力音の再生設定を持つ`AudioElement`。 / 表示条件: `useSounds` がオンのとき |
| Custom Gravity Sound | `customGravitySound` | `AudioClip` | – | カスタム重力に切り替えたときの効果音クリップ。 / 表示条件: `useSounds` がオンのとき |
| Custom Gravity Audio Element | `customGravityAudioElement` | `AudioElement` | – | カスタム重力音の再生設定を持つ`AudioElement`。 / 表示条件: `useSounds` がオンのとき |
| Use Sounds On Characters | `useSoundsOnCharacters` | `bool` | – | キャラクターの入退室時に効果音を鳴らす。 / 表示条件: `useSounds` がオンのとき |
| Sound On Entering | `soundOnEntering` | `AudioClip` | – | キャラクターが入室したときの効果音クリップ。 / 表示条件: `useSounds.boolValue && useSoundsOnCharacters.boolValue` |
| On Entering Audio Element | `onEnteringAudioElement` | `AudioElement` | – | 入室音の再生設定を持つ`AudioElement`。 / 表示条件: `useSounds.boolValue && useSoundsOnCharacters.boolValue` |
| Sound On Exiting | `soundOnExiting` | `AudioClip` | – | キャラクターが退室したときの効果音クリップ。 / 表示条件: `useSounds.boolValue && useSoundsOnCharacters.boolValue` |
| On Exiting Audio Element | `onExitingAudioElement` | `AudioElement` | – | 退室音の再生設定を持つ`AudioElement`。 / 表示条件: `useSounds.boolValue && useSoundsOnCharacters.boolValue` |

### Debug Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Debug Mode Active | `debugModeActive` | `bool` | – | 毎フレーム室内判定を計算して結果を記録する。 |
| Debug Mode List Active | `debugModeListActive` | `bool` | – | 室内登録時にデバッグ用のオブジェクトリストへ追加する。 / 表示条件: `debugModeActive` がオンのとき |
| Show Debug Print | `showDebugPrint` | `bool` | – | 重力適用の処理内容をコンソールへ出力する。 |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | true | 部屋の輪郭線や中心位置のギズモを表示する。 |
| Center Gizmo Scale | `centerGizmoScale` | `Vector3` | Vector3.one | 部屋中心に描くキューブのギズモサイズ。 / 表示条件: `showGizmo` がオンのとき |
| Room Center Color | `roomCenterColor` | `Color` | Color.gray | 部屋中心に描くキューブのギズモ色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.white | シーンビューに表示するラベル文字の色。 / 表示条件: `showGizmo` がオンのとき |
| Lines Color | `linesColor` | `Color` | Color.yellow | 部屋の輪郭を結ぶ線のギズモ色。 / 表示条件: `showGizmo` がオンのとき |
| Use Handle For Waypoints | `useHandleForWaypoints` | `bool` | – | シーンビューで輪郭点をハンドル操作できるようにする。 / 表示条件: `showGizmo` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `nonAffectedObjectsTagList` | `List<string>` | new List<string> () | – |
| `charactersTagList` | `List<string>` | new List<string> () | – |
| `roomPointsList` | `List<Transform>` | new List<Transform> () | – |
| `roomPoints2DList` | `List<Vector2>` | new List<Vector2> () | – |
| `objectsInsideList` | `List<GameObject>` | new List<GameObject> () | – |
| `charactersInsideList` | `List<GameObject>` | new List<GameObject> () | – |
| `charactersInsideListAtStart` | `List<GameObject>` | new List<GameObject> () | – |
| `objectInfoList` | `List<objectInfo>` | new List<objectInfo> () | – |
| `offsetOnNewRoomPoint` | `float` | 2 | – |
| `roomCenter` | `Vector3` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectToAdd(GameObject newObject)` | キャラクターはリスト登録して重力モードを設定し、非対象タグ以外のオブジェクトは`setObjectInsideState`で処理する。 |
| `checkObjectToRemove(GameObject newObject)` | 室内判定を再確認し、外に出たキャラクターの重力を外部設定へ戻し、オブジェクトは`removeObjectFromRoom`で外す。 |
| `removeObjectFromRoom(GameObject newObject)` | オブジェクトをリストから外し、掴まれていれば重力コンポーネントや`useGravity`、ルーム参照を戻す。 |
| `setObjectInsideState(GameObject newObject)` | Rigidbodyに応じて通常/無重力/カスタム重力を適用し、`grabbedObjectState`へルームを記録する。 |
| `ContainsPoint(Vector2 currentPosition)` | ルーム頂点の2Dポリゴンで内外判定し、点が室内か返す。 |
| `checkInsideFarthestPosition(Vector3 currentPosition)` | 最高点と最低点の高さの間にあるか返す。 |
| `objectInsideRoom(GameObject objectToCheck)` | オブジェクトが室内リストに含まれるか返す。 |
| `FindParentWithTag(GameObject childObject, List<string> tagList)` | 親をたどってタグリストに一致する親があるか返す。 |
| `setNewGravityForceValueForObjectsInsideRoom(float newGravityForceValue)` | 室内オブジェクトの重力値を新しい値で設定する。 |
| `setOriginalGravityForceValueForObjectsInsideRoom()` | 室内オブジェクトの重力値を元の値へ戻す。 |
| `setGravityForceValueForObjectsInsideRoom(bool setOriginal, float newValue)` | 室内のオブジェクトとキャラクターへ、元の値か新しい重力値を適用する。 |
| `setZeroGravityStateOnRoom()` | 既に無重力なら何もせず、無重力にして音を鳴らし、室内の重力更新と力を加える。 |
| `setRegularGravityStateOnRoom()` | 既に通常重力なら何もせず、通常重力へ切替えて音を鳴らし室内を更新する。 |
| `setCustomGravityStateOnRoom()` | カスタム重力音を鳴らし、通常/無重力フラグを下ろして室内を更新する。 |
| `setCustomGravityStateOnRoom(Transform newGravityDirectionTransform)` | 指定Transformの上方向を重力方向として設定し、室内の重力を更新する。 |
| `setOriginalGravityDirectionStateOnRoom()` | `gravityDirectionTransform`の上方向を重力方向に戻して室内を更新する。 |
| `updateObjectsAndCharactersGravityInsideRoom()` | 室内の全オブジェクトに`setObjectInsideState`を適用し、キャラクターの重力も更新する。 |
| `setCharactersGravityStateOnRoom(bool hasRegularGravity, bool hasZeroGravity)` | 室内キャラクターへ通常/無重力/カスタム重力を適用し、必要なら重力値も変更する。 |
| `addForceToObjectsOnZeroGravity()` | 設定が有効なら室内のRigidbodyへ方向×力の`AddForce`を行う。 |
| `addExplosionForceToObjectsOnZeroGravity()` | 室内のRigidbodyへ指定位置からの爆発力を加える。 |
| `playSound(AudioElement sound)` | 音が有効なら指定音を`AudioPlayer`で再生する。 |
| `addObjectToRoom(GameObject objectToAdd)` | `checkObjectToAdd`を呼ぶだけ。 |
| `addObjectsToRoom(Transform parentToCheck)` | 子のRigidbodyのうち動的かつCollider付きのものを室内へ追加する。 |
| `addChildsFromParent(Transform parentToCheck)` | 子の動的Rigidbodyを判定なしで`objectsInsideList`へ追加する。 |
| `isRoomHasZeroGravityActive()` | ルームが無重力か返す。 |
| `renameRoomPoints()` | ルーム頂点を1から連番にリネームしてコンポーネントを更新する。 |
| `addRoomPoint()` | 頂点を新規作成して親に付け、末尾の位置+オフセットに置いてリストへ追加する。 |
| `addRoomPoint(int index)` | 指定頂点の次に新しい頂点を作成して挿入し、名前を振り直す。 |
| `removeRoomPoint(int index)` | 指定頂点のGameObjectを破棄してリストから削除する。 |
| `removeAllRoomPoints()` | 全頂点のGameObjectを破棄してリストを空にする。 |

## 内部型

- `objectInfo`（class）
- `characterInfo`（class）
