# hideCharacterFixedPlaceSystemPlayerManagement

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Hide System/hideCharacterFixedPlaceSystemPlayerManagement.cs:6`

**概要**: プレイヤー側で現在の固定隠れ場所とフリー隠れゾーンを保持し、隠れ中のカメラ入力要求を委譲する管理コンポーネント。

## インスペクター設定

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Hiding | `playerHiding` | `bool` | – | – |
| Player Hiding On Free Zone | `playerHidingOnFreeZone` | `bool` | – | – |
| Current Fixed Hide System | `currentFixedHideSystem` | `hideCharacterFixedPlaceSystem` | – | – |
| Current Hide From Enemies System | `currentHideFromEnemiesSystem` | `hideFromEnemiesSystem` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | – |
| Even On State Enabled | `evenOnStateEnabled` | `UnityEvent` | – | – |
| Event On State Disabled | `eventOnStateDisabled` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Game Object | `characterGameObject` | `GameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setPlayerHidingState(bool state)` | `playerHiding`を設定し、状態変化イベントを使う設定なら対応するイベントを発火する。 |
| `setCurrentFixedHideSystem(hideCharacterFixedPlaceSystem newFixedHideSystem)` | `currentFixedHideSystem`を設定するだけ。 |
| `setPlayerHidingOnFreeZoneState(bool state)` | フリー隠れゾーン内かどうかのフラグを設定するだけ。 |
| `setCurrentHideFromEnemiesSystem(hideFromEnemiesSystem newHideFromEnemiesSystem)` | `currentHideFromEnemiesSystem`を設定するだけ。 |
| `removeCurrentHideFromEnemiesSystem()` | フリー隠れゾーン中なら、現在の敵隠れシステムから自身のキャラクターを除外する。 |
| `hideInputResetCameraTransform()` | 隠れ中かつ固定隠れ場所がある時のみ、そのカメラ入力リセットを呼ぶ。 |
| `hideInputSetIncreaseZoomStateByButton(bool state)` | 隠れ中かつ固定隠れ場所がある時のみ、拡大入力を委譲する。 |
| `hideInputSetDecreaseZoomStateByButton(bool state)` | 隠れ中かつ固定隠れ場所がある時のみ、縮小入力を委譲する。 |
| `hideInputSetZoomValueByMouseWheel(bool state)` | 隠れ中かつ固定隠れ場所がある時のみ、マウスホイール入力を委譲する。 |
| `checkEventsOnStateChange(bool state)` | イベント使用時のみ、`state`に応じて有効/無効のイベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `evenOnStateEnabled` | `UnityEvent` | – |
| `eventOnStateDisabled` | `UnityEvent` | – |
