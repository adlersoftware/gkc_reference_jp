# matchPlayerToTargetSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/matchPlayerToTargetSystem.cs:7`

**概要**: 周囲のキャラクターから条件を満たす対象を選び、`activateMatchPositionCoroutine` で位置と回転を補間して攻撃位置へ合わせる。`charactersAround` の追加・削除と対象検出・喪失イベントを管理する。

**公式ドキュメント抜粋**（[Match Player To Target System](../../docs/player-controller-components/essential-components/match-player-to-target-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Match System Enabled | `matchSystemEnabled` | `bool` | true | – |
| Match Speed | `matchSpeed` | `float` | 10 | – |
| Position Offset | `positionOffset` | `float` | – | – |
| Ignore Custom Position Offset | `ignoreCustomPositionOffset` | `bool` | – | – |
| Use Distance Percentage As Offset | `useDistancePercentageAsOffset` | `bool` | – | – |
| Position Offset Percentage | `positionOffsetPercentage` | `float` | – | Range (0, 1) |
| Min Distance To Match Position | `minDistanceToMatchPosition` | `float` | – | – |
| Max Distance To Match Position | `maxDistanceToMatchPosition` | `float` | – | – |
| Min Angle To Match Rotation | `minAngleToMatchRotation` | `float` | – | – |
| Max Angle To Match Rotation | `maxAngleToMatchRotation` | `float` | – | – |
| Adjust Rotation Even If Not Moved | `adjustRotationEvenIfNotMoved` | `bool` | – | – |
| Min Distance To Match Rotation | `minDistanceToMatchRotation` | `float` | – | – |
| Max Distance To Match Rotation | `maxDistanceToMatchRotation` | `float` | – | – |
| Use Max Distance To Camera Center | `useMaxDistanceToCameraCenter` | `bool` | – | – |
| Max Distance To Camera Center | `maxDistanceToCameraCenter` | `float` | – | – |
| Use Move Input As Direction To Closest Target | `useMoveInputAsDirectionToClosestTarget` | `bool` | – | – |

### Vertical Distance Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Adjust Vertical Position Enabled | `adjustVerticalPositionEnabled` | `bool` | – | – |
| Raycast Distance For Vertical Position | `raycastDistanceForVerticalPosition` | `float` | – | – |
| Layer Mask For Vertical Position | `layerMaskForVerticalPosition` | `LayerMask` | – | – |
| Check Max Vertical Distance With Target | `checkMaxVerticalDistanceWithTarget` | `bool` | – | – |
| Max Vertical Distance With Target | `maxVerticalDistanceWithTarget` | `float` | – | – |
| Use Local Vertical Distance | `useLocalVerticalDistance` | `bool` | – | – |
| Check If Obstacles To Target | `checkIfObstaclesToTarget` | `bool` | – | – |
| Layer To Check Target | `layerToCheckTarget` | `LayerMask` | – | – |

### Front Position Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Front Position As Position To Match | `useFrontPositionAsPositionToMatch` | `bool` | – | – |
| Front Position As Position To Match Offset | `frontPositionAsPositionToMatchOffset` | `Vector3` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Main Player On List For AI | `addMainPlayerOnListForAI` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Movement Active | `movementActive` | `bool` | – | – |
| Match Position Paused | `matchPositionPaused` | `bool` | – | – |
| Get Closest Target Without Conditions Active | `getClosestTargetWithoutConditionsActive` | `bool` | – | – |
| Characters Around | `charactersAround` | `List<Transform>` | new List<Transform> () | – |

### Events

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Targets Change | `useEventsOnTargetsChange` | `bool` | – | – |
| Event On Targets Detected | `eventOnTargetsDetected` | `UnityEvent` | – | – |
| Event On Targets Removed | `eventOnTargetsRemoved` | `UnityEvent` | – | – |
| Use Event On First Target Detected | `useEventOnFirstTargetDetected` | `bool` | – | – |
| Event On First Target Detected | `eventOnFirstTargetDetected` | `UnityEvent` | – | – |
| Use Event On Last Target Removed | `useEventOnLastTargetRemoved` | `bool` | – | – |
| Event On Last Target Removed | `eventOnLastTargetRemoved` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Debug Target To Match Transform | `debugTargetToMatchTransform` | `Transform` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `findPlayerOnScene()` | シーン上のメインプレイヤーを取得し、`addCharacterAround` に渡す。 |
| `addCharacterAround(Transform newCharacter)` | 未登録ならリストへ追加し、最初の対象なら検出イベントを発火する。 |
| `removeCharacterAround(Transform newCharacter)` | リストから外し、空になったら対象喪失イベントを発火する。 |
| `clearAllCharactersAround()` | リストを空にし、対象解除イベントと最後の対象喪失イベントを発火する。 |
| `setMatchPositionPausedState(bool state)` | `matchPositionPaused` を設定するだけ。 |
| `setMatchSystemEnabledstate(bool state)` | `matchSystemEnabled` を設定するだけ。 |
| `setAddMainPlayerOnListForAIState(bool state)` | `addMainPlayerOnListForAI` を設定するだけ。 |
| `activateMatchPosition(float customOffset)` | 有効/停止状態を確認し、デバッグ対象か現在の対象を選んで位置合わせを開始する。 |
| `activateMatchPosition(Transform targetToUse, float customOffset)` | 既存の移動を止め、対象とオフセットで位置合わせコルーチンを開始する。 |
| `stopMovementIfActive()` | `movementActive` のときだけ `stopMovement` を呼ぶ。 |
| `stopMovement()` | 移動コルーチンを停止し、`movementActive` を false にする。 |
| `setUseFrontPositionAsPositionToMatchState(bool state)` | `useFrontPositionAsPositionToMatch` を設定するだけ。 |
| `getCurrentTargetToMatchPosition()` | 生存対象から画面距離・角度・上下差・障害物を条件に最適な `Transform` を返す。 |
| `setGetClosestTargetWithoutConditionsActiveState(bool state)` | `getClosestTargetWithoutConditionsActive` を設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnTargetsDetected` | `UnityEvent` | – |
| `eventOnTargetsRemoved` | `UnityEvent` | – |
| `eventOnFirstTargetDetected` | `UnityEvent` | – |
| `eventOnLastTargetRemoved` | `UnityEvent` | – |
