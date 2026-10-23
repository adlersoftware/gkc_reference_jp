# setCharacterAsChildSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/setCharacterAsChildSystem.cs:6`

**概要**: プレイヤーと子キャラクターを親子関係にし、入力・速度・IK・コライダー衝突を同期させる。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Parenting Enabled | `parentingEnabled` | `bool` | true | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On State Change | `useEventOnStateChange` | `bool` | – | – |
| Event On Activate Child State | `eventOnActivateChildState` | `UnityEvent` | – | – |
| Event On Deactivate Child State | `eventOnDeactivateChildState` | `UnityEvent` | – | – |
| Event On Stop Parenting From Characters Check State | `eventOnStopParentingFromCharactersCheckState` | `UnityEvent` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Parenting Active | `parentingActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Character | `mainCharacter` | `playerController` | – | – |
| Child Character | `childCharacter` | `playerController` | – | – |
| Child Parent Position | `childParentPosition` | `Transform` | – | – |
| Main Child Parent | `mainChildParent` | `Transform` | – | – |
| Child Input Manager | `childInputManager` | `playerInputManager` | – | – |
| Main Character IK Component | `mainCharacterIKComponent` | `OnAnimatorIKComponent` | – | – |
| Child Rigidbody | `childRigidbody` | `Rigidbody` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`があれば停止するだけ。 |
| `toggleParenting()` | `parentingActive`を反転して`enableOrDisableParenting`を呼ぶ。 |
| `enableOrDisableParenting(bool state)` | 親子設定を`state`に切り替え、入力停止・`isKinematic`・コライダー無視・IK・更新コルーチンをまとめて設定する。 |
| `setMainCharacter(GameObject newCharacter)` | `playerController`をメインキャラクターに設定してIKとRigidbodyを取得し直す（子キャラ指定時は端末リストから外すだけ）。 |
| `setChildCharacter(GameObject newCharacter)` | `playerController`を子キャラクターに設定し、`playerInputManager`を取得し直す。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnActivateChildState` | `UnityEvent` | – |
| `eventOnDeactivateChildState` | `UnityEvent` | – |
| `eventOnStopParentingFromCharactersCheckState` | `UnityEvent` | – |
