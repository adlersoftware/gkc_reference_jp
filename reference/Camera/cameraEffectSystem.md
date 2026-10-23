# cameraEffectSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Camera Effect/cameraEffectSystem.cs:6`

**概要**: 登録したカメラエフェクトを名前やインデックスで切り替える管理コンポーネント。`OnRenderImage` から現在のエフェクトへ画像を渡し、切替時に対応する UnityEvent を発火する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Effect Enabled | `cameraEffectEnabled` | `bool` | true | – |
| Render Effect Active | `renderEffectActive` | `bool` | true | – |
| Start With Camera Effect Active | `startWithCameraEffectActive` | `bool` | – | – |
| Camera Effect Change Disabled | `cameraEffectChangeDisabled` | `bool` | – | – |
| Current Camera Effect Index | `currentCameraEffectIndex` | `int` | – | – |

### Extra Cameras Effect

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Render Extra Cameras | `renderExtraCameras` | `bool` | – | – |
| Extra Camera Effect System List | `extraCameraEffectSystemList` | `List<extraCameraEffectSystem>` | new List<extraCameraEffectSystem> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Effect Active | `cameraEffectActive` | `bool` | – | – |
| Current Camera Effect | `currentCameraEffect` | `cameraEffect` | – | – |

### Camera Effect Info List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Camera Effect Info List | `cameraEffectInfoList` | `List<cameraEffectInfo>` | new List<cameraEffectInfo> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Camera | `mainCamera` | `Camera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `extraRenderImage(RenderTexture source, RenderTexture destination, Camera currentCamera)` | 追加カメラ用の描画入口で、有効時のみ現在のエフェクトの `renderEffect` に画像とカメラを渡す。 |
| `setCameraEffectByName(string cameraStateName)` | 名前が一致する要素のインデックスを `currentCameraEffectIndex` に入れ、エフェクトを有効化する。 |
| `setMainCameraEffectByName(string cameraStateName)` | 名前で探した要素だけ `activeAsMainCameraEffect` を true、他を false にして有効化する。 |
| `disableMainCameraEffectActiveState(string cameraStateName)` | 名前で探した要素の `activeAsMainCameraEffect` を false にし、エフェクトを無効化する。 |
| `setIfCurrentCameraEffectRemainActive(bool state)` | true ならメインカメラエフェクトの有無を確認し、false なら有効時に無効化する。 |
| `checkIfMainCameraEffectsAreActive()` | `activeAsMainCameraEffect` が立つ最初の要素を現在のエフェクトとして有効化する。 |
| `canUseCameraEffect()` | `cameraEffectEnabled` と `cameraEffectChangeDisabled`（開始時設定済みか）から切替可否を返す。 |
| `enableOrDisableCameraEffectActive()` | 現在の有効状態を反転して `setCameraEffectActiveState` を呼ぶだけ。 |
| `setCameraEffectActiveState(bool state)` | 使用可否を確認し、有効フラグと `enabled`、`currentCameraEffect` を更新して有効/無効イベントと追加カメラを切り替える。 |
| `setCurrentCameraEffect(cameraEffect newCameraEffect)` | `currentCameraEffect` を差し替えるだけ。 |
| `setNextCameraEffect()` | 現在の無効イベントを発火し、インデックスを次（末尾なら0）へ進めて有効イベントを発火、必要なら有効化する。 |
| `setPreviousCameraEffect()` | 現在の無効イベントを発火し、インデックスを前（先頭なら末尾）へ戻して有効イベントを発火する。 |
| `inputSetNextCameraEffect()` | `setNextCameraEffect` を呼ぶだけ。 |
| `inputSetPreviousCameraEffect()` | `setPreviousCameraEffect` を呼ぶだけ。 |
| `inputEnableOrDisableCameraEffectActive()` | `enableOrDisableCameraEffectActive` を呼ぶだけ。 |

## 内部型

- `cameraEffectInfo`（class）
