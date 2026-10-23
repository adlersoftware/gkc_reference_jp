# customOrderBehaviorToFollow

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `customOrderBehavior`
- **ソース**: `AI/Custom Orders/customOrderBehaviorToFollow.cs:5`

**概要**: 追従注文用に、ロックオン中や画面内の対象を選び、無ければ注文発行者を返すビヘイビア。

## インスペクター設定

### Custom Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Tag To Locate | `tagToLocate` | `List<string>` | new List<string> () | – |
| Check If Target On Lock On View Enabled | `checkIfTargetOnLockOnViewEnabled` | `bool` | true | – |
| Send Player As Target | `sendPlayerAsTarget` | `bool` | true | – |
| Ignore To Get Closest Enemy | `ignoreToGetClosestEnemy` | `bool` | – | – |

### Target Detection Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Get Closest Target To Camera View If No Lock On Active | `getClosestTargetToCameraViewIfNoLockOnActive` | `bool` | – | – |
| Max Distance To Find Target | `maxDistanceToFindTarget` | `float` | 300 | – |
| Search Point To Look Components | `searchPointToLookComponents` | `bool` | true | – |
| Look Only If Target On Screen | `lookOnlyIfTargetOnScreen` | `bool` | – | – |
| Check Obstacles To Target | `checkObstaclesToTarget` | `bool` | – | – |
| Layer To Look | `layerToLook` | `LayerMask` | – | – |
| Point To Look Components Layer | `pointToLookComponentsLayer` | `LayerMask` | – | – |
| Get Closest To Camera Center | `getClosestToCameraCenter` | `bool` | – | – |
| Use Max Distance To Camera Center | `useMaxDistanceToCameraCenter` | `bool` | – | – |
| Max Distance To Camera Center | `maxDistanceToCameraCenter` | `float` | 200 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Camera Gizmo | `showCameraGizmo` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Camera Transform | `playerCameraTransform` | `Transform` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `canAIAttack(Transform AIFriend)` | `attackType`が`none`以外なら攻撃可能と判定する。 |
| `getClosestEnemy(Transform centerPointTransform)` | `tagToLocate`の生存対象から`centerPointTransform`に最も近い1体を返す。 |
| `getClosestEnemyToScreenView()` | 画面内かつ遮蔽の無いタグ対象や`pointToLook`対象から、画面中心に最も近いものを1つ返す。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`activateOrder(Transform character)`, `getCustomTarget(Transform character, Transform orderOwner)`

</details>
