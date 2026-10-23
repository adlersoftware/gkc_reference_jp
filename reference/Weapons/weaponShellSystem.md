# weaponShellSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/weaponShellSystem.cs:6`
- **属性**: `RequireComponent (typeof(AudioElementHolder))`

**概要**: 排出される薬莢の初速・ランダム回転・衝突無視・再生音を設定するコンポーネント。

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Random Rotation To Shells | `addRandomRotationToShells` | `bool` | true | – |
| Random Rotation X Range | `randomRotationXRange` | `Vector2` | new Vector2 (-20, 20) | – |
| Random Rotation Y Range | `randomRotationYRange` | `Vector2` | new Vector2 (-20, 20) | – |
| Random Rotation Z Range | `randomRotationZRange` | `Vector2` | new Vector2 (-20, 20) | – |
| Random Rotation Multiplier | `randomRotationMultiplier` | `float` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Audio Element Holder | `audioElementHolder` | `AudioElementHolder` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setExtraColliderToIgnore(Collider extraCollider)` | `extraCollider`があれば`mainCollider`との衝突を無視するよう設定する。 |
| `setShellValues(Vector3 forceDirection, Collider playerCollider, AudioElement clipToUse)` | 速度をリセットして`forceDirection`の力を加え、ランダム回転・プレイヤーとの衝突無視・再生音を設定する。 |
