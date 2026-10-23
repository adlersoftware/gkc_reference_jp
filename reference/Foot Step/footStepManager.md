# footStepManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Foot Step/footStepManager.cs:7`

**概要**: 足音の種類（地形テクスチャやサーフェス名）ごとに効果音・足跡・パーティクル・ノイズを再生し、足音状態リストで音量や状態遷移を制御するマネージャー。

**公式ドキュメント抜粋**（[Foot Step Manager](../../docs/player-controller-components/player-controller/foot-step-manager.md)）

> Used to detect the current surface where the character is located and play different sounds, particles, and footprints over it, including terrains, and configure different states, for a walk, run, crouch, etc… in order to configure different volumes for the steps and noise values for the AI.

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Use Footstep Setting

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Steps Enabled | `stepsEnabled` | `bool` | true | 足音システム全体の有効/無効。オフだと足音判定を行わない。 |
| Sounds Enabled | `soundsEnabled` | `bool` | – | 足音クリップの再生を有効にする。オフでも足跡は生成される。 |

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Type Of Foot Step | `typeOfFootStep` | `footStepType` | – | 検出方法。`triggers`は足トリガー、`raycast`は地面レイキャスト。 / 表示条件: `stepsEnabled` がオンのとき |
| Layer | `layer` | `LayerMask` | – | 地面判定レイキャストと足跡設置の対象レイヤー。 / 表示条件: `stepsEnabled` がオンのとき |
| Left Foot | `leftFoot` | `GameObject` | – | 左足のGameObject。足跡やパーティクルの位置に使う。 / 表示条件: `stepsEnabled` がオンのとき |
| Right Foot | `rightFoot` | `GameObject` | – | 右足のGameObject。足跡やパーティクルの位置に使う。 / 表示条件: `stepsEnabled` がオンのとき |
| Default Surface Name | `defaultSurfaceName` | `string` | "Concrete" | `footStepSurfaceSystem`が無い面で使う既定のサーフェス名。 / 表示条件: `stepsEnabled` がオンのとき |
| Use Pooling System Enabled | `usePoolingSystemEnabled` | `bool` | true | 足跡とパーティクルを`GKC_PoolingSystem`で生成する。 / 表示条件: `stepsEnabled` がオンのとき |
| Main Noise Mesh Manager Name | `mainNoiseMeshManagerName` | `string` | "Noise Mesh Manager" | ノイズメッシュマネージャーを識別する名前。既定のまま使用する。 / 表示条件: `stepsEnabled` がオンのとき |

### General Volume Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Feet Volume Range Clamps | `useFeetVolumeRangeClamps` | `bool` | – | 足音の音量を`feetVolumeRangeClamps`の範囲に制限する。 / 表示条件: `stepsEnabled` がオンのとき |
| Feet Volume Range Clamps | `feetVolumeRangeClamps` | `Vector2` | new Vector2 (0.8f, 1.2f) | 足音音量の最小値と最大値。ランダム音量のクランプに使う。 / 表示条件: `stepsEnabled.boolValue && useFeetVolumeRangeClamps.boolValue` |

