# playerDamageOnScreenInfoSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/playerDamageOnScreenInfoSystem.cs:6`

**概要**: プレイヤー単位のダメージ数値表示。対象の頭上にテキストを生成し、`damageOnScreenInfoSystem`と対象リストを共有して移動演出付きで表示する。

**公式ドキュメント抜粋**（[Player Damage On Screen Info System](../../docs/character-level-components/character/player-damage-on-screen-info-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Damage Active | `showDamageActive` | `bool` | true | – |
| Show Damage Paused | `showDamagePaused` | `bool` | – | – |
| Damage On Screen Id | `damageOnScreenId` | `int` | – | – |
| Place Mark Above Damaged Targets | `placeMarkAboveDamagedTargets` | `bool` | – | – |
| Use Random Direction | `useRandomDirection` | `bool` | – | – |
| Use Projectile Direction | `useProjectileDirection` | `bool` | – | – |
| Movement Speed | `movementSpeed` | `float` | – | – |
| Movement Amount | `movementAmount` | `float` | – | – |
| Max Radius To Instantiate | `maxRadiusToInstantiate` | `float` | – | – |
| Down Movement Amount | `downMovementAmount` | `float` | 2 | – |
| Check Distance To Target | `checkDistanceToTarget` | `bool` | – | – |
| Distance Multiplier Amount | `distanceMultiplierAmount` | `float` | – | – |
| Critical Damage Text | `criticalDamageText` | `string` | "CRITICAL!" | – |

### Text Color Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Random Color | `useRandomColor` | `bool` | – | – |
| Random Color Alpha | `randomColorAlpha` | `float` | – | – |
| Damage Color | `damageColor` | `Color` | Color.red | – |
| Heal Color | `healColor` | `Color` | Color.green | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Panel Name | `mainPanelName` | `string` | "Damage On Screen Info" | – |
| Use Canvas Group On Icons | `useCanvasGroupOnIcons` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Target Info List | `targetInfoList` | `List<damageOnScreenInfoSystem.targetInfo>` | new List<damageOnScreenInfoSystem.tar… | – |
| Ignore Show Damage Info Active | `ignoreShowDamageInfoActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player | `player` | `GameObject` | – | – |
| Damage Number Parent | `damageNumberParent` | `Transform` | – | – |
| Damage Number Target Parent | `damageNumberTargetParent` | `GameObject` | – | – |
| Damage Number Text | `damageNumberText` | `GameObject` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Damage On Screen Info Manager | `damageOnScreenInfoManager` | `damageOnScreenInfoSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addNewTarget(damageOnScreenInfoSystem.targetInfo newTarget)` | `newTarget`のID重複を除き、アイコン用オブジェクトを生成して一覧に追加する。初期状態は非表示。 |
| `setDamageInfo(int targetIndex, float amount, bool isDamage, Vector3 direction, float healthAmount, float criticalDamageProbability)` | `amount`の数値テキストを生成して色と符号を設定し、会心時は`createCriticalDamageText`、続けて移動コルーチンを開始する。 |
| `createCriticalDamageText(damageOnScreenInfoSystem.targetInfo currentTargetInfoToCheck, Vector3 movementDirection)` | `criticalDamageText`を太字で生成し、`moveNumber`で移動させる。 |
| `removeElementFromList(int objectID)` | `objectID`の対象アイコンを破棄して一覧から削除する。 |
| `removeElementFromListByPlayer(int objectID)` | `damageOnScreenInfoManager`側の対象リストも削除してから、自身の一覧から消す。 |
| `getRandomDirection()` | `-1`から`1`のランダムな2D方向を返すだけ。 |
| `setShowDamageActiveState(bool state)` | `showDamageActive`を`state`にするだけ。 |
| `setIgnoreShowDamageInfoActiveState(bool state)` | `ignoreShowDamageInfoActive`を`state`にするだけ。 |
