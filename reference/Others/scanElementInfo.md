# scanElementInfo

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/scanElementInfo.cs:10`
- **属性**: `System.Serializable`

**概要**: スキャン対象の情報を`dataBase.txt`へ保存・削除し、既読状態を管理する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Data Object | `dataObject` | `elementInfo` | – | – |
| Data Game Object | `dataGameObject` | `GameObject` | – | – |
| Use Custom Scan Speed | `useCustomScanSpeed` | `bool` | – | – |
| Custom Scan Speed | `customScanSpeed` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Object Scanned | `objectScanned` | `bool` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event Function | `useEventFunction` | `bool` | – | – |
| Event Function | `eventFunction` | `UnityEvent` | new UnityEvent () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `saveElement()` | 未スキャンなら既存データベースを読み、`dataObject`に連番`id`を振って追記保存し`objectScanned`を立てる。 |
| `removeELement()` | データベースから`dataObject.id`と一致する要素を削除して保存し、既読状態と`id`をリセットする。 |
| `isScanned()` | `dataObject.read`をそのまま返すだけ。 |
| `scanObject()` | `dataObject.read`を`true`にし、イベントが設定されていれば`eventFunction`を発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventFunction` | `UnityEvent` | – |

## 内部型

- `elementInfo`（class）