### Foot Prints Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Foot Prints | `useFootPrints` | `bool` | – | 足跡オブジェクトを地面に生成する。 / 表示条件: `stepsEnabled` がオンのとき |
| Use Foot Prints From States | `useFootPrintsFromStates` | `bool` | – | フットステップ（面）ごとに足跡プレハブを切り替える。 / 表示条件: `stepsEnabled.boolValue && useFootPrints.boolValue` |
| Right Foot Print | `rightFootPrint` | `GameObject` | – | 右足用に生成する足跡プレハブ。 / 表示条件: `useFootPrints.boolValue && !useFootPrintsFromStates.boolValue` |
| Left Foot Print | `leftFootPrint` | `GameObject` | – | 左足用に生成する足跡プレハブ。 / 表示条件: `useFootPrints.boolValue && !useFootPrintsFromStates.boolValue` |
| Max Foot Print Distance | `maxFootPrintDistance` | `float` | – | 足跡を置くレイキャストの最大距離。これより遠い面には置かない。 / 表示条件: `stepsEnabled.boolValue && useFootPrints.boolValue` |
| Distance Between Prints In Fisrt Person | `distanceBetweenPrintsInFisrtPerson` | `float` | – | 一人称視点で足跡を中心から左右にずらす距離。 / 表示条件: `stepsEnabled.boolValue && useFootPrints.boolValue` |
| Use Foot Print Max Amount | `useFootPrintMaxAmount` | `bool` | – | 足跡の最大数を制限し、古いものから削除する。 / 表示条件: `stepsEnabled.boolValue && useFootPrints.boolValue` |
| Foot Print Max Amount | `footPrintMaxAmount` | `int` | – | シーンに残す足跡の最大数。古いものから削除される。 / 表示条件: `useFootPrints.boolValue && useFootPrintMaxAmount.boolValue` |
| Remove Foot Prints In Time | `removeFootPrintsInTime` | `bool` | – | 一定時間後に足跡をまとめて削除する（非プーリング時）。 / 表示条件: `stepsEnabled.boolValue && useFootPrints.boolValue` |
| Time To Remove Foot Prints | `timeToRemoveFootPrints` | `float` | – | 足跡をまとめて削除するまでの秒数。 / 表示条件: `useFootPrints.boolValue && removeFootPrintsInTime.boolValue` |
| Vanish Foot Prints | `vanishFootPrints` | `bool` | – | 足跡を`fadeObject`で徐々に消す。 / 表示条件: `stepsEnabled.boolValue && useFootPrints.boolValue` |
| Vanish Speed | `vanishSpeed` | `float` | – | `fadeObject`で足跡が消える速さ。 / 表示条件: `useFootPrints.boolValue && vanishFootPrints.boolValue` |

### Foot Particles Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Foot Particles | `useFootParticles` | `bool` | – | 足元にパーティクルを生成する。 / 表示条件: `stepsEnabled` がオンのとき |
| Use Foot Particles From States | `useFootParticlesFromStates` | `bool` | – | フットステップ（面）ごとにパーティクルを切り替える。 / 表示条件: `stepsEnabled.boolValue && useFootParticles.boolValue` |
| Foot Particles | `footParticles` | `GameObject` | – | 足元に生成するパーティクルのプレハブ。 / 表示条件: `useFootParticles.boolValue && !useFootParticlesFromStates.boolValue` |

### Footstep Noise State List

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Foot Step State List | `useFootStepStateList` | `bool` | – | 足音の状態リストを使い、間隔や音量を状態ごとに変える。 / 表示条件: `stepsEnabled` がオンのとき |
| Current Foot Step State Name | `currentFootStepStateName` | `string` | – | 開始時に適用する足音状態の名前。 / 表示条件: `stepsEnabled.boolValue && useFootStepStateList.boolValue` |
| Noise Detection Layer | `noiseDetectionLayer` | `LayerMask` | – | 足音のノイズを検知させるAIのレイヤーマスク。 / 表示条件: `stepsEnabled.boolValue && useFootStepStateList.boolValue` |
| Use Noise On Steps Enabled | `useNoiseOnStepsEnabled` | `bool` | true | 足音の発生時にAIへノイズを通知する。 / 表示条件: `stepsEnabled` がオンのとき |
| Use Noise Mesh | `useNoiseMesh` | `bool` | true | 足音でノイズメッシュを生成するかの全体スイッチ。 / 表示条件: `stepsEnabled` がオンのとき |
| Show Noise Detection Gizmo | `showNoiseDetectionGizmo` | `bool` | – | ノイズ検知範囲をデバッグ線で表示する。 / 表示条件: `stepsEnabled` がオンのとき |

