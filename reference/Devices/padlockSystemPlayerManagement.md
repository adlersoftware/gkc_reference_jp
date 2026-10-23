# padlockSystemPlayerManagement

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/padlockSystemPlayerManagement.cs:6`

**概要**: プレイヤー側の南京錠パズル入力を、現在の`padlockSystem`へ中継する管理コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Padlock | `usingPadlock` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | – |
| Even On State Enabled | `evenOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentPadlockSystem(padlockSystem newPadlockSystem)` | 操作対象の`padlockSystem`を保持するだけ。 |
| `setUsingPadlockState(bool state)` | `usingPadlock`を設定し、状態変化イベントを呼ぶ。 |
| `inputRotateWheel(bool directionUp)` | 使用中かつ対象があるとき、回転方向`directionUp`を`inputRotateWheel`へ中継する。 |
| `checkEventsOnStateChange(bool state)` | `useEventsOnStateChange`が有効なとき、`state`に応じ開始/終了イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `evenOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
