# weaponAttachmentSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/Attachments/weaponAttachmentSystem.cs:11`

**概要**: 武器に装着するアタッチメントの有効・選択状態と、そのUIアイコン／スロットを管理するコンポーネント。編集メニューの開閉に合わせてカメラ・IK・HUDを切り替える。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Edit Attachments Enabled | `editAttachmentsEnabled` | `bool` | true | オフにするとアタッチメント編集画面を開けなくなる。 |
| Can Edit Weapon Without Attchments | `canEditWeaponWithoutAttchments` | `bool` | true | アタッチメント未装着の武器でも編集画面を開けるようにする。 |
| Can Change Attachment With Number Keys | `canChangeAttachmentWithNumberKeys` | `bool` | true | 数字キー入力で各スロットのアタッチメントを切り替える。 |
| Use Offset Panels | `useOffsetPanels` | `bool` | – | アイコンと接続線をオフセット位置のトランスフォーム基準で表示する。 |
| Third Person Camera Movement Speed | `thirdPersonCameraMovementSpeed` | `float` | 0.8f | 三人称での編集カメラ移動速度。大きいほど速く移動する。 |
| Set Picked Attachments | `setPickedAttachments` | `bool` | true | 拾ったアタッチメントをそのまま装着状態にする。 |
| Use Smooth Transition Free Camera | `useSmoothTransitionFreeCamera` | `bool` | true | フリーカメラ時に編集画面への移行を滑らかに補間する。 |
| Use Smooth Transition Locked Camera | `useSmoothTransitionLockedCamera` | `bool` | true | ロックカメラ時に編集画面への移行を滑らかに補間する。 |

### UI Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| UI Lines Scale Multiplier | `UILinesScaleMultiplier` | `float` | 0.1f | UI接続線の長さに掛ける倍率。線の伸び方を調整する。 |
| Dual Weapon Offset Scale | `dualWeaponOffsetScale` | `float` | 0.5f | 二丁持ち時にアタッチメントアイコンへ掛ける縮小倍率。 |
| Disable HUD When Editing Attachments | `disableHUDWhenEditingAttachments` | `bool` | – | 編集画面を開いている間、武器HUDを非表示にする。 |
| Show Current Attachment Hover Info | `showCurrentAttachmentHoverInfo` | `bool` | – | カーソルを合わせたアタッチメントの説明パネルを表示する。 |

### Sound Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Start Edit Weapon Sound | `startEditWeaponSound` | `AudioClip` | – | 編集画面を開いたときに鳴らす効果音クリップ。 |
| Start Edit Weapon Audio Element | `startEditWeaponAudioElement` | `AudioElement` | – | 編集開始音の再生先や音量を持つ`AudioElement`。 |
| Stop Edit Weapon Sound | `stopEditWeaponSound` | `AudioClip` | – | 編集画面を閉じたときに鳴らす効果音クリップ。 |
| Stop Edit Weapon Audio Element | `stopEditWeaponAudioElement` | `AudioElement` | – | 編集終了音の再生先や音量を持つ`AudioElement`。 |

### Attachment State

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | アタッチメント選択処理のデバッグログを出力する。 |