### Player Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Manager | `playerManager` | `playerController` | – | プレイヤーコントローラー参照。接地や移動状態の判定に使う。 / 表示条件: `stepsEnabled` がオンのとき |
| Left Foot Step | `leftFootStep` | `footStep` | – | 左足の`footStep`コンポーネント。音量範囲の設定に使う。 / 表示条件: `stepsEnabled` がオンのとき |
| Right Foot Step | `rightFootStep` | `footStep` | – | 右足の`footStep`コンポーネント。音量範囲の設定に使う。 / 表示条件: `stepsEnabled` がオンのとき |
| Left Foot Collider | `leftFootCollider` | `Collider` | – | 左足のコライダー。足音の有効/無効切替で制御する。 / 表示条件: `stepsEnabled` がオンのとき |
| Right Foot Collider | `rightFootCollider` | `Collider` | – | 右足のコライダー。足音の有効/無効切替で制御する。 / 表示条件: `stepsEnabled` がオンのとき |
| Camera Audio Source | `cameraAudioSource` | `AudioSource` | – | 足音を再生する`AudioSource`。 / 表示条件: `stepsEnabled` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `footStepStateList` | `List<footStepState>` | new List<footStepState> () | – |
| `defaultGroundFootStepState` | `string` | "Walking" | – |
| `footSteps` | `footStepsLayer[]` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `changeFootStespType(bool state)` | レイキャスト方式なら強制的に無効化し、左右の足オブジェクトの表示と`usingAnimator`を`state`に合わせる。 |
| `GetMainTexture(Vector3 playerPos)` | 地形のアルファマップから、`playerPos`の位置で最も比重の大きいテクスチャのインデックスを返す。 |
| `getSound(Vector3 pos, GameObject ground, footStep.footType footSide)` | 地面に合う足音を選んで足跡・パーティクル・ノイズを出し、音を返す。見つからなければ`null`。 |
| `placeFootPrint(footStep.footType footSide, int footStepIndex)` | 足の位置からレイキャストし、地面に合った足跡を生成する。`footStepIndex`で状態別の足跡を選ぶ。 |
| `createFootPrint(GameObject foot, Vector3 position, Quaternion rotation, Vector3 normal, Transform currentSurfaceParent)` | 足跡をプールか生成で出現させ、`normal`に合わせて向きを直し、親設定・フェード・最大数削除を行う。 |
| `createParticles(footStep.footType footSide, int footStepIndex)` | 対応する足の位置にパーティクルを生成し、状態別の設定があればそれを優先して使う。 |
| `enableOrDisableFootSteps(bool state)` | 左右の足コライダーの有効状態を`state`に設定するだけ。 |
| `enableOrDisableFootStepsWithDelay(bool state, float delayAmount)` | 左右の`footStep`に、`delayAmount`秒後の有効/無効切り替えを依頼する。 |
| `enableOrDisableFootStepsComponents(bool state)` | 左右の`footStep`コンポーネントの有効状態を`state`に設定するだけ。 |
| `setRightFootStep(GameObject rigth)` | 右足オブジェクト`rightFoot`を設定するだけ。 |
| `setLeftFootStep(GameObject left)` | 左足オブジェクト`leftFoot`を設定するだけ。 |
| `setDefaultGroundFootStepState()` | 既定の地面足音状態名`defaultGroundFootStepState`で`setFootStepState`を呼ぶだけ。 |
| `setFootStepState(string stateName)` | 名前一致の状態をカレントにし、左右の音量範囲を更新して、設定があれば遅延遷移も予約する。 |
| `setNewFootStepStateAfterDelay(string newState, float delayAmount)` | 既存の遅延コルーチンを止め、`delayAmount`秒後に`newState`へ切り替えるコルーチンを開始する。 |
| `stopSetNewFootStepStateAfterDelayCoroutine()` | 足音状態の遅延切り替えコルーチンが存在すれば停止するだけ。 |
| `isDelayToNewStateActive()` | 足音状態の遅延切り替えが実行中かどうかを返すだけ。 |
| `setUseNoiseMeshState(bool state)` | ノイズメッシュを使うかどうかの`useNoiseMesh`を設定するだけ。 |
| `setNoiseOnStep(Vector3 footPosition)` | 現在の足音状態がノイズ有効なら、その半径でノイズ信号を送り、必要ならノイズメッシュも生成する。 |
| `setDefaultFeelVolumeRange()` | 左右の`footStep`の音量範囲を`feetVolumeRangeClamps`に戻すだけ。 |
| `removeSound(int footStepIndex, int soundIndex)` | 音削除の処理はコメントアウトされたままで、`updateComponent`を呼ぶだけ。 |
| `setWallRunningState(bool wallRunningActiveValue, bool wallRunningOnRightSideValue)` | 壁走り中かどうかと右側かどうかのフラグを設定するだけ。 |
| `setFootStepPausedState(bool state)` | 足音を止めるフラグ`footStepPaused`を設定するだけ。 |
| `updateComponent()` | `GKC_Utils.updateComponent`で自身のインスペクタ表示を更新するだけ。 |

## 内部型

- `footStepType`（enum）
- `footStepsLayer`（class）
- `footStepState`（class）
