# spriteAnimatorSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/spriteAnimatorSystem.cs:7`

**概要**: 3Dキャラクターを2Dスプライト表示へ切り替えるコンポーネント。Animator と SpriteAnimator、メッシュ、武器表示、ルートモーションを排他的に切り替える。

**公式ドキュメント抜粋**（[Sprite Animator System](../../docs/player-controller-components/elements-used-by-other-components/sprite-animator-system.md)）

> 

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Ability Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sprite Animator Enabled | `spriteAnimatorEnabled` | `bool` | true | – |
| Sprite Animator Active | `spriteAnimatorActive` | `bool` | – | – |
| Adjust Sprite To Rotation To Camera Direction | `adjustSpriteToRotationToCameraDirection` | `bool` | – | – |
| Ground State | `groundState` | `string` | "Grounded" | – |
| Moving State | `movingState` | `string` | "Moving" | – |
| Air Speed State | `airSpeedState` | `string` | "Air Speed Y" | – |
| Jump State | `jumpState` | `string` | "Jump" | – |
| Run State | `runState` | `string` | "Run" | – |
| Camera Angle State | `cameraAngleState` | `string` | "Camera Angle" | – |
| Idle Animator Name | `idleAnimatorName` | `string` | "Idle" | – |
| Walk Animator Name | `walkAnimatorName` | `string` | "Walk" | – |
| Jump Animator Name | `jumpAnimatorName` | `string` | "Jump" | – |
| On Air Up Animator Name | `onAirUpAnimatorName` | `string` | "On Air Up" | – |
| On Air Down Animator Name | `onAirDownAnimatorName` | `string` | "On Air Down" | – |
| Land Animator Name | `landAnimatorName` | `string` | "Land" | – |
| Jump Animation Duration | `jumpAnimationDuration` | `float` | 1 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Idle Active | `idleActive` | `bool` | – | – |
| Walk Active | `walkActive` | `bool` | – | – |
| Jump Active | `jumpActive` | `bool` | – | – |
| Run Active | `runActive` | `bool` | – | – |
| On Air Up Active | `onAirUpActive` | `bool` | – | – |
| On Air Down Active | `onAirDownActive` | `bool` | – | – |
| Land Active | `landActive` | `bool` | – | – |
| Player Is Moving | `playerIsMoving` | `bool` | – | – |
| Idle Previously Active | `idlePreviouslyActive` | `bool` | – | – |
| Walk Previously Active | `walkPreviouslyActive` | `bool` | – | – |
| Jump Previously Active | `jumpPreviouslyActive` | `bool` | – | – |
| Player On Ground | `playerOnGround` | `bool` | – | – |
| Player On Ground Previously | `playerOnGroundPreviously` | `bool` | – | – |
| Player Has Jumped | `playerHasJumped` | `bool` | – | – |
| Air Speed | `airSpeed` | `float` | – | – |
| Horizontal Input | `horizontalInput` | `float` | – | – |
| Vertical Input | `verticalInput` | `float` | – | – |
| Current Camera Angle | `currentCameraAngle` | `float` | – | – |
| Current Camera Angle Value | `currentCameraAngleValue` | `float` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Sprite Enabled | `eventOnSpriteEnabled` | `UnityEvent` | – | – |
| Event On Sprite Disabled | `eventOnSpriteDisabled` | `UnityEvent` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Controller Transform | `playerControllerTransform` | `Transform` | – | – |
| Main Animator | `mainAnimator` | `Animator` | – | – |
| Main Sprite Animator | `mainSpriteAnimator` | `Animator` | – | – |
| Player Sprite Game Object | `playerSpriteGameObject` | `GameObject` | – | – |
| Player Sprite Transform | `playerSpriteTransform` | `Transform` | – | – |
| Movement Last Direction | `movementLastDirection` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setSpriteAnimatorActiveState(bool state)` | Animator と SpriteAnimator を排他で切り替え、メッシュ・武器・ルートモーション・表示を更新する。 |
| `checkEventState(bool state)` | 開始なら `eventOnSpriteEnabled`、終了なら `eventOnSpriteDisabled` を送出する。 |
| `setSpriteAnimatorActiveStateFromEditor(bool state)` | `setSpriteAnimatorActiveState(state)` を呼ぶだけ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnSpriteEnabled` | `UnityEvent` | – |
| `eventOnSpriteDisabled` | `UnityEvent` | – |
