# sharedActionZone

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/Shared Action System/sharedActionZone.cs:5`

**概要**: 特定位置で共有アクションを再生するためのゾーン。対象アクション名、アクション用オブジェクト、距離や角度の条件、初期位置などを保持する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shared Action Zone Enabled | `sharedActionZoneEnabled` | `bool` | true | – |
| Shared Action Name | `sharedActionName` | `string` | – | – |
| Disable Shared Action Zone After Use | `disableSharedActionZoneAfterUse` | `bool` | – | – |
| Set Player As First Character | `setPlayerAsFirstCharacter` | `bool` | – | – |
| Set AI As First Character If Signal Owner | `setAIAsFirstCharacterIfSignalOwner` | `bool` | – | – |
| Use Shared Action Content | `useSharedActionContent` | `bool` | true | – |
| Main Shared Action Content | `mainSharedActionContent` | `sharedActionContent` | – | – |
| Shared Action Content Prefab | `sharedActionContentPrefab` | `GameObject` | – | – |

### Range Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Shared Zone Inside Range | `useSharedZoneInsideRange` | `bool` | – | – |
| Use Zone Position Range | `useZonePositionRange` | `bool` | – | – |
| X Range | `xRange` | `Vector2` | – | – |
| Z Range | `zRange` | `Vector2` | – | – |
| Use Zone Rotation Range | `useZoneRotationRange` | `bool` | – | – |
| Rotation Range | `rotationRange` | `float` | – | – |
| Use Custom Shared Zone Rotation Center | `useCustomSharedZoneRotationCenter` | `bool` | – | – |
| Custom Shared Zone Transform | `customSharedZoneTransform` | `Transform` | – | – |

### Condition Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Max Distance To Use Shared Action Zone | `maxDistanceToUseSharedActionZone` | `float` | – | – |
| Use Max Distance XZ To Use Shared Action Zone | `useMaxDistanceXZToUseSharedActionZone` | `bool` | – | – |
| Max Distance X To Use Shared Action Zone | `maxDistanceXToUseSharedActionZone` | `float` | – | – |
| Max Distance Z To Use Shared Action Zone | `maxDistanceZToUseSharedActionZone` | `float` | – | – |
| Use Min Distance To Activate Action First Character | `useMinDistanceToActivateActionFirstCharacter` | `bool` | – | – |
| Min Distance To Activate Action First Character | `minDistanceToActivateActionFirstCharacter` | `float` | – | – |
| Use Min Angle To Activate Action First Character | `useMinAngleToActivateActionFirstCharacter` | `bool` | – | – |
| Min Angle To Activate Action First Character | `minAngleToActivateActionFirstCharacter` | `float` | – | – |
| Use Min Distance To Activate Action Second Character | `useMinDistanceToActivateActionSecondCharacter` | `bool` | – | – |
| Min Distance To Activate Action Second Character | `minDistanceToActivateActionSecondCharacter` | `float` | – | – |
| Use Min Angle To Activate Action Second Character | `useMinAngleToActivateActionSecondCharacter` | `bool` | – | – |
| Min Angle To Activate Action Second Character | `minAngleToActivateActionSecondCharacter` | `float` | – | – |
| Use Min Angle To Activate Action On Characters Direction | `useMinAngleToActivateActionOnCharactersDirection` | `bool` | – | – |
| Min Angle To Activate Action On Characters Direction | `minAngleToActivateActionOnCharactersDirection` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Shared Action Content Found | `mainSharedActionContentFound` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `storeInitialPosition()` | 必要ならアクション用オブジェクトを生成し、未保存の初期位置と初期角度を記録する。 |
| `getInitialPosition()` | `initialPosition`を返すだけ。 |
| `getInitialEuler()` | `initialEuler`を返すだけ。 |
| `setSharedActionZoneEnabledState(bool state)` | `sharedActionZoneEnabled`に`state`を設定するだけ。 |
| `isSharedActionZoneEnabled()` | `sharedActionZoneEnabled`の値を返すだけ。 |
| `setDisableSharedActionZoneAfterUseState(bool state)` | `disableSharedActionZoneAfterUse`に`state`を設定するだけ。 |
| `getSharedActionName()` | `sharedActionName`を返すだけ。 |
| `isUseSharedActionContentActive()` | `useSharedActionContent`の値を返すだけ。 |
| `getSharedActionContent()` | `mainSharedActionContent`を返すだけ。 |
| `getSetPlayerAsFirstCharacter()` | `setPlayerAsFirstCharacter`の値を返すだけ。 |
| `getSetAIAsFirstCharacterIfSignalOwner()` | `setAIAsFirstCharacterIfSignalOwner`の値を返すだけ。 |
| `getMaxDistanceToUseSharedActionZone()` | `maxDistanceToUseSharedActionZone`を返すだけ。 |
| `spawnSharedActionObjectOnSceneFromEditor()` | プレハブからアクション用オブジェクトを生成して選択状態にし、シーンを更新する。 |
| `getSharedActionManagerrOnScene()` | シーン上の`sharedActionZoneManager`を検索し、無ければ新規GameObjectに追加して選択する。 |
