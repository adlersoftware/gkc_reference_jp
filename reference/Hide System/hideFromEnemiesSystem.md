# hideFromEnemiesSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Hide System/hideFromEnemiesSystem.cs:5`

**概要**: フリー隠れゾーンのトリガー内にいるキャラクターを管理し、AI可視状態・状態アイコン・敵のターゲットを切り替えるコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Layer To Characters | `layerToCharacters` | `LayerMask` | – | – |
| Time Delay To Hiden Again If Discovered | `timeDelayToHidenAgainIfDiscovered` | `float` | – | – |
| Check If Character Can Be Hidden Again Rate | `checkIfCharacterCanBeHiddenAgainRate` | `float` | 0.5f | – |
| Lose Track Of Player By AI On Trigger Enter Enabled | `loseTrackOfPlayerByAIOnTriggerEnterEnabled` | `bool` | – | – |
| Reactivate Player Collider On Exit Trigger | `reactivatePlayerColliderOnExitTrigger` | `bool` | – | – |

### Hide Conditions Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Need To Crouch | `characterNeedToCrouch` | `bool` | – | – |
| Max Move Amount | `maxMoveAmount` | `float` | – | – |
| Character Cant Move | `characterCantMove` | `bool` | – | – |
| Hidden For A Time | `hiddenForATime` | `bool` | – | – |
| Hidden For A Time Amount | `hiddenForATimeAmount` | `float` | – | – |

### Character State Icon Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Character State Icon | `useCharacterStateIcon` | `bool` | – | – |
| Visible Character State Name | `visibleCharacterStateName` | `string` | – | – |
| Not Visible Character State Name | `notVisibleCharacterStateName` | `string` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hidden Character Info List | `hiddenCharacterInfoList` | `List<hiddenCharacterInfo>` | new List<hiddenCharacterInfo> () | – |
| Characters On Hidden List | `charactersOnHiddenList` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCharacterState(string stateName, int characterIndex)` | 状態アイコンを使う設定の時のみ、指定インデックスのキャラクターのアイコン名を設定する。 |
| `addCharacterFromHiddenZone(GameObject newCharacter)` | `newCharacter`がnullでなければ、隠れゾーンへ追加する。 |
| `removeCharacterFromHiddenZone(GameObject newCharacter)` | `newCharacter`がnullでなければ、隠れゾーンから除外する。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | コライダーがnullでなければ、そのオブジェクトを進入/退出として隠れゾーンの処理に渡す。 |
| `isCharacterHiddenOnZone(GameObject characterToCheck)` | 隠れ中リストに対象キャラクターがいるかどうかを返す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnTriggerEnter(Collider col)`, `OnTriggerExit(Collider col)`

</details>

## 内部型

- `hiddenCharacterInfo`（class）
