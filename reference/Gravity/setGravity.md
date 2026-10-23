# setGravity

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Gravity/setGravity.cs:5`

**概要**: トリガーやアニメーション付きの矢印として、範囲内のプレイヤー・NPC・車両・Rigidbodyの重力方向を一括変更する。中心点、無重力、カスタム重力値、親設定などをまとめて適用できる。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use With Player | `useWithPlayer` | `bool` | – | オンで`playerTag`を持つプレイヤーに重力変更を適用。 |
| Use With NPC | `useWithNPC` | `bool` | – | オンで`friendTag`と`enemyTag`のNPCにも重力変更を適用。 |
| Use With Vehicles | `useWithVehicles` | `bool` | – | オンで`vehicleGravityControl`を持つ乗り物にも重力を適用。 |
| Rotate Vehicle To Gravity Direction | `rotateVehicleToGravityDirection` | `bool` | – | オンで乗り物を新しい重力方向へ向けて回転させる。 |
| Use Center Point On Vehicle | `useCenterPointOnVehicle` | `bool` | – | オンで乗り物にも`centerPoint`を重力中心として渡す。 |
| Player Tag | `playerTag` | `string` | "Player" | プレイヤーと判定するタグ。一致した物体に重力を適用。 |
| Friend Tag | `friendTag` | `string` | "friend" | 味方NPCと判定するタグ。`useWithNPC`と組み合わせて使用。 |
| Enemy Tag | `enemyTag` | `string` | "enemy" | 敵NPCと判定するタグ。`useWithNPC`と組み合わせて使用。 |
| Use With Any Rigidbody | `useWithAnyRigidbody` | `bool` | – | オンでタグに関係なくRigidbody物体へ人工重力を付与。 |
| Check Only For Artificial Gravity System | `checkOnlyForArtificialGravitySystem` | `bool` | – | オンで人工重力用コンポーネントを持つ物体だけを対象に限定。 / 表示条件: `useWithAnyRigidbody` がオンのとき |
| Type Of Trigger | `typeOfTrigger` | `triggerType` | – | 重力を切り替えるタイミング。侵入時・退出時・両方から選択。 |
| Set Gravity Mode | `setGravityMode` | `bool` | true | オンで以下の重力モード設定をトリガー時に反映する。 |
| Set Regular Gravity | `setRegularGravity` | `bool` | – | オンで通常重力へ戻し、人工重力を解除する。 / 表示条件: `setGravityMode` がオンのとき |
| Set Zero Gravity | `setZeroGravity` | `bool` | – | オンで無重力モードを有効にする。 / 表示条件: `setGravityMode` がオンのとき |
| Disable Zero Gravity | `disableZeroGravity` | `bool` | – | オンで無重力モードを回転なしで解除する。 / 表示条件: `setGravityMode` がオンのとき |
| Set Custom Gravity Force | `setCustomGravityForce` | `bool` | – | オンで`customGravityForce`の値を重力加速度として設定。 |
| Custom Gravity Force | `customGravityForce` | `float` | – | キャラクターや物体に設定する重力加速度の値。 / 表示条件: `setCustomGravityForce` がオンのとき |
| Set Custom Gravity Force On Characters Enabled | `setCustomGravityForceOnCharactersEnabled` | `bool` | – | オンでキャラクターにもカスタム重力値を適用し、退出時に戻す。 |

### Grabbed Objects Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Drop Object If Gabbed | `dropObjectIfGabbed` | `bool` | true | オンで重力変更時につかんでいる物体を落とさせる。 |
| Drop Object Only If Not Grabbed Physically | `dropObjectOnlyIfNotGrabbedPhysically` | `bool` | – | オンで物理的につかんでいない場合のみ落下させる。 |

### Gravity Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Gravity Direction | `useCustomGravityDirection` | `bool` | – | オンで`customGravityDirection`を重力方向として使用。 |
| Custom Gravity Direction | `customGravityDirection` | `Vector3` | – | 適用する重力方向のベクトル。中心点より優先される。 / 表示条件: `useCustomGravityDirection` がオンのとき |
| Use Center Point | `useCenterPoint` | `bool` | – | オンで`centerPoint`へ向かう方向に重力を発生させる。 |
| Center Point | `centerPoint` | `Transform` | – | 重力の中心となる位置。未設定ならこの物体自身を使用。 / 表示条件: `useCenterPoint` がオンのとき |
| Use Center Point On Characters | `useCenterPointOnCharacters` | `bool` | – | オンでキャラクターにも中心点を重力中心として設定する。 / 表示条件: `useCenterPoint` がオンのとき |
| Use Center Point For Rigidbodies | `useCenterPointForRigidbodies` | `bool` | – | オンでRigidbody物体にも中心点を重力中心として設定。 |
| Use Inverse Direction To Center Point | `useInverseDirectionToCenterPoint` | `bool` | – | オンで中心点へ引く重力の向きを反転させる。 / 表示条件: `useCenterPointForRigidbodies` がオンのとき |
| Change Gravity Direction Active | `changeGravityDirectionActive` | `bool` | – | オンで算出した方向へ重力を直接変更する。 |
| Rotate To Surface Smoothly | `rotateToSurfaceSmoothly` | `bool` | true | オンで`changeOnTrigger`を使い滑らかに姿勢を回転させる。 |
| Set Circumnavigate Surface State | `setCircumnavigateSurfaceState` | `bool` | – | オンで表面回り込みの設定をトリガー時に反映する。 |
| Circumnavigate Surface State | `circumnavigateSurfaceState` | `bool` | – | 表面を回り込む移動を有効にするかどうかの値。 / 表示条件: `setCircumnavigateSurfaceState` がオンのとき |
| Set Check Surface In Front State | `setCheckSurfaceInFrontState` | `bool` | – | オンで前方の表面チェック設定をトリガー時に反映する。 / 表示条件: `setCircumnavigateSurfaceState` がオンのとき |
| Check Surface In Front State | `checkSurfaceInFrontState` | `bool` | – | 前方の表面チェックを有効にするかどうかの値。 / 表示条件: `setCircumnavigateSurfaceState.boolValue && setCheckSurfaceInFrontState.boolValue` |
| Set Check Surface Below Ledge State | `setCheckSurfaceBelowLedgeState` | `bool` | – | オンで足場下の縁チェック設定をトリガー時に反映する。 / 表示条件: `setCircumnavigateSurfaceState` がオンのとき |
| Check Surface Below Ledge State | `checkSurfaceBelowLedgeState` | `bool` | – | 足場下の縁チェックを有効にするかどうかの値。 / 表示条件: `setCircumnavigateSurfaceState.boolValue && setCheckSurfaceBelowLedgeState.boolValue` |
| Preserve Player Velocity | `preservePlayerVelocity` | `bool` | true | オンで重力方向変更時にプレイヤーの速度を維持する。 |
| Store Set Gravity Manager | `storeSetGravityManager` | `bool` | true | オンでこのトリガーを現在の重力設定元として記録させる。 |

### Set Parent Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Target Parent | `setTargetParent` | `bool` | – | オンで重力変更時に`targetParent`へ親子付けする。 |
| Set Rigidbodies Parent | `setRigidbodiesParent` | `bool` | – | オンでRigidbody物体の親を`targetParent`に設定する。 |
| Target Parent | `targetParent` | `GameObject` | – | 重力変更時に親として設定するオブジェクト。 / 表示条件: `setTargetParent.boolValue \|\| setRigidbodiesParent.boolValue` |

### Animation Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Animation | `useAnimation` | `bool` | true | オンでアニメーションを再生し矢印などの演出を動かす。 |
| Animation Name | `animationName` | `string` | "arrowAnim" | `mainAnimation`で再生するアニメーションのクリップ名。 / 表示条件: `useAnimation` がオンのとき |
| Main Animation | `mainAnimation` | `Animation` | – | 再生に使う`Animation`。未設定なら自動で取得を試みる。 / 表示条件: `useAnimation` がオンのとき |

### Center Point List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Center Point List | `useCenterPointList` | `bool` | – | オンで複数の中心点から最も近いものを重力中心にする。 |
| Use Center If Point List Too Close | `useCenterIfPointListTooClose` | `bool` | true | オンで中心点一覧より`centerPoint`が近い場合に優先する。 |
| Use Center Point List For Rigidbodies | `useCenterPointListForRigidbodies` | `bool` | – | オンでRigidbody物体にも中心点一覧を使用させる。 |

### Initial Objects On Gravity List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Initial Objects On Gravity List | `useInitialObjectsOnGravityList` | `bool` | – | オンで開始時に一覧内の物体へ重力変更を適用する。 |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | オンで対象判定などのデバッグログをコンソールに出力。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `movePlayerToGravityPosition` | `bool` | – | – |
| `raycastPositionToGetGravityPosition` | `Transform` | – | – |
| `layermaskToGetGravityPosition` | `LayerMask` | – | – |
| `teleportSpeed` | `float` | – | – |
| `rotationSpeed` | `float` | – | – |
| `centerPointList` | `List<Transform>` | new List<Transform> () | – |
| `artificialObjectGravityList` | `List<artificialObjectGravity>` | new List<artificialObjectGravity> () | – |
| `vehicleGameObjectList` | `List<GameObject>` | new List<GameObject> () | – |
| `initialObjectsOnGravityList` | `List<GameObject>` | new List<GameObject> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkObjectGravityOnEnter(GameObject objectToCheck)` | Colliderを取得して侵入扱いで`checkTriggerType`を呼ぶ。 |
| `checkObjectGravityOnExit(GameObject objectToCheck)` | Colliderを取得して退出扱いで`checkTriggerType`を呼ぶ。 |
| `checkTriggerType(Collider col, bool isEnter)` | Colliderがnullかトリガーなら戻り、そうでなければ`checkObjectOnGravitySystem`へ渡す。 |
| `checkObjectOnGravitySystem(GameObject objectToCheck, bool isEnter)` | プレイヤー/NPC/車両/任意Rigidbodyの種類に応じ、重力方向・無重力・中心点・重力値・親設定を一括で変更する。 |
| `getGravityDirection(Vector3 objectPosition)` | カスタム方向・中心点(リスト中最寄り)・自身の上方向の順で重力方向を返す。 |
| `reverseGravityDirection()` | 中心点と逆方向の設定を反転し、保持している全`artificialObjectGravity`にも反映する。 |

## 内部型

- `triggerType`（enum）
