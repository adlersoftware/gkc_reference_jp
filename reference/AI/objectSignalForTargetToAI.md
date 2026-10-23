# objectSignalForTargetToAI

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `AI/objectSignalForTargetToAI.cs:5`

**概要**: このオブジェクトをAIの検出対象として通知するコンポーネント。ノイズシグナルを一定間隔または単発で送り、単一AIの追跡状態を監視する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Range To Detect AI | `rangeToDetectAI` | `float` | 20 | – |
| Layer Detection | `layerDetection` | `LayerMask` | – | – |
| Activate Detection At Start | `activateDetectionAtStart` | `bool` | – | – |
| Send Detection Signal Rate | `sendDetectionSignalRate` | `float` | – | – |
| Check To Send To Single AI | `checkToSendToSingleAI` | `bool` | – | – |
| Disable Signal Once AI Reached | `disableSignalOnceAIReached` | `bool` | – | – |
| Noise ID | `noiseID` | `int` | -1 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Single AI Detected | `singleAIDetected` | `bool` | – | – |
| Current AI Detected | `currentAIDetected` | `GameObject` | – | – |
| Current Find Objectives System | `currentFindObjectivesSystem` | `findObjectivesSystem` | – | – |
| Current AI Nav Mesh | `currentAINavMesh` | `AINavMesh` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateSignalWithRate()` | 既存の監視コルーチンを止め、一定間隔でシグナルを送る`checkSignalCoroutine`を開始する。 |
| `checkToDetectAI()` | 単一AI指定なら最寄りAIへノイズを送って参照を保存し、そうでなければ範囲内へノイズシグナルをまとめて送る。 |
