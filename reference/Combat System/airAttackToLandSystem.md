# airAttackToLandSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/airAttackToLandSystem.cs:7`

**概要**: 空中からの攻撃で地面へ落下させる処理を制御するコンポーネント。開始/終了イベントと下向きレイキャストによる地面検出を持つ。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Down Force Amount | `downForceAmount` | `float` | 5 | – |
| Raycast Layermask | `raycastLayermask` | `LayerMask` | – | – |
| Min Distance To Detect Ground | `minDistanceToDetectGround` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Attack Landing In Process | `attackLandingInProcess` | `bool` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Start Attack | `eventOnStartAttack` | `UnityEvent` | – | – |
| Event On End Attack | `eventOnEndAttack` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateAirAttackToLand()` | 前回のコルーチンを止めて落下を再開し、地面を検出するまで`downForceAmount`の下向き力を加え、前後イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnStartAttack` | `UnityEvent` | – |
| `eventOnEndAttack` | `UnityEvent` | – |
