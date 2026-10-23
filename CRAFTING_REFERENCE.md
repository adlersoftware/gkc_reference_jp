# Crafting System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Crafting System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **15 型 / 221 メソッド**
- 注釈付き: **221 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

`craftingSystem` がレシピと素材の消費・生成を担い、`craftingUISystem` がクラフト画面、`craftingStationSystem` / `energyStationSystem` / `materialExtractionStationSystem` が作業台・エネルギー・採掘を担当します。

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`craftingSystem`](reference/Crafting%20System/craftingSystem.md) | クラフト機能の窓口となるコンポーネントで、在庫・設計図・作業台・設置モードの各システムへ処理を委譲する。材料消費やブループリント解禁、時間制クラフトの進行情報の取得も公開APIとして提供する。 | 55/55 |
| [`craftingUISystem`](reference/Crafting%20System/craftingUISystem.md) | クラフトメニューのUI本体で、設計図・在庫・修理・分解・配置・アップグレードの各パネルを制御する。材料消費と生成、作業台カテゴリの絞り込み、時間制クラフトのコルーチン開始までを担う。 | 42/42 |
| [`durabilityInfo`](reference/Crafting%20System/durabilityInfo.md) | オブジェクトの耐久度を保持し、増減・全快・破損判定とイベント発火、遅延回復コルーチン、在庫側耐久値の同期を行う。エディタ用setterはコンポーネント更新も伴う。 | 21/21 |
| [`craftingPlacementSystem`](reference/Crafting%20System/craftingPlacementSystem.md) | カメラからのレイキャストで設置位置を決め、プレビュー生成・回転・設置確定・ステーション接続を扱う。設置中はコルーチンで毎フレーム位置を更新する。 | 20/20 |
| [`craftingStationSystem`](reference/Crafting%20System/craftingStationSystem.md) | 入出力`craftingSocket`・接続先ステーション一覧・エネルギー供給元を保持する基底クラス。状態変化フックは`virtual`の空実装で、派生クラスが上書きする。 | 17/17 |
| [`energyStationSystem`](reference/Crafting%20System/energyStationSystem.md) | `craftingStationSystem`を継承したエネルギー供給ステーション。時間経過でエネルギーを消費・再充填し、出力接続先へ現在量と無限エネルギー状態を伝える。 | 11/11 |
| [`materialExtractionStationSystem`](reference/Crafting%20System/materialExtractionStationSystem.md) | `craftingStationSystem`を継承した採取ステーション。周囲の`materialsZoneSystem`を探して一定間隔で素材を在庫バンクかスポーンで取り出し、エネルギー消費と供給元を扱う。 | 10/10 |
| [`materialsZoneSystem`](reference/Crafting%20System/materialsZoneSystem.md) | 採取可能な素材量を素材ごとに持つゾーン。採取で残量が減り、空になると無効化と任意の遅延再補充を行い、外部要素からの採取も処理する。 | 10/10 |
| [`craftedObjectPlacedHelper`](reference/Crafting%20System/craftedObjectPlacedHelper.md) | 設置済みオブジェクトに付く補助コンポーネント。設置/回収イベント、設置状態、回収可否、ステーション接続解除の伝播を提供する。 | 9/9 |
| [`craftingSocket`](reference/Crafting%20System/craftingSocket.md) | ステーションの入出力を表すソケット。接続先ステーションと、`LineRenderer`による接続線の表示・端点更新を管理する。 | 8/8 |
| [`simpleBreakObject`](reference/Crafting%20System/simpleBreakObject.md) | 破壊可能オブジェクト。爆発ダメージ・破片生成・フェード・死亡処理・イベントをまとめて実行し、`fixBrokenObject`で破壊前の状態に戻せる。 | 6/6 |
| [`craftingWorkbenchSystem`](reference/Crafting%20System/craftingWorkbenchSystem.md) | 作業台。プレイヤーの`craftingSystem`に自身を現在の作業台として登録し、クラフト画面の開放/終了と在庫バンクへの格納を扱う。 | 5/5 |
| [`processStationSystem`](reference/Crafting%20System/processStationSystem.md) | `craftingStationSystem`を継承した加工ステーション。素材バンクの素材をブループリントの加工情報に従って加工品バンクへ変換し、エネルギーを消費する。 | 4/4 |
| [`materialExtractionStationUISystem`](reference/Crafting%20System/materialExtractionStationUISystem.md) | 採取ステーションのUI。ゾーン数・各ゾーン残量・エネルギー量のテキストを更新し、稼働中はコルーチンで追従する。 | 2/2 |
| [`craftingZoneSystem`](reference/Crafting%20System/craftingZoneSystem.md) | トリガーゾーン。タグ一致のプレイヤーが出入りした際に、配置モードの一時停止状態を切り替える。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 素材消費・生成・UI スロット更新・イベント発火・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

