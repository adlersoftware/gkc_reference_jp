# camera2_5dZoneLimitSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Player Camera/camera2_5dZoneLimitSystem.cs:5`

**概要**: 2.5D ゾーンのカメラ移動範囲（幅・高さ・奥行き）をプレイヤーカメラに適用するコンポーネント。プレイヤーでなければ搭乗中の車両のドライバーからカメラを探す。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Camera Limit | `useCameraLimit` | `bool` | true | – |
| Set Camera Forward Position | `setCameraForwardPosition` | `bool` | – | – |
| Camera Forward Position | `cameraForwardPosition` | `float` | – | – |
| Use Move In X Axis On2 5d | `useMoveInXAxisOn2_5d` | `bool` | – | – |

### Limit Width Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Width Limit | `useWidthLimit` | `bool` | true | – |
| Width Limit Right | `widthLimitRight` | `float` | – | – |
| Width Limit Left | `widthLimitLeft` | `float` | – | – |

### Limit Height Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Height Limit | `useHeightLimit` | `bool` | true | – |
| Height Limit Upper | `heightLimitUpper` | `float` | – | – |
| Height Limit Lower | `heightLimitLower` | `float` | – | – |

### Limit Depth Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Depth Limit | `useDepthLimit` | `bool` | – | – |
| Depth Limit Front | `depthLimitFront` | `float` | – | – |
| Depth Limit Backward | `depthLimitBackward` | `float` | – | – |

### Set Limit At Start Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Game With This Limit | `startGameWithThisLimit` | `bool` | – | – |
| Player For View | `playerForView` | `GameObject` | – | – |
| Use Multiple Players | `useMultiplePlayers` | `bool` | – | – |
| Player For View List | `playerForViewList` | `List<GameObject>` | new List<GameObject> () | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.white | – |
| Gizmo Radius | `gizmoRadius` | `float` | 0.2f | – |
| Depth Gizmo Color | `depthGizmoColor` | `Color` | Color.white | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCameraLimitOnPlayer()` | `currentPlayer` がいれば `playerCamera.setCameraLimit` に範囲値を渡し、必要ならカメラ前方位置も設定する。 |
| `setCameraLimitOnPlayer(GameObject newPlayer)` | プレイヤーを設定してから、保存済みの範囲設定をカメラに適用する。 |
| `setCurrentPlayer(GameObject newPlayer)` | null なら警告。`playerComponentsManager` から各マネージャを取得し、プレイヤーでなければ車両ドライバーに切り替える。 |
| `setConfigurationToPlayer()` | `setCameraLimitOnPlayer` を呼ぶだけ。 |
