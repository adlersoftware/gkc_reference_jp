# grapplingHookTargetsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/Custom Abilities/Grappling Hook System/grapplingHookTargetsSystem.cs:6`

**概要**: プレイヤーが狙えるグラップリング対象を管理し、対象アイコンの生成・表示・削除を行う。`grapplingHookSystem` とテレポートシステムへ対象を引き渡す。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Grappling Hook Targets Active | `showGrapplingHookTargetsActive` | `bool` | true | – |
| Layer For Third Person | `layerForThirdPerson` | `LayerMask` | – | – |
| Layer For First Person | `layerForFirstPerson` | `LayerMask` | – | – |
| Check Obstacles To Grappling Hook Targets | `checkObstaclesToGrapplingHookTargets` | `bool` | – | – |
| Grappling Hook System List | `grapplingHookSystemList` | `List<grapplingHookSystem>` | new List<grapplingHookSystem> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Grappling Hook Targets Paused | `showGrapplingHookTargetsPaused` | `bool` | – | – |
| Closest Target | `closestTarget` | `Transform` | – | – |
| Grappling Hook Target Info List | `grapplingHookTargetInfoList` | `List<grapplingHookTargetInfo>` | new List<grapplingHookTargetInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Grappling Hook Target Icon Prefab | `grapplingHookTargetIconPrefab` | `GameObject` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Game Object | `playerGameObject` | `GameObject` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Grappling Hook Target Icons Parent | `grapplingHookTargetIconsParent` | `Transform` | – | – |
| Main Player Teleport System | `mainPlayerTeleportSystem` | `playerTeleportSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentGrapplingHookTargetState(bool state)` | 現在の対象アイコンの表示を `state` に合わせて切り替え、`iconCurrentlyEnabled` を更新する。 |
| `disableGrapplingHookTargets()` | `enableOrDisableGrapplingHookTargets(false)` を呼ぶだけ。 |
| `enableGrapplingHookTargets()` | `enableOrDisableGrapplingHookTargets(true)` を呼ぶだけ。 |
| `enableOrDisableGrapplingHookTargets(bool state)` | 全対象のアイコン表示を `state` に合わせて切り替え、`iconCurrentlyEnabled` を更新する。 |
| `addNewGrapplingHookTarget(Transform targetTransform)` | アイコンのプレハブを生成して対象情報をリストに追加し、`hookTargetsDetected` を立てる。 |
| `removeNewGrapplingHookTarget(Transform targetTransform)` | 一致する対象のアイコンを破棄してリストから外し、空ならフックとテレポートの対象を解除する。 |
| `pauseOrResumeShowGrapplingHookTargets(bool state)` | `showGrapplingHookTargetsPaused` を設定し、アイコン親の表示を反転させる。 |

## 内部型

- `grapplingHookTargetInfo`（class）