### Element Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Weapon System | `weaponSystem` | `playerWeaponSystem` | – | この武器の`playerWeaponSystem`参照。HUD表示の制御に使う。 / 表示条件: `showElementSettings` がオンのとき |
| IK Weapon Manager | `IKWeaponManager` | `IKWeaponSystem` | – | `IKWeaponSystem`参照。編集カメラ位置の取得に使う。 / 表示条件: `showElementSettings` がオンのとき |
| Weapons Manager | `weaponsManager` | `playerWeaponsManager` | – | `playerWeaponsManager`参照。編集画面の開閉に使う。 / 表示条件: `showElementSettings` がオンのとき |
| Attachment Info Game Object | `attachmentInfoGameObject` | `GameObject` | – | アタッチメントアイコンのUIプレハブ。スロット生成に使う。 / 表示条件: `showElementSettings` がオンのとき |
| Attachment Slot Game Object | `attachmentSlotGameObject` | `GameObject` | – | スロットボタンのUIプレハブ。各アイコン配下に生成される。 / 表示条件: `showElementSettings` がオンのとき |
| Weapon Attachments Menu | `weaponAttachmentsMenu` | `GameObject` | – | 編集開始時に複製して表示するメニューのUIプレハブ。 / 表示条件: `showElementSettings` がオンのとき |
| Attachment Hover Info Panel Game Object | `attachmentHoverInfoPanelGameObject` | `Transform` | – | ホバー情報パネルの表示位置を決めるトランスフォーム。 / 表示条件: `showElementSettings` がオンのとき |
| Attachment Hover Info Text | `attachmentHoverInfoText` | `Text` | – | ホバー時にアタッチメント名や説明を表示する`Text`。 / 表示条件: `showElementSettings` がオンのとき |
| Weapons Camera | `weaponsCamera` | `Camera` | – | アタッチメント編集用カメラ。UI位置の計算に使う。 / 表示条件: `showElementSettings` がオンのとき |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | 各`AudioElement`に割り当てる`AudioSource`。 / 表示条件: `showElementSettings` がオンのとき |
| Remove Attachment Sound | `removeAttachmentSound` | `AudioClip` | – | アタッチメントを取り外したときの効果音クリップ。 / 表示条件: `showElementSettings` がオンのとき |
| Remove Attachment Audio Element | `removeAttachmentAudioElement` | `AudioElement` | – | 取り外し音の再生先や音量を持つ`AudioElement`。 / 表示条件: `showElementSettings` がオンのとき |

