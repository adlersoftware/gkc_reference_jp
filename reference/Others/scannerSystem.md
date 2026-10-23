# scannerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/Scanner System/scannerSystem.cs:7`

**概要**: 一人称視点のスキャナーモードを制御するコンポーネントで、注視対象のスキャン進捗スライダー、カメラFOV/ズーム、弱点表示、入力イベントをまとめて扱う。

**公式ドキュメント抜粋**（[Scanner System](../../docs/player-controller-components/elements-used-by-other-components/scanner-system.md)）

> 

## インスペクター設定

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Scanner System Enabled | `scannerSystemEnabled` | `bool` | – | – |
| Infinite Scan Distance | `infiniteScanDistance` | `bool` | – | – |
| Scan Distance | `scanDistance` | `float` | – | – |
| Scan Distance Affected By Zoom | `scanDistanceAffectedByZoom` | `bool` | – | – |
| Scan Distance Extra With Zoom | `scanDistanceExtraWithZoom` | `float` | – | – |
| Layer | `layer` | `LayerMask` | – | – |
| Ignore Change To First Person Enabled | `ignoreChangeToFirstPersonEnabled` | `bool` | – | – |
| Remove Located Object If Disabled On Scene | `removeLocatedObjectIfDisabledOnScene` | `bool` | true | – |

### Camera Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Initial Camera Fov | `initialCameraFov` | `float` | – | – |
| Zoom Camera Fov | `zoomCameraFov` | `float` | – | – |
| Fov Change Speed | `fovChangeSpeed` | `float` | – | – |
| Scan Speed | `scanSpeed` | `float` | – | – |
| Scane Icon Movement Speed | `scaneIconMovementSpeed` | `float` | – | – |
| Use Max Distance To Camera Center | `useMaxDistanceToCameraCenter` | `bool` | – | – |
| Max Distance To Camera Center | `maxDistanceToCameraCenter` | `float` | – | – |
| Use Auto Scanner | `useAutoScanner` | `bool` | – | – |

### Scanner Messages Settings Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Scan Complete String | `scanCompleteString` | `string` | "SCAN COMPLETED" | – |
| Scan Visor Active String | `scanVisorActiveString` | `string` | "SCAN VISOR ACTIVE" | – |
| Scanning String | `scanningString` | `string` | "SCANNING..." | – |
| Empty Scanner Info String | `emptyScannerInfoString` | `string` | "..." | – |

### Other Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Weak Spot Scanner | `useWeakSpotScanner` | `bool` | – | – |
| Scanner Animation Name | `scannerAnimationName` | `string` | "scannerTarget" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Hold Scanner Input Active | `holdScannerInputActive` | `bool` | – | – |
| Scanned Object | `scannedObject` | `GameObject` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Scanner Enabled | `eventOnScannerEnabled` | `UnityEvent` | – | – |
| Event On Scanner Disabled | `eventOnScannerDisabled` | `UnityEvent` | – | – |

