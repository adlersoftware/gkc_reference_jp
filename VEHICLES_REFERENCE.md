# Vehicles メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Vehicles/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **30 型 / 623 メソッド**
- 注釈付き: **623 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

`vehicleHUDManager` が車両の HUD・燃料・エンジン・体力をまとめ、`vehicleController` が入力と物理、`IKDrivingSystem` が運転 IK、`GKCSimpleRiderSystem` が騎乗、`vehicleWeaponSystem` が車載武器を担当します。車種別の挙動は `Vehicle Controllers/` 以下に分かれています。

## 車両中核・HUD・ライダー

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`vehicleHUDManager`](reference/Vehicles/vehicleHUDManager.md) | 車両の体力・ブースト（エネルギー）・燃料の値と対応する`Slider`を保持し、被弾・破壊処理やHUD更新、乗降・カメラ・入力の各マネージャへの委譲をまとめる`healthManagement`派生コンポーネント。自爆・射出・ホーンなどの車両操作APIも公開する。 | 193/193 |
| [`IKDrivingSystem`](reference/Vehicles/IKDrivingSystem.md) | 車両の座席と乗員を管理し、乗降処理・IK目標・カメラ切替・運転手の取得・破壊時の排出や爆発を担当する。`mainRiderSystem`を継承し、各席の`IKDrivingInformation`を保持する。 | 63/63 |
| [`vehicleWeaponSystem`](reference/Vehicles/vehicleWeaponSystem.md) | 車両に搭載する武器システム。武器リストの選択・弾倉と残弾の管理・リロード・発射体生成・レーザーや照準カーソル、HUDへの弾薬表示とカメラ揺れを一括して制御する。 | 47/47 |
| [`GKCSimpleRiderSystem`](reference/Vehicles/GKCSimpleRiderSystem.md) | 座席単位の簡易ライダー/乗降システム。プレイヤーやAIを運転席・助手席へ乗降させ、乗客ごとのコンポーネント参照と状態ID、HUD・入力・カメラ・武器の切り替えを管理する。 | 39/39 |
| [`playerHUDManager`](reference/Vehicles/playerHUDManager.md) | 車両乗車中に使うHUD管理コンポーネント。プレイヤーHUD・車両HUDの表示制御と、現在車両への体力/エネルギー/燃料/弾薬操作の橋渡し、HUD要素の有効/無効切り替えを担当する。 | 33/33 |
| [`vehicleDamageReceiver`](reference/Vehicles/vehicleDamageReceiver.md) | 車両の各コライダーに付いて被弾を受け、`vehicleHUDManager`へ体力・燃料・エネルギー処理を中継する受信コンポーネント。`healthManagement`の抽象メソッドも上書き実装する。 | 24/24 |
| [`mainRiderSystem`](reference/Vehicles/mainRiderSystem.md) | 車両のライダー（搭乗者）まわりの共通インターフェース。派生クラスが上書きする前提で、多くの仮想メソッドは空実装かnull/false/0を返す。 | 16/16 |
| [`vehicleBuilder`](reference/Vehicles/vehicleBuilder.md) | エディタ上で車両メッシュの差し替え、設定イベントの実行、シーンへの配置を行うビルダー。パーツのインスタンス化とHUDマネージャへの登録をまとめて行う。 | 12/12 |
| [`vehicleInterface`](reference/Vehicles/vehicleInterface.md) | 車両のUIキャンバスとUI要素リストを管理し、押された要素に応じて値送信イベントを発火するインターフェース。パネルの移動・回転操作も扱う。 | 10/10 |
| [`hoverBoardWayPoints`](reference/Vehicles/hoverBoardWayPoints.md) | ホバーボード用レールのウェイポイント群を保持し、トリガーに進入した車両へレール移動を開始させるコンポーネント。エディタで点の追加・削除・改名も行う。 | 6/6 |
| [`launchTrayectory`](reference/Vehicles/launchTrayectory.md) | カメラの向きから着弾点をレイキャストし、放物線の軌跡と着地点アイコンをLineRendererで表示する照準補助。2.5D/3Dビューやヘッドトラックにも対応する。 | 4/4 |
| [`vehicleInteractionPanelSystem`](reference/Vehicles/vehicleInteractionPanelSystem.md) | 近くの車両を検知したときに運転/同乗の入力アイコンや満車表示を出すパネル。入力に応じてプレイヤーを車両へ搭乗させる。 | 4/4 |
| [`shipInterfaceInfo`](reference/Vehicles/shipInterfaceInfo.md) | 宇宙船HUDのテキストやバーを毎フレーム更新する船用インターフェース。武器名・弾薬・体力・エネルギー・燃料などを表示する。 | 3/3 |
| [`skidsManager`](reference/Vehicles/skidsManager.md) | タイヤ痕を1つのメッシュに蓄積して描画するスキッドマーク管理。追加された節点から頂点・法線・UV・三角形を組み直す。 | 2/2 |
| [`vehicleLaser`](reference/Vehicles/vehicleLaser.md) | 車両搭載レーザーの照射判定と描画を行うコンポーネント。ヒット位置に火花やパーティクルを出し、継続的にダメージを与える。 | 2/2 |
| [`GKCRiderSocketSystem`](reference/Vehicles/GKCRiderSocketSystem.md) | ライダー系コンポーネントへの参照を保持するだけの小さなソケット。`mainRiderSystem` を外部から取得するために使う。 | 1/1 |

