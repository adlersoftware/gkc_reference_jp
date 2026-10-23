# surfaceToSlice

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/New Weapon Behaviors/surfaceToSlice.cs:6`

**概要**: 切断可能なサーフェスとして、切断可否・回転数制限・断面マテリアル・切断方向の判定・遅延破棄などを保持し、切断イベントを発火するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cut Surface Enabled | `cutSurfaceEnabled` | `bool` | true | – |
| Use Custom Force Amount | `useCustomForceAmount` | `bool` | – | – |
| Custom Force Amount | `customForceAmount` | `float` | – | – |
| Use Custom Force Mode | `useCustomForceMode` | `bool` | – | – |
| Custom Force Mode | `customForceMode` | `ForceMode` | – | – |
| Use Box Collider | `useBoxCollider` | `bool` | – | – |
| Ignore Regular Damage If Cut Surface Not Enabled | `ignoreRegularDamageIfCutSurfaceNotEnabled` | `bool` | – | – |
| Main Surface To Slice | `mainSurfaceToSlice` | `GameObject` | – | – |

### Material Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cross Section Material | `crossSectionMaterial` | `Material` | – | – |

### Tag and Layer Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Tag On Cut | `setNewTagOnCut` | `bool` | – | – |
| New Tag On Cut | `newTagOnCut` | `string` | – | – |
| Set New Layer On Cut | `setNewLayerOnCut` | `bool` | – | – |
| New Layer On Cut | `newLayerOnCut` | `string` | – | – |

### Particle Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Particles On Slice | `useParticlesOnSlice` | `bool` | – | – |
| Particles On Slice Prefab | `particlesOnSlicePrefab` | `GameObject` | – | – |

### Slice Limit Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Cut Multiple Times Active | `cutMultipleTimesActive` | `bool` | true | – |
| Use Limited Number Of Cuts | `useLimitedNumberOfCuts` | `bool` | – | – |
| Limited Number Of Cuts | `limitedNumberOfCuts` | `int` | – | – |

### Slice Direction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check For Custom Slice Direction | `checkForCustomSliceDirection` | `bool` | – | – |
| Max Slice Direction Angle | `maxSliceDirectionAngle` | `float` | – | – |
| Custom Slice Direction Up | `customSliceDirectionUp` | `Transform` | – | – |
| Allow Reverse Slice Direction | `allowReverseSliceDirection` | `bool` | – | – |

### Character Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Is Character | `objectIsCharacter` | `bool` | – | – |
| Ignore Damage If Slice Not Activated | `ignoreDamageIfSliceNotActivated` | `bool` | – | – |
| Main Simple Slice System | `mainSimpleSliceSystem` | `simpleSliceSystem` | – | – |

### Bullet Time Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Time Bullet On Slice Enabled | `useTimeBulletOnSliceEnabled` | `bool` | – | – |
| Time Bullet Duration | `timeBulletDuration` | `float` | 3 | – |
| Time Scale | `timeScale` | `float` | 0.2f | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Destroy Sliced Parts After Delay | `destroySlicedPartsAfterDelay` | `bool` | – | – |
| Delay To Destroy Sliced Parts | `delayToDestroySlicedParts` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Main Simple Slice System Assigned | `mainSimpleSliceSystemAssigned` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Cut | `useEventOnCut` | `bool` | – | – |
| Event On Cut | `eventOnCut` | `UnityEvent` | – | – |
| Copy Event On Sliced Objects | `copyEventOnSlicedObjects` | `bool` | – | – |
| Use Event Before Cut | `useEventBeforeCut` | `bool` | – | – |
| Event Before Cut | `eventBeforeCut` | `UnityEvent` | – | – |
| Ignore Destroy Original Object | `ignoreDestroyOriginalObject` | `bool` | – | – |
| Events On Ignore Destroy Original Object | `eventsOnIgnoreDestroyOriginalObject` | `UnityEvent` | – | – |
| Use Event To Send New Sliced Parts | `useEventToSendNewSlicedParts` | `bool` | – | – |
| Event To Send New Sliced Parts | `eventToSendNewSlicedParts` | `eventParameters.eventToCallWithGameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkEventsOnIgnoreDestroyOriginalObject()` | `ignoreDestroyOriginalObject`が有効なら元オブジェクトを破棄しない場合のイベントを発火する。 |
| `checkEventBeforeSlice()` | `useEventBeforeCut`が有効なら切断前イベントを発火するだけ。 |
| `checkEventOnCut()` | `useEventOnCut`が有効なら切断時イベントを発火するだけ。 |
| `copySurfaceInfo(surfaceToSlice surfaceToCopy)` | 切断時刻を更新し、断面マテリアル・タグ・レイヤー・回転数・力・破棄設定・イベントを複製先へ引き継ぐ。 |
| `isObjectCharacter()` | `objectIsCharacter`を返すだけ。 |
| `isIgnoreDamageIfSliceNotActivatedActive()` | `ignoreDamageIfSliceNotActivated`を返すだけ。 |
| `isCutSurfaceEnabled()` | `cutSurfaceEnabled`を返すだけ。 |
| `setCutSurfaceEnabledState(bool state)` | 切断可能フラグを設定し、デバッグ時のみログを出すだけ。 |
| `setIgnoreRegularDamageIfCutSurfaceNotEnabledState(bool state)` | 切断無効時に通常ダメージを無視するフラグを設定するだけ。 |
| `isIgnoreRegularDamageIfCutSurfaceNotEnabled()` | 切断無効時に通常ダメージを無視するフラグを返すだけ。 |
| `getLastTimeSliced()` | 最後に切断された時刻を返すだけ。 |
| `sliceCanBeActivated(float minDelayToSliceSameObject)` | 残り切断回数が0でなく、前回切断から`minDelayToSliceSameObject`以上経過していればtrueを返す。 |
| `checkSliceDirectionResult(Vector3 sliceDirectionRight, Vector3 sliceDirectionUp)` | カスタム方向判定が有効なら、指定した右・上方向と`customSliceDirectionUp`の角度差が許容範囲内かを判定する。 |
| `getMainSimpleSliceSystem()` | `mainSimpleSliceSystem`を返すだけ。 |
| `setMainSimpleSliceSystem(GameObject newObject)` | 指定オブジェクトから`simpleSliceSystem`を取得して設定するだけ。 |
| `setMainSimpleSliceSystemCheckingNotNull(GameObject newObject)` | `simpleSliceSystem`を設定し、取得できたかどうかで`cutSurfaceEnabled`を更新する。 |
| `setDestructionPending(bool state)` | `simpleSliceSystem`が確保できていれば破棄待ちフラグを設定する。 |
| `setUseTimeBulletValue(bool state)` | 切断時にバレットタイムを使うかどうかのフラグを設定するだけ。 |
| `checkTimeBulletOnCut()` | バレットタイム設定が有効なら指定時間とタイムスケールで発動させる。 |
| `getCrossSectionMaterial()` | 断面マテリアルを返すだけ。 |
| `setCrossSectionMaterial(Material newMaterial)` | 断面マテリアルを設定するだけ。 |
| `checkDestroySlicedPartsAfterDelay()` | 遅延破棄が有効でキャラでなければ、`destroyGameObject`を付与して`delayToDestroySlicedParts`のタイマーを開始する。 |
| `setMainSurfaceToSlice(GameObject newObject)` | 切断対象サーフェスのGameObjectを設定するだけ。 |
| `getMainSurfaceToSlice()` | `mainSurfaceToSlice`を返し、未設定なら自身のGameObjectを設定して返す。 |
| `setCutSurfaceEnabledStateFromEditor(bool state)` | 切断可能状態を設定したうえでコンポーネントとシーンを更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCut` | `UnityEvent` | – |
| `eventBeforeCut` | `UnityEvent` | – |
| `eventsOnIgnoreDestroyOriginalObject` | `UnityEvent` | – |
