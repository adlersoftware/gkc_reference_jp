# applyEffectOnArea

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/applyEffectOnArea.cs:6`

**概要**: トリガーまたはオーバーラップ球で範囲内のオブジェクトを検出し、`effectAmount`の効果を適用するエリア。ステータス増減・遠隔イベント・退出時処理・継続時間付き有効化を備える。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Effect Enabled | `effectEnabled` | `bool` | true | – |
| Effect Active | `effectActive` | `bool` | – | – |
| Use Effect Rate | `useEffectRate` | `bool` | – | – |
| Effect Rate | `effectRate` | `float` | – | – |
| Effect Amount | `effectAmount` | `float` | – | – |
| Disable Effect Area Trigger On Disable Area | `disableEffectAreaTriggerOnDisableArea` | `bool` | true | – |
| Apply Value At Once | `applyValueAtOnce` | `bool` | – | – |
| Area Effect Duration | `areaEffectDuration` | `float` | – | – |
| Activate Area Effect At Start | `activateAreaEffectAtStart` | `bool` | – | – |
| Apply Effect On Exit | `applyEffectOnExit` | `bool` | – | – |

### Object Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Collider Trigger For Detection | `useColliderTriggerForDetection` | `bool` | true | – |
| Use Overlap Sphere For Detection | `useOverlapSphereForDetection` | `bool` | – | – |
| Overlap Sphere Radius | `overlapSphereRadius` | `float` | – | – |
| Overlap Center Position | `overlapCenterPosition` | `Transform` | – | – |
| Use Overlap On Update | `useOverlapOnUpdate` | `bool` | – | – |
| Check If Object Has Rigidbody | `checkIfObjectHasRigidbody` | `bool` | true | – |
| Check Obstacle Between Area And Target Found | `checkObstacleBetweenAreaAndTargetFound` | `bool` | – | – |
| Obstacle To Check Layermask | `obstacleToCheckLayermask` | `LayerMask` | – | – |

### Objects To Affect Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer To Affect | `layerToAffect` | `LayerMask` | – | – |
| Tag To Affect List | `tagToAffectList` | `List<string>` | new List<string> () | – |
| Use Objects To Ignore List | `useObjectsToIgnoreList` | `bool` | – | – |
| Objects To Ignore List | `objectsToIgnoreList` | `List<GameObject>` | new List<GameObject> () | – |
| Ignore Main Character Colliders | `ignoreMainCharacterColliders` | `bool` | – | – |
| Main Character Game Object | `mainCharacterGameObject` | `GameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Detected Object List | `detectedObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| Player Stats System List | `playerStatsSystemList` | `List<playerStatsSystem>` | new List<playerStatsSystem> () | – |

### Remote Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remove Event Name List | `removeEventNameList` | `List<string>` | new List<string> () | – |

### Stats To Affect Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Stat Info List | `statInfoList` | `List<statInfo>` | new List<statInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Effect Active | `eventOnEffectActive` | `UnityEvent` | – | – |
| Event On Effect Deactivate | `eventOnEffectDeactivate` | `UnityEvent` | – | – |
| Send Objects Detected On Event | `sendObjectsDetectedOnEvent` | `bool` | – | – |
| Event To Send Objects Detected | `eventToSendObjectsDetected` | `eventParameters.eventToCallWithGameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Collider | `mainCollider` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkEffectToDetectedObjects()` | 検出済みの各オブジェクトに`effectAmount`を`valueToAdd`として設定し、`applyEffect`を呼ぶ。 |
| `applyEffect(GameObject objectToAffect)` | 仮想メソッドで、既定では`sendObjectsDetectedOnEvent`が真なら検出オブジェクトをイベント送信するだけ。 |
| `checkApplyEffectOnExit(GameObject objectToAffect)` | 本体が空で何もしない。派生クラス用の仮想フック。 |
| `applyEffectOnStats()` | 保持する`playerStatsSystem`すべてに`statInfoList`の各ステータス増減を適用する。 |
| `setObjectToCheckManually(GameObject objectToCheck)` | 対象の`Collider`を取得して`OnTriggerEnter`を直接呼び、手動で検出扱いにする。 |
| `checkObjectsWithOverlap()` | 中心と半径で`Physics.OverlapSphere`し、非トリガーのコライダーを検出処理に回す。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | タグ/レイヤーと遮蔽判定を通った対象を一覧へ追加し、`useEffectRate`無効なら即効果適用、退出時は解除する。 |
| `toggleEffectActive()` | `setEffectActiveState`に現在値の否定を渡して有効状態を反転するだけ。 |
| `setEffectActiveState(bool state)` | `effectActive`を設定し、コライダー有効化・検出リスト消去・有効/無効イベント発火を行う。 |
| `removeDetectedObject(GameObject objectToRemove)` | 検出リストと`playerStatsSystemList`から対象を外し、空なら`objectsInside`を偽にする。 |
| `setEffectActiveStateWithDuration()` | 進行中のコルーチンを止め、`areaEffectDuration`秒だけ有効にするコルーチンを開始する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnEffectActive` | `UnityEvent` | – |
| `eventOnEffectDeactivate` | `UnityEvent` | – |

## 内部型

- `statInfo`（class）
