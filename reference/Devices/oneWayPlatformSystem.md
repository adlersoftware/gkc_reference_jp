# oneWayPlatformSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/oneWayPlatformSystem.cs:5`

**概要**: 一方通行の足場。進入方向やしゃがみ・入力の条件に応じ、プレイヤーとのコリジョンを選択的に無視する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Check | `tagToCheck` | `List<string>` | new List<string> () | – |
| Ignore Collision On Top | `ignoreCollisionOnTop` | `bool` | – | – |
| Ignore Collision On Bottom | `ignoreCollisionOnBottom` | `bool` | – | – |

### Conditions Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Needs To Crouch To Ignore | `playerNeedsToCrouchToIgnore` | `bool` | – | – |
| Use Only Crouch To Ignore | `useOnlyCrouchToIgnore` | `bool` | – | – |
| Use Only Move Input Down To Ignore | `useOnlyMoveInputDownToIgnore` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Found | `playerFound` | `bool` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Passengers Info List | `passengersInfoList` | `List<passengersInfo>` | new List<passengersInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Platform Collider | `platformCollider` | `Collider` | – | – |
| Platform Transform | `platformTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkTriggerInfo(Collider col, bool isEnter)` | タグ一致時、入場で搭乗者を追加し下方向の衝突を必要なら無視、退場で衝突を戻して搭乗者を除去する。 |
| `addPassenger(Transform newPassenger)` | 未登録なら`playerController`とコライダーを取得して搭乗者リストへ追加する。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`OnTriggerEnter(Collider col)`, `OnTriggerExit(Collider col)`

</details>

## 内部型

- `passengersInfo`（class）
