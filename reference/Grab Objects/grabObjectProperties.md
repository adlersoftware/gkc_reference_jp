# grabObjectProperties

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Grab Objects/grabObjectProperties.cs:6`

**概要**: オブジェクト個別の重さ・追加把持距離・投擲用の質量などを保持し、把持／解放イベントを中継するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Uses Weight | `objectUsesWeight` | `bool` | true | – |
| Object Weight | `objectWeight` | `float` | – | – |
| Use Extra Grab Distance | `useExtraGrabDistance` | `bool` | – | – |
| Extra Grab Distance | `extraGrabDistance` | `float` | – | – |

### Mass Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Mass To Throw | `useCustomMassToThrow` | `bool` | – | – |
| Custom Mass To Throw | `customMassToThrow` | `float` | – | – |
| Custom Object Mass Divider On Throw | `customObjectMassDividerOnThrow` | `float` | 1 | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Grab Object | `useEventsOnGrabObject` | `bool` | – | – |
| Event On Grab Object | `eventOnGrabObject` | `UnityEvent` | – | – |
| Use Events On Drop Object | `useEventsOnDropObject` | `bool` | – | – |
| Event On Drop Object | `eventOnDropObject` | `UnityEvent` | – | – |
| Use Event To Set Player | `useEventToSetPlayer` | `bool` | – | – |
| Event To Set Player | `eventToSetPlayer` | `eventParameters.eventToCallWithGameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Trigger | `mainTrigger` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getObjectWeight()` | `objectUsesWeight` が有効なら `objectWeight`、無効なら 0 を返す。 |
| `getExtraGrabDistance()` | `useExtraGrabDistance` が有効なら `extraGrabDistance`、無効なら 0 を返す。 |
| `checkEventsOnGrabObject()` | `useEventsOnGrabObject` が有効なら `eventOnGrabObject` を発火するだけ。 |
| `checkEventsOnDropObject()` | `useEventsOnDropObject` が有効なら `eventOnDropObject` を発火するだけ。 |
| `checkEventToSetPlayer(GameObject newPlayer)` | `useEventToSetPlayer` が有効なら `eventToSetPlayer` に引数のプレイヤーを渡して発火する。 |
| `getMainTrigger()` | `mainTrigger` を返すだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnGrabObject` | `UnityEvent` | – |
| `eventOnDropObject` | `UnityEvent` | – |
