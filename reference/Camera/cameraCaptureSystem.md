# cameraCaptureSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Camera/Captures/cameraCaptureSystem.cs:9`

**概要**: スクリーンショットの撮影とPNG保存、保存済み画像のギャラリー表示・拡大・削除を、`ScrollRect`やボタンなどのUIとともに扱うコンポーネント。保存先は`gameManager`の設定に従う。

**公式ドキュメント抜粋**（[Camera Capture System](../../docs/character-level-components/character/camera-capture-system.md)）

> Used for different elements, including the photo mode in-game, the smartphone camera tool and the save system to take captures of the scene when the player is saving, using the main camera to take such capture

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Screen Resolution | `useScreenResolution` | `bool` | – | – |
| Capture Resolution | `captureResolution` | `Vector2` | – | – |
| Disable Buttons Color | `disableButtonsColor` | `Color` | – | – |
| Original Color | `originalColor` | `Color` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Gallery Opened | `galleryOpened` | `bool` | – | – |
| Current Capture Index | `currentCaptureIndex` | `int` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Capture List Scroll Rect | `captureListScrollRect` | `ScrollRect` | – | – |
| Capture Slot Prefab | `captureSlotPrefab` | `GameObject` | – | – |
| Scroll Bar | `scrollBar` | `Scrollbar` | – | – |
| Expanded Capture Menu | `expandedCaptureMenu` | `GameObject` | – | – |
| Expanded Capture Image | `expandedCaptureImage` | `RawImage` | – | – |
| Expand Button | `expandButton` | `Image` | – | – |
| Delete Button | `deleteButton` | `Image` | – | – |
| Custom Camera For Editor Captures | `customCameraForEditorCaptures` | `Camera` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMainSettings()` | `gameManager`を取得し、相対パス設定・キャプチャ保存フォルダ名・ファイル名を読み込む。 |
| `checkSettings()` | 未初期化なら`getDataPath`で保存先を求めて保持する。 |
| `loadCaptures()` | 保存先のPNGを作成日時順に読み込み、枚数が変わっていればスロットを作り直してテクスチャを設定する。 |
| `getSaveButtonSelected(Button button)` | 押されたボタンのキャプチャのインデックスを求め、削除/拡大ボタンの色と可否を更新する。 |
| `addCaptureSlot(int index, string fileName)` | スロットのプレハブを複製して名前とファイル名を設定し、`captureList`へ追加する。 |
| `changeButtonsColor(bool delete, bool expand)` | 削除/拡大ボタンの色を有効色か無効色へ切り替え、`canDelete`と`canExpand`も設定する。 |
| `openCaptureGallery()` | `openOrCloseCapturesGallery(true)`を呼ぶだけ。 |
| `closeCaptureGallery()` | `openOrCloseCapturesGallery(false)`を呼ぶだけ。 |
| `openOrCloseCapturesGallery(bool state)` | `galleryOpened`を設定し、開く時は読み込み、閉じる時はボタン無効化と拡大メニュー非表示を行う。 |
| `getDataPath()` | 相対パス設定に応じた保存先フォルダを作成し、末尾に`/`を付けた文字列を返す。 |
| `takeCapture(Camera currentCamera)` | カメラを`RenderTexture`へ描画して`Texture2D`化し、ランダム名のPNGとして保存して元の設定へ戻す。 |
| `takeCaptureWithCameraEditor()` | 設定を読み直した後、`customCameraForEditorCaptures`を対象に撮影処理を呼ぶ。 |
| `deleteCapture()` | 選択中で削除可能ならPNGを消し、スロット破棄・ボタン無効化・スクロール位置リセットを行う。 |
| `deleteExpandedCapture()` | 拡大表示中のキャプチャを削除し、残りがあれば次か前を拡大してスクロールをリセットする。 |
| `expandCapture()` | 選択中で拡大可能なら拡大メニューを表示し、選択キャプチャのテクスチャを設定する。 |
| `expandNextCapture()` | ギャラリー表示中のみインデックスを次へ進め、末尾なら0へ戻してテクスチャを差し替える。 |
| `expandPreviousCapture()` | ギャラリー表示中のみインデックスを前へ進め、先頭なら末尾へ回してテクスチャを差し替える。 |
| `closeExpandCaptureMenu()` | `changeButtonsColor(false, false)`でボタンを無効化するだけ。 |
| `destroyCaptureSlot(int slotIndex)` | 指定スロットのGameObjectを破棄し、リストから除去する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`を呼んでインスペクタ表示を更新する。 |

## 内部型

- `captureButtonInfo`（class）
