# crate

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `PickUps/crate.cs:6`

**概要**: 速度の出た衝突で壊れる木箱。破片の生成・飛散・フェード削除と破壊音を扱い、`canBeBroken` で破壊を抑止できる。

**公式ドキュメント抜粋**（[GKC Update 3.02f](../../docs/annex/changelog/gkc-update-3.02f.md)）

> Added option in the current feature to make the player to always look in camera direction to disable this state when the player is running or sprinting, similar to resident evil 2 remake. LIke that, when the player walks, he uses the strafe movement and when he is in run or sprint state, he can rotate toward the direction of the input respect the direction of the camera, like if the option to look toward camera direction is not active in this state Added the elements and options to use an injured state in the animator, making it very flexible and being able to use it in different situations. I have added a random idle component to allow to configure a list of random idles, its duration and a random option to play them in any order. The player can also use weapons and aim in this injured mode as well Added improvements to the animator system to make a better transition from free moving to…

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Broken Sound | `brokenSound` | `AudioClip` | – | – |
| Broken Audio Element | `brokenAudioElement` | `AudioElement` | – | – |
| Min Velocity To Break | `minVelocityToBreak` | `float` | – | – |
| Break Force | `breakForce` | `float` | 10 | – |
| Force Mode | `forceMode` | `ForceMode` | – | – |

### Fade or Remove Broken Pieces

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Fade Broken Pieces | `fadeBrokenPieces` | `bool` | true | – |
| Remove Broken Pieces Enabled | `removeBrokenPiecesEnabled` | `bool` | true | – |
| Time To Remove | `timeToRemove` | `float` | 3 | – |
| Default Shader Name | `defaultShaderName` | `string` | "Legacy Shaders/Transparent/Diffuse" | – |
| Use Custom Shader | `useCustomShader` | `bool` | – | – |
| Custom Shader | `customShader` | `Shader` | – | – |
| Color Property Name | `colorPropertyName` | `string` | "_Color" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Can Be Broken | `canBeBroken` | `bool` | true | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Broken Crate | `brokenCrate` | `GameObject` | – | – |
| Transparent Shader | `transparentShader` | `Shader` | – | – |
| Main Rigidbody | `mainRigidbody` | `Rigidbody` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `breakCrate()` | 表示とコライダーを無効化して破片を生成・飛散させ、死亡処理と破棄コルーチンを開始する。 |
| `crateCanBeBrokenState(bool state)` | `canBeBroken` を設定するだけ。 |
| `getCrateRigidbody()` | `mainRigidbody` が未設定なら自身の `Rigidbody` を取得する。 |
| `setBarrelRigidbody(Rigidbody rigidbodyToUse)` | `mainRigidbody` を差し替えるだけ（名前は樽用だが木箱の剛体を設定する）。 |
