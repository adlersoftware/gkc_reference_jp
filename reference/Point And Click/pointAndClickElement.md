# pointAndClickElement

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Point And Click/pointAndClickElement.cs:6`

**概要**: ポイントアンドクリックで操作できる要素（デバイス・乗り物・味方・敵）に付け、クリック時に使うオブジェクト、移動先、表示テキストを`playerNavMeshSystem`へ提供します。ホバー/使用イベントとトリガー検出も持ちます。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Element Enabled | `elementEnabled` | `bool` | true | – |
| Element Type | `elementType` | `typeOfObject` | – | – |
| Use On Off Device State | `useOnOffDeviceState` | `bool` | – | – |
| Is Pickup | `isPickup` | `bool` | – | – |
| Active Panel After Stop Use | `activePanelAfterStopUse` | `bool` | – | – |
| Disable Panel After Use | `disablePanelAfterUse` | `bool` | – | – |
| Follow Object To Use Position | `followObjectToUsePosition` | `bool` | – | – |
| Use Front Rear Position For Nav Mesh | `useFrontRearPositionForNavMesh` | `bool` | – | – |
| Use Custom Element Min Distance | `useCustomElementMinDistance` | `bool` | – | – |
| Custom Element Min Distance | `customElementMinDistance` | `float` | – | – |
| Use Custom Element Name | `useCustomElementName` | `bool` | – | – |
| Custom Element Name | `customElementName` | `string` | – | – |
| Layer For Elements | `layerForElements` | `LayerMask` | – | – |

### Element Text Info Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Element Text Info | `useElementTextInfo` | `bool` | – | – |
| Element Text Info | `elementTextInfo` | `string` | – | TextArea (1, 10) |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Element | `usingElement` | `bool` | – | – |
| Hoverving Point And Click Element | `hovervingPointAndClickElement` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Activate Element Event | `activateElementEvent` | `UnityEvent` | – | – |
| Deactivate Element Event | `deactivateElementEvent` | `UnityEvent` | – | – |

### Events On Hover Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Hover | `useEventsOnHover` | `bool` | – | – |
| Event On Hover On | `eventOnHoverOn` | `UnityEvent` | – | – |
| Event On Hover Off | `eventOnHoverOff` | `UnityEvent` | – | – |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.green | – |
| Gizmo Color | `gizmoColor` | `Color` | Color.white | – |
| Gizmo Radius | `gizmoRadius` | `float` | 0.3f | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object To Use | `objectToUse` | `GameObject` | – | – |
| Position For Nav Mesh | `positionForNavMesh` | `Transform` | – | – |
| Front Position For Nav Mesh | `frontPositionForNavMesh` | `Transform` | – | – |
| Rear Position For Nav Mesh | `rearPositionForNavMesh` | `Transform` | – | – |
| Main Collider | `mainCollider` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setElementEnabledState(bool state)` | 初期化済みなら`elementEnabled`と`mainCollider.enabled`を設定し、登録された`playerNavMeshSystem`のパネルを閉じる。 |
| `getPointAndClickElementTextInfo()` | `elementTextInfo`を返すだけ。 |
| `usePointAndClickElement()` | `usingElement`を反転し、種別ごとの空ブロックを経て、状態に応じて`activateElementEvent`か`deactivateElementEvent`を呼ぶ。 |
| `isDevice()` | `elementType`がdeviceかどうかを返すだけ。 |
| `isFriend()` | `elementType`がfriendかどうかを返すだけ。 |
| `isEnemy()` | `elementType`がenemyかどうかを返すだけ。 |
| `getElementToUse()` | `objectToUse`を返すだけ。 |
| `getPositionForNavMesh(Vector3 playerPosition)` | 前後位置設定があればプレイヤー方向との内積で前方/後方のTransformを返し、無ければ`positionForNavMesh`を返す。 |
| `removeElement()` | 自身のGameObjectを`Destroy`するだけ。 |
| `checkIfRemove()` | `isPickup`を返すだけ。 |
| `setHoveringPointAndClickElementState(bool state)` | ホバー状態を設定し、`useEventsOnHover`が有効ならオン/オフイベントを呼ぶ。 |
| `checkTriggerInfo(Collider col, bool isEnter)` | 要素レイヤーのプレイヤーが侵入/退出したら、その`playerNavMeshSystem`をリストへ追加/削除し検出状態を設定する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `activateElementEvent` | `UnityEvent` | – |
| `deactivateElementEvent` | `UnityEvent` | – |
| `eventOnHoverOn` | `UnityEvent` | – |
| `eventOnHoverOff` | `UnityEvent` | – |

## 内部型

- `typeOfObject`（enum）
