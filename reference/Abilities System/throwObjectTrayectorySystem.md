# throwObjectTrayectorySystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/throwObjectTrayectorySystem.cs:5`

**概要**: 投擲物の生成、放物線の照準、発射を担当するコンポーネント。カメラのレイキャストで着弾点を求めて速度を計算する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Throw Object Enabled | `throwObjectEnabled` | `bool` | true | – |
| Layer To Check Throw Object | `layerToCheckThrowObject` | `LayerMask` | – | – |
| Max Raycast Distance | `maxRaycastDistance` | `float` | 30 | – |
| Use Infinite Raycast Distance | `useInfiniteRaycastDistance` | `bool` | – | – |
| Use Max Distance When No Surface Found | `useMaxDistanceWhenNoSurfaceFound` | `bool` | – | – |
| Max Distance When No Surface Found | `maxDistanceWhenNoSurfaceFound` | `float` | – | – |
| Throw Position | `throwPosition` | `Transform` | – | – |
| Object To Throw | `objectToThrow` | `GameObject` | – | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Add Launch Object Component | `addLaunchObjectComponent` | `bool` | – | – |
| Add Grabbed Object State Component | `addGrabbedObjectStateComponent` | `bool` | – | – |
| Rotate Object Toward Throw Direction | `rotateObjectTowardThrowDirection` | `bool` | – | – |
| Check If Locked Camera Active | `checkIfLockedCameraActive` | `bool` | – | – |
| Ignore Collisions With Player Enabled | `ignoreCollisionsWithPlayerEnabled` | `bool` | true | – |

### Custom Throw Direction Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Throw In Custom Transform Direction | `throwInCustomTransformDirection` | `bool` | – | – |
| Custom Transform Direction | `customTransformDirection` | `Transform` | – | – |
| Custom Throw Direction Amount | `customThrowDirectionAmount` | `float` | 400 | – |
| Use Custom Throw Position | `useCustomThrowPosition` | `bool` | – | – |
| Use Custom Throw Local Position | `useCustomThrowLocalPosition` | `bool` | – | – |
| Custom Throw Position | `customThrowPosition` | `Vector3` | – | – |
| Custom Throw Rotation | `customThrowRotation` | `Vector3` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | – |
| Current Object To Throw | `currentObjectToThrow` | `GameObject` | – | – |
| Current Throw Speed | `currentThrowSpeed` | `Vector3` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Player Controller Game Object | `playerControllerGameObject` | `GameObject` | – | – |
| Target Position Transform | `targetPositionTransform` | `Transform` | – | – |
| Player Camera Game Object | `playerCameraGameObject` | `Transform` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Player Collider | `playerCollider` | `Collider` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentObjectToThrow(GameObject newObject)` | 投擲位置にオブジェクトを配置・表示し、`Rigidbody` をキネマティックにしてプレイヤーとの衝突を無視する。 |
| `instantiateObject()` | `currentObjectToThrow` が無ければ投擲位置と回転でプレハブを生成し、設定処理に渡す。 |
| `calculateThrowDirection()` | カメラのレイキャストで着弾点を求め、`currentTargetPosition` を更新する（ロックオンカメラにも対応）。 |
| `throwObject()` | 必要ならオブジェクトを生成し、放物線速度か指定方向の速度で `Rigidbody` に力を加えて射出する。 |
| `inputThrowObject()` | `throwObjectEnabled` の時だけ `throwObject` を呼ぶ。 |
| `inputInstantiateObject()` | `throwObjectEnabled` の時だけ `instantiateObject` を呼ぶ。 |
| `inputCalculateThrowDirection()` | `throwObjectEnabled` の時だけ `calculateThrowDirection` を呼ぶ。 |