### Gizmo Options

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | アタッチメント位置の球とオフセット線を描画する。 |
| Show Dual Weapons Gizmo | `showDualWeaponsGizmo` | `bool` | – | ギズモを二丁持ち用オフセット位置へ向けて描画する。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `editingAttachments` | `bool` | – | – |
| `attachmentInfoList` | `List<attachmentPlace>` | new List<attachmentPlace> () | – |
| `showElementSettings` | `bool` | – | – |
| `usingDualWeapon` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeAttachmentSystem()` | `weaponsManager`からカメラ・キャンバス等を取得して初期化し、アクティブなら0.4秒後に初期状態を設定するコルーチンを開始する。 |
| `checkInitializeAttachmentElements()` | 未初期化なら待ち時間なしでアタッチメントの初期状態を設定するだけ。 |
| `instantiateAttachmentIcons()` | アタッチメントメニューと各アイコン・スロットのUIを生成し、名前・番号・選択状態を`attachmentInfoList`へ紐付ける。 |
| `stopUpdateCoroutine()` | 実行中の`updateCoroutine`を停止するだけ。 |
| `activateAttachmentUIPanels()` | 編集状態に応じてメニューを表示し、各アイコンのスケールと画面上の位置をカメラ投影で更新する。 |
| `openOrCloseWeaponAttachmentEditor(bool state)` | 編集状態を切り替え、一人称移行・カメラ・IK・HUDの制御、サウンド再生、メニュー生成と更新コルーチンを行う。 |
| `canUseSmoothTransition()` | カメラタイプと`useSmoothTransition`設定の組み合わせで滑らかな遷移が可能かを返すだけ。 |
| `cancelWeaponAttachmentEditor()` | 編集中なら状態を解除してIK編集とメニューを止め、カメラを元の親・位置・回転へ戻す。 |
| `checkIfAttachmentSystemInitialized()` | 未初期化で初期化処理中でもなければ`setAttachmentInitialState`を呼ぶが、開始後1秒以内は何もしない。 |
| `setAttachmentInitialState()` | 各アタッチメントの有効・選択状態を反映してGameObject表示とレイヤーを設定し、置換対象や手位置イベントを切り替える。 |
| `setAttachmentState(bool state, int attachmentInfoListIndex, int attachmentPlaceListIndex, string attachmentName)` | 指定名のアタッチメントだけを有効化し、他を解除して表示・レイヤー・選択番号・イベント・サウンドを更新する。 |
| `checkPressedAttachmentButton(Button pressedButton)` | 押されたボタンが現在の選択と同じなら何もせず、別スロットなら`setAttachmentState`で切り替えて選択アイコンを更新する。 |
| `setAttachmentsState(bool state, bool changeCurrentState)` | `onlyEnabledWhileCarrying`のアタッチメントの表示とイベントを状態に合わせ、HUDを使うものがあればパネルを有効にする。 |
| `checkAttachmentsHUD()` | 現在有効なアタッチメントがHUDを使う場合だけアタッチメントパネルを表示する。 |
| `checkAttachmentsOnDrawWeapon()` | 武器を抜いた際に現在状態を変えず`setAttachmentsState(true,false)`を呼ぶだけ。 |
| `checkAttachmentsOnKeepWeapon()` | 武器を納めた際に現在状態を変えず`setAttachmentsState(false,false)`を呼ぶだけ。 |
| `isAttachmentAlreadyActiveOnWeapon(string attachmentName)` | 指定名のアタッチメントが既に有効かを全スロット走査して返すだけ。 |
| `pickupAttachment(string attachmentName)` | 未所持の指定アタッチメントを有効化してスロットとアイコンを表示し、設定に応じて即選択してtrueを返す。 |
| `enableAllAttachments()` | 全アタッチメント名について`pickupAttachment`を呼び、すべて取得状態にする。 |
| `playSound(AudioElement sound)` | `AudioElement`がnullでなければピッチを確認して`AudioPlayer`で1ショット再生するだけ。 |
| `setAdjustThirdPersonCameraActiveState(bool state)` | 三人称カメラ調整の有効フラグを設定するだけ。 |
| `adjustThirdPersonCamera()` | 調整が有効なら実行中のカメラ移動を止め、三人称アタッチメント用カメラ位置へ移動するコルーチンを開始する。 |
| `canBeOpened()` | 編集が許可され、IK武器がアタッチメント対応で、編集可または装着済みの場合のみtrueを返す。 |
| `enableOrDisableAllAttachmentPlaces(bool value)` | 全アタッチメントプレイスの有効フラグを一括設定してコンポーネントを更新するだけ。 |
| `enableOrDisableAllAttachment(bool value, int attachmentPlaceIndex)` | 指定プレイス内の全アタッチメントの有効フラグを一括設定してコンポーネントを更新するだけ。 |
| `useEventOnPress()` | 有効かつ選択中のアタッチメントの`eventOnPress`を順に発火する。 |
| `useEventOnPressDown()` | 有効かつ選択中のアタッチメントの`eventOnPressDown`を順に発火する。 |
| `useEventOnPressUp()` | 有効かつ選択中のアタッチメントの`eventOnPressUp`を順に発火する。 |
| `setSecondaryWeaponAttachmentSystem(weaponAttachmentSystem newAttachment)` | 二丁持ち用の相手側アタッチメントシステム参照を設定するだけ。 |
| `setUsingDualWeaponState(bool state)` | 二丁持ち状態のフラグを設定するだけ。 |
| `assignWeaponToAttachment(IKWeaponSystem newIKWeaponSystem)` | `IKWeaponSystem`を登録して武器管理・武器システムを取得し、UI参照を割り当ててコンポーネントを更新する。 |
| `removeWeaponFromAttachment()` | 保持しているIK武器と武器システムの参照をnullにしてコンポーネントを更新するだけ。 |
| `assignWeaponAttachmentUI()` | プレイヤーの`weaponsAttachmentUIManager`からメニュー・アイコン・スロット・ホバーパネル・武器カメラの参照を取得する。 |
| `getPersistanceAttachmentWeaponInfoList()` | 各プレイスの有効状態と各アタッチメントの有効・選択状態を永続化用リストに詰め替えて返す。 |
| `initializeAttachmentValues(List<persistanceWeaponAttachmentPlaceInfo> weaponAttachmentList)` | 永続化リストの値でプレイスとアタッチメントの有効・選択状態を上書き復元する。 |

## 内部型

- `attachmentPlace`（class）
