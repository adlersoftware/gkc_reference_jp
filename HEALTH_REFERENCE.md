# Health メソッドリファレンス

`Assets/Game Kit Controller/Scripts/Health/` 以下のコンポーネントについて、public メソッドの実装を読んで日本語の一行解説を付けたものです（GKC 3.77h）。

- 対象: **16 型 / 407 メソッド**
- 注釈付き: **407 メソッド**（100%）
- 生成元: 各 `.cs` の実装。説明はコードの挙動のみに基づきます。

`health` が体力・ダメージ・回復・蘇生の中核で、`healthManagement` はその基底、`shieldSystem` がシールド、`healthBarManagementSystem` / `playerHealthBarManagementSystem` が HP バー UI、`characterDamageReceiver` が部位ごとの被弾を仲介します。

| 型 | 概要 | 注釈 |
| --- | --- | --- |
| [`health`](reference/Health/health.md) | キャラクターや車両の体力を管理する`healthManagement`派生コンポーネントで、`healthAmount`の増減、シールド、弱点（部位）ごとのダメージ倍率、被弾・死亡・復活イベント、ヘルスバー表示、ラグドール連携をまとめて扱う。 | 173/173 |
| [`healthManagement`](reference/Health/healthManagement.md) | `health`などの各コンポーネントが継承する体力処理の基底クラス。ほぼ全てのメソッドが空実装か固定値の返却で、実際の処理は派生クラスが担当する。`checkHealthAmountOnSpot`だけが部位体力の減算とイベント発火を実装している。 | 70/70 |
| [`shieldSystem`](reference/Health/shieldSystem.md) | `useShield`と`shieldAmount`を保持し、被弾時のダメージ肩代わり、時間経過での自動回復、スライダーや`healthBarManager`への反映を行う。状態変化時には`eventOnStartShield`や`eventOnDamageShield`などのイベントを発火する。 | 28/28 |
| [`characterDamageReceiver`](reference/Health/characterDamageReceiver.md) | コライダーごとに付与される中継コンポーネント。受け取ったダメージに`damageMultiplier`を掛けて`health`へ転送し、回復・シールド・弱点・即死などのAPIも`healthManagement`として仲介する。 | 23/23 |
| [`playerHealthBarManagementSystem`](reference/Health/playerHealthBarManagementSystem.md) | プレイヤー側の体力バー管理。`healthSliderInfoList`で敵NPCの頭上スライダーを生成・更新し、オンスクリーンのメイン体力表示や親パネルの表示状態と同期する。 | 23/23 |
| [`healthBarManagementSystem`](reference/Health/healthBarManagementSystem.md) | シーン内の体力バーを管理するシングルトンで、`healthSliderInfoList`にスライダー情報を保持し、登録された各`playerHealthBarManagementSystem`へ値や表示状態を一括転送する。`showSlidersActive`が偽の場合は大半のメソッドが早期リターンする。 | 22/22 |
| [`damageHitReactionSystem`](reference/Health/damageHitReactionSystem.md) | 被弾方向・カテゴリ・確率から`hitReactionInfoList`のリアクションを選んで再生するシステム。ブロック/パリィの猶予やダメージ量に応じた`damageStateInfo`イベントも扱う。 | 18/18 |
| [`applyEffectOnArea`](reference/Health/applyEffectOnArea.md) | トリガーまたはオーバーラップ球で範囲内のオブジェクトを検出し、`effectAmount`の効果を適用するエリア。ステータス増減・遠隔イベント・退出時処理・継続時間付き有効化を備える。 | 11/11 |
| [`setHealthCustomWeakSpotID`](reference/Health/setHealthCustomWeakSpotID.md) | 名前付きのカスタム状態ごとに、弱点の部位HP ID・被弾時送信関数・体力オンスポット設定を`health`へまとめて適用するコンポーネント。 | 9/9 |
| [`damageScreenSystem`](reference/Health/damageScreenSystem.md) | 被弾時に画面を赤くフェードさせ、攻撃者の方向アイコンを出すダメージスクリーン。`usedByAI`でAI用に抑止でき、体力に応じて色の濃さを変える。 | 8/8 |
| [`playerDamageOnScreenInfoSystem`](reference/Health/playerDamageOnScreenInfoSystem.md) | プレイヤー単位のダメージ数値表示。対象の頭上にテキストを生成し、`damageOnScreenInfoSystem`と対象リストを共有して移動演出付きで表示する。 | 8/8 |
| [`damageOnScreenInfoSystem`](reference/Health/damageOnScreenInfoSystem.md) | シーン共有のダメージ表示マネージャ（シングルトン）。`currentID`で対象を登録し、複数の`playerDamageOnScreenInfoSystem`へ表示要求を配信する。 | 6/6 |
| [`damageInScreen`](reference/Health/damageInScreen.md) | 自分の体力変化を画面数値で見せるためのコンポーネント。起動時に`damageOnScreenInfoSystem`へ対象登録し、以降はID経由で表示を委譲する。 | 5/5 |
| [`damageOrHealTrigger`](reference/Health/damageOrHealTrigger.md) | トリガー内のオブジェクトへ継続的にダメージ・回復・エネルギー/燃料補給を行う。対象判定はタグ一覧とプレイヤー/車両/キャラクタの種別フラグで行う。 | 1/1 |
| [`destroyableObject`](reference/Health/destroyableObject.md) | 破壊可能オブジェクト。破片化・フェード・破壊音・爆発力を適用し、任意で`setExplosion`による範囲ダメージとイベントを発生させる。 | 1/1 |
| [`externalDamageProperties`](reference/Health/externalDamageProperties.md) | ダメージの発生源を保持する小さなコンポーネント。`currentDamageOwner`を差し替え、変更時にイベントで通知する。 | 1/1 |

# 注釈の読み方

- 「`xxx` を設定するだけ」は、内部処理を伴わない単純なセッターです。
- ダメージ計算・無敵/シールド判定・HP バー更新・被弾演出・イベント発火・コルーチンを伴うものは、その旨を書いています。
- 空実装は「本体が空で何もしない」と明記しています。
- 自動生成のため、特定条件下でのみ走る処理などは取りこぼしている可能性があります。

