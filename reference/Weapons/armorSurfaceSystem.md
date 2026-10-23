# armorSurfaceSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/armorSurfaceSystem.cs:7`

**概要**: 装甲サーフェスとして、当たった弾を蓄積して持ち主へ跳ね返すコンポーネント。装甲の有効状態・耐久値・優先度・当たり判定サイズを管理する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Armor Active | `armorActive` | `bool` | true | – |
| Armor Owner | `armorOwner` | `GameObject` | – | – |
| Use Min Angle To Return Projectile To Owner | `useMinAngleToReturnProjectileToOwner` | `bool` | – | – |
| Min Angle To Return Projectile To Owner | `minAngleToReturnProjectileToOwner` | `float` | – | – |

### Armor Health Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Armor Health Amount | `useArmorHealthAmount` | `bool` | – | – |
| Armor Health Amount | `armorHealthAmount` | `float` | – | – |
| Max Armor Health Amount | `maxArmorHealthAmount` | `float` | – | – |
| Disable Armor On Empty Health | `disableArmorOnEmptyHealth` | `bool` | – | – |

### Break Through Armor Surface Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Block Projectiles From Breaking Through Surface Enabled | `blockProjectilesFromBreakingThroughSurfaceEnabled` | `bool` | – | – |
| Armor Surface Priority Value | `armorSurfacePriorityValue` | `int` | -1 | – |

### Return Projectiles Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Throw Projectiles To Previous Owner Enabled | `throwProjectilesToPreviousOwnerEnabled` | `bool` | true | – |
| Use New Damage Layer On Return Projectiles | `useNewDamageLayerOnReturnProjectiles` | `bool` | – | – |
| New Damage Layer On Return Projectiles | `newDamageLayerOnReturnProjectiles` | `LayerMask` | – | – |
| Set Use Custom Ignore Tags On Return Projectiles State | `setUseCustomIgnoreTagsOnReturnProjectilesState` | `bool` | – | – |
| Use Custom Ignore Tags On Return Projectiles State | `useCustomIgnoreTagsOnReturnProjectilesState` | `bool` | – | – |
| Custom Tags To Ignore On Return Projectiles List | `customTagsToIgnoreOnReturnProjectilesList` | `List<string>` | new List<string> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Projectiles Stored | `projectilesStored` | `List<projectileSystem>` | new List<projectileSystem> () | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Return Projectiles On Contact | `returnProjectilesOnContact` | `bool` | – | – |
| Event To Return Projectiles On Contact | `eventToReturnProjectilesOnContact` | `UnityEvent` | – | – |
| Use Event On Deflect Projectiles Activated | `useEventOnDeflectProjectilesActivated` | `bool` | – | – |
| Event On Deflect Projectiles Activated | `eventOnDeflectProjectilesActivated` | `UnityEvent` | – | – |
| Use Event On Armor Health Empty | `useEventOnArmorHealthEmpty` | `bool` | – | – |
| Event On Armor Health Empty | `eventOnArmorHealthEmpty` | `UnityEvent` | – | – |
| Use Event On Armor Health Damaged | `useEventOnArmorHealthDamaged` | `bool` | – | – |
| Event On Armor Health Damaged | `eventOnArmorHealthDamaged` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Collider | `mainCollider` | `BoxCollider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addProjectile(projectileSystem newProjectile)` | 未登録なら弾を蓄積し、接触時返却イベントが有効なら発火する。 |
| `throwProjectilesStored(Vector3 throwDirection)` | 蓄積した弾をすべて、設定に応じて持ち主を無視しつつ指定方向へ返却してリストを空にする。 |
| `throwProjectilesStoredCheckingDirection(Transform playerTransform, Transform mainCameraTransform)` | 蓄積弾があれば返却イベントを発火し、プレイヤー方向との角度を判定して弾ごとに返却先と設定を調整する。 |
| `thereAreProjectilesStored()` | 蓄積中の弾があるかを返すだけ。 |
| `destroyProjetilesOnShield()` | 蓄積した弾をすべて破棄してリストを空にする。 |
| `isArmorEnabled()` | `armorActive`を返すだけ。 |
| `isBlockProjectilesFromBreakingThroughSurfaceEnabled()` | 弾の貫通を防ぐフラグを返すだけ。 |
| `getArmorSurfacePriorityValue()` | 装甲サーフェスの優先度値を返すだけ。 |
| `setNewArmorOwner(GameObject newObject)` | 装甲の持ち主を設定するだけ。 |
| `getArmorOwner()` | 装甲の持ち主を返すだけ。 |
| `setArmorActiveState(bool state)` | 装甲の有効状態を設定し、遅延切り替えコルーチンが動いていれば停止する。 |
| `setTriggerScaleValues(Vector3 newCenterValues, Vector3 newSizeValues)` | `mainCollider`があれば中心とサイズを指定値に変更するだけ。 |
| `setEnableArmorSurfaceStateWithDuration(float delayDuration, bool stateBeforeDelay, bool stateAfterDelay)` | 既存の遅延処理を止め、アクティブなオブジェクトなら指定時間後に状態を変えるコルーチンを開始する。 |
| `stopSetArmorSurfaceStateAfterDelayCoroutine()` | 遅延切り替えコルーチンを停止し、実行中フラグもfalseにするだけ。 |
| `setArmorDamage(float damageAmount)` | 耐久値が有効ならダメージを減算し、0以下なら装甲を無効化して空イベント、それ以外は被弾イベントを発火する。 |
| `addArmorHealth(float healthAmount)` | 耐久値が有効なら加算して最大値でクランプし、残量が正なら装甲を有効化する。 |
| `isUseArmorHealthAmountEnabled()` | 耐久値機能の有効フラグを返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToReturnProjectilesOnContact` | `UnityEvent` | – |
| `eventOnDeflectProjectilesActivated` | `UnityEvent` | – |
| `eventOnArmorHealthEmpty` | `UnityEvent` | – |
| `eventOnArmorHealthDamaged` | `UnityEvent` | – |
