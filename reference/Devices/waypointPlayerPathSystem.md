# waypointPlayerPathSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/waypointPlayerPathSystem.cs:8`

**概要**: ウェイポイント巡回路。順番制/順不同の到達判定、タイマー、マップアイコン、ライン表示、完了/失敗イベントを管理する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| In Order | `inOrder` | `bool` | – | 指定した順番どおりにポイントを踏む必要があるか。 |
| Show One By One | `showOneByOne` | `bool` | – | 目標を1つずつ表示し、順番を強制するか。 |
| Trigger Radius | `triggerRadius` | `float` | – | ポイントの到達判定に使う半径の既定値。 |
| Show Off Screen Icon | `showOffScreenIcon` | `bool` | – | 画面外のポイントにアイコンを表示するか。 |
| Show Map Window Icon | `showMapWindowIcon` | `bool` | – | マップ画面にポイントのアイコンを出すか。 |
| Show Distance | `showDistance` | `bool` | – | 目標までの距離を画面に表示するか。 |
| Path Active | `pathActive` | `bool` | – | パスが進行中かどうかの実行時の状態。 |
| Main Manager Name | `mainManagerName` | `string` | "Screen Objectives Manager" | 画面目標を管理するマネージャーの名前。 |

### Events To Call Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Path Complete | `eventOnPathComplete` | `UnityEvent` | new UnityEvent () | 全ポイント到達時に呼ぶイベント。 |
| Event On Path Incomplete | `eventOnPathIncomplete` | `UnityEvent` | new UnityEvent () | 制限時間切れなどで失敗した時に呼ぶイベント。 |
| Use Timer | `useTimer` | `bool` | – | 制限時間のタイマーを有効にするか。 / 表示条件: `advancedSettings` がオンのとき |
| Timer Speed | `timerSpeed` | `float` | – | タイマーの残り時間が減る速さの倍率。 / 表示条件: `advancedSettings` がオンのとき |
| Minutes To Complete | `minutesToComplete` | `float` | – | 制限時間として設定する分数の値。 / 表示条件: `advancedSettings` がオンのとき / Range (0, 60) |
| Seconds To Complete | `secondsToComplete` | `float` | – | 制限時間として設定する秒数の値。 / 表示条件: `advancedSettings` がオンのとき / Range (0, 60) |
| Extra Time Per Point | `extraTimePerPoint` | `float` | – | ポイントに到達するたびに加算する秒数。 / 表示条件: `advancedSettings` がオンのとき |
| Path Complete Audio Sound | `pathCompleteAudioSound` | `AudioClip` | – | 全ポイント到達時に鳴らすAudioClip。 / 表示条件: `advancedSettings` がオンのとき |
| Path Complete Audio Element | `pathCompleteAudioElement` | `AudioElement` | – | 完了音の再生設定をまとめたAudioElement。 / 表示条件: `advancedSettings` がオンのとき |
| Path Uncomplete Audio Sound | `pathUncompleteAudioSound` | `AudioClip` | – | 失敗した時に鳴らすAudioClip。 / 表示条件: `advancedSettings` がオンのとき |
| Path Uncomplete Audio Element | `pathUncompleteAudioElement` | `AudioElement` | – | 失敗音の再生設定をまとめたAudioElement。 / 表示条件: `advancedSettings` がオンのとき |
| Second Timer Sound | `secondTimerSound` | `AudioClip` | – | 残り時間が少ない時に鳴らすAudioClip。 / 表示条件: `advancedSettings` がオンのとき |
| Second Timer Audio Element | `secondTimerAudioElement` | `AudioElement` | – | 残り時間わずかの合図音の再生設定。 / 表示条件: `advancedSettings` がオンのとき |
| Second Sound Timer Lower Than | `secondSoundTimerLowerThan` | `float` | – | 合図音を鳴らし始める残り秒数のしきい値。 / 表示条件: `advancedSettings` がオンのとき |
| Point Reached Sound | `pointReachedSound` | `AudioClip` | – | ポイント到達時に鳴らすAudioClip。 / 表示条件: `advancedSettings` がオンのとき |
| Point Reached Audio Element | `pointReachedAudioElement` | `AudioElement` | – | 到達音の再生設定をまとめたAudioElement。 / 表示条件: `advancedSettings` がオンのとき |
| Use Line Renderer | `useLineRenderer` | `bool` | – | 残りのポイントを結ぶ線を表示するか。 / 表示条件: `advancedSettings` がオンのとき |
| Line Renderer Color | `lineRendererColor` | `Color` | Color.yellow | 残りの経路を結ぶラインの描画色。 / 表示条件: `advancedSettings` がオンのとき |
| Line Renderer Width | `lineRendererWidth` | `float` | – | 残りの経路を結ぶラインの太さ。 / 表示条件: `advancedSettings` がオンのとき |

### Gizmo Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | シーンビューにポイントのギズモを表示するか。 |
| Show Info Label | `showInfoLabel` | `bool` | true | シーンビューに半径やアイコン設定を表示するか。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | – | シーンビューのラベルの文字色。 / 表示条件: `showGizmo` がオンのとき |
| Gizmo Radius | `gizmoRadius` | `float` | – | ポイントを示す球ギズモの半径。 / 表示条件: `showGizmo` がオンのとき |
| Use Regular Gizmo Radius | `useRegularGizmoRadius` | `bool` | – | 全ポイントで共通の`triggerRadius`を使うか。 / 表示条件: `showGizmo` がオンのとき |
| Use Handle For Vertex | `useHandleForVertex` | `bool` | – | ポイントを移動させるハンドルを表示するか。 / 表示条件: `showGizmo` がオンのとき |
| Handle Radius | `handleRadius` | `float` | – | ポイント移動ハンドルの大きさ。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |
| Handle Gizmo Color | `handleGizmoColor` | `Color` | – | ポイント移動ハンドルを描く色。 / 表示条件: `showGizmo.boolValue && useHandleForVertex.boolValue` |
| Show Do Position Handles | `showDoPositionHandles` | `bool` | – | ポイントの位置操作ギズモを表示するか。 / 表示条件: `showGizmo` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `wayPoints` | `List<wayPointInfo>` | new List<wayPointInfo> () | – |
| `pointsReached` | `int` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `convertSeconds()` | 残り時間を`MM:SS`形式の文字列に変換する。 |
| `addNewWayPoint()` | 既存の最後のポイント前方に新規ポイントと`mapObjectInformation`を生成し、一覧へ追加する。 |
| `renamePoints()` | 各ポイント名を連番へ振り直し、`updateComponent`を呼ぶ。 |
| `pointReached(Transform point)` | 設定に応じ到達判定し、正しければカウント・追加時間・効果音、全達成で完了イベント、誤順なら`stopPath`を実行する。 |
| `setCurrentUser(GameObject user)` | `currentUser`を保持するだけ。 |
| `resetPath()` | プレイヤーから音源とHUDを取得し、到達状況・タイマー・マップアイコンを初期化して経路を開始する。 |
| `stopPath()` | 経路を停止し、タイマー・マップアイコン・ラインを片付けて未完了イベントと効果音を実行する。 |
| `playAudioSourceShoot(AudioElement clip)` | プレイヤーの音源を割り当て、`AudioPlayer.PlayOneShot`で再生する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`で更新を要求する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPathComplete` | `UnityEvent` | – |
| `eventOnPathIncomplete` | `UnityEvent` | – |

## 内部型

- `wayPointInfo`（class）
