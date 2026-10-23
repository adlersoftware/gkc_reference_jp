# enableOrDisableObjectOnDistanceManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/enableOrDisableObjectOnDistanceManager.cs:6`

**概要**: 距離管理システムへ自身を登録する側のコンポーネントで、有効・無効の切り替え時にイベントを発火する。

## インスペクター設定

### Behavior Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Object To Main System | `addObjectToMainSystem` | `bool` | true | – |
| Add Object On Start With Delay | `addObjectOnStartWithDelay` | `bool` | – | – |
| Delay To Add Object On Start | `delayToAddObjectOnStart` | `float` | 0.01f | – |
| Add Object On Awake | `addObjectOnAwake` | `bool` | – | – |
| Main Transform | `mainTransform` | `Transform` | – | – |
| Main Manager Name | `mainManagerName` | `string` | "Disable Objects On Distance Manager" | – |
| Set Active State On Main Transform Enabled | `setActiveStateOnMainTransformEnabled` | `bool` | true | – |

### Distance Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Distance | `useCustomDistance` | `bool` | – | – |
| Max Distance Object Enabled On Screen | `maxDistanceObjectEnabledOnScreen` | `float` | – | – |
| Max Distance Object Enable Out Of Screen | `maxDistanceObjectEnableOutOfScreen` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Active | `objectActive` | `bool` | true | – |
| Object Info Sent To Main System | `objectInfoSentToMainSystem` | `bool` | – | – |
| Main Enable Or Disable Objects On Distance System Located | `mainEnableOrDisableObjectsOnDistanceSystemLocated` | `bool` | – | – |
| Main Enable Or Disable Objects On Distance System | `mainEnableOrDisableObjectsOnDistanceSystem` | `enableOrDisableObjectsOnDistanceSystem` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Enable Object | `eventOnEnableObject` | `UnityEvent` | – | – |
| Event On Disable Object | `eventOnDisableObject` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `removeObjectFromSystem()` | メインシステムを取得済みなら`removeObject`に自身の`mainTransform`を渡して登録を解除する。 |
| `setActiveState(bool state)` | `objectActive`が変わる時だけ更新し、有効化/無効化のイベントを発火する。 |
| `setAddObjectToMainSystemState(bool state)` | `addObjectToMainSystem`を更新し、非再生時のみ登録または解除と非アクティブ化を行う。 |
| `isSetActiveStateOnMainTransformEnabled()` | `setActiveStateOnMainTransformEnabled`をそのまま返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnEnableObject` | `UnityEvent` | – |
| `eventOnDisableObject` | `UnityEvent` | – |
