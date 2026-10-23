# sleepingStateIconSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/sleepingStateIconSystem.cs:5`

**概要**: 睡眠状態のキャラクターの頭上に「Z」アイコンを生成し、上昇・拡大・色変化させて睡眠演出を行うシステム。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Life Time | `lifeTime` | `float` | – | – |
| Increase Size Speed | `increaseSizeSpeed` | `float` | – | – |
| Max Number Of Icons At Time | `maxNumberOfIconsAtTime` | `int` | – | – |
| Spawn Rate | `spawnRate` | `float` | – | – |
| Sleep Duration | `sleepDuration` | `float` | – | – |
| Spawn Position Offset | `spawnPositionOffset` | `float` | – | – |
| Local Offset | `localOffset` | `Vector3` | new Vector3 (0, 0, 0.13f) | – |

### Icon Movement Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Movement Speed | `movementSpeed` | `float` | – | – |
| Vertical Speed | `verticalSpeed` | `float` | – | – |
| Horizontal Movement Amount | `horizontalMovementAmount` | `float` | – | – |
| Horizontal Movement Speed | `horizontalMovementSpeed` | `float` | – | – |

### Color Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Change Text Color To Duration | `changeTextColorToDuration` | `bool` | – | – |
| Start Color | `startColor` | `Color` | Color.white | – |
| End Color | `endColor` | `Color` | Color.red | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sleep State Active | `sleepStateActive` | `bool` | – | – |
| Transition Color | `transitionColor` | `float` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sleep Icon | `sleepIcon` | `GameObject` | – | – |
| Spawn Position | `spawnPosition` | `Transform` | – | – |
| Health Manager | `healthManager` | `health` | – | – |
| Parent To Attach | `parentToAttach` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setSleepState(bool state)` | trueなら鎮静時間を取得してアイコン生成コルーチンを開始、falseなら停止して全アイコンを破棄する。 |
| `stopSleepCoroutine()` | `sleepCoroutine`が実行中なら停止するだけ。 |

## 内部型

- `sleepIconInfo`（class）
