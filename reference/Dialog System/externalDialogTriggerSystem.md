# externalDialogTriggerSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Dialog System/externalDialogTriggerSystem.cs:5`

**概要**: 外部から既存の `dialogContentSystem` のダイアログを開始するトリガー。対象キャラクターやプレイヤーを指定し、`electronicDevice` 経由で会話を開始する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Dialog Index | `setNewDialogIndex` | `bool` | – | – |
| New Dialog Index | `newDialogIndex` | `int` | – | – |
| Check Dialog Content System ID | `checkDialogContentSystemID` | `bool` | – | – |
| ID To Check | `IDToCheck` | `int` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Dialog Content System | `mainDialogContentSystem` | `dialogContentSystem` | – | – |
| Main Electronic Device | `mainElectronicDevice` | `electronicDevice` | – | – |

### Set Object Manually Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Assign Object Manually | `assignObjectManually` | `bool` | – | – |
| Player To Configure | `playerToConfigure` | `GameObject` | – | – |
| Search Player On Scene If Not Assigned | `searchPlayerOnSceneIfNotAssigned` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateDialogByCharacter(GameObject newCharacter)` | `characterDialogContentSystem` から内容とデバイスを取り、ID 一致時のみ開始する。 |
| `activateDialog()` | 手動指定時はプレイヤーの有無を確認・検索し、問題なければ `startDialog` を呼ぶ。 |
| `activateDialogToPlayer(GameObject playerToCheck)` | `playerToCheck` を対象プレイヤーに設定し、`startDialog` を呼ぶ。 |
| `findPlayerOnScene()` | `searchPlayerOnSceneIfNotAssigned` 有効時、シーンのメインプレイヤーを対象に設定する。 |
