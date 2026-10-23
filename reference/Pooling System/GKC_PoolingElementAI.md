# GKC_PoolingElementAI

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `GKC_PoolingElement`
- **ソース**: `Pooling System/GKC_PoolingElementAI.cs:5`

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Random Player Mode On Spawn Enabled | `setRandomPlayerModeOnSpawnEnabled` | `bool` | – | – |
| Set Main Player As Target On Spawn Enabled | `setMainPlayerAsTargetOnSpawnEnabled` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Health | `mainHealth` | `health` | – | – |
| Main Ragdoll Activator | `mainRagdollActivator` | `ragdollActivator` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Main AI Nav Mesh | `mainAINavMesh` | `AINavMesh` | – | – |
| Main Gravity System | `mainGravitySystem` | `gravitySystem` | – | – |
| Main Player States Manager | `mainPlayerStatesManager` | `playerStatesManager` | – | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`checkObjectStateAfterSpawn()`, `checkObjectStateBeforeDespawn()`

</details>
