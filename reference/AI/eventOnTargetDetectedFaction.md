# eventOnTargetDetectedFaction

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/eventOnTargetDetectedFaction.cs:6`

**概要**: 陣営名ごとに登録したUnityEventを、対象の検知・解除のタイミングで発火させるコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Targets Enabled | `checkTargetsEnabled` | `bool` | true | – |

### Targets Info List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Target Info List | `eventOnTargetInfoList` | `List<eventOnTargetInfo>` | new List<eventOnTargetInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTargetDetected(GameObject newTarget)` | 有効時かつ対象がnullでなければ、陣営名を取得して文字列版の`checkTargetDetected`を呼ぶ。 |
| `removeTargetDetected(GameObject newTarget)` | 有効時かつ対象がnullでなければ、陣営名を取得して文字列版の`removeTargetDetected`を呼ぶ。 |
| `checkTargetDetected(string targetFactioName)` | 同名で有効な陣営情報があれば`eventOnAddTarget`を`Invoke`する。 |
| `removeTargetDetected(string targetFactioName)` | 同名で有効な陣営情報があれば`eventOnRemoveTarget`を`Invoke`する。 |
| `setCheckTargetsEnabledState(bool state)` | `checkTargetsEnabled`を`state`に設定するだけ。 |
| `setCheckTargetsEnabledStateFromEditor(bool state)` | 有効状態を設定したうえで`updateComponent`を呼び、シーンを更新する。 |

## 内部型

- `eventOnTargetInfo`（class）
