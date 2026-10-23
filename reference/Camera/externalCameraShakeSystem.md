# externalCameraShakeSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Player Camera/externalCameraShakeSystem.cs:6`

**概要**: 距離やアクション名を条件に、周囲のプレイヤーの `headBob` へ外部シェイクを要求するコンポーネント。シェイク名は外部シェイクリスト管理マネージャから取得する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| External Camera Shake Enabled | `externalCameraShakeEnabled` | `bool` | true | カメラシェイク機能の有効/無効。オフだと揺れを一切発生させない。 |
| Main Manager Name | `mainManagerName` | `string` | "External Shake List Manager" | 外部シェイク管理マネージャーを識別する名前。既定のまま使用する。 |
| Set Player Manually | `setPlayerManually` | `bool` | – | オンにすると範囲検出ではなく`currentPlayer`のカメラだけを揺らす。 |
| Current Player | `currentPlayer` | `GameObject` | – | 揺らす対象のプレイヤー。`setPlayerManually`有効時に使う。 / 表示条件: `setPlayerManually.boolValue \|\| useShakeListTriggeredByActions.boolValue` |
| Use Shake List Triggered By Actions | `useShakeListTriggeredByActions` | `bool` | – | アクション名からシェイクを呼び出すリストを使用する。 |

### Shake Triggered By Action List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shake Using Distance | `shakeUsingDistance` | `bool` | – | 距離に応じてシェイクの強さを減衰させる。 |
| Min Distance To Shake | `minDistanceToShake` | `float` | – | シェイクが届く最大距離。`OverlapSphere`の半径とギズモ球に使う。 |
| Layer | `layer` | `LayerMask` | – | シェイク対象を検出する`OverlapSphere`のレイヤーマスク。 |
| Use Shake Event | `useShakeEvent` | `bool` | – | シェイク開始時と終了時のイベントを有効にする。 |
| Event At Start | `eventAtStart` | `UnityEvent` | – | シェイク開始時に実行するイベント。 / 表示条件: `useShakeEvent` がオンのとき |
| Event At End | `eventAtEnd` | `UnityEvent` | – | シェイク終了時に実行するイベント。 / 表示条件: `useShakeEvent` がオンのとき |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンに効果範囲のギズモ円を表示する。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.black | シーン上のギズモラベルの文字色。 / 表示条件: `showGizmo` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `externalShakeName` | `string` | – | – |
| `shakeTriggeredByActionList` | `List<shakeTriggeredByActionInfo>` | new List<shakeTriggeredByActionInfo> () | – |
| `nameIndex` | `int` | – | – |
| `nameList` | `string []` | – | – |
| `externalShakeManager` | `externalShakeListManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getExternalShakeList()` | シェイクリスト管理マネージャを検索または生成し、登録されているシェイク名を `nameList` に複製して更新する。 |
| `setCurrentPlayer(GameObject player)` | null なら無視し、`currentPlayer` を設定して未取得なら `headBob` を取得する。 |
| `setCurrentPlayerAndActivateCameraShake(GameObject player)` | プレイヤーを設定してから `setCameraShake` でシェイクを発生させる。 |
| `setCameraShake()` | 有効時、イベント設定を控え、手動設定ならプレイヤーを割り当てて `externalShakeName` のシェイクを起こす。 |
| `setCameraShakeByAction(string actionName)` | `shakeTriggeredByActionList` からアクション名が一致する要素を探し、その `shakeName` とイベント設定でシェイクする。 |
| `setCameraShakeByName(string shakeName)` | 手動設定なら `currentPlayer` に、そうでなければ範囲内のコライダーにシェイク信号を送る。 |
| `setExternalShakeSignal(GameObject objectToCall, string shakeName)` | 距離条件を満たすか確認して減衰率を算出し、対象の `headBob` にイベントとシェイク名を渡す。 |
| `updateComponent()` | コンポーネントとダーティシーンを更新するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventAtStart` | `UnityEvent` | – |
| `eventAtEnd` | `UnityEvent` | – |
| `currentEventAtStart` | `UnityEvent` | – |
| `currentEventAtEnd` | `UnityEvent` | – |

## 内部型

- `shakeTriggeredByActionInfo`（class）
