# damageScreenSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/damageScreenSystem.cs:6`

**概要**: 被弾時に画面を赤くフェードさせ、攻撃者の方向アイコンを出すダメージスクリーン。`usedByAI`でAI用に抑止でき、体力に応じて色の濃さを変える。

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Screen Enabled | `damageScreenEnabled` | `bool` | – | – |
| Damage Color | `damageColor` | `Color` | – | – |
| Max Alpha Damage | `maxAlphaDamage` | `float` | 0.6f | – |
| Fade To Damage Color Speed | `fadeToDamageColorSpeed` | `float` | – | – |
| Fade To Transparent Speed | `fadeToTransparentSpeed` | `float` | – | – |
| Time To Start To Heal | `timeToStartToHeal` | `float` | – | – |
| Show Damage Direction | `showDamageDirection` | `bool` | – | – |
| Show Damage Position When Enemy Visible | `showDamagePositionWhenEnemyVisible` | `bool` | – | – |
| Show All Damage Directions | `showAllDamageDirections` | `bool` | – | – |
| Check Health Amount On Start | `checkHealthAmountOnStart` | `bool` | – | – |
| Used By AI | `usedByAI` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Damage Screen | `damageScreen` | `GameObject` | – | – |
| Damage Direction Icon | `damageDirectionIcon` | `GameObject` | – | – |
| Damage Position Icon | `damagePositionIcon` | `GameObject` | – | – |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |
| Damage Image | `damageImage` | `RawImage` | – | – |
| Healt Manager | `healtManager` | `health` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Enemies Damage List | `enemiesDamageList` | `List<damageInfo>` | new List<damageInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `checkHealthState()` | 画面有効かつ現在HPが最大未満なら負傷状態にしてダメージスクリーンを表示する。 |
| `setDamageDirectionWithDamageScreen(GameObject enemy)` | `setDamageDir(enemy, true)`を呼び、画面フラッシュ付きで方向を表示する。 |
| `setDamageDirectionWithoutDamageScreen(GameObject enemy)` | `setDamageDir(enemy, false)`を呼び、画面フラッシュ無しで方向だけ表示する。 |
| `setDamageDir(GameObject enemy, bool showDamageImageValue)` | `showAllDamageDirections`なら敵ごとに方向/位置アイコンを生成・更新し、負傷状態と画面表示を開始する。 |
| `setUsedByAIState(bool state)` | `usedByAI`を`state`にするだけ。 |
| `setDamageScreenEnabledState(bool state)` | `damageScreenEnabled`を`state`にするだけ。 |
| `updateScreenValues()` | `Screen.width`と`Screen.height`を内部の画面サイズ変数へ取り込むだけ。 |
| `setDamageScreenEnabledStateFromEditor(bool state)` | 設定後に`GKC_Utils.updateComponent`で更新するだけ。 |

## 内部型

- `damageInfo`（class）
