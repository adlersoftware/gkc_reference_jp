# Combat System メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Combat System/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **22 型 / 343 メソッド**
- 注釈付き: **343 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

`meleeWeaponsGrabbedManager` が近接武器の装備・攻撃・投擲をまとめ、`closeCombatSystem` が素手のコンボ、`sliceSystem` がメッシュ切断、`matchPlayerToTargetSystem` が攻撃時の位置合わせを担当します。

## 戦闘中核

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`closeCombatSystem`](reference/Combat%20System/closeCombatSystem.md) | 近接コンボ攻撃の中核で、`combatTypeInfo` のコンボ進行、ダメージトリガーの有効化、攻撃入力・ガード・被弾イベントを制御する。攻撃の成否に応じてインデックスや待ち時間を更新し、`disableCombat` で戦闘状態を終了する。 | 74/74 |
| [`matchPlayerToTargetSystem`](reference/Combat%20System/matchPlayerToTargetSystem.md) | 周囲のキャラクターから条件を満たす対象を選び、`activateMatchPositionCoroutine` で位置と回転を補間して攻撃位置へ合わせる。`charactersAround` の追加・削除と対象検出・喪失イベントを管理する。 | 14/14 |
| [`perfectDodgeSystem`](reference/Combat%20System/perfectDodgeSystem.md) | 回避成功時に周囲のキャラクタとプレイヤーを一定時間減速させる演出を制御し、開始/終了イベントを発火する。 | 2/2 |
| [`objectToUseMatchTargetSystem`](reference/Combat%20System/objectToUseMatchTargetSystem.md) | トリガー内に入ったキャラクタを`matchPlayerToTargetSystem`の周囲リストへ登録/解除する。 | 1/1 |

## 近接戦闘

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`meleeWeaponsGrabbedManager`](reference/Combat%20System/meleeWeaponsGrabbedManager.md) | 近接武器の所持リストと盾を管理する中核コンポーネントで、武器の装備/納刀、体へのメッシュ表示、インベントリ・クイックアクセス連携、耐久値、IK、武器抽選や入力処理をまとめて扱う。実際の攻撃やアニメーションは`grabbedObjectMeleeAttackSystem`へ委譲する。 | 106/106 |
| [`meleeCombatThrowReturnWeaponSystem`](reference/Combat%20System/meleeCombatThrowReturnWeaponSystem.md) | 掴んだ近接武器の投擲・帰還・テレポートを制御し、`continueThrowObjectCoroutine` で剛体に力を加え、`returnObjectCoroutine` で手元へ補間移動させる。表面ごとの音・ダメージ・イベントやスタミナ消費も扱う。 | 37/37 |
| [`meleeShieldObjectSystem`](reference/Combat%20System/meleeShieldObjectSystem.md) | 盾オブジェクトの所持者と耐久値を管理し、ブロック時の耐久減少や修理・破壊を`durabilityInfo`へ委譲する。 | 16/16 |
| [`meleeWeaponRangeAttacksManager`](reference/Combat%20System/meleeWeaponRangeAttacksManager.md) | 近接武器に付属する遠距離攻撃（ボウ等）を、`simpleWeaponSystem`による射撃と`playerCamera`のレティクル、エイム/ストレイフ/しゃがみ状態の切り替えとして中継するコンポーネント。 | 13/13 |
| [`meleeAttackSurfaceInfo`](reference/Combat%20System/meleeAttackSurfaceInfo.md) | 攻撃面（サーフェス）の名前・有効状態、武器投擲時のオフセットや付着設定、耐久倍率、各種イベント/リモートイベントを保持するデータコンポーネント。 | 10/10 |
| [`meleeWeaponTransformInfoSystem`](reference/Combat%20System/meleeWeaponTransformInfoSystem.md) | 実行中に手に持った武器と武器メッシュのlocal位置・回転を調整し、その値をScriptableObjectへコピー/貼り付けする開発・調整用コンポーネント。 | 9/9 |
| [`dualWieldMeleeWeaponObjectSystem`](reference/Combat%20System/dualWieldMeleeWeaponObjectSystem.md) | 左手に持たせる二刀流用の近接武器オブジェクトとその`hitCombat`の攻撃判定を管理する。 | 8/8 |
| [`meleeUISystem`](reference/Combat%20System/meleeUISystem.md) | 近接武器の名前とアイコンを表示するUIパネルの表示切替とテキスト更新を担当する。 | 3/3 |
| [`searchMeleeSurfaceSystem`](reference/Combat%20System/searchMeleeSurfaceSystem.md) | 近接攻撃時に足元や隠しサーフェスを探索し、サーフェス情報を攻撃システムへ渡す。 | 3/3 |
| [`hiddenMeleeSurface`](reference/Combat%20System/hiddenMeleeSurface.md) | 斬撃サーフェスを隠しサーフェスとして扱うためのフラグを保持する小型コンポーネント。 | 2/2 |
| [`meleeWeaponAttackListInfoSocket`](reference/Combat%20System/meleeWeaponAttackListInfoSocket.md) | 武器の攻撃情報とテンプレートのコピーを`grabPhysicalObjectMeleeAttackSystem`へ仲介するソケット。 | 2/2 |
| [`objectToFollowOnThrowMeleeWeapon`](reference/Combat%20System/objectToFollowOnThrowMeleeWeapon.md) | 投擲した近接武器が追従する対象トランスフォームを保持する。 | 2/2 |
| [`airAttackToLandSystem`](reference/Combat%20System/airAttackToLandSystem.md) | 空中からの攻撃で地面へ落下させる処理を制御するコンポーネント。開始/終了イベントと下向きレイキャストによる地面検出を持つ。 | 1/1 |
| [`meleeCombatAttackStartState`](reference/Combat%20System/meleeCombatAttackStartState.md) | ダメージ判定トリガーのリセットを許可するフラグを持つ小型コンポーネント。 | 1/1 |

## スライス／破砕

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`simpleSliceSystem`](reference/Combat%20System/simpleSliceSystem.md) | キャラクタやオブジェクト単体のスライス処理を`sliceSystemUtils`へ委譲する簡易スライスコンポーネント。 | 16/16 |
| [`cuttingModeSystem`](reference/Combat%20System/cuttingModeSystem.md) | スライス用のカットモードを管理し、パネル回転・カメラ・アニメータ・スタミナ・バレットタイムを連動させる。 | 9/9 |
| [`sliceSystem`](reference/Combat%20System/sliceSystem.md) | オーバーラップボックスで対象を検出してメッシュを切断し、破片の剛体・力・ダメージ・イベントを処理する中核コンポーネント。 | 9/9 |
| [`runtimeShatterRecursive`](reference/Combat%20System/runtimeShatterRecursive.md) | 対象オブジェクトを指定回数だけ再帰的に粉砕し、生成した破片にコライダーと剛体を付ける。 | 5/5 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- 攻撃状態・ダメージ・IK/アニメーション・イベント発火・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

