# enableOrDisableAIOnDistanceManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/enableOrDisableAIOnDistanceManager.cs:5`

**概要**: 距離管理からAIキャラクターの有効/無効を切り替え、メッシュ・Animator・カメラも連動させる。

## インスペクター設定

### Behavior Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enable Or Disable AI On Distance Enabled | `enableOrDisableAIOnDistanceEnabled` | `bool` | true | – |
| Set Active State On Player Camera Game Object | `setActiveStateOnPlayerCameraGameObject` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| AI Enable Active | `AIEnableActive` | `bool` | true | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main AI Navmesh | `mainAINavmesh` | `AINavMesh` | – | – |
| Player Camera Game Object | `playerCameraGameObject` | `GameObject` | – | – |
| Main Player States Manager | `mainPlayerStatesManager` | `playerStatesManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisbleAI(bool state)` | 設定有効かつ状態変化時のみ、`AINavMesh`の停止、メッシュ・重心・Animator・カメラの状態を`state`に合わせる。 |
| `setEnableOrDisableAIOnDistanceEnabledState(bool state)` | `enableOrDisableAIOnDistanceEnabled`に`state`を代入するだけ。 |
