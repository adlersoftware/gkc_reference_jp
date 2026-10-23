# objectStatsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Stats System/Objects Stats/objectStatsSystem.cs:6`

**概要**: オブジェクト固有のステータスを`statInfoList`で持ち、読み込み時初期化とセーブ用の値取得/設定イベントを提供する。主人公側の`objectsStatsSystem`に登録される。

## インスペクター設定

### Stats Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Object Name | `objectName` | `string` | – | – |
| Use Stats | `useStats` | `bool` | – | – |
| Load Stats Delay | `loadStatsDelay` | `float` | – | – |
| Stat Info List | `statInfoList` | `List<statInfo>` | new List<statInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Character Located | `characterLocated` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Character Game Object | `mainCharacterGameObject` | `GameObject` | – | – |
| Main Object Stats Info Template | `mainObjectStatsInfoTemplate` | `objectStatsInfoTemplate` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addObjectStatsToMainManager()` | 主人公を確認し、その`objectsStatsSystem`へ自身を追加する。 |
| `setMainCharacterGameObject(GameObject newObject)` | `mainCharacterGameObject`を差し替えるだけ。 |
| `checkMainCharacterGameObject()` | 未取得なら探索し、`characterLocated`をその有無に合わせて更新する。 |
| `getMainCharacterGameObject()` | 本体が空のvirtualメソッドで、派生クラスが主人公を設定する。 |
| `checkStatsStateOnLoad()` | `useStats`が有効なら、`loadStatsDelay`の有無で即時または遅延の読み込み時設定を行う。 |
| `setStatsOnLoadWithDelay()` | `loadStatsDelay`秒待ってから`setStatsOnLoad`を呼ぶコルーチンを開始する。 |
| `setStatsOnLoad()` | 各`statInfo`の初期化イベントを、数値またはboolの値付きで発火する。 |
| `setCurrentStatNameToSave(string newValue)` | 保存対象のステータス名`currentStatNameToCheck`を設定するだけ。 |
| `setCurrentFloatValueToSave(float newValue)` | 保存対象名に一致するステータスの`currentFloatValue`を更新し、見つかれば終了する。 |
| `setCurrentBoolValueToSave(bool newValue)` | 保存対象名に一致するステータスの`currentBoolState`を更新し、見つかれば終了する。 |
| `checkEventOnStatsSave()` | 各ステータス名を保存対象に設定しながら、数値取得またはbool取得イベントを順に発火する。 |

## 内部型

- `statInfo`（class）
