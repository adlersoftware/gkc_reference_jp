# buildPlayer

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Player/Character Builder/buildPlayer.cs:7`

**概要**: キャラクターモデルの差し替え（ビルド）と、テンプレート化された設定リスト（AI種別、敵/中立、武器など）を新キャラクターへ適用するエディタ/ランタイム両用のビルダー。

**公式ドキュメント抜粋**（[Build Player](../../docs/character-level-components/character/build-player.md)）

> It is used for the character creator wizard when a new character or player is configured, in order to place and tweak the new model as a new character. It is also where the “Manual Character Creator is located”, you can see more of this in this doc.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Place New Character Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Place New Character On Scene Center Enabled | `placeNewCharacterOnSceneCenterEnabled` | `bool` | true | ONにすると新キャラをシーン中心に置き、カメラをその正面へ移動する。 |
| Layer To Place NPC | `layerToPlaceNPC` | `LayerMask` | – | シーン中心を使わない時、エディタカメラのレイで配置する対象レイヤー。 |
| Main Chest Mount Point Name | `mainChestMountPointName` | `string` | "Chest" | 胸ボーンを登録するボーンマウントポイントの名前。 |

### Build Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Build Player Type | `buildPlayerType` | `bool` | – | ONにすると新モデルをプレイヤーとして構築し、各種マネージャーを追加する。 |
| Has Weapons Enabled | `hasWeaponsEnabled` | `bool` | – | ONにすると構築時に武器リストを有効のままにする。 |
| Clear Old Weak Spot List On Create New Character Enabled | `clearOldWeakSpotListOnCreateNewCharacterEnabled` | `bool` | – | ONにすると作成時に旧モデルの弱点リストを消去する。 |

### Build Player Manually

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Assign New Model Manually | `assignNewModelManually` | `bool` | – | ONにするとボーンを自動検索せず、手動指定したボーンを使う。 |
| Explanation | `explanation` | `string` | "Drop on the scene the model prefab f… | 手動ビルドの手順を示すエディタ表示用の説明文。処理には影響しない。 / 表示条件: `assignNewModelManually` がオンのとき / TextArea (5, 15) |
| New Character Model | `newCharacterModel` | `GameObject` | – | 差し替える新しいキャラクターモデルのプレハブ。 / 表示条件: `assignNewModelManually` がオンのとき |
| Head | `head` | `Transform` | – | 新モデルの頭ボーン。頭トラッキングの対象に設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Neck | `neck` | `Transform` | – | 新モデルの首ボーン。未設定なら頭の親から自動取得する。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Chest | `chest` | `Transform` | – | 新モデルの胸ボーン。武器の親や上半身回転の基準に設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Spine | `spine` | `Transform` | – | 新モデルの背骨ボーン。上半身回転システムに設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Right Lower Arm | `rightLowerArm` | `Transform` | – | 新モデルの右前腕ボーン。ボーン参照の更新に使用する。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Left Lower Arm | `leftLowerArm` | `Transform` | – | 新モデルの左前腕ボーン。ボーン参照の更新に使用する。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Right Hand | `rightHand` | `Transform` | – | 新モデルの右手ボーン。武器の右手の親として設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Left Hand | `leftHand` | `Transform` | – | 新モデルの左手ボーン。武器の左手の親として設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Right Lower Leg | `rightLowerLeg` | `Transform` | – | 新モデルの右下腿ボーン。IKフットの脚情報に設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Left Lower Leg | `leftLowerLeg` | `Transform` | – | 新モデルの左下腿ボーン。IKフットの脚情報に設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Right Foot | `rightFoot` | `Transform` | – | 新モデルの右足ボーン。IKフットの脚情報に設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Left Foot | `leftFoot` | `Transform` | – | 新モデルの左足ボーン。IKフットの脚情報に設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Right Toes | `rightToes` | `Transform` | – | 新モデルの右つま先ボーン。IKフットの脚情報に設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Left Toes | `leftToes` | `Transform` | – | 新モデルの左つま先ボーン。IKフットの脚情報に設定される。 / 表示条件: `assignNewModelManually.boolValue && newCharacterModel.objectReferenceValue` |
| Apply Character Settings On Manual Build | `applyCharacterSettingsOnManualBuild` | `bool` | – | ONにすると手動ビルド時にもキャラクター設定リストを適用する。 / 表示条件: `assignNewModelManually` がオンのとき |

### Update Spine and Chest Bones

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Set New Spine And Chest Bones Manually | `setNewSpineAndChestBonesManually` | `bool` | – | ONにすると下記の胸・背骨ボーンで既存キャラの参照を更新する。 |
| Chest | `chest` | `Transform` | – | 新モデルの胸ボーン。武器の親や上半身回転の基準に設定される。 / 表示条件: `setNewSpineAndChestBonesManually` がオンのとき |
| Spine | `spine` | `Transform` | – | 新モデルの背骨ボーン。上半身回転システムに設定される。 / 表示条件: `setNewSpineAndChestBonesManually` がオンのとき |

### Settings Searcher

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Setting To Search | `objectSearcherName` | `string` | "" | 設定リストを名前で絞り込む検索文字列。 |

### Save/Load Settings List To File

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| New Character Settings Template | `newCharacterSettingsTemplate` | `characterSettingsTemplate` | – | 設定リストの保存・読み込みに使うキャラクターテンプレート。 |

### Create New Character Template Data

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character Template ID | `characterTemplateID` | `int` | 0 | テンプレートの識別ID。読み込み時に現在のIDと一致するか確認する。 |
| Character Template Data Path | `characterTemplateDataPath` | `string` | "Assets/Game Kit Controller/Scriptabl… | テンプレートを新規作成する保存先フォルダのパス。 / TextArea (2, 3) |
| Character Template Name | `characterTemplateName` | `string` | "New Template" | 新規作成するテンプレートのアセット名。 |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Create Player | `eventOnCreatePlayer` | `UnityEvent` | – | キャラクター構築完了時に呼ばれるイベント。 |
| Event To Send New Player Model | `eventToSendNewPlayerModel` | `eventParameters.eventToCallWithGameObject` | – | 構築した新キャラクターモデルを引数で渡すイベント。 |

### Character Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player | `player` | `GameObject` | – | 構築対象のプレイヤー（またはAI）のルートGameObject。 / 表示条件: `showElements` がオンのとき |
| Grab Physical Object | `grabPhysicalObject` | `GameObject` | – | 構築後にキャラクター情報を設定する物理オブジェクト掴みシステム。 / 表示条件: `showElements` がオンのとき |
| Current Character Model | `currentCharacterModel` | `GameObject` | – | 現在使用中のモデル。構築時に破棄され新モデルに置き換わる。 / 表示条件: `showElements` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `hips` | `Transform` | – | – |
| `settingsInfoCategoryList` | `List<settingsInfoCategory>` | new List<settingsInfoCategory> () | – |
| `temporalSettingsInfoList` | `List<settingsInfo>` | new List<settingsInfo> () | – |
| `characterSettingToConfigureIfAIIsEnemy` | `string` | "AI Is Enemy" | – |
| `characterSettingToConfigureIfAIIsNeutral` | `string` | "AI Is Neutral" | – |
| `characterSettingToConfigureFollowFactionPartnerOnTrigger` | `string` | "Follow Faction Partner On Trigger" | – |
| `characterSettingToConfigureAIType` | `string` | "AI Type" | – |
| `characterSettingsTemplateInfoList` | `List<characterSettingsTemplateInfo>` | new List<characterSettingsTemplateInf… | – |
| `characterBodyElementsList` | `List<characterBodyElements>` | new List<characterBodyElements> () | – |
| `objectSearchResultList` | `List<int>` | new List<int> () | – |
| `searchObjectsActive` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setNewCharacterModelToReplaceInRuntime(GameObject newObject)` | nullでなければ `newCharacterModel` に設定するだけ。 |
| `buildCharacterInRuntime()` | ランタイム差し替え用フラグを立てて `buildCharacter` を呼び、設定適用とプレハブ展開を抑制する。 |
| `checkElementsBeforeReplacingCharacterModelInRuntime()` | 再生中なら `GKC_Utils.checkPlayerStates` でプレイヤー状態を整える。 |
| `checkElementsAfterReplacingCharacterModelInRuntime()` | 再生中なら武器の位置と親をリセットし、上半身回転値の再計算と武器親の更新を行う。 |
| `buildCharacterByButton()` | 手動ビルド設定に応じて設定適用を省略し、プレハブ展開後に `buildCharacter` を呼ぶ。 |
| `setCheckUnpackCharacterPrefabActiveState(bool state)` | `checkUnpackCharacterPrefabActive` を設定するだけ。 |
| `setCharacterSettingsStatus(bool characterHasBeenPreInstantiatedOnEditorValue, bool characterIsAI, bool configuredAsEnemy, bool configuredAsNeutral, string newTemplateNameToApply, bool useTemplateListValue)` | プリインスタンス済みか、AIか、敵/中立か、テンプレート名、テンプレートリスト使用か、の設定状態をまとめて保持する。 |
| `setCharacterVariables(bool characterIsPlayerType, bool hasWeapons, bool characterIsInstantiated, GameObject newModel)` | プレイヤー種別、武器有無、インスタンス化済みか、新モデルをまとめて設定する。 |
| `setCharacterBones(Transform newHead, Transform newNeck, Transform newChest, Transform newSpine, Transform newHips, Transform newRightLowerArm, Transform newLeftLowerArm, Transform newRightHand, Transform newLeftHand, Transform newRightLowerLeg, Transform newLeftLowerLeg, Transform newRightFoot, Transform newLeftFoot, Transform newRightToes, Transform newLeftToes)` | 頭・首・胸・腰・腕・脚など15個のボーン参照をまとめて設定するだけ。 |
| `getCharacterBones()` | 新モデルのAnimatorからHumanoidボーンを取得し、見つからない場合は警告を出力する。 |
| `checkAllBonesFound()` | 必要な15個のボーンがすべて非nullかどうかを返す。 |
| `buildCharacter()` | ボーン確認後、新モデルへ各要素を再設定し、旧モデルを破棄または無効化してイベントを発火する。 |
| `setNewSpineAndChestBones()` | 設定済みのspine/chestを上半身回転・武器・IKへ再適用し、コンポーネントを更新する。 |
| `setCustomChestUpVectorValue(Vector3 newValue)` | 値を保持し、`-Vector3.one` 以外なら次回ビルド時の適用フラグを立てる。 |
| `getPlayerGameObject()` | `player` を返すだけ。 |
| `setCharacterValuesAndAdjustSettingsExternally(bool characterHasBeenPreInstantiatedOnEditorValue, bool characterIsAI, bool configuredAsEnemy, bool configuredAsNeutral, string newTemplateNameToApply, bool useTemplateListValue, bool characterIsPlayerType, bool hasWeapons, bool characterIsInstantiated)` | 設定状態と各種変数をまとめて設定した後、`adjustSettings` を呼ぶ。 |
| `adjustSettings()` | AIかテンプレート使用時に敵・中立などを反映し、カテゴリごとに `adjustSettingsFromList` で設定を適用する。 |
| `setCharacterIsEnemyAndNeutralAIValueExternally(bool isEnemyAIValue, bool isNeutralAIValue)` | 設定リスト内の敵/中立の値を書き換え、コンポーネントとシーンを更新する。 |
| `adjustSettingsFromList(List<settingsInfo> settingsList)` | 有効な設定ごとにbool/float/string/vector3/通常値のイベントを発火し、最後にシーンをダーティにする。 |
| `adjustSettingsFromEditor()` | `temporalSettingsInfoList` の値をカテゴリ設定へコピーし適用して更新する。 |
| `adjustSingleSettingsFromEditor(int currentIndex)` | 指定indexの設定だけをカテゴリへコピーして適用し、更新して処理を終える。 |
| `setTemporalSettingsInfoList()` | カテゴリ設定の複製を作って `temporalSettingsInfoList` に詰め直し、更新する。 |
| `clearTemporalSettingsInfoList()` | `temporalSettingsInfoList` を空にしてコンポーネントを更新する。 |
| `saveSettingsListToFile()` | `newCharacterSettingsTemplate` に現在の設定カテゴリをIDごとコピーして保存する。 |
| `loadSettingsListFromFile()` | テンプレートのカテゴリと設定を名前で照合して現在の設定へコピーし、一時リストを更新する。 |
| `createSettingsListTemplate()` | `GKC_Utils.createSettingsListTemplate` にパス・名前・ID・設定リストを渡すだけ。 |
| `setTemplateFromListAsCurrentToApply(int templateIndex)` | 指定indexのテンプレートを現在のテンプレートにして読み込み、コンポーネントを更新する。 |
| `setTemplateFromListAsCurrentToApplyOnCharacterCreatorEditor(int templateIndex)` | `setTemplateFromListAsCurrentToApply` をそのまま呼ぶだけ。 |
| `setTemplateFromListAsCurrentToApplyByName(string templateName)` | 名前一致のindexを探して `setTemplateFromListAsCurrentToApply` を呼ぶ。 |
| `clearObjectsSearcResultList()` | 検索結果リストと検索文字列・検索中フラグをクリアして更新する。 |
| `showObjectsBySearchName()` | `objectSearcherName` を含む設定名のindexを `objectSearchResultList` に集める。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnCreatePlayer` | `UnityEvent` | – |

## 内部型

- `settingsInfoCategory`（class）
- `settingsInfo`（class）
- `characterSettingsTemplateInfo`（class）
- `characterBodyElements`（class）
