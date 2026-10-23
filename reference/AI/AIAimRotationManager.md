# AIAimRotationManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/Custom AI Behavior/AIAimRotationManager.cs:5`

**概要**: 名前付きの照準回転状態をカメラや旋回速度へ適用し、必要に応じてランダムな照準オフセットを付与する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| AI Aim Rotation Enabled | `AIAimRotationEnabled` | `bool` | true | – |
| Set AI Aim Rotation State On Awake | `setAIAimRotationStateOnAwake` | `bool` | – | – |
| AI Aim Rotation State On Awake Name | `AIAimRotationStateOnAwakeName` | `string` | – | – |

### AI Aim Rotation States List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| AI Aim Rotation Info List | `AIAimRotationInfoList` | `List<AIAimRotationInfo>` | new List<AIAimRotationInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Random Aim Position Offset Active | `randomAimPositionOffsetActive` | `bool` | – | – |
| Current AI Aim Rotation Info Name | `currentAIAimRotationInfoName` | `string` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Find Objectives System | `mainFindObjectivesSystem` | `findObjectivesSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の更新コルーチンを停止し、`randomAimPositionOffsetActive`をfalseにする。 |
| `setAIAImRotationState(string stateName)` | 名前が一致して有効な状態を選び、カメラ回転速度・旋回速度・ランダム照準オフセットを各コンポーネントへ適用する。 |
| `setAIAimRotationEnabledState(bool state)` | `AIAimRotationEnabled`を`state`に設定するだけ。 |
| `setAIAimRotationEnabledStateFromEditor(bool state)` | 有効状態を設定したうえで`updateComponent`を呼び、シーンとインスペクタ表示を更新する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`と`updateDirtyScene`でシーン状態を更新するだけ。 |

## 内部型

- `AIAimRotationInfo`（class）
