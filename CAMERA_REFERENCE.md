# Camera メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Camera/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **27 型 / 606 メソッド**
- 注釈付き: **606 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

中心は `playerCamera`（視点・カメラステート・注視・リクティクル）で、`cameraControllerManager` がカメラ状態の共通管理、`headBob` が揺れ、`vehicleCameraController` が車両視点を担当します。

## カメラエフェクト

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`cameraEffectSystem`](reference/Camera/cameraEffectSystem.md) | 登録したカメラエフェクトを名前やインデックスで切り替える管理コンポーネント。`OnRenderImage` から現在のエフェクトへ画像を渡し、切替時に対応する UnityEvent を発火する。 | 15/15 |
| [`photoModeSystem`](reference/Camera/photoModeSystem.md) | フォトモード用のフリーカメラ。プレイヤーカメラをピボットに付け替えて自由移動・回転させ、タイムスケール停止や撮影イベントを扱う。 | 14/14 |
| [`cameraEffect`](reference/Camera/cameraEffect.md) | カメラエフェクトの基底クラス。`renderEffect` を仮想メソッドとして持つだけで、実際の描画は派生クラスが実装する。 | 1/1 |
| [`pixelCameraEffect`](reference/Camera/pixelCameraEffect.md) | 画面をブロック状にピクセル化するポストエフェクト。`BlockCount` とカメラのアスペクト比からブロック数を算出してシェーダに渡し、ブリットする。 | 1/1 |
| [`solidCameraEffect`](reference/Camera/solidCameraEffect.md) | テクスチャを画面全体に敷くソリッド系のポストエフェクト。ブロック数・色・テクスチャをシェーダに渡してブリットする。 | 1/1 |

## キャプチャ

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`cameraCaptureSystem`](reference/Camera/cameraCaptureSystem.md) | スクリーンショットの撮影とPNG保存、保存済み画像のギャラリー表示・拡大・削除を、`ScrollRect`やボタンなどのUIとともに扱うコンポーネント。保存先は`gameManager`の設定に従う。 | 20/20 |
| [`cameraPerspectiveSystem`](reference/Camera/cameraPerspectiveSystem.md) | プレイヤーが目標物をカメラ内に収めると「撮影成功」と判定するシステム。距離・角度・画面内判定を行い、撮影音、オブジェクトの有効化、イベント、近接音を扱う。 | 4/4 |
| [`remoteEventOnCameraCaptureSystem`](reference/Camera/remoteEventOnCameraCaptureSystem.md) | 撮影時のレイキャストで見つかったオブジェクトの `eventObjectFoundOnCaptureSystem` を呼び出す中継コンポーネント。カプセルキャストにも対応する。 | 2/2 |

## カットシーン

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`cameraWaypointSystem`](reference/Camera/cameraWaypointSystem.md) | カットシーン用に、プレイヤーカメラを経由点またはベジェ曲線に沿って移動させ、終了時には元の位置と回転へ戻すコンポーネント。ウェイポイントの追加・削除・名前振り直しはエディタ用関数として提供される。 | 19/19 |
| [`pauseOrResumePlayerControllerAndCameraSystem`](reference/Camera/pauseOrResumePlayerControllerAndCameraSystem.md) | カットシーンなどでプレイヤーの入力・移動・カメラ・HUDをまとめて停止/再開するシステム。カメラの親変更、タイムスケール、遅延再開も扱う。 | 11/11 |
| [`simpleShowHideMouseCursor`](reference/Camera/simpleShowHideMouseCursor.md) | `menuPause` 経由でマウスカーソルとゲームパッドカーソルの表示を切り替える小規模コンポーネント。 | 3/3 |

