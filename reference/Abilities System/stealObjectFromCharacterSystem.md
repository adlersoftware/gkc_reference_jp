# stealObjectFromCharacterSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/stealObjectFromCharacterSystem.cs:6`

**概要**: 注視中または周囲のキャラクターから武器を盗む能力。確率・距離・クールダウンで成否を判定する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Steal Enabled | `stealEnabled` | `bool` | true | – |
| Probability To Steal Weapon | `probabilityToStealWeapon` | `float` | 0 | Range (0, 100) |
| Steal Weapon Only If Not Pickups Located | `stealWeaponOnlyIfNotPickupsLocated` | `bool` | – | – |
| Use Max Distance To Steal Weapon | `useMaxDistanceToStealWeapon` | `bool` | – | – |
| Max Distance To Get Steal Weapon | `maxDistanceToGetStealWeapon` | `float` | – | – |
| Use Max Distance To Camera Center | `useMaxDistanceToCameraCenter` | `bool` | – | – |
| Max Distance To Camera Center | `maxDistanceToCameraCenter` | `float` | – | – |
| Min Wait Time To Activate Steal | `minWaitTimeToActivateSteal` | `float` | 2 | – |

### Weapon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Steal Current Weapon | `stealCurrentWeapon` | `bool` | true | – |
| Ignore Draw On Steal Weapon | `ignoreDrawOnStealWeapon` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Steal | `useEventOnSteal` | `bool` | – | – |
| Event On Steal Weapon | `eventOnStealWeapon` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main AI Around Manager | `mainAIAroundManager` | `AIAroundManager` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Inventory Manager | `mainInventoryManager` | `inventoryManager` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateStealFromCharacter()` | 有効かつクールダウン外なら、確率判定を経て対象の武器を盗み、成功時に時刻を記録する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStealWeapon` | `UnityEvent` | – |
