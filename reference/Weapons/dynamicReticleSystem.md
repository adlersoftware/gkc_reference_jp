# dynamicReticleSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/dynamicReticleSystem.cs:6`

**概要**: 移動・走り・視点回転・射撃・空中などに応じて照準の大きさを変え、武器の拡散値へ反映するシステム。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dynamic Reticle Enbled | `dynamicReticleEnbled` | `bool` | true | – |
| Use Delay To Reset Reticle Size | `useDelayToResetReticleSize` | `bool` | – | – |
| Delay To Reset Reticle Size | `delayToResetReticleSize` | `float` | – | – |

### Reticle List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Dynamic Reticle Info List | `dynamicReticleInfoList` | `List<dynamicReticleInfo>` | new List<dynamicReticleInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Reticle Active | `reticleActive` | `bool` | – | – |
| Current Reticle Size Delta | `currentReticleSizeDelta` | `Vector2` | – | – |
| Current Reticle Name | `currentReticleName` | `string` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止するだけ。 |
| `enableOrDisableReticleByName(string reticleName, bool state)` | 名前で照準情報を引き、表示と拡散値を切り替え、有効にした場合は更新コルーチンを回す。 |
| `isReticleActive()` | `reticleActive`を返すだけ。 |

## 内部型

- `dynamicReticleInfo`（class）
