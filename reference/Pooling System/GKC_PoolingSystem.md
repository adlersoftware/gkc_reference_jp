# GKC_PoolingSystem

- **種別**: class
- **ソース**: `Pooling System/GKC_PoolingSystem.cs:4`

## 静的メソッド

| シグネチャ | 説明 |
| --- | --- |
| `static void Preload(GameObject prefab, int qty = 1)` | If you want to preload a few copies of an object at the start of a scene, you can use this. Really not needed unless you're going to go from zero instances to 100+ very quickly. Could technically be optimized more, but in practice the Spawn/Despawn sequence is going to be pretty darn quick and this avoids code duplication. |
| `static GameObject Spawn(GameObject prefab, Vector3 pos, Quaternion rot)` | Spawns a copy of the specified prefab (instantiating one if required). NOTE: Remember that Awake() or Start() will only run on the very first spawn and that member variables won't get reset.  OnEnable will run after spawning -- but remember that toggling IsActive will also call that function. |
| `static GameObject Spawn(GameObject prefab, Vector3 pos, Quaternion rot, int qty)` | – |
| `static void Despawn(GameObject obj)` | Despawn the specified gameobject back into its pool. |

## 内部型

- `Pool`（class）
- `PoolMember`（class）
