# examineObjectSystemPlayerManagement

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/examineObjectSystemPlayerManagement.cs:6`

**概要**: プレイヤー側の観察入力を現在の観察対象へ中継する管理コンポーネント。ズームと回転リセット、キャンセルを扱う。

## インスペクター設定

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Examining Object | `examiningObject` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | – |
| Even On State Enabled | `evenOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setExaminingObjectState(bool state)` | 観察中フラグと開始時刻を更新し、状態変化イベントを呼ぶ。 |
| `setcurrentExanimeObject(examineObjectSystem newExamineObject)` | 操作対象の`examineObjectSystem`を保持するだけ。 |
| `examineObjectInputSetZoomValue(bool value)` | 観察中のみ、`value`を対象の`inputSetZoomValue`へ中継する。 |
| `examineObjectInputResetRotation()` | 観察中のみ、対象の`inputResetRotation`を呼ぶ。 |
| `examineObjectInputResetRotationAndPosition()` | 観察中のみ、対象の`inputResetRotationAndPosition`を呼ぶ。 |
| `examineObjectInputCancelExamine()` | 観察開始から0.4秒未満は無視し、それ以降は対象の`inputCancelExamine`を呼ぶ。 |
| `examineObjectInputCheckIfMessage()` | 観察中のみ、対象の`inputCheckIfMessage`を呼ぶ。 |
| `checkEventsOnStateChange(bool state)` | `useEventsOnStateChange`が有効なとき、`state`に応じ開始/終了イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `evenOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
