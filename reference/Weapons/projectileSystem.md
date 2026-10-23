# projectileSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/Projectiles/projectileSystem.cs:8`

**概要**: 弾丸やミサイルなど共通の投射物コンポーネント。命中判定、ダメージ、爆発、デカール、プール管理を担当する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Continuous Speculative Ingame | `setContinuousSpeculativeIngame` | `bool` | – | 起動時に剛体を連続衝突判定へ切り替える。 |
| Armor Surface Layer | `armorSurfaceLayer` | `string` | "Armor Surface" | アーマー面として扱うレイヤー名を指定する。 |
| Ability Function Name At Start | `abilityFunctionNameAtStart` | `string` | – | 発射時に自身へ送る機能関数の名前。 |
| Ability Function Name | `abilityFunctionName` | `string` | – | 着弾時に自身へ送る機能関数の名前。 |
| Use Custom Values | `useCustomValues` | `bool` | – | 武器側の設定を使わず固有値で動かすかどうか。 |
| Fake Projectile Trail | `fakeProjectileTrail` | `fakeProjectileTrailSystem` | – | 偽の飛翔軌跡を表示するトレイルの参照。 |

### Disable Projectile Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| No Impact Disable Timer | `noImpactDisableTimer` | `float` | – | 何にも当たらない時に消えるまでの秒数。 / 表示条件: `useCustomValues.boolValue && useDisableTimer.boolValue` |

### Impact Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Impact | `useEventOnImpact` | `bool` | – | 着弾時にイベントを呼ぶかどうか。 |
| Event On Impact | `eventOnImpact` | `UnityEvent` | – | 着弾した時に実行されるイベント。 / 表示条件: `useEventOnImpact` がオンのとき |
| Use Layer Mask Impact | `useLayerMaskImpact` | `bool` | – | 着弾イベントをレイヤーで限定するかどうか。 / 表示条件: `useEventOnImpact` がオンのとき |
| Layer Mask Impact | `layerMaskImpact` | `LayerMask` | – | 着弾イベントを発火する対象レイヤーのマスク。 / 表示条件: `useEventOnImpact.boolValue && useLayerMaskImpact.boolValue` |
| Send Object Detected On Impact Event | `sendObjectDetectedOnImpactEvent` | `bool` | – | 着弾したオブジェクトをイベントに渡すかどうか。 / 表示条件: `useEventOnImpact` がオンのとき |
| Object Detected On Impact Event | `objectDetectedOnImpactEvent` | `eventParameters.eventToCallWithGameObject` | – | 着弾したオブジェクトを引数に渡すイベント。 / 表示条件: `useEventOnImpact.boolValue && sendObjectDetectedOnImpactEvent.boolValue` |

### Explosion Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Explosion | `useEventOnExplosion` | `bool` | – | 爆発時にイベントを呼ぶかどうか。 |
| Even On Explosion | `evenOnExplosion` | `UnityEvent` | – | 爆発した時に実行されるイベント。 / 表示条件: `useEventOnExplosion` がオンのとき |

### Events On Adhere To Surface Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Adhere To Surface | `useEventOnAdhereToSurface` | `bool` | – | 表面に貼り付いた時にイベントを呼ぶかどうか。 |
| Event On Adhere To Surface | `eventOnAdhereToSurface` | `eventParameters.eventToCallWithGameObject` | – | 貼り付いた表面のオブジェクトを渡すイベント。 / 表示条件: `useEventOnAdhereToSurface` がオンのとき |

### Events On Projectile Fired Externally Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Projectile Fired Externally | `useEventOnProjectileFiredExternally` | `bool` | – | 外部から発射された時にイベントを呼ぶかどうか。 |
| Event On Projectile Fired Externally | `eventOnProjectileFiredExternally` | `UnityEvent` | – | 外部から発射された時に実行するイベント。 / 表示条件: `useEventOnProjectileFiredExternally` がオンのとき |

