# attachmentInfo

- **種別**: class
- **ソース**: `Weapons/Attachments/attachmentInfo.cs:8`
- **属性**: `System.Serializable`

**概要**: 武器アタッチメント1種の名前・スロット・イベント・選択音をまとめた情報クラス。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Name | `Name` | `string` | – | – |
| Attachment Enabled | `attachmentEnabled` | `bool` | true | – |
| Attachment Active | `attachmentActive` | `bool` | – | – |
| Currently Active | `currentlyActive` | `bool` | – | – |
| Attachment Use HUD | `attachmentUseHUD` | `bool` | – | – |
| Only Enabled While Carrying | `onlyEnabledWhileCarrying` | `bool` | – | – |
| Attachment Game Object | `attachmentGameObject` | `GameObject` | – | – |
| Activate Event | `activateEvent` | `UnityEvent` | – | – |
| Deactivate Event | `deactivateEvent` | `UnityEvent` | – | – |
| Attachment Slot Manager | `attachmentSlotManager` | `attachmentSlot` | – | – |
| Select Attachment Sound | `selectAttachmentSound` | `AudioClip` | – | – |
| Select Attachment Audio Element | `selectAttachmentAudioElement` | `AudioElement` | – | – |
| Use Event On Press | `useEventOnPress` | `bool` | – | – |
| Event On Press | `eventOnPress` | `UnityEvent` | – | – |
| Use Event On Press Down | `useEventOnPressDown` | `bool` | – | – |
| Event On Press Down | `eventOnPressDown` | `UnityEvent` | – | – |
| Use Event On Press Up | `useEventOnPressUp` | `bool` | – | – |
| Event On Press Up | `eventOnPressUp` | `UnityEvent` | – | – |
| Use Event Hand Position | `useEventHandPosition` | `bool` | – | – |
| Activate Event Hand Position | `activateEventHandPosition` | `UnityEvent` | – | – |
| Deactivate Event Hand Position | `deactivateEventHandPosition` | `UnityEvent` | – | – |
| Use Attachment Hover Info | `useAttachmentHoverInfo` | `bool` | – | – |
| Attachment Hover Info | `attachmentHoverInfo` | `string` | – | TextArea (3, 10) |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `InitializeAudioElements()` | `selectAttachmentSound`があれば`selectAttachmentAudioElement.clip`に代入する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `activateEvent` | `UnityEvent` | – |
| `deactivateEvent` | `UnityEvent` | – |
| `eventOnPress` | `UnityEvent` | – |
| `eventOnPressDown` | `UnityEvent` | – |
| `eventOnPressUp` | `UnityEvent` | – |
| `activateEventHandPosition` | `UnityEvent` | – |
| `deactivateEventHandPosition` | `UnityEvent` | – |
