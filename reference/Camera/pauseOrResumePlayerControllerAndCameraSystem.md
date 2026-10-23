# pauseOrResumePlayerControllerAndCameraSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Cutscene/pauseOrResumePlayerControllerAndCameraSystem.cs:6`

**概要**: カットシーンなどでプレイヤーの入力・移動・カメラ・HUDをまとめて停止/再開するシステム。カメラの親変更、タイムスケール、遅延再開も扱う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Search Player On Scene If Not Assigned | `searchPlayerOnSceneIfNotAssigned` | `bool` | true | – |
| Assign Player Manually | `assignPlayerManually` | `bool` | – | – |
| Current Player | `currentPlayer` | `GameObject` | – | – |
| Player Camera Game Object | `playerCameraGameObject` | `GameObject` | – | – |
| Unlock Cursor | `unlockCursor` | `bool` | – | – |
| Enable Gamepad Cursor | `enableGamepadCursor` | `bool` | – | – |
| Resume Player After Delay | `resumePlayerAfterDelay` | `bool` | – | – |
| Delay To Resume Player | `delayToResumePlayer` | `float` | – | – |
| Activate Player Mesh Model | `activatePlayerMeshModel` | `bool` | true | – |
| Pause Escape Menu | `pauseEscapeMenu` | `bool` | – | – |

### Time Scale Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Custom Time Scale | `setCustomTimeScale` | `bool` | – | – |
| Custom Time Scale | `customTimeScale` | `float` | – | – |
| Pause AI When Open Menu | `pauseAIWhenOpenMenu` | `bool` | – | – |
| Pause Character Priority | `pauseCharacterPriority` | `int` | 1 | – |
| Ignore Change Fixed Delta Time | `ignoreChangeFixedDeltaTime` | `bool` | – | – |

### Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Is Moved | `cameraIsMoved` | `bool` | – | – |
| Reset Camera Position Speed | `resetCameraPositionSpeed` | `float` | – | – |
| Set Camera Direction At End | `setCameraDirectionAtEnd` | `bool` | – | – |
| Camera Direction | `cameraDirection` | `Transform` | – | – |
| Pivot Direction | `pivotDirection` | `Transform` | – | – |
| Set New Camera Parent | `setNewCameraParent` | `bool` | – | – |
| New Camera Parent | `newCameraParent` | `Transform` | – | – |

### HUD Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Disable Secondary Player HUD | `disableSecondaryPlayerHUD` | `bool` | – | – |
| Disable All Player HUD | `disableAllPlayerHUD` | `bool` | true | – |
| Disable Touch Controls | `disableTouchControls` | `bool` | true | – |
| Disable Dynami UI Elements | `disableDynamiUIElements` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Components Paused | `playerComponentsPaused` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Pause | `useEventOnPause` | `bool` | – | – |
| Event On Pause | `eventOnPause` | `UnityEvent` | – | – |
| Event To Send Camera | `eventToSendCamera` | `eventParameters.eventToCallWithGameObject` | – | – |
| Use Event On Resume | `useEventOnResume` | `bool` | – | – |
| Event On Resume | `eventOnResume` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getCurrentPlayer(GameObject player)` | 停止中は何もせず、`playerComponentsManager` からコントローラ・カメラ・ヘッドボブ等の各マネージャを取得する。 |
| `pauseOrPlayPlayerComponents(bool state)` | 入力・頭部追従・ヘッドボブ・カメラを停止し、HUDやカーソル、イベント、カメラの親、タイムスケール、AIもまとめて切り替える。 |
| `setTimeScale(float newValue)` | `Time.timeScale` を設定し、`ignoreChangeFixedDeltaTime` が無効なら0以外のとき `fixedDeltaTime` も更新する。 |
| `checkCharacterMesh(bool state)` | `activatePlayerMeshModel` 有効かつ一人称のときキャラクターメッシュを切り替え、デバイス使用中なら重力中心も切り替える。 |
| `resetCameraPositionIfCharacterPaused()` | プレイヤー停止中のみ `resetCameraPosition` を呼ぶ。 |
| `resetCameraPositionIfCharacterPausedWithoutTransition()` | 停止中でカメラ移動済みなら、向きを反映してカメラを元の親・位置へ即時戻し再開する。 |
| `resetCameraPosition()` | カメラ移動済みなら、既存のリセット処理を止めてリセット用コルーチンを開始する。 |
| `setCameraDirection()` | `setCameraDirectionAtEnd` 有効時、カメラとピボットを指定 Transform の向きに合わせ `lookAngleValue` を更新する。 |
| `resumePlayerAfterTimeDelay()` | 既存の再開予約を止め、`delayToResumePlayer` 後に再開するコルーチンを開始する。 |
| `stopResumePlayerAfterTimeDelay()` | 再開用コルーチンを停止するだけ。 |
| `findPlayerOnScene()` | `searchPlayerOnSceneIfNotAssigned` が有効なとき、シーンのメインプレイヤーを取得して割り当てる。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPause` | `UnityEvent` | – |
| `eventOnResume` | `UnityEvent` | – |
