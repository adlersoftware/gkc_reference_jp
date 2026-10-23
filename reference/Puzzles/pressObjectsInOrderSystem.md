# pressObjectsInOrderSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Puzzles/pressObjectsInOrderSystem.cs:8`

**概要**: 決められた順序で押される位置を判定し、順序を間違えるとリセットする仕組み。使用中は毎フレーム入力を監視する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Incorrect Order Sound | `useIncorrectOrderSound` | `bool` | – | 順番を間違えた時にエラー音を鳴らすかどうか。 |
| Incorrect Order Sound | `incorrectOrderSound` | `AudioClip` | – | 順番を間違えた時に再生するサウンドクリップ。 / 表示条件: `useIncorrectOrderSound` がオンのとき |
| Incorrect Order Audio Element | `incorrectOrderAudioElement` | `AudioElement` | – | エラー音を再生するためのオーディオ要素。 / 表示条件: `useIncorrectOrderSound` がオンのとき |
| Press Objects While Mouse Pressed | `pressObjectsWhileMousePressed` | `bool` | – | マウス押下中もレイキャストで対象を押せるようにする。 |
| Press Objects Layer | `pressObjectsLayer` | `LayerMask` | – | 押下判定のレイキャスト対象となるレイヤー。 / 表示条件: `pressObjectsWhileMousePressed` がオンのとき |

### Current State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Pressed Object System | `usingPressedObjectSystem` | `bool` | – | 押下順パズルの判定を有効にするかどうか。 |
| All Positions Pressed | `allPositionsPressed` | `bool` | – | 全位置が押されて完成したかどうかの状態。 |
| Correct Pressed Index | `correctPressedIndex` | `int` | – | 次に押すべき位置のインデックス。 |

### Events State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| All Positions Pressed Event | `allPositionsPressedEvent` | `UnityEvent` | – | 全位置を押し切った時に呼ばれるイベント。 |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera | `mainCamera` | `Camera` | – | 画面座標からレイを作るためのカメラ参照。 |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | 効果音を再生するオーディオソースの参照。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `positionInfoList` | `List<positionInfo>` | new List<positionInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkPressedPosition(string positionName)` | 使用中なら次の期待位置と照合し、正しければイベントと進行、誤りならリセットと効果音を行う。 |
| `resetPressedObjects()` | 進行インデックスを0に戻し、全位置の押下フラグを下ろす。 |
| `startOrStopPressedObjectSystem()` | 使用状態を反転させるだけ。 |
| `setUsingPressedObjectSystemState(bool state)` | 使用フラグを設定し、更新コルーチンの再起動やカメラ・タッチ環境の取得を行う。 |
| `stopUpdateCoroutine()` | 更新コルーチンがあれば停止するだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `allPositionsPressedEvent` | `UnityEvent` | – |

## 内部型

- `positionInfo`（class）
