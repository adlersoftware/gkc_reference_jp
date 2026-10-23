# Abilities System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Abilities System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **31 型 / 382 メソッド**
- 注釈付き: **382 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

`playerAbilitiesSystem` がアビリティの発動・クールダウン・消費を管理し、`playerAbilitiesUISystem` がスロット UI、`abilityInfo` が 1 アビリティ分のデータを保持します。スタミナ／酸素／ダッシュなどは個別コンポーネントとして実装されています。

## アビリティ中核・UI

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerAbilitiesSystem`](reference/Abilities%20System/playerAbilitiesSystem.md) | プレイヤーのアビリティ一覧を保持し、選択・押下/押上入力、有効/無効化、クールダウンやエネルギー消費、UI連携をまとめて扱う中核コンポーネント。入力系は`input...`、実処理は`press...`と`confirm...`に分かれる。 | 63/63 |
| [`playerAbilitiesUISystem`](reference/Abilities%20System/playerAbilitiesUISystem.md) | アビリティのホイールメニューとDpadクイックアクセスUIを構築・更新し、スロット選択、アイコン割当、クールダウン/制限表示、タッチ入力を担当する。 | 50/50 |
| [`abilityInfo`](reference/Abilities%20System/abilityInfo.md) | 1つのアビリティの設定と状態（有効可否、クールダウン、時間制限、エネルギー、押下状態、イベント、コルーチン）を保持する基底クラス。効果本体は派生クラス側が実装する。 | 42/42 |
| [`staminaSystem`](reference/Abilities%20System/staminaSystem.md) | スタミナ値・最大値・消費レート・回復コルーチンを管理するコンポーネント。名前付きのスタミナ状態ごとに使用中フラグや空/回復イベントを持ち、円形/通常スライダーや残量テキストのUIも更新する。 | 33/33 |
| [`dashSystem`](reference/Abilities%20System/dashSystem.md) | 一人称と三人称それぞれのダッシュ設定（速度・継続時間・クールダウン・スタミナ消費・方向別イベント）を保持し、`dashInfo`単位でIDや一時停止状態を切り替える。実行時は入力方向やストレイフ状態からダッシュ方向を決めて移動とカメラを制御する。 | 25/25 |
| [`oxygenSystem`](reference/Abilities%20System/oxygenSystem.md) | 酸素残量・消費レート・回復レートを管理し、`oxygenStateInfo`単位で使用中の消費や音・イベントを切り替える。残量が尽きると死亡イベントを発火し、スライダーとテキストのUIも更新する。 | 20/20 |
| [`magicSpellActionSystem`](reference/Abilities%20System/magicSpellActionSystem.md) | 魔法スペルをリストで管理し、種類名やインデックスで選択して発動コルーチン・遠隔イベント・カスタムアクション・エナジー消費を実行する。魔法システムの開始/終了時にはストレイフモードやしゃがみ状態を保存・復元する。 | 19/19 |
| [`throwObjectTrayectorySystem`](reference/Abilities%20System/throwObjectTrayectorySystem.md) | 投擲物の生成、放物線の照準、発射を担当するコンポーネント。カメラのレイキャストで着弾点を求めて速度を計算する。 | 7/7 |
| [`simpleStrafeAndAimState`](reference/Abilities%20System/simpleStrafeAndAimState.md) | ストレイフモードとエイム状態をまとめて切り替える補助コンポーネント。元のストレイフIDやカメラ状態を保存し、解除時に復元する。 | 5/5 |
| [`playerAbilitiesUIEditorSystem`](reference/Abilities%20System/playerAbilitiesUIEditorSystem.md) | アビリティUIの編集画面を開閉し、ホイールとスロット一覧を更新するUIコンポーネント。スロット生成やスクロール位置のリセットも行う。 | 4/4 |
| [`simpleThrowFireWaveAbility`](reference/Abilities%20System/simpleThrowFireWaveAbility.md) | 状態フラグと開始・終了イベントだけを持つ単純な火炎波アビリティ。 | 2/2 |
| [`particleCollisionDetection`](reference/Abilities%20System/particleCollisionDetection.md) | パーティクル衝突を検出し、位置や相手オブジェクトをイベントで通知するコンポーネント。レイヤーと最大検出回数の制限を持つ。 | 1/1 |
| [`wallRunningZoneSystem`](reference/Abilities%20System/wallRunningZoneSystem.md) | ゾーンに入ったプレイヤーの壁走り設定を切り替えるトリガー。退出時には元の壁走り設定へ戻す。 | 1/1 |

## カスタムアビリティ

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`playerTeleportSystem`](reference/Abilities%20System/playerTeleportSystem.md) | プレイヤーのテレポート能力。照準した地点への移動、操作とカメラFOVの制御、フック対象への移動を扱う。 | 13/13 |
| [`drainStatSystem`](reference/Abilities%20System/drainStatSystem.md) | カメラ前方の対象を検出し、時間経過で相手のステータスを吸い取って自分を強化するドレイン能力。対象検出、吸収コルーチン、対象を引き寄せる処理をまとめて持つ。 | 12/12 |
| [`playerShieldSystem`](reference/Abilities%20System/playerShieldSystem.md) | プレイヤーのシールドと手元レーザーを扱うアビリティ。飛来する弾を防ぎ、貯めた弾を撃ち返す機能も持つ。 | 9/9 |
| [`manualDetonationMineSystem`](reference/Abilities%20System/manualDetonationMineSystem.md) | 手動起爆式の地雷の設置と起爆を管理するコンポーネント。設置イベント、現在の地雷、設置時刻を保持する。 | 4/4 |
| [`manualDetonationMineObject`](reference/Abilities%20System/manualDetonationMineObject.md) | 手動起爆式の地雷オブジェクト。起爆用イベントを持ち、所有する `manualDetonationMineSystem` に自身の解除を依頼する。 | 3/3 |
| [`playerStealthSystem`](reference/Abilities%20System/playerStealthSystem.md) | ステルスモードの状態と制限時間を管理するアビリティ。状態変化をイベントで通知し、時間切れで自動解除する。 | 3/3 |
| [`laserPlayer`](reference/Abilities%20System/laserPlayer.md) | プレイヤーに当たったレーザーを反射・描画する `laser` 派生クラス。ヒット位置、レーザーの色、屈折回数を保持する。 | 2/2 |
| [`laserVisionSystem`](reference/Abilities%20System/laserVisionSystem.md) | レーザーでオブジェクトを切断するビジョン能力。レーザー位置の移動量から切断方向を決め、`sliceSystem` でスライスする。 | 2/2 |
| [`slowDownAllAIOnSceneSystem`](reference/Abilities%20System/slowDownAllAIOnSceneSystem.md) | シーン内のAIを一時停止・再開させてスローダウンさせる能力。敵のみを対象にする設定も持つ。 | 2/2 |
| [`removeGravityFromCharacterSystem`](reference/Abilities%20System/removeGravityFromCharacterSystem.md) | ラグドール化したキャラクターの重力を一定時間だけ切り、上方向の力とトルクを加えるコンポーネント。 | 1/1 |
| [`removeGravityFromObjectSystem`](reference/Abilities%20System/removeGravityFromObjectSystem.md) | オブジェクトの重力を一定時間だけ解除して力を加え、減速・キネマティック切替の後に元の重力へ戻す。 | 1/1 |
| [`simpleLaser`](reference/Abilities%20System/simpleLaser.md) | カメラから照射するシンプルなレーザー。ヒット判定、ダメージ、レーザードットの表示を扱う。 | 1/1 |
| [`stealObjectFromCharacterSystem`](reference/Abilities%20System/stealObjectFromCharacterSystem.md) | 注視中または周囲のキャラクターから武器を盗む能力。確率・距離・クールダウンで成否を判定する。 | 1/1 |

## グラップリングフック

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`grapplingHookSystem`](reference/Abilities%20System/grapplingHookSystem.md) | フック先の表面検出、スイング/引き寄せ力の毎フレーム適用、対象剛体の吸引、外部コントローラやカメラ・アニメーションの切り替えを担う。対象オブジェクトの`objectToAttractWithGrapplingHook`設定により吸引方法や遠隔イベントも変化する。 | 29/29 |
| [`objectToAttractWithGrapplingHook`](reference/Abilities%20System/objectToAttractWithGrapplingHook.md) | グラップリングフックで引き寄せられるオブジェクト側の設定。引力状態の切替、終了時の減速と速度復帰、複数 `Rigidbody` の検索を扱う。 | 10/10 |
| [`grapplingHookEffect`](reference/Abilities%20System/grapplingHookEffect.md) | グラップリングフックのロープを `LineRenderer` で螺旋状に描画するエフェクト。`DoGrapple` で対象点を決め、更新時に頂点を毎フレーム再計算する。 | 7/7 |
| [`grapplingHookTargetsSystem`](reference/Abilities%20System/grapplingHookTargetsSystem.md) | プレイヤーが狙えるグラップリング対象を管理し、対象アイコンの生成・表示・削除を行う。`grapplingHookSystem` とテレポートシステムへ対象を引き渡す。 | 7/7 |
| [`grapplingHookTarget`](reference/Abilities%20System/grapplingHookTarget.md) | グラップリングフックの対象地点コンポーネント。プレイヤーがトリガーに入ると対象リストへ登録し、フック・スイング受信時のイベントを持つ。 | 3/3 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- クールダウン・消費・イベント発火・UI 更新・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

