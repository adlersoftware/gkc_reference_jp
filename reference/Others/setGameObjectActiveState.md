# setGameObjectActiveState

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/setGameObjectActiveState.cs:5`

**概要**: 対象`GameObject`のSetActive状態を保持し、反転や開始時の初期化を行う。

**公式ドキュメント抜粋**（[Set Game Object Active State](../../docs/toplevelcomponents/player-and-game-management/set-game-object-active-state.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set Initial State | `setInitialState` | `bool` | – | – |
| Initial State | `initialState` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Active | `objectActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Active | `objectToActive` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `changeActiveState()` | `objectActive`を反転させて`setActiveState`を呼ぶ。 |
| `setActiveState(bool state)` | `objectActive`を`state`にし、`objectToActive`の`activeSelf`が異なる場合だけSetActiveする。 |
| `changeActiveStateFromEditor()` | `changeActiveState`を呼んだ後に`updateComponent`でシーンを更新する。 |
