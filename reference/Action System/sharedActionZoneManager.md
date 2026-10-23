# sharedActionZoneManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Action System/Shared Action System/sharedActionZoneManager.cs:6`

**概要**: シーン内の共有アクションゾーンを一覧管理するコンポーネント。ゾーン全体の有効状態とゾーンリストを保持する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shared Action Zones Enabled | `sharedActionZonesEnabled` | `bool` | true | – |

### Shared Action Zone Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shared Action Zone List | `sharedActionZoneList` | `List<sharedActionZone>` | new List<sharedActionZone> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isSharedActionZonesEnabled()` | `sharedActionZonesEnabled`の値を返すだけ。 |
| `getSharedActionZoneList()` | `sharedActionZoneList`を返すだけ。 |
| `setSharedActionZonesEnabledState(bool state)` | `sharedActionZonesEnabled`に`state`を設定するだけ。 |
| `getAllSharedActionZonesOnScene()` | シーン上の全`sharedActionZone`を集めてリストを再構築し、シーンを更新する。 |
