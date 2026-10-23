# GKC_PlayerPrefabSpawner

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Online System/GKC_PlayerPrefabSpawner.cs:6`

**概要**: オンライン時にプレイヤープレハブの生成位置とメインプレイヤー状態を初期化するコンポーネント。非メインプレイヤーではカメラ・入力・HUDを無効化する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Player Prefab Spawn On Start Enabled | `checkPlayerPrefabSpawnOnStartEnabled` | `bool` | – | – |
| Is Main Player | `isMainPlayer` | `bool` | – | – |
| Spawn Position | `spawnPosition` | `Vector3` | – | – |
| Spawn Rotation | `spawnRotation` | `Vector3` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Player Spawn | `useEventsOnPlayerSpawn` | `bool` | – | – |
| Event On Main Player | `eventOnMainPlayer` | `UnityEvent` | – | – |
| Event On Pawn Character | `eventOnPawnCharacter` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Save Game System | `mainSaveGameSystem` | `saveGameSystem` | – | – |
| Pause Manager | `pauseManager` | `menuPause` | – | – |
| Main Map System | `mainMapSystem` | `mapSystem` | – | – |
| Main Player Input Manager | `mainPlayerInputManager` | `playerInputManager` | – | – |

### Main Managers

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Characters Manager | `mainPlayerCharactersManager` | `playerCharactersManager` | – | – |
| Main Input Manager | `mainInputManager` | `inputManager` | – | – |
| Main Game Manager | `mainGameManager` | `gameManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPositionToSpawn(Vector3 newValue)` | `spawnPosition`を`newValue`に設定するだけ。 |
| `setRotationToSpawn(Vector3 newValue)` | `spawnRotation`を`newValue`に設定するだけ。 |
| `checkPlayerPrefabSpawnOnAwake()` | 起動時に各マネージャを取得し、プレイヤー数からメイン判定してカメラ・入力・HUD・マップ・イベントを初期化する。 |
| `checkPlayerPrefabSpawn()` | プレイヤーを`spawnPosition`と`spawnRotation`へ移動し、メインプレイヤーなら入力マネージャを初期化する。 |
| `setIsMainPlayerState(bool state)` | `isMainPlayer`を`state`に設定するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnMainPlayer` | `UnityEvent` | – |
| `eventOnPawnCharacter` | `UnityEvent` | – |
