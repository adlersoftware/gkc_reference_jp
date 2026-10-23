# launchedObjects

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/launchedObjects.cs:5`

**概要**: 発射されたオブジェクトに付与され、衝突相手へ速度由来のダメージや遠隔イベントを与えるコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check Collisions Enabled | `checkCollisionsEnabled` | `bool` | true | – |
| Remove Component On Collision Enabled | `removeComponentOnCollisionEnabled` | `bool` | true | – |

### Damage Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Custom Damage Amount | `useCustomDamageAmount` | `bool` | – | – |
| Custom Damage Amount | `customDamageAmount` | `float` | – | – |
| Search Player As Damage Attacker | `searchPlayerAsDamageAttacker` | `bool` | – | – |
| Damage Type ID | `damageTypeID` | `int` | -1 | – |
| Damage Can Be Blocked | `damageCanBeBlocked` | `bool` | true | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Check On Trigger Enter Enabled | `checkOnTriggerEnterEnabled` | `bool` | – | – |
| Layermask To Check On Trigger Enter | `layermaskToCheckOnTriggerEnter` | `LayerMask` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Remote Event On Objects Found | `useRemoteEventOnObjectsFound` | `bool` | – | – |
| Remote Event Name List | `remoteEventNameList` | `List<string>` | new List<string> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setOnTriggerInfoCheckState(bool state, LayerMask newLayermask)` | トリガー接触チェックの有効フラグと、対象レイヤーの`LayerMask`を設定する。 |
| `setUseCustomDamageAmountValues(bool state, float amount)` | 固定ダメージを使うかどうかと、そのダメージ量を設定する。 |
| `setCurrentPlayer(GameObject player)` | 攻撃者となるプレイヤーを設定するだけ。 |
| `setCurrentPlayerAndCollider(GameObject player, Collider playerCollider)` | プレイヤーとそのコライダーを設定し、以後の衝突無視に備える。 |
| `setIgnoreShieldState(bool state)` | シールドを無視するフラグを設定するだけ。 |
| `setCanActivateReactionSystemTemporally(bool state)` | リアクションの一時有効化フラグを設定するだけ。 |
| `setCamageReactionID(int newValue)` | ダメージリアクションIDを設定するだけ。 |
| `setCheckCollisionsEnabledState(bool state)` | 衝突判定そのものの有効フラグを設定するだけ。 |
