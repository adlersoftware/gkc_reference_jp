# preventCharacterCollisionOnTop

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/preventCharacterCollisionOnTop.cs:5`

**概要**: キャラクターの上に乗られた時に押し出す力を加え、位置ずれを防ぐ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Collision Check Enabled | `collisionCheckEnabled` | `bool` | true | – |
| Min Time To Push Character | `minTimeToPushCharacter` | `float` | 1 | – |
| Min Distance To Push Character | `minDistanceToPushCharacter` | `float` | 1.5f | – |
| Push Down Extra Force | `pushDownExtraForce` | `float` | 1 | – |
| Layer To Ignore | `layerToIgnore` | `LayerMask` | – | – |
| Push Force | `pushForce` | `float` | 10 | – |
| Push Force Mode | `pushForceMode` | `ForceMode` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Push In Process | `pushInProcess` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止し、`pushInProcess`を`false`にする。 |