## AI・ウェイポイント

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`vehicleAINavMesh`](reference/Vehicles/vehicleAINavMesh.md) | NavMesh上を走るAI車両の追従・巡回路・回避・ブレーキ制御をまとめたコンポーネント。入力値の上書きや目標の再評価も行う。 | 10/10 |
| [`WaypointCircuit`](reference/Vehicles/WaypointCircuit.md) | Transformのリストから周回コースを組み、距離に応じた位置と方向をCatmull-Rom補間で返すウェイポイント回路。経路の追加や名前整列、位置リセットなどのエディタ補助も持つ。 | 9/9 |
| [`WaypointProgressTracker`](reference/Vehicles/WaypointProgressTracker.md) | `WaypointCircuit`上の進捗距離を進めながら、注視点`target`を先読み位置へ動かす追従トラッカー。スムーズとポイント間の2モードを切り替えられる。 | 4/4 |
| [`remoteVehicleNavmeshOverride`](reference/Vehicles/remoteVehicleNavmeshOverride.md) | 外部オブジェクトから`vehicleAINavMesh`へ追従ターゲットを設定/解除する小さなブリッジ。目標の種別や自動ブレーキ設定も一緒に渡す。 | 2/2 |

## 車種別コントローラ

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`vehicleController`](reference/Vehicles/vehicleController.md) | 車両操作の基底コントローラーで、搭乗中の入力を読み取り、ブースト・燃料・エンジンON/OFF・2.5D回転・ホバーボードのウェイポイント移動を扱う。派生コントローラー向けに多くのメソッドが空の仮想関数として用意されている。 | 68/68 |
| [`carController`](reference/Vehicles/carController.md) | 車輪コライダーと`Rigidbody`で走行する四輪車両のコントローラ。車体のリーン、ギアとエンジン音、スキッド痕、ブースト、乗降時の揺れ、転倒時の自動復帰を扱う。 | 15/15 |
| [`boatController`](reference/Vehicles/boatController.md) | 水面オブジェクトの浮力と帆・風の状態で進むボート用コントローラ。帆と風検知の切替イベント、船体密度の増減、ジャンプ台連携を持つ。 | 13/13 |
| [`motorBikeController`](reference/Vehicles/motorBikeController.md) | 二輪車用コントローラ。低速時の車体リーンと足の接地調整、スタンドアニメーション、エンジン音、スキッド／排気パーティクルを扱う。 | 12/12 |
| [`airCraftController`](reference/Vehicles/airCraftController.md) | 航空機用コントローラ。ピッチ・ヨー・ロール入力、離着陸ギアと翼のアニメーション、エンジン／風／離着陸音、トレイルの表示を扱う。 | 8/8 |
| [`sphereController`](reference/Vehicles/sphereController.md) | 球体を転がす物理ベースのビークルコントローラ。接地・スナップ判定、ジャンプ、壁登り、水中判定、ブーストを扱う。 | 7/7 |
| [`flyingController`](reference/Vehicles/flyingController.md) | 上下・左右・ロールで飛ぶ飛行ビークルのコントローラ。高さ入力、ロール入力、エンジン音と排気／ブーストパーティクルを扱う。 | 5/5 |
| [`hoverBoardController`](reference/Vehicles/hoverBoardController.md) | ホバーボード用コントローラ。複数のホバーエンジン推力、車体安定化トルク、ジャンプ、ブースト、搭乗者アニメーション連携を扱う。 | 5/5 |
| [`hoverCraftController`](reference/Vehicles/hoverCraftController.md) | ホバーエンジンの推力で浮上するホバークラフト用コントローラ。浮上用レイキャスト、ジャンプ入力の保持、ブースト、パーティクルを扱う。 | 5/5 |
| [`hoverBoardAnimationSystem`](reference/Vehicles/hoverBoardAnimationSystem.md) | ホバーボード搭乗中のプレイヤーの`Animator`と上半身IKを制御する補助コンポーネント。頭・腕・胴の向きをボードの動きに追従させる。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- HUD 更新・燃料/体力・物理挙動・イベント発火・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