### Scanner Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Scanner HUD | `scannerHUD` | `GameObject` | – | – |
| Scan Icon | `scanIcon` | `GameObject` | – | – |
| Scan Icon Rect | `scanIconRect` | `RectTransform` | – | – |
| Icon Animation | `iconAnimation` | `Animation` | – | – |
| Icon Rect Transform | `iconRectTransform` | `RectTransform` | – | – |
| Scanner Camera | `scannerCamera` | `GameObject` | – | – |
| Scanner Camera UI | `scannerCameraUI` | `GameObject` | – | – |
| Slider | `slider` | `Slider` | – | – |
| Object Name | `objectName` | `Text` | – | – |
| Object Info | `objectInfo` | `Text` | – | – |
| Scan Status | `scanStatus` | `Text` | – | – |
| Health Info Parent | `healthInfoParent` | `Transform` | – | – |
| Health Element | `healthElement` | `GameObject` | – | – |
| Object Scanned Health Name Text | `objectScannedHealthNameText` | `Text` | – | – |
| Object Scanned Health Amount Text | `objectScannedHealthAmountText` | `Text` | – | – |
| Scanner Main Camera | `scannerMainCamera` | `Camera` | – | – |
| Main Player Camera | `mainPlayerCamera` | `playerCamera` | – | – |
| Player Controller Manager | `playerControllerManager` | `playerController` | – | – |
| Main Camera Transform | `mainCameraTransform` | `Transform` | – | – |
| Main Camera | `mainCamera` | `Camera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `playerIsBusy()` | `playerControllerManager` がデバイス・サブメニュー・プレイヤーメニューのいずれかを使用中なら true を返す。 |
| `activateScanner()` | `enableScanner` を呼び、スキャン対象が残っていれば `reset` で表示と保持情報を初期化する。 |
| `executeScanner()` | 保持入力中に `slider` を進め、最大到達で対象をスキャン済みにして `objectChecked` で情報を表示する。 |
| `setScannedObjectInfo()` | `scannedObject` から `scanElementInfo` を取得し、弱点スキャン有効時は体力や車両の弱点リストを追加する。 |
| `enableScanner()` | 条件を満たすと `scannerModeIsActivated` を反転し、一人称化・`reset`・イベント発火・FOV 更新を行う。 |
| `disableScanner()` | スキャナモードを解除し、`reset`・アイコン非表示・FOV 再計算・無効イベント発火を行う。 |
| `checkEventsOnEnableDisableScanner()` | `scannerModeIsActivated` に応じて有効/無効イベントを発火するだけ。 |
| `checkScannerCameraFov()` | ズーム中かどうかで目標 FOV を選び、`checkFovCoroutine` でカメラ FOV を変更する。 |
| `enableOrDisableScannerZoom(bool value)` | `zoomActive` を設定して目標 FOV を選び、`checkScanDistance` と FOV 変更コルーチンを実行する。 |
| `checkScanDistance(bool value)` | `scanDistanceAffectedByZoom` が有効なら、ズーム時に `distanceToScan` を加算・復元する。 |
| `isScannerActivated()` | `scannerModeIsActivated` を返すだけ。 |
| `checkFovCoroutine(float targetValue)` | 実行中の FOV コルーチンを停止し、`changeFovValue` を新たに開始する。 |
| `changeFovValue(float targetValue)` | `scannerMainCamera` の FOV を目標値まで徐々に動かし、前後でスキャナ用カメラ部品の有効状態を切り替える。 |
| `enableOrDisableScannerCameraComponents(bool state)` | `enableOrDisableScannerCamera` を呼び、UI と `scannerHUD` の表示も連動させる。 |
| `enableOrDisableScannerCamera(bool state)` | 一時停止フラグが立っていなければ `scannerMainCamera` の有効状態を設定する。 |
| `toggleScannerCameraElement()` | `scannerMainCamera` の現在の有効状態を反転させる。 |
| `setPauseEnableOrDisableScannerCameraElementState(bool state)` | カメラ要素の有効切替を止めるフラグを設定するだけ。 |
| `togglePauseEnableOrDisableScannerCameraElementState()` | カメラ要素の有効切替を止めるフラグを反転するだけ。 |
| `addHealthWeakSpotList()` | 体力や車両の弱点に合わせて弱点表示要素を生成・再利用し、倍率テキストと名前・体力を表示する。 |
| `disableHealtWeakSpotList()` | 弱点表示要素をすべて非アクティブにして `used` を false にし、親も非表示にする。 |
| `inputHoldScanner()` | システムが有効でプレイヤーが多忙でなければ `holdScannerInputActive` を true にする。 |
| `inputReleaseScanner()` | 条件を満たすと `holdScannerInputActive` を false にし `activateScanner` を呼ぶ。 |
| `setScannerSystemEnabledState(bool state)` | `scannerSystemEnabled` を設定するだけ。 |
| `setScannerSystemEnabledStateFromEditor(bool state)` | 状態を設定したうえで `GKC_Utils.updateComponent` により表示を更新する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnScannerEnabled` | `UnityEvent` | – |
| `eventOnScannerDisabled` | `UnityEvent` | – |