### Projectile Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Trail Renderer | `mainTrailRenderer` | `TrailRenderer` | – | 発射時に表示するトレイルの参照。 |
| Main Collider | `mainCollider` | `Collider` | – | 弾の当たり判定や範囲計算に使うコライダー。 |
| Secondary Bullet Mesh Collider | `secondaryBulletMeshCollider` | `MeshCollider` | – | 貫通用メッシュに付くコライダーの参照。 |
| Main Map Object Information | `mainMapObjectInformation` | `mapObjectInformation` | – | マップアイコンの登録や解除に使う参照。 |
| Audio Clip Bip Manager | `audioClipBipManager` | `audioClipBip` | – | 遅延してビープ音を鳴らすコンポーネント参照。 |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | 速度や `kinematic` を制御する剛体の参照。 |
| Bullet Mesh | `bulletMesh` | `GameObject` | – | 着弾時に非表示にする弾のメッシュ。 |
| Secondary Bullet Mesh | `secondaryBulletMesh` | `GameObject` | – | 貫通時に有効にする2つ目のメッシュ。 |
| Main Projectile Impact System | `mainProjectileImpactSystem` | `projectileImpactSystem` | – | 着弾演出を生成するインパクトシステムの参照。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `currentProjectileInfo` | `projectileInfo` | – | – |
| `disableProjectileMeshOnImpact` | `bool` | true | – |
| `useLayerMaskCollision` | `bool` | – | – |
| `layerMaskCollision` | `LayerMask` | – | – |
| `useEventOnCollision` | `bool` | – | – |
| `eventOnCollision` | `UnityEvent` | – | – |
| `projectileInitialized` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `parentDestroyed()` | `secondaryBulletMesh` があれば親を外してコライダーを戻し、なければ自身を破棄する。 |
| `setEnemy(GameObject obj)` | `missileWaiting` を開始し、設定秒後に目標と射撃位置を設定する。 |
| `setIgnoreProjectileWithAbilityState(bool state)` | `ignoreProjectileWithAbilityState` を設定するだけ。 |
| `checkSurface(Collider col)` | 命中コライダーに対し貫通/防御判定、ダメージ、爆発、デカール、切断などの命中処理を実行する。 |
| `checkMapIcon()` | マップ情報を取得し、割り当て済みなら `removeMapObject` でアイコンを消す。 |
| `createMapIconInfo()` | マップ情報を取得し、割り当て済みなら `createMapIconInfo` でアイコンを生成する。 |
| `checkExplodeProjectile()` | 爆発遅延の設定があればコルーチンで待ってから、なければ即座に爆発処理を呼ぶ。 |
| `explodeProjectileFunction()` | 爆発系なら親を一時解除して爆発ダメージを適用し、焦げ跡・マップアイコン・無効化を行う。 |
| `setProjectileScorch()` | `decalManager` で着弾デカールを付け、失敗時はレイキャストで焦げ跡・効果音・粒子を出す。 |
| `createImpactSound(AudioElement impactSoundEffect)` | `projectileImpactSystem` をプール生成または再利用し、渡された効果音で着弾音を鳴らす。 |
| `canActivateEffect(Collider col)` | 未使用かつ対象レイヤーで、除外タグや所有者条件を満たすコライダーかを判定して返す。 |
| `creatImpactParticles()` | 未生成なら `impactParticles` をプール生成またはインスタンス化し、生成済みフラグを立てる。 |
| `disableBullet(float time)` | `noImpactDisableTimer` を設定し、貫通設定がなければ kinematic 化して弾メッシュを隠す。 |
| `setKinematicState(bool state)` | `mainRigidbody` の `isKinematic` を設定するだけ。 |
| `setProjectileInfo(projectileInfo info)` | `useCustomValues` でなければ弾情報を複製し、無効化タイマーと発射時刻を設定する。 |
| `setProjectileOnwer(GameObject owner)` | `currentProjectileInfo.owner` を設定するだけ。 |
| `setTargetToDamageLayer(LayerMask layer)` | `currentProjectileInfo.targetToDamageLayer` を設定するだけ。 |
| `setUseCustomIgnoreTags(bool state, List<string> newCustomTagsToIgnoreList)` | 除外タグ使用フラグと `customTagsToIgnoreList` を設定するだけ。 |
| `rayCastShoot(Collider surface, Vector3 position, Vector3 forwardDirection)` | 着弾位置へ移動して初期化し、遅延設定なら遅延付きで、なければ即 `checkSurface` を呼ぶ。 |
| `setProjectileLocalRotation(Vector3 newProjectileLocalRotation)` | `projectileLocalRotation` を設定するだけ。 |
| `checkSurfaceWithDelay(Collider surface)` | 既存の遅延処理を止め、`checkSurfaceWithDelayCoroutine` を開始する。 |
| `checkRemoteEvents(GameObject objectToCheck)` | 対象（null なら `objectToDamage`）の `remoteEventSystem` に登録済みイベントを送る。 |
| `checkRemoteEventOnProjectile(string remoteEventName)` | 自身の `remoteEventSystem` で指定名のリモートイベントを呼ぶ。 |
| `checkRemoteEventsOnProjectile(List<string> remoteEventNameList)` | 自身の `remoteEventSystem` で受け取った名前リストのイベントを順に呼ぶ。 |
| `creatFakeProjectileTrail(Vector3 targetPosition)` | 偽トレイルを初期化して目標位置まで飛ばし、プール時は破棄を無効化に切り替える。 |
| `setDestroyTrailAfterTimeState(bool state)` | 偽トレイルの時間経過破棄設定を切り替える。 |
| `setFakeProjectileTrailSpeedMultiplier(float newValue)` | 偽トレイルの速度倍率を設定する。 |
| `destroyProjectileWithDelay(float newTime)` | `newTime` は使わず爆発コルーチンを開始するだけ（非アクティブ時は即破棄）。 |
| `destroyProjectile()` | マップアイコンを消し、プール時は返却・リセット・退避移動、通常時は `Destroy` する。 |
| `isProjectileUsed()` | `projectileUsed` を返すだけ。 |
| `setProjectileUsedState(bool state)` | `projectileUsed` を設定するだけ。 |
| `initializeProjectile()` | 初期化済みなら戻り、各参照取得・メッシュ回転・速度/重力・粒子・開始メッセージを行う。 |
| `returnBullet(Vector3 direction, GameObject owner, bool ignoreProjectileOwner)` | 所有者や方向へ向き直し、所有者と速度を再設定してコライダー有効・kinematic 解除で飛ばし直す。 |
| `attachProjectileToSurface()` | レイ/球体キャストで面を探し、`decalManager` で刺さった状態にしてコライダーを無効化し、イベントを呼ぶ。 |
| `checkEventOnProjectileFiredExternally()` | フラグが立っていれば `eventOnProjectileFiredExternally` を発火するだけ。 |
| `enableOrDisableProjectileCollider(bool state)` | 衝突検出モードを調整し、`state` に応じて kinematic・重力・二次メッシュコライダーを設定する。 |
| `checkProjectilesParent()` | 表面添着フラグを立て、親から `healthManagement` を取得する。 |
| `setIgnoreParentDestroyedState(bool state)` | `ignoreParentDestroyed` を設定するだけ。 |
| `enableOrDisableSecondaryMeshCollider(bool state)` | `secondaryBulletMeshCollider` の有効状態を設定するだけ。 |
| `enableOrDisableMainTrailRenderer(bool state)` | 無視設定がなければトレイルレンダラーの有効状態を設定する。 |
| `projectimeImpactState(GameObject objectToDamage)` | 命中イベント使用時、対象レイヤーが一致すれば `callEventOnImpact` を呼ぶ。 |
| `callEventOnImpact()` | `objectToDamage` を渡す命中イベントと `eventOnImpact` を発火する。 |
| `checkCollisionDetectionMode()` | 設定時のみ、一度だけ `ContinuousSpeculative` の衝突検出モードを適用する。 |
| `getProjectileRigibody()` | `mainRigidbody` を返すだけ。 |
| `setNewProjectileDamage(float newValue)` | `projectileDamage` を上書き設定するだけ。 |
| `setProjectileDamageMultiplier(float newValue)` | `projectileDamage` に倍率を掛けるだけ。 |
| `getProjectileComponents(bool calledFromEditor)` | 各種コンポーネント参照を取得し、エディタ呼び出しなら `updateComponent` で更新する。 |
| `resetProjectile()` | メッシュ・速度・対象・衝突リスト・トレイル・親子関係など全状態を初期化する。 |
| `checkToResetProjectile()` | 以前プールへ戻されていればリセットしてアイコンを再生成し、そうでなければ捕獲フラグを下ろす。 |
| `setProjectileSpecialActionActiveState(bool state)` | 本体が空で何もしない。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnImpact` | `UnityEvent` | – |
| `eventOnCollision` | `UnityEvent` | – |
| `evenOnExplosion` | `UnityEvent` | – |
| `eventOnProjectileFiredExternally` | `UnityEvent` | – |
