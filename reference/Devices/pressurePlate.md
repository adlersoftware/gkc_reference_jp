# pressurePlate

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Devices/pressurePlate.cs:6`

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Min Distance | `minDistance` | `float` | – | – |
| Tags To Ignore | `tagsToIgnore` | `List<string>` | new List<string>{ "Player" } | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Unlock Function Call | `unlockFunctionCall` | `UnityEvent` | new UnityEvent () | – |
| Lock Function Call | `lockFunctionCall` | `UnityEvent` | new UnityEvent () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Using Plate | `usingPlate` | `bool` | – | – |
| Active Function Called | `activeFunctionCalled` | `bool` | – | – |
| Disable Function Called | `disableFunctionCalled` | `bool` | – | – |
| Objects | `objects` | `List<GameObject>` | new List<GameObject> () | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Plate | `plate` | `GameObject` | – | – |
| Final Position | `finalPosition` | `Transform` | – | – |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `unlockFunctionCall` | `UnityEvent` | – |
| `lockFunctionCall` | `UnityEvent` | – |
