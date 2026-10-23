# characterModelListManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Character Builder/characterModelListManager.cs:6`

**概要**: キャラクターモデルをリストから差し替えるコンポーネント。ID・名前・前後移動で選択し、BuildPlayer 経由でモデルの再構築、装備、身長、ラグドール設定を更新する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Character Model Name | `currentCharacterModelName` | `string` | – | – |
| Character Model Info List | `characterModelInfoList` | `List<characterModelInfo>` | new List<characterModelInfo> () | – |
| Set Character Model On Start | `setCharacterModelOnStart` | `bool` | – | – |
| Character Model On Start Name | `characterModelOnStartName` | `string` | – | – |
| Use Random Character Model On Start | `useRandomCharacterModelOnStart` | `bool` | – | – |
| Ignore Set Initial Armor Cloth Set On Change Model | `ignoreSetInitialArmorClothSetOnChangeModel` | `bool` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Current Character Model Index | `currentCharacterModelIndex` | `int` | – | – |
| Current Character Model ID | `currentCharacterModelID` | `int` | – | – |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Event On Replace Character Model | `useEventOnReplaceCharacterModel` | `bool` | – | – |
| Event On Replace Character Model | `eventOnReplaceCharacterModel` | `UnityEvent` | – | – |
| Use Event To Send Current Character Model Selected | `useEventToSendCurrentCharacterModelSelected` | `bool` | – | – |
| Event To Send Current Character Model Selected | `eventToSendCurrentCharacterModelSelected` | `eventParameters.eventToCallWithGameObject` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Build Player | `mainBuildPlayer` | `buildPlayer` | – | – |
| Main Body Mount Points System | `mainBodyMountPointsSystem` | `bodyMountPointsSystem` | – | – |
| Original Runtime Animator Controller | `originalRuntimeAnimatorController` | `RuntimeAnimatorController` | – | – |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Main Player Components Manager | `mainPlayerComponentsManager` | `playerComponentsManager` | – | – |
| Main Ragdoll Builder | `mainRagdollBuilder` | `ragdollBuilder` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `getCurrentCharacterModelID()` | プレイヤーがいればそのモデルID、なければ `currentCharacterModelID` を返す。 |
| `replaceCharacterModelByID(int id)` | IDが一致するモデルを探し、その名前で `replaceCharacterModel` を呼ぶ。 |
| `replaceCharacterModel()` | `currentCharacterModelName` を引数に `replaceCharacterModel` を呼ぶだけ。 |
| `replaceCharacterModel(string name)` | 同名なら中止し、旧モデルのイベント、生成、Animator・ボーン・装備・身長の更新、各種イベントを行う。 |
| `setNextCharacterModel()` | `setNextOrPreviousCharacterModel(true)` を呼ぶだけ。 |
| `setPreviousCharacterModel()` | `setNextOrPreviousCharacterModel(false)` を呼ぶだけ。 |
| `setNextOrPreviousCharacterModel(bool state)` | インデックスを前後へ循環させ、名前で `replaceCharacterModel` を呼ぶ。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnReplaceCharacterModel` | `UnityEvent` | – |

## 内部型

- `characterModelInfo`（class）
