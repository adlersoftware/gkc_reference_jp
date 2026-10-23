# switchCompanionSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Game Manager/switchCompanionSystem.cs:6`

**概要**: キャラクターをAI/プレイヤーへ切り替えるイベントを保持し、入力からの次キャラ切替を`playerCharactersManager`へ委譲するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Switch Companion Enabled | `switchCompanionEnabled` | `bool` | true | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event To Set Character As AI | `eventToSetCharacterAsAI` | `UnityEvent` | – | – |
| Event To Set Character As Player | `eventToSetCharacterAsPlayer` | `UnityEvent` | – | – |
| Event To Set Character As Only Player Active | `eventToSetCharacterAsOnlyPlayerActive` | `UnityEvent` | – | – |
| Event To Set Character As Player Not Active | `eventToSetCharacterAsPlayerNotActive` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Player Characters Manager | `mainPlayerCharactersManager` | `playerCharactersManager` | – | – |
| Mainfriend List Manager | `mainfriendListManager` | `friendListManager` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateEventToSetCharacterAsAI()` | `eventToSetCharacterAsAI`を発火するだけ。 |
| `activateEventToSetCharacterAsPlayer()` | `eventToSetCharacterAsPlayer`を発火するだけ。 |
| `activateEventToSetCharacterAsOnlyPlayerActive()` | `eventToSetCharacterAsOnlyPlayerActive`を発火するだけ。 |
| `activateEventToSetCharacterAsPlayerNotActive()` | `eventToSetCharacterAsPlayerNotActive`を発火するだけ。 |
| `inputSwitchToNextCharacter()` | 有効でメニュー・ポーズ・デバイス使用中でなければ、次キャラ切替を`playerCharactersManager`へ委譲する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventToSetCharacterAsAI` | `UnityEvent` | – |
| `eventToSetCharacterAsPlayer` | `UnityEvent` | – |
| `eventToSetCharacterAsOnlyPlayerActive` | `UnityEvent` | – |
| `eventToSetCharacterAsPlayerNotActive` | `UnityEvent` | – |
