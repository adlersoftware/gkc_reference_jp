# perfectDodgeSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/perfectDodgeSystem.cs:6`

**概要**: 回避成功時に周囲のキャラクタとプレイヤーを一定時間減速させる演出を制御し、開始/終了イベントを発火する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Perfect Dogde Enabled | `perfectDogdeEnabled` | `bool` | true | – |

### Slow Down Character Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character State Affected Name | `characterStateAffectedName` | `string` | "Character Slow Down Velocity" | – |
| Slow Down Speed On Characters | `slowDownSpeedOnCharacters` | `float` | 0.2f | – |
| Slow Down Speed Duration On Characters | `slowDownSpeedDurationOnCharacters` | `float` | 4 | – |
| Activate Slow Down On Main Player | `activateSlowDownOnMainPlayer` | `bool` | – | – |
| Slow Down Speed On Player | `slowDownSpeedOnPlayer` | `float` | 0.8f | – |
| Slow Down Speed Duration On Player | `slowDownSpeedDurationOnPlayer` | `float` | 2 | – |
| Use Cool Down | `useCoolDown` | `bool` | – | – |
| Cool Down Amount | `coolDownAmount` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Perfect Dodge Active | `perfectDodgeActive` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On State Change | `useEventsOnStateChange` | `bool` | – | – |
| Event On Perfect Dodge Enabled | `eventOnPerfectDodgeEnabled` | `UnityEvent` | – | – |
| Event On Perfect Dodge Disabled | `eventOnPerfectDodgeDisabled` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activatePerfectDodgeToCharacter(GameObject newCharacter)` | 対象キャラクタの`playerComponentsManager`をリストへ追加し、単体指定モードで`checkState`を実行する。 |
| `activatePerfectDodge()` | 単体指定なしで`checkState`を呼び、全キャラクタの減速と自プレイヤーの速度低下を発動する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnPerfectDodgeEnabled` | `UnityEvent` | – |
| `eventOnPerfectDodgeDisabled` | `UnityEvent` | – |
