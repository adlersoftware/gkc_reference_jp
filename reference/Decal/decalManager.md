# decalManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Decal/decalManager.cs:6`

**概要**: デカール(弾痕・焦げ跡)システムのシングルトン管理コンポーネント。表面別の`impactInfo`設定やフェード、デカールの親オブジェクトを保持する。

**公式ドキュメント抜粋**（[Decal Manager](../../docs/additional-managers/decal-manager.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fade Decals | `fadeDecals` | `bool` | – | オンにすると着弾デカールをフェードさせて消す。 |
| Fade Speed | `fadeSpeed` | `float` | – | デカールのフェード速度。値が大きいほど早く消える。 |
| Projectile Impact Sound Prefab | `projectileImpactSoundPrefab` | `GameObject` | – | 着弾音用のプレハブ。開始時に静的変数へコピーされる。 |

### Decal System Enabled Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable Full Decall System | `disableFullDecallSystem` | `bool` | – | オンにすると着弾デカール処理全体を停止する。 |
| Decals Placed On Surfaces Enabled | `decalsPlacedOnSurfacesEnabled` | `bool` | true | オンにすると着弾点に焦げ跡デカールを配置する。 |
| Particles Placed On Surface Enabled | `particlesPlacedOnSurfaceEnabled` | `bool` | true | オンにすると着弾点にパーティクルを生成する。 |
| Sounds Placed On Surface Enabled | `soundsPlacedOnSurfaceEnabled` | `bool` | true | オンにすると着弾時に効果音を再生する。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `impactListInfo` | `List<impactInfo>` | new List<impactInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getComponentInstance()` | 初期化済みなら何もせず、別インスタンスがあれば自身を破棄し、それ以外は静的`Instance`に登録する。 |
| `surfaceUseNoise(int surfaceIndex)` | 範囲内の`surfaceIndex`なら該当`impactInfo`の`useNoise`を返し、範囲外はfalseを返す。 |

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static string getMainManagerName()` | – |
| `static void setScorch(Quaternion rotation, GameObject scorch, RaycastHit hit, GameObject collision, bool projectilesPoolEnabled)` | – |
| `static bool placeProjectileInSurface(Quaternion rotation, Transform projectile, RaycastHit hit, GameObject objectToDamage, bool attachToLimbs, bool ignoreSetProjectilePositionOnImpact)` | – |
| `static bool setImpactDecal(int impactIndex, Transform projectile, GameObject objectToDamage, float projectileRayDistance, LayerMask projectilelayer, bool useSorch, bool projectilesPoolEnabled)` | – |
| `static void setImpactSoundParent(Transform newImpactSound)` | – |
| `static void setScorchFromList(Quaternion rotation, GameObject scorch, RaycastHit hit, GameObject collision, float scorchScale, bool fadeScorch, float timeToFade, bool projectilesPoolEnabled)` | – |
| `static int checkIfHasDecalImpact(GameObject objectToCheck)` | – |
| `static void setScorchParent(Transform objectDetected, GameObject newScorch, Vector3 impactPosition)` | – |
| `static int GetMainTexture(Vector3 playerPos, Terrain terrain)` | – |
| `static Transform getDecalParent()` | – |

## 内部型

- `impactInfo`（class）
