# simpleSniperSightSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/simpleSniperSightSystem.cs:5`

**概要**: スナイパーサイト表示時にカメラ状態とFOVを切り替え、解除時は元のカメラ状態へ戻すシステム。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sniper Sight Third Person Enabled | `sniperSightThirdPersonEnabled` | `bool` | true | – |
| Sniper Sight First Person Enabled | `sniperSightFirstPersonEnabled` | `bool` | true | – |
| Sniper Sight Third Person Without Aim Enabled | `sniperSightThirdPersonWithoutAimEnabled` | `bool` | – | – |
| Sniper Camera Third Person State Name | `sniperCameraThirdPersonStateName` | `string` | "Sniper Camera View Third Person" | – |
| Sniper Camera First Person State Name | `sniperCameraFirstPersonStateName` | `string` | "Sniper Camera View First Person" | – |
| Sniper Camera FBA State Name | `sniperCameraFBAStateName` | `string` | "Sniper Camera View FBA" | – |
| Sniper Camera Third Person Crouch State Name | `sniperCameraThirdPersonCrouchStateName` | `string` | "Sniper Camera View Third Person Crouch" | – |
| Sniper Camera First Person Crouch State Name | `sniperCameraFirstPersonCrouchStateName` | `string` | "Sniper Camera View First Person Crouch" | – |
| Sniper Camera FBA Crouch State Name | `sniperCameraFBACrouchStateName` | `string` | "Sniper Camera View FBA Crouch" | – |
| New Camera Fov Value Third Person | `newCameraFovValueThirdPerson` | `float` | 20 | – |
| New Camera Fov Value First Person | `newCameraFovValueFirstPerson` | `float` | 15 | – |
| Change Fov Smoothly | `changeFovSmoothly` | `bool` | – | – |
| Change Fov Speed | `changeFovSpeed` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sniper Sight Active | `sniperSightActive` | `bool` | – | – |
| Previuous Camera State | `previuousCameraState` | `string` | – | – |
| Sniper Sight Active Previously | `sniperSightActivePreviously` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Sniper Sight Panel Game Object | `sniperSightPanelGameObject` | `GameObject` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Weapons Manager | `mainPlayerWeaponsManager` | `playerWeaponsManager` | – | – |
| Weapons Camera | `weaponsCamera` | `Camera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `enableOrDisableSniperSight(bool state)` | 一人称・三人称やFBA、照準入力などの条件を確認し、満たせば`setSniperSightState`でサイトを切り替える。 |
| `disableSniperSight()` | 一人称状態を渡して`setSniperSightState(false, …)`を呼ぶだけ。 |
| `disableSniperSightIfActive()` | サイトが有効なら解除して`sniperSightActivePreviously`を立て、後で復帰できるようにする。 |
| `enableSniperSightIfActivePreviously()` | 以前アクティブで照準中なら再度有効化し、最後に`sniperSightActivePreviously`を下ろす。 |
