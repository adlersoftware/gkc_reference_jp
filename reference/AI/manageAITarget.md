# manageAITarget

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Turret/manageAITarget.cs:6`

**概要**: タレットの視界トリガー情報から敵factionを判定し、最も近い敵を目標として取得する。視界半径の拡大、factionへの警告、イベント発火、ハッキング結果の反映までを担う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### AI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Time To Check Suspect | `timeToCheckSuspect` | `float` | – | – |
| Layer Mask | `layerMask` | `LayerMask` | – | – |
| Layer To Check Targets | `layerToCheckTargets` | `LayerMask` | – | – |
| Function To Shoot | `functionToShoot` | `string` | – | – |
| Extra Field Of View Radius On Spot | `extraFieldOfViewRadiusOnSpot` | `float` | – | – |
| Check Raycast To View Target | `checkRaycastToViewTarget` | `bool` | true | – |
| Layer To Check Raycast To View Target | `layerToCheckRaycastToViewTarget` | `LayerMask` | – | – |

### Range Vision Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vision Range | `visionRange` | `float` | 90 | – |
| Min Distance To Adquire Target | `minDistanceToAdquireTarget` | `float` | 2 | – |
| Allow Detection When Too Close Even Not Visible | `allowDetectionWhenTooCloseEvenNotVisible` | `bool` | – | – |
| Ignore Vision Range Active | `ignoreVisionRangeActive` | `bool` | – | – |
| Check If Target Is Physically Visible Radius | `checkIfTargetIsPhysicallyVisibleRadius` | `float` | 0.2f | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Faction To Change Name | `factionToChangeName` | `string` | "Friend Turrets" | – |
| Surprised Character State Name | `surprisedCharacterStateName` | `string` | "Surprised" | – |
| Wondering Character State Name | `wonderingCharacterStateName` | `string` | "Wondering" | – |
| Alert Faction On Spotted | `alertFactionOnSpotted` | `bool` | – | – |
| Alert Faction Radius | `alertFactionRadius` | `float` | 10 | – |

### AI State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| On Spotted | `onSpotted` | `bool` | – | – |
| Paused | `paused` | `bool` | – | – |
| Hacking | `hacking` | `bool` | – | – |
| Checking Threat | `checkingThreat` | `bool` | – | – |
| Target Is Character | `targetIsCharacter` | `bool` | – | – |
| Target Is Vehicle | `targetIsVehicle` | `bool` | – | – |
| Threat Info Stored | `threatInfoStored` | `bool` | – | – |
| Seeing Current Target | `seeingCurrentTarget` | `bool` | – | – |
| Enemy To Shoot | `enemyToShoot` | `GameObject` | – | – |
| Posible Threat | `posibleThreat` | `GameObject` | – | – |
| Place To Shoot | `placeToShoot` | `Transform` | – | – |
| Different Enemy | `differentEnemy` | `bool` | – | – |
| Current Object Detected By Raycast | `currentObjectDetectedByRaycast` | `GameObject` | – | – |

### Targets Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enemies | `enemies` | `List<GameObject>` | new List<GameObject> () | – |
| Not Enemies | `notEnemies` | `List<GameObject>` | new List<GameObject> () | – |
| Full Enemy List | `fullEnemyList` | `List<GameObject>` | new List<GameObject> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.red | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Spotted | `useEventsOnSpotted` | `bool` | – | – |
| Event On Spotted | `eventOnSpotted` | `UnityEvent` | – | – |
| Event On No Targets To Attack | `eventOnNoTargetsToAttack` | `UnityEvent` | – | – |

### AI Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Ray Cast Position | `rayCastPosition` | `Transform` | – | – |
| Fov Trigger | `fovTrigger` | `SphereCollider` | – | – |
| Hack Device | `hackDevice` | `GameObject` | – | – |
| View Trigger | `viewTrigger` | `checkCollisionType` | – | – |
| Faction Manager | `factionManager` | `characterFactionManager` | – | – |
| Character State Icon Manager | `characterStateIconManager` | `characterStateIconSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `resetCheckThreatValues()` | 射撃位置・容疑目標・脅威判定フラグとタイマーを初期化し、状態アイコンも消す。 |
| `checkCharacterFaction(GameObject character, bool damageReceived)` | 既知の敵かfactionが敵(被弾時は攻撃者判定)ならtrue。faction無視はfalse、車両は運転者で判定。 |
| `checkShootOrigin(GameObject attacker)` | 未発見時に攻撃者を敵として登録し、factionの検出済み敵へ追加して`hasBeenAttacked`を立てる。 |
| `checkIfTargetIsPhysicallyVisible(GameObject targetToCheck, bool checkingSuspect)` | 射撃位置から対象へレイを飛ばし、遮蔽物が無ければtrueを返す。車両時は対象車両の部位判定を用いる。 |
| `targetAdquired()` | `onSpotted`を立て、視界半径を拡大し`viewTrigger`を無効化、factionへ検出登録と警告・イベントを行う。 |
| `shootTarget()` | 本体はコメントのみで、何も処理しない。 |
| `pauseAI(bool state)` | `paused`フラグを設定するだけ。 |
| `checkPossibleTarget(GameObject objectToCheck)` | 対象のColliderを取得し、進入扱いで`checkTriggerInfo`を呼ぶ。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | 対象レイヤーなら進入時に敵/非敵へ登録し、退出時に敵/非敵から解除する。進入時は`paused`なら無視する。 |
| `canCheckSuspect(int suspectLayer)` | `layerToCheckTargets`に対象レイヤーが含まれるかを返す。 |
| `setCorrectlyHackedState()` | 成功として`setHackResult(true)`を呼ぶだけ。 |
| `setIncorrectlyHackedState()` | 失敗として`setHackResult(false)`を呼ぶだけ。 |
| `setHackResult(bool state)` | `hacking`を下ろし、成功時はfactionをfriendへ変えて敵リストを消去、失敗時は`hackFailed`を立てる。 |
| `activateHack()` | `hacking`をtrueにするだけ。 |
| `checkCharactersAroundAI()` | `notEnemies`の全オブジェクトを敵として再検出させる。 |
| `setCharacterStateIcon(string stateName)` | `characterStateIconManager`へ状態アイコンの表示を依頼する。 |
| `disableCharacterStateIcon()` | `characterStateIconManager`へ状態アイコンの非表示を依頼する。 |
| `setAIStateToDead()` | `enabled`をfalseにしてAIを停止するだけ。 |
| `checkEventsOnSpotted(bool state)` | イベント有効時、trueで発見イベント、falseで対象消失イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnSpotted` | `UnityEvent` | – |
| `eventOnNoTargetsToAttack` | `UnityEvent` | – |