## その他（透明化・カリング・分割画面）

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`setTransparentSurfacesSystem`](reference/Camera/setTransparentSurfacesSystem.md) | 透明化対象サーフェスを共有するシングルトン的なマネージャ。シェーダの差し替えとアルファ値のコルーチン補間で、透明/通常を切り替える。 | 11/11 |
| [`playerCullingSystem`](reference/Camera/playerCullingSystem.md) | プレイヤーのレンダラーを対象に、マテリアルの透明度を補間してカリング（フェード）するシステム。対象レンダラーと元シェーダをリストで保持する。 | 10/10 |
| [`setTransparentSurfaces`](reference/Camera/setTransparentSurfaces.md) | プレイヤーとカメラの間にあるサーフェスを検出し、マネージャ経由で一時的に透明化するコンポーネント。プレイヤーIDごとに透明化対象を管理する。 | 6/6 |
| [`simpleMoveCameraToPosition`](reference/Camera/simpleMoveCameraToPosition.md) | メインカメラを指定オブジェクトの子にして、位置と回転を補間移動させるコンポーネント。移動終了で元の親へ戻す。 | 3/3 |
| [`dynamicSplitScreenSystem`](reference/Camera/dynamicSplitScreenSystem.md) | 2人のプレイヤーが離れたときに画面を動的に分割するシステム。距離に応じてスプリッタ、2台目のカメラ、カリングマスクを制御する。 | 2/2 |

## プレイヤーカメラ

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerCamera`](reference/Camera/playerCamera.md) | プレイヤーのカメラ全体を管理するコンポーネントで、三人称/一人称/フルボディアウェアネス(FBA)の視点切替、フリー/ロックオンカメラの状態、ピボットとメインカメラの位置・回転、頭ボブ、リーン、マウスホイールでの距離変更、シェイクやノイズなどを制御する。入力用ラッパーとエディタ用ヘルパーも多数持つ。 | 344/344 |
| [`cameraControllerManager`](reference/Camera/cameraControllerManager.md) | プレイヤーのカメラ系コンポーネント用の基底クラスで、全メソッドが`virtual`の空実装か既定値の返却になっている。実際の挙動は派生クラスがオーバーライドして実装する。 | 35/35 |
| [`headBob`](reference/Camera/headBob.md) | 一人称/三人称の頭部ボブと、発砲・ダメージなどの外部シェイクを状態リストとコルーチンで制御するコンポーネント。`mainCameraTransform`のローカル位置と回転を直接補間する。 | 30/30 |
| [`externalCameraShakeSystem`](reference/Camera/externalCameraShakeSystem.md) | 距離やアクション名を条件に、周囲のプレイヤーの `headBob` へ外部シェイクを要求するコンポーネント。シェイク名は外部シェイクリスト管理マネージャから取得する。 | 8/8 |
| [`setCameraFOVValue`](reference/Camera/setCameraFOVValue.md) | メインカメラの FOV を増減・設定し、クランプ範囲内に収める小規模コンポーネント。カメラ未設定時はプレイヤーカメラやシーンから取得する。 | 6/6 |
| [`camera2_5dZoneLimitSystem`](reference/Camera/camera2_5dZoneLimitSystem.md) | 2.5D ゾーンのカメラ移動範囲（幅・高さ・奥行き）をプレイヤーカメラに適用するコンポーネント。プレイヤーでなければ搭乗中の車両のドライバーからカメラを探す。 | 4/4 |
| [`externalShakeListManager`](reference/Camera/externalShakeListManager.md) | シーン内で共有する外部シェイク定義リストを保持するシングルトン的なマネージャ。全 `headBob` へリストや現在のシェイク状態を配布する。 | 4/4 |
| [`camera2_5dSplineZoneOptions`](reference/Camera/camera2_5dSplineZoneOptions.md) | 2.5D スプラインマップのゾーン用オプションで、ゾーン進入時にプレイヤーの `playerCamera` を取得してロックカメラの回転追従を制御する小規模コンポーネント。 | 3/3 |
| [`cameraStateInfo`](reference/Camera/cameraStateInfo.md) | カメラ状態1つ分の設定値（位置オフセット、FOV、リーン、頭部追従など）を保持するシリアライズ可能クラス。別の状態から値をコピーまたは補間代入する。 | 1/1 |

## 車両カメラ

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`vehicleCameraController`](reference/Camera/vehicleCameraController.md) | 車両運転中のカメラを、複数の`vehicleCameraStateInfo`状態の切り替えで管理するコンポーネント。注視方向・ズーム・揺れ・衝突距離・乗降時のリセットを扱い、状態変更は各マネージャへ通知される。 | 41/41 |
| [`vehicleCameraShake`](reference/Camera/vehicleCameraShake.md) | 車両のメインカメラにヘッドボブ/シェイク状態を適用するコンポーネント。状態名ごとの回転揺れを補間し、外部シェイクは継続時間後に停止する。 | 7/7 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- カメラ位置/FOV/ステートの補間・シェイク・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

