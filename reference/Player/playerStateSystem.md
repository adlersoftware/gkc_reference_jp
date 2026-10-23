# playerStateSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/playerStateSystem.cs:6`

**概要**: プレイヤーの状態を名前で管理するコンポーネント。優先度と割り込み可否を見て状態を切り替え、開始/終了イベントと持続時間コルーチンを扱う。

**公式ドキュメント抜粋**（[Player State System](../../docs/player-controller-components/essential-components/player-state-system.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player States Enabled | `playerStatesEnabled` | `bool` | true | プレイヤー状態システムを有効にするかどうか。 |
| Activate State On Start | `activateStateOnStart` | `bool` | – | オンにすると開始時に指定した状態を適用する。 |
| State To Activate On Start | `stateToActivateOnStart` | `string` | – | 開始時に適用する状態を一覧から名前で指定する。 / 表示条件: `activateStateOnStart` がオンのとき |

### States Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | 状態の切替結果などをコンソールに出力する。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `playerStateInfoList` | `List<playerStateInfo>` | new List<playerStateInfo> () | – |
| `currentStateName` | `string` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPlayerState(string stateName)` | 名前で状態を探し、変更可否を確認したうえで他の状態を終了イベント付きで止め、新しい状態を開始して持続時間コルーチンを起動する。 |
| `checkIfStateCanChange(int stateIndexToCheck)` | 割り込み不可で優先度が高い状態が動作中なら false を返す。 |
| `setUseTemporalDurationOnState(string stateName)` | `名前_時間` 形式を分割して数値化し、対象状態の一時持続時間と使用フラグを設定する。 |
| `setStateEnabledState(bool state, string stateName)` | 名前が一致する状態の `stateEnabled` を設定する。 |
| `setStateEnabledState(string stateName)` | `setStateEnabledState(true, stateName)` を呼ぶだけ。 |
| `setStateDisabledState(string stateName)` | `setStateEnabledState(false, stateName)` を呼ぶだけ。 |
| `setActivateStateOnStartState(bool state)` | `activateStateOnStart` を設定するだけ。 |
| `setStateToActivateOnStartValue(string newName)` | `stateToActivateOnStart` を設定するだけ。 |
| `setStateEnabledStateFromEditor(string stateName)` | 状態を有効化してから `updateComponent` を呼ぶ。 |
| `setStateDisabledStateFromEditor(string stateName)` | 状態を無効化してから `updateComponent` を呼ぶ。 |
| `setActivateStateOnStartStateFromEditor(bool state)` | 値を設定してから `updateComponent` を呼ぶ。 |
| `setStateToActivateOnStartValueFromEditor(string newName)` | 値を設定してから `updateComponent` を呼ぶ。 |

## 内部型

- `playerStateInfo`（class）
